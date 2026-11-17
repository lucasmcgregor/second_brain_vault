---
type: skill
name: audit
module: vault
status: active
created: 2026-09-14
updated: 2026-11-17
triggers: [vault health, audit the vault, is my vault tidy, check the vault, scheduled weekly sweep]
summary: Run the deterministic health scan, interpret the result, and propose fixes.
---

# audit

Finds drift between what is in the vault and what its registries claim. **Read-only** — it detects; [[_ai/modules/vault/skills/maintain-indexes|maintain-indexes]] repairs.

## Run the tool, don't do this by hand

```bash
python3 <vault>/_ai/tools/vault-audit.py <vault>
python3 <vault>/_ai/tools/vault-audit.py <vault> --json          # for scheduled tasks
python3 <vault>/_ai/tools/vault-audit.py <vault> --stale-days=30
```

Exit codes: `0` clean · `1` issues found · `2` not a vault.

Reading every file to check for drift is slow, expensive and misses things. The tool is deterministic and complete. Use it. If it needs a new check, add the check to the tool rather than doing that check by hand — that is the whole point of `_ai/tools/`.

## What it reports, and what each finding means

| Finding | What it actually means | Fix |
|---|---|---|
| Folder with no `index.md` | A folder is invisible to navigation | Create the index, register it in the parent |
| Not registered in parent index | A file exists that no agent will ever find | `maintain-indexes` |
| Registry row pointing at nothing | The index promises something that isn't there | Remove the row, or find where the file went |
| Broken wikilink | Usually a rename that didn't update inbound links | Repoint or remove |
| Frontmatter problem | Breaks registry rebuilds and Obsidian search | Add the missing keys |
| Stale active item | A project or activity marked live that nobody has touched | Raise with the owner — `paused`, `done`, or genuinely still live? |
| Possible credential outside `_ai/config` | A secret in the wrong place | Move it to `_ai/config/`, tell the owner, don't echo the value |

## Triage

Do not dump the raw output. Group it:

1. **Structural** — missing indexes, unregistered files. Breaks navigation. Fix now.
2. **Integrity** — phantom rows, broken links, frontmatter. Degrades quality. Fix in batch.
3. **Judgement** — stale items, possible secrets. Needs the owner's decision. Ask, don't act.

Then offer to run `maintain-indexes` on groups 1 and 2, and put group 3 to the owner as questions.

Stale-item findings are not defects. A project untouched for three months might be paused, finished, or abandoned — only the owner knows which. Ask; never set the status yourself.

## Unattended runs

A scheduled audit uses `--json`, writes a dated report to `_ai/memory/transient/`, registers it, and adds an open-work row **only if** there are structural or integrity findings. Do not wake the owner for a clean vault. Never auto-fix judgement findings, and never move a suspected credential without telling the owner.
