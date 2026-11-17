---
type: index
status: archived
created: 2026-09-14
updated: 2026-11-17
summary: Inactive material kept for the record — not scanned unless explicitly directed.
---

# home/archives — Archives

Finished, dormant or abandoned material that the owner wants to keep. Kept for the record, not for working in.

## Do not scan this folder by default

This is the main rule of this folder. Enter only when:

- The owner explicitly asks about something archived or historical, **or**
- a search everywhere else has genuinely failed — and then say that you are falling back to archives before you do.

A routine question, a status sweep, or "find my notes on X" does **not** reach here. Archives exist so that the active vault stays small and fast to scan; scanning them anyway gives up the whole benefit.

## Registry

The single source of truth for what is in here. Keep it accurate — it exists so the folder itself rarely needs opening.

| Item | Was | Archived | Why | Where it came from |
|---|---|---|---|---|
| _(nothing archived yet)_ | | | | |

## Archiving protocol

1. **Ask first.** Archiving is the owner's decision, never an assumption.
2. Promote anything durable — decisions, outcomes, reusable reference — into `_ai/memory/permanent/` or `home/documents/` *before* moving. Archives are cold storage, not a lookup path.
3. Move the folder or file in whole, preserving its internal structure.
4. Set `status: archived` in its frontmatter and add a line at the top: what it was, when it was archived, why.
5. Add a registry row above; remove the row from the source area's index.
6. Check for inbound `[[wikilinks]]` from active areas and update them, so nothing active points into cold storage without warning.

## Unarchiving

If something becomes active again, move it back to its proper area, clear the `archived` status, restore its registry row there, and remove the row here. Do not work on files in place inside archives.
