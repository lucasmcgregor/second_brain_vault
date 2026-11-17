---
type: index
status: active
created: 2026-09-14
updated: 2026-11-17
summary: Working memory and the handoff board — read this at every boot to find open work.
---

# _ai/memory/transient — Working Memory

Short-lived memory: task state, scratch, drafts, and the handoff board where processes leave work for each other.

**Read this index at every boot.** It is how a session finds out what the last one left unfinished.

## Open work

Anything listed here is incomplete. Clear the row when the task is done.

| Item | Task | Left by | Waiting on | Since |
|---|---|---|---|---|
| _(nothing open)_ | | | | |

## Handoffs

The vault coordinates agents through documents, not direct calls. A process that produces output another process should act on writes a handoff file here and adds a row below.

| Handoff | From | Intended reader | Status | Written |
|---|---|---|---|---|
| _(none)_ | | | | |

A handoff document states: what was produced, where it is, what the reader is expected to do with it, and anything the reader must not assume. Write it so a different model on a different account could act on it with no other context.

## Conventions

- Prefix working files with their task: `budget-review-scratch.md`.
- Prefix handoffs with `handoff-`: `handoff-budget-review-to-drafting.md`.
- Set `status: active | blocked | done` in frontmatter and keep it honest.
- **Write state before you run out of turn**, not after. A session can end at any point; anything only in your context is lost.

## Cleanup protocol

When a task finishes:

1. Promote anything durable into [[_ai/memory/permanent/index|permanent/]].
2. Delete the scratch — ask first if you are unsure whether it was durable.
3. Clear the rows above.

Stale rows are worse than empty ones: a boot that reads three finished tasks as open wastes the session. If a row is older than a month with no movement, flag it to the owner rather than leaving it.
