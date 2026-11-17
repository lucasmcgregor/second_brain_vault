---
type: skill
name: capture
module: vault
status: active
created: 2026-09-14
updated: 2026-11-17
triggers: [file this, save this, capture this, add this to my vault, make a note of, remember this]
summary: Route a new piece of material to the right folder with correct frontmatter and a registry entry.
---

# capture

Takes something loose — a thought, a link, a document, a decision — and files it properly. The everyday skill, and the one that decides whether the vault stays navigable or silently fills with unfiled notes.

## Procedure

1. **Decide what it is** using the decision list in `AGENTS.md` §8:
   - Has a goal and an end → `home/projects/`
   - Ongoing, no end date → `home/activities/`
   - Information the owner will look up later → `home/documents/`
   - Personal or private → `home/personal/` (this wins over the others)
   - Something *you* need to remember across sessions → `_ai/memory/permanent/`
   - Something you need only until this task ends → `_ai/memory/transient/`
2. **Check it isn't a duplicate.** Read the target folder's registry first. Updating an existing note beats creating a near-copy — near-duplicates are how a reference collection becomes unusable.
3. **Name it** for its subject: lowercase, hyphenated, no spaces. Dated notes take an ISO prefix.
4. **Write it** with full frontmatter (`AGENTS.md` §7). The `summary` line is not optional — it becomes the registry row.
5. **Register it** in the parent `index.md` in this same turn.
6. **Link it** — add `[[wikilinks]]` to related notes, and where it matters, a link back from those notes. The graph is how the owner navigates by hand.
7. **Confirm** in one line: what you filed, where, and why there.

## When the destination is ambiguous

Ask — briefly, with your recommendation first. Filing something in the wrong place is cheap to fix; the expensive failure is filing it somewhere they will never look.

Two cases that come up constantly:

- **Project or activity?** If there is a definition of "done", it is a project. If it will still be running next year in the same shape, it is an activity. When both fit, make the project and link it from the activity.
- **Document or memory?** If *the owner* will look it up, it is a document in `home/`. If *you* need it to behave correctly, it is memory in `_ai/`. Facts about the world are theirs; facts about how they want to work are yours.

If the owner is unavailable (scheduled task), file it to `_ai/memory/transient/`, register it, and note that it needs a home. Never guess a permanent location unattended.

## Rules

- **Never write scratch or drafts into `home/`.** The owner's half stays clean.
- Never create a new top-level folder without asking.
- When creating a new subfolder, create its `index.md` at the same time and register the folder in its parent.
- If what the owner handed you is really several things, say so and file them separately. One idea per file.
