---
type: index
status: active
created: 2026-09-14
updated: 2026-11-17
summary: Long-term agent memory, split into permanent and transient; the vault's only memory store.
---

# _ai/memory — Agent Memory

This folder is the **entire memory of the agent system.** Nothing is retained in a chat, in a model, or in an external service. If it is not written here, the next session will not know it.

That constraint is deliberate. It means the owner can read, edit, correct and delete what the agents remember, and it means any account or client can pick the work up cold.

## Two kinds of memory

| | [[_ai/memory/permanent/index\|permanent/]] | [[_ai/memory/transient/index\|transient/]] |
|---|---|---|
| Holds | Decisions, preferences, facts, profiles, conventions | Task state, scratch, handoffs, drafts |
| Lifespan | Until explicitly revised | Until the task finishes |
| Read at boot | On demand | **Always** |
| Deleted when | Superseded — and then superseded, not erased | The task is done and outcomes are promoted |

## Write protocol

Before ending any turn that produced something worth keeping, ask: *what would the next session need in order to continue?* Write that, then.

- **A decision was made** → permanent. Record what was decided, the alternatives, and the reasoning. Outcomes without reasons rot.
- **A preference was expressed** → permanent. "The owner prefers X" is worth a line forever.
- **A task is mid-flight** → transient. Write state before you run out of turn, not after.
- **A process is handing off to another process** → transient, as a handoff document naming the intended reader.
- **In doubt** → transient. Promoting later is cheap; a bloated permanent memory is not.

## Recall protocol

1. Read `transient/index.md` at boot — always.
2. Read `permanent/index.md` when the task touches prior context, a stated preference, or anything phrased as "we decided" / "you said" / "last time".
3. **Cite the file you recalled from.** "Per `[[decisions/naming-convention]]`…" — never state a remembered fact without its source, so the owner can check and correct it.
4. If memory and the owner disagree, the owner is right. Then update the memory file and say you did.

## Promotion and expiry

- When a transient task finishes, promote its durable conclusions into `permanent/` and delete the rest.
- When a permanent memory is superseded, mark it `status: archived`, add a pointer to what replaced it, and keep it. Memory should be revisable but not silently rewritten.
