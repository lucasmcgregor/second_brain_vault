#!/usr/bin/env python3
"""
vault-audit.py - health check for an agent-ready Obsidian vault.

Detects drift between what is actually in the vault and what its index
registries claim is there. READ-ONLY: it reports, it never fixes. Repairs are
the job of the `maintain-indexes` skill, which reads this output.

Checks:
  1. folders with no index.md
  2. files and folders missing from their parent index registry
  3. registry rows pointing at things that no longer exist
  4. broken [[wikilinks]]
  5. missing or incomplete frontmatter
  6. stale items (status: active, not updated in N days)
  7. possible credentials outside _ai/config/
  8. malformed, unclosed, nested or duplicated <!--zone:...--> markers

Usage:
    python3 vault-audit.py <vault-path> [--json] [--stale-days N]

Exit codes:
    0  clean        1  issues found        2  bad usage / not a vault

Changelog:
    2026-09-14  created.
    2026-11-17  root marker is AGENTS.md (agent-neutral); CLAUDE.md and
                README.md are recognised root files; README.md needs no frontmatter;
                removed a no-op branch.
"""

import sys, os, re, json, datetime

SKIP_DIRS = {".obsidian", ".trash", ".git", "node_modules"}
ROOT_MARKER = "AGENTS.md"  # the vault's entry point; marks a folder as a vault
ROOT_FILES = {"index.md", "AGENTS.md", "CLAUDE.md", "README.md"}  # never need a registry row
REQUIRED_FM = ("type", "status", "updated")
ZONE_OPEN = re.compile(
    r"<!--\s*zone:(?P<type>[A-Za-z0-9_-]+)\s*:\s*(?P<id>[A-Za-z0-9_.-]+)"
    r"(?:\s+status:\s*(?P<status>[A-Za-z0-9_-]+))?\s*-->"
)
ZONE_CLOSE = re.compile(r"<!--\s*/\s*zone(?:\s*:\s*(?P<id>[A-Za-z0-9_.-]+))?\s*-->")
ZONE_LOOSE = re.compile(r"<!--\s*zone\b[^>]*-->")
ZONE_INVALID = re.compile(r"<!\s*/\s*--\s*zone\b[^>]*>")
VALID_STATUS = {"draft", "completed", "locked"}

SECRET_RE = re.compile(
    r'(?i)\b(password|passwd|api[_-]?key|secret|token|client[_-]?secret|access[_-]?key)\b\s*[:=]\s*\S{8,}'
)


def read(path):
    try:
        with open(path, encoding="utf-8") as fh:
            return fh.read()
    except (OSError, UnicodeDecodeError):
        return ""


def frontmatter(text):
    """Minimal YAML-ish frontmatter parse. Returns {} if absent."""
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    out = {}
    for line in text[3:end].splitlines():
        if not line.strip() or line.startswith((" ", "\t", "#")):
            continue
        if ":" in line:
            k, v = line.split(":", 1)
            out[k.strip()] = v.strip()
    return out


def strip_code(text):
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    return re.sub(r"`[^`\n]*`", "", text)


def wikilinks(text):
    """Link targets, ignoring code spans, aliases, escaped pipes and headings."""
    out = []
    for raw in re.findall(r"\[\[([^\]\n]+)\]\]", strip_code(text)):
        target = re.split(r"\\\||\|", raw)[0]
        target = target.split("#")[0].split("^")[0].strip()
        if target:
            out.append(target)
    return out


def check_zones(text):
    """Zone marker integrity for one document. Returns a list of problems."""
    body = strip_code(text)
    problems = []

    for m in ZONE_INVALID.finditer(body):
        problems.append(f"invalid close marker {m.group(0)!r} - use <!-- /zone -->")

    valid_open_spans = {m.start() for m in ZONE_OPEN.finditer(body)}
    for m in ZONE_LOOSE.finditer(body):
        if m.start() not in valid_open_spans:
            problems.append(f"malformed open marker {m.group(0)!r}")

    events = [(m.start(), "open", m) for m in ZONE_OPEN.finditer(body)]
    events += [(m.start(), "close", m) for m in ZONE_CLOSE.finditer(body)]
    events.sort(key=lambda e: e[0])

    stack, seen = [], set()
    for _, kind, m in events:
        if kind == "open":
            zid, status = m.group("id"), m.group("status")
            if stack:
                problems.append(f"zone '{zid}' opens inside zone '{stack[-1]}' - zones must not nest")
            if zid in seen:
                problems.append(f"duplicate zone id '{zid}'")
            seen.add(zid)
            if status and status not in VALID_STATUS:
                problems.append(
                    f"zone '{zid}' has unknown status '{status}' - expected {'/'.join(sorted(VALID_STATUS))}"
                )
            stack.append(zid)
        else:
            if not stack:
                problems.append("close marker with no open zone")
                continue
            opened = stack.pop()
            cid = m.group("id")
            if cid and cid != opened:
                problems.append(f"close marker names '{cid}' but the open zone is '{opened}'")
    for zid in stack:
        problems.append(f"zone '{zid}' is never closed")

    return problems


def walk(root):
    """Yield (dirpath, subdirs, files) with hidden and skipped dirs pruned."""
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = sorted(
            d for d in dirnames if not d.startswith(".") and d not in SKIP_DIRS
        )
        filenames = sorted(f for f in filenames if not f.startswith("."))
        yield dirpath, dirnames, filenames


def days_since(datestr):
    for fmt in ("%Y-%m-%d", "%Y/%m/%d"):
        try:
            d = datetime.datetime.strptime(str(datestr).strip()[:10], fmt).date()
            return (datetime.date.today() - d).days
        except ValueError:
            continue
    return None


