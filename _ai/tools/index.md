---
type: index
status: active
created: 2026-09-14
updated: 2026-11-17
summary: Scripts and executables the agent runs in its sandbox, versioned in the vault rather than rewritten each session.
---

# _ai/tools — Tools

Scripts the agent runs in its sandbox. When a task is repetitive or must be deterministic, it belongs in code, and that code belongs here — versioned in the vault like memory and modules, not regenerated from scratch every session.

**Check this registry before writing a script.** A tool that already exists has already been tested.

## Registry

Mirror every row into the tool registry in [[_ai/index]] when you add one.

| Tool | Language | What it does | Inputs → Outputs | Used by | Updated |
|---|---|---|---|---|---|
| `vault-audit.py` | Python 3 (stdlib only) | Read-only health scan of the whole vault | vault path → text report, or `--json` | [[_ai/modules/vault/skills/audit\|vault / audit]] | 2026-11-17 |

**vault-audit.py** — `python3 _ai/tools/vault-audit.py <vault> [--json] [--stale-days=N]`
Exit `0` clean · `1` issues found · `2` not a vault. Detects: folders with no index, files missing from their parent registry, registry rows pointing at nothing, broken wikilinks, missing frontmatter, stale active items, possible credentials outside `_ai/config/`. It never writes — repairs are [[_ai/modules/vault/skills/maintain-indexes|maintain-indexes]]'s job. New checks belong in this script, not in a skill doing them by hand.

## Conventions

- One tool per file, named for what it does: `merge-csv.py`, `extract-frontmatter.py`.
- Every tool opens with a docstring/header: purpose, usage example, arguments, exit codes, dependencies.
- Take arguments; do not hard-code paths. Never hard-code credentials — read them from [[_ai/config/index]].
- Deterministic and idempotent where possible: running it twice should not corrupt anything.
- Fail loudly with a clear message rather than silently producing a wrong result.

## Running a tool

Run a tool by passing it the vault path. If your client executes code in a separate sandbox, copy the tool there first. Never write scratch output back into `_ai/tools/`.

## Maintenance

- When you fix a bug in a tool, fix it **in the vault file**, not just in the copy you ran. Otherwise the fix is lost.
- Bump `updated` and note the change in the file header.
- If a tool is superseded, mark it and point to its replacement rather than deleting it outright.
