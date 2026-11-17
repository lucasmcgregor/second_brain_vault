---
type: skill
name: mount
module: vault
status: active
created: 2026-09-14
updated: 2026-11-17
triggers: [mount the vault, load the vault, start a session, any scheduled task that touches the vault]
summary: Make the vault available to this session and to any agent or task that follows it.
---

# mount

Makes the vault live. First action of any session that touches it, including unattended and scheduled ones.

## Preconditions

The vault folder is connected to the session as a local folder, and `<vault>/AGENTS.md` exists.

If the folder is not connected, say so plainly and stop. **Do not search the filesystem for it, and do not create a vault.** A vault conjured in the wrong place is worse than no vault — the real one silently stops receiving work.

## Procedure

1. **Confirm** `<vault>/AGENTS.md` exists. Note the absolute path; you will need it for the receipt.
2. **Read `AGENTS.md`** in full. It is the rules, not a summary.
3. **Read `_ai/global-instructions.md` and `_ai/document-conventions.md`** — behaviour and document handling. Both are binding on everything that follows.
4. **Read `_ai/index.md`** — module and tool registries.
5. **Read `_ai/memory/transient/index.md`** — open work and handoffs.
6. **Load matching modules only.** This module is always loaded. Others load if their triggers match the task; if nothing matches, load nothing else.
7. **Write the mount receipt** (below).
8. **Report** — see Reporting.

Do not read anything under `home/` during mount. Routing does that on demand, and mounting should stay cheap enough that nobody is tempted to skip it.

## The mount receipt

Overwrite `_ai/memory/transient/mount-status.md` — one file, replaced each mount, never a growing log:

```yaml
---
type: memory
status: active
created: 2026-09-14
updated: <today>
summary: Most recent vault mount.
---
```

Body: absolute vault path · mount timestamp · who mounted it (this session, or the scheduled task's name) · modules available · count of open items and handoffs found · any warnings.

This is how the vault coordinates across processes. A scheduled task that runs at 07:00 and a conversation at lunchtime never speak to each other, but both can read this file to confirm the vault is live, where it is, and what exists inside it — without repeating the whole boot chain.

## The mount contract

After a successful mount, any skill or agent may rely on all of these:

- the vault's absolute path is known;
- the rules in `AGENTS.md`, `global-instructions.md` and `document-conventions.md` are in force;
- the module and tool registries are known;
- open work and handoffs are known;
- `mount-status.md` is current.

Explicitly **not** guaranteed: that the indexes are *accurate* (that is `audit`'s job), or that any part of `home/` has been read. Do not assume either.

## Reporting

**Attended** — report briefly and wait: vault path, open work, anything that looks stale. If the About the owner zone in `_ai/global-instructions.md` is empty, this is a fresh vault: offer to run [[_ai/modules/vault/skills/setup|setup]]. Do not start work the owner has not asked for.

**Unattended** (scheduled task, no one watching) — do not ask questions. Proceed on the most reasonable reading, record the assumption in the receipt, and carry on. If a precondition genuinely fails, write a `handoff-` file to `_ai/memory/transient/` describing what blocked, register it, and stop. Do not improvise around a missing vault.

## Failure modes

| Symptom | Do |
|---|---|
| Folder not connected | Say so; ask the owner to connect it. Do not go looking. |
| No `AGENTS.md` at root | This is not the vault. Stop and say which path you checked. |
| Transient index full of finished-looking work | Flag it; offer to run `checkpoint` cleanup. Do not silently ignore rows. |
| Folder connected read-only | Mount, report read-only, and refuse write skills rather than failing halfway through one. |
