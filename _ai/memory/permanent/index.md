---
type: index
status: active
created: 2026-09-14
updated: 2026-11-17
summary: Durable agent memory — decisions, preferences, facts and profiles that outlive any single task.
---

# _ai/memory/permanent — Permanent Memory

Durable memory. Things here are true until explicitly revised, and are the reason a cold session can behave like a continuing one.

## What belongs here

- **Decisions** — what was decided, what else was considered, and *why*.
- **Preferences** — how the owner likes things done: tone, formats, tools, working rhythms.
- **Facts and profiles** — stable context about people, systems, commitments, recurring constraints.
- **Conventions** — agreed patterns that are not yet formal enough to be instructions in `AGENTS.md`.

## What does not

Task state, drafts, scratch, anything that will be irrelevant next month. That is transient memory. When in doubt, start transient and promote.

## Conventions

- One subject per file. `owner-working-preferences.md`, not `notes.md`.
- Suffix decisions with their date when they supersede something: `2026-09-14-vault-structure.md`.
- Always frontmatter, always a `summary` line — that line becomes the registry row.
- **Superseding, not overwriting:** when a memory stops being true, set `status: archived`, add `Superseded by [[...]]` at the top, and write the new one. History matters.
- Every file answers: *what*, *why*, *when*, *who decided*.

## Registry

| File | Kind | Summary | Status | Updated |
|---|---|---|---|---|
| _(none yet)_ | | | | |
