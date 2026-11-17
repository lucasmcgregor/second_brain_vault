---
type: skill
name: archive
module: vault
status: active
created: 2026-09-14
updated: 2026-11-17
triggers: [this is finished, put this away, archive this, we are done with, clean up finished projects]
summary: Retire finished or dormant work into archives without leaving it half-moved.
---

# archive

Moves finished work into `home/archives/`. The failure this skill exists to prevent is the half-archived state: folder moved, registries not updated, so the project shows as active in one index and as archived in another.

## Ask first, always

Archiving is the owner's decision, never an inference from a project looking finished. Propose it, state what you would move and why, and wait. Under a scheduled task, flag the candidate and stop — do not archive unattended.

## Procedure

Run all six steps or none. A partial archive is worse than no archive.

1. **Promote what should outlive it.** Durable decisions → `_ai/memory/permanent/`. Reusable reference → `home/documents/`. Archives are cold storage, not a lookup path — anything that will be needed again must leave before the move.
2. **Move it whole**, preserving internal structure. Don't flatten a project folder into a file on the way out.
3. **Mark it**: `status: archived` in frontmatter, and a line at the top of its index — what it was, when archived, why.
4. **Update both registries** — add the row in `home/archives/index.md`, remove it from the source area's index. Both, in the same turn.
5. **Fix inbound links.** Search active areas for `[[wikilinks]]` pointing at what you moved and repoint them. An active project linking into cold storage is how archives get scanned by accident.
6. **Verify** — run the audit. It catches exactly the mistakes this procedure is prone to.

## Unarchiving

Move it back to its proper area, clear the `archived` status, restore its registry row there, remove the archives row, repoint links. **Never work on a file in place inside archives** — that leaves live work somewhere nothing is allowed to scan.

## Judgement

- A project with no movement for months is a *candidate*, not a decision. Paused, finished and abandoned look identical from the outside and are filed differently.
- An activity that stopped is archived; an activity between bursts is `paused`. Ask which.
- If the owner wants something deleted rather than archived, confirm once, then delete. Archiving is the default alternative to deletion, not a substitute for their judgement.
