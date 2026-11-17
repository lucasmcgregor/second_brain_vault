---
type: skill
name: maintain-indexes
module: vault
status: active
created: 2026-09-14
updated: 2026-11-17
triggers: [tidy the indexes, clean up the vault, fix the registries, an audit found drift]
summary: Repair index registries so they match what is actually in the vault.
---

# maintain-indexes

Repairs the drift that [[_ai/modules/vault/skills/audit|audit]] detects. This writes, so it proposes before it acts.

The registries are the navigation system; the whole structure is worth exactly as much as they are accurate. Everything here is in service of that one fact.

## Procedure

1. **Run the audit first.** Always. Repairing from a guess about what is wrong produces new drift.
2. **Group the findings** — structural, integrity, judgement (see the audit skill).
3. **Propose.** Show the owner the list of writes you intend to make: which rows are being added, removed or corrected, in which files. Don't narrate; show the diff in substance.
4. **Apply** the approved changes, then **re-run the audit** to confirm it comes back clean. An unverified repair is not a repair.

## Repairs

**Missing registry row** — read the file's frontmatter, copy its `summary` into the row, fill the rest from `status` and `updated`. If the file has no `summary`, read enough of it to write one honest line, and add the summary to its frontmatter too so the next rebuild is free.

**Phantom row** — the registry names something that no longer exists. Look for it first: renamed, moved, archived? Repoint the row if you find it, remove it if you don't. Removing a row for a file that was merely moved loses it for good.

**Missing `index.md`** — create it from the folder's sibling indexes: purpose, conventions, registry table with the right columns for that area. Register the folder in its parent.

**Broken wikilink** — almost always a rename. Search for the target's likely new name before deleting the link. Repoint if found; remove and note it if not.

**Missing frontmatter** — add the required keys. Set `updated` to the file's actual modification date, not today's, unless you changed the content.

**Stale rows** — bring `status` and `updated` in line with reality where reality is unambiguous. Where it is not — an active project nobody has touched in months — that is the owner's call. Ask.

## Rules

- **Never delete a file** in this skill. It repairs indexes, not contents. Deleting is always the owner's decision.
- Never change a note's meaning to fit a registry row. The file is the truth; the row describes it.
- Do the whole folder at once. Half-repaired registries are indistinguishable from unrepaired ones.
- If the same drift keeps recurring in the same place, the convention is wrong, not the vault. Raise it rather than repairing it every week.