def audit(root, stale_days):
    issues = {k: [] for k in (
        "missing_index", "unregistered", "phantom_rows", "broken_links",
        "frontmatter", "stale", "secrets", "zones",
    )}

    md_paths, index_text, all_basenames = [], {}, {}

    for dirpath, dirnames, filenames in walk(root):
        rel_dir = os.path.relpath(dirpath, root)
        rel_dir = "" if rel_dir == "." else rel_dir

        # 1. every folder needs an index.md (root uses AGENTS.md instead)
        if rel_dir == "":
            if ROOT_MARKER not in filenames:
                issues["missing_index"].append(f"/ (no {ROOT_MARKER} at vault root)")
        elif "index.md" not in filenames:
            issues["missing_index"].append(rel_dir + "/")

        idx = os.path.join(dirpath, "index.md")
        if os.path.isfile(idx):
            index_text[rel_dir] = read(idx)

        for fn in filenames:
            if fn.endswith(".md"):
                rel = os.path.join(rel_dir, fn) if rel_dir else fn
                md_paths.append(rel)
                all_basenames.setdefault(fn[:-3], []).append(rel)

    # 2. contents missing from their parent registry
    for dirpath, dirnames, filenames in walk(root):
        rel_dir = os.path.relpath(dirpath, root)
        rel_dir = "" if rel_dir == "." else rel_dir
        parent_text = index_text.get(rel_dir)
        if parent_text is None:
            continue
        for fn in filenames:
            stem, ext = os.path.splitext(fn)
            if ext not in (".md", ".py", ".sh", ".js") or fn in ROOT_FILES:
                continue
            if stem not in parent_text:
                issues["unregistered"].append(
                    f"{os.path.join(rel_dir, fn) if rel_dir else fn}  (not in {rel_dir or '.'}/index.md)"
                )
        for dn in dirnames:
            if dn not in parent_text:
                issues["unregistered"].append(
                    f"{os.path.join(rel_dir, dn) if rel_dir else dn}/  (folder not in {rel_dir or '.'}/index.md)"
                )

    # 3+4. link integrity, both directions
    for rel in md_paths:
        text = read(os.path.join(root, rel))
        holder = os.path.dirname(rel)
        for target in wikilinks(text):
            if os.path.isfile(os.path.join(root, target + ".md")):
                continue
            if os.path.isfile(os.path.join(root, holder, target + ".md")):
                continue
            if os.path.basename(target) in all_basenames:
                continue
            bucket = "phantom_rows" if os.path.basename(rel) == "index.md" else "broken_links"
            issues[bucket].append(f"{rel} -> [[{target}]]")

    # 5+6+7. per-file content checks
    for rel in md_paths:
        text = read(os.path.join(root, rel))
        fm = frontmatter(text)
        if rel == "README.md":  # human-facing; rendered by GitHub, so no frontmatter
            pass
        elif not fm:
            issues["frontmatter"].append(f"{rel}  (no frontmatter)")
        else:
            missing = [k for k in REQUIRED_FM if k not in fm]
            if missing:
                issues["frontmatter"].append(f"{rel}  (missing: {', '.join(missing)})")
            if fm.get("status") == "active" and "updated" in fm:
                age = days_since(fm["updated"])
                if age is None:
                    issues["frontmatter"].append(f"{rel}  (unparseable updated: {fm['updated']})")
                elif age > stale_days:
                    issues["stale"].append(f"{rel}  (active, untouched {age} days)")

        if "allow agent write" in fm and fm["allow agent write"].lower() not in ("true", "false"):
            issues["frontmatter"].append(
                f"{rel}  (allow agent write must be true or false, got {fm['allow agent write']!r})"
            )

        for problem in check_zones(text):
            issues["zones"].append(f"{rel}  ({problem})")

        if not rel.startswith("_ai/config" + os.sep) and rel != "_ai/config/index.md":
            for m in SECRET_RE.finditer(strip_code(text)):
                issues["secrets"].append(f"{rel}  (looks like a {m.group(1)})")

    return issues, len(md_paths)


HEADINGS = [
    ("missing_index", "Folders with no index.md"),
    ("unregistered", "Not registered in their parent index"),
    ("phantom_rows", "Registry rows pointing at nothing"),
    ("broken_links", "Broken wikilinks"),
    ("frontmatter", "Frontmatter problems"),
    ("stale", "Stale active items"),
    ("zones", "Zone marker problems"),
    ("secrets", "Possible credentials outside _ai/config"),
]


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    flags = [a for a in sys.argv[1:] if a.startswith("--")]
    if len(args) != 1:
        print(__doc__)
        return 2

    root = os.path.abspath(os.path.expanduser(args[0]))
    if not os.path.isfile(os.path.join(root, ROOT_MARKER)):
        print(f"Not a vault (no {ROOT_MARKER} at root): {root}", file=sys.stderr)
        return 2

    stale_days = 90
    for f in flags:
        if f.startswith("--stale-days"):
            stale_days = int(f.split("=")[1]) if "=" in f else stale_days

    issues, scanned = audit(root, stale_days)
    total = sum(len(v) for v in issues.values())

    if "--json" in flags:
        print(json.dumps(
            {"vault": root, "scanned": scanned, "total_issues": total, "issues": issues},
            indent=2,
        ))
        return 1 if total else 0

    print(f"Vault audit: {root}")
    print(f"{scanned} notes scanned, {total} issue(s)\n")
    if not total:
        print("Clean. Registries match contents, links resolve, frontmatter complete.")
        return 0
    for key, title in HEADINGS:
        rows = issues[key]
        if rows:
            print(f"{title}  ({len(rows)})")
            for r in rows:
                print(f"  - {r}")
            print()
    return 1


if __name__ == "__main__":
    sys.exit(main())
