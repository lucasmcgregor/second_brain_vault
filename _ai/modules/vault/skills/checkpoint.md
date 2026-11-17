---
type: skill
name: checkpoint
module: vault
status: active
created: 2026-09-14
updated: 2026-11-17
triggers: [before we finish, save where we got to, checkpoint, hand this off, end of session, context running low]
summary: Write session state, decisions and handoffs into vault memory so the next session can continue cold.
---

# checkpoint

The skill that makes "no memory outside the vault" survive contact with reality. Run it before a session ends, before a handoff, and whenever context is getting long.

The test to apply: **could a different model, on a different account, on a different machine, pick this up tomorrow with only the vault?** If not, you have not checkpointed.

## When

- The owner signals the session is ending.
- Work is handing off to another process or a scheduled task.
- Context is getting long — checkpoint *before* the squeeze, not during it.
- A decision was just made. Don't wait for the end of the session for this one.

## Procedure

1. **Sort what happened** into three piles:
   - **Durable** — decisions, preferences, facts that will matter in six months → `_ai/memory/permanent/`
   - **In-flight** — where the work got to, what's next → `_ai/memory/transient/`
   - **Disposable** — everything else. Don't write it.
2. **Write the durable items.** One subject per file. Record *what* was decided, *what else* was considered, and *why*. An outcome without its reasoning is useless later, and worse, it looks authoritative.
3. **Write the in-flight state** to a task file in `transient/`: what's done, what's next, what's blocked, what you were about to do.
4. **Write a handoff** if another process should act: `handoff-<task>-to-<reader>.md`, stating what was produced, where it is, what the reader should do, and what they must not assume. Write it for a reader with no context, because that is what they will have.
5. **Update `transient/index.md`** — open work rows and handoff rows.
6. **Update the work's own index** — project or activity status and next action.
7. **Tell the owner in one line** what you wrote and where.

## Rules

- **Write before you run out of turn, not after.** A session can end at any point. State only in your context is state that is already lost.
- Promote to `permanent/` sparingly. A bloated permanent memory gets skimmed, and skimmed memory is unreliable memory. When in doubt, transient.
- Never overwrite a permanent memory that is merely out of date: set `status: archived`, add `Superseded by [[...]]`, write the new one. Memory should be revisable, not quietly rewritten.
- Clear finished rows from `transient/index.md`. Three completed tasks listed as open is worse than an empty table — it wastes every future boot.
- Don't checkpoint nothing. If the session produced no durable state, say so and write nothing.
