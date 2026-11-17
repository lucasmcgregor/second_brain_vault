---
type: document
status: active
created: 2026-09-14
updated: 2026-11-17
summary: One-time setup for Claude Cowork / desktop — the loader stub that makes it pick up this vault and its module.
---

# Loading the vault into Claude Cowork

Client-specific. For other agents, and for Claude Code, see [[_ai/modules/vault/bootstrap/connect-an-agent|connect-an-agent]].

There is a gap to close: connecting the vault folder to a Cowork session lets Claude *read* the files, but nothing tells it to read `AGENTS.md` and boot. The loader stub below closes it.

The stub is deliberately **a pointer, not logic**. Every rule, skill and convention stays in the vault, versioned with it. The stub only says where the vault is and what to read first — so it should never need changing, and the vault stays the single source of truth.

## Setup (once)

1. Connect the vault folder to Cowork, so Claude can read and write it.
2. Save the block below as a skill named `vault` on the owner's machine — typically `~/.claude/skills/vault/SKILL.md`. If the path isn't right on their setup, paste the block into Cowork and ask it to save it as a skill called `vault`.
3. Replace `<VAULT_PATH>` with the vault's absolute path — the folder containing `AGENTS.md`.
4. Turn off Claude's own memory so nothing about the vault is kept on Claude's side — see [[_ai/modules/vault/bootstrap/connect-an-agent|connect-an-agent]] § Keep memory in the vault.
5. Test: start a fresh session and say "mount the vault". It should report the vault path, the modules available, and any open work.

```markdown
---
name: vault
description: Load the owner's Obsidian vault and its agent system. Use at the start of any session that touches the vault, whenever the owner says "mount the vault" or "load the vault", and before answering anything about their projects, activities, documents or notes.
---

# vault

The vault is at `<VAULT_PATH>`.

This file contains no rules. It only points at them.

1. Read `<VAULT_PATH>/AGENTS.md` in full and follow its boot protocol.
2. That will send you to `_ai/index.md`, then `_ai/memory/transient/index.md`.
3. Read `_ai/modules/vault/SKILL.md` — the vault keeper module — and follow it.

If anything here ever conflicts with the vault's `AGENTS.md`, the vault wins.
```

## Scheduled tasks

A scheduled task starts a fresh session with no memory of any conversation, so its prompt must mount the vault itself. Begin every vault-touching task prompt with:

> Mount the vault at `<VAULT_PATH>` — read AGENTS.md and follow its boot protocol — then …

The task then runs unattended: it won't ask questions, it records its assumptions in the mount receipt, and it leaves its output as a registered file in `_ai/memory/transient/` for the next session to pick up. See [[_ai/modules/vault/skills/mount|mount]].

A weekly health sweep is the obvious first one:

> Mount the vault at `<VAULT_PATH>`, run the audit skill, and write the report to `_ai/memory/transient/`.

## If the vault moves

Change `<VAULT_PATH>` in the stub, and in any scheduled task prompts. Nothing inside the vault stores its own absolute path except the mount receipt, which is overwritten on the next mount.
