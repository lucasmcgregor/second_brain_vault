---
type: module
name: vault
status: active
created: 2026-09-14
updated: 2026-11-17
triggers: [set up the vault, mount the vault, load the vault, start a vault session, where is, where does this go, what is in my vault, file this, capture this, save this conversation, write this up, tidy the indexes, vault health, audit the vault, archive this, checkpoint, before we finish]
tools: [vault-audit.py]
summary: The agent that maintains this vault — mounts it, files things into it, keeps its indexes true, and reports on its health.
---

# vault — the vault keeper

The module that maintains the vault itself. It is the **one module that is always loaded**; every other module assumes it has already run.

It works against the local filesystem — the vault is a folder on the owner's machine, connected to whatever agent client is running the session. There is no server, no sync service and no external store in the path. Read and write the files directly.

## What it is responsible for

- **Mounting** the vault so this session, and any agent or scheduled task that follows, can use it.
- **Filing** new material into the right place with the right frontmatter and registry entry.
- **Maintaining** the indexes that make the vault navigable.
- **Reporting** — telling the owner where things are and what state the vault is in.

## What it is not

It does not do the owner's work. It maintains the container their work lives in. Writing their project plan is the job of whatever module or conversation owns that project; making sure the plan is filed, registered, linked and findable next month is this module's job.

## Skills

| When the owner… | Skill | Writes? |
|---|---|---|
| Is using a fresh copy of the vault, or asks to set up | [[_ai/modules/vault/skills/setup\|setup]] | Yes — the owner profile, with approval |
| Starts a session, or a scheduled task begins | [[_ai/modules/vault/skills/mount\|mount]] | Mount receipt only |
| Asks where something is, or what state things are in | [[_ai/modules/vault/skills/orient\|orient]] | No — read-only |
| Hands you something to file | [[_ai/modules/vault/skills/capture\|capture]] | Yes |
| Wants a conversation persisted as a document | [[_ai/modules/vault/skills/export-conversation\|export-conversation]] | Yes |
| Asks for a health check, or a scheduled sweep runs | [[_ai/modules/vault/skills/audit\|audit]] | No — read-only |
| Asks you to tidy up, or an audit found drift | [[_ai/modules/vault/skills/maintain-indexes\|maintain-indexes]] | Yes |
| Finishes a session, or work hands off | [[_ai/modules/vault/skills/checkpoint\|checkpoint]] | Yes |
| Retires something finished | [[_ai/modules/vault/skills/archive\|archive]] | Yes |

Load a skill by reading its file. Load only the one that matches.

## Operating principles

1. **The vault is the memory.** If it is not written to a file here, the next session will not know it. Write before the turn ends, not after.
2. **Indexes are the interface.** Navigation happens through registries, not directory listings. A registry that lies is worse than no registry.
3. **Same-turn registration.** Create a file and register it in the same turn. A session can be cut off between the two.
4. **The owner's half stays clean.** Scratch, drafts and working state go in `_ai/memory/transient/`, never in `home/`.
5. **Propose, don't assume, under `_ai/`.** Changes here change every future session.
6. **Archive, don't delete.** Ask before either.
7. **Cite your source.** When you state something recalled from memory, name the file it came from so the owner can correct it.

## Tools

| Tool | Use |
|---|---|
| [[_ai/tools/index\|vault-audit.py]] | Deterministic health scan. Always run it rather than reading every file to check for drift — it is faster, cheaper and does not miss things. |

## Changelog

- **2026-09-14** — created. Seven skills, one tool.
- **2026-09-14** — added `export-conversation`. Eight skills. Splits the ad-hoc conversation case out of `capture`, which assumed an already-formed artifact; `checkpoint` continues to own session state rather than session content.
- **2026-11-17** — made generic: owner no longer named, owner folder renamed to `home/`, entry point `CLAUDE.md` → `AGENTS.md`, client-neutral wording. Added `setup`. Nine skills.
