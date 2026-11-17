---
type: index
status: active
created: 2026-09-14
updated: 2026-11-17
summary: Registry of the agent system — modules, tools, memory and config for this vault.
---

# _ai — Agent System

**This is where you start.** Boot step 3, after the root `AGENTS.md` and the two core instruction files.

Everything the agent system is made of lives here as files: instructions, capabilities, memory, scripts and configuration. Nothing is installed into any agent client, and nothing is stored outside the vault. Mounting this vault *is* the installation.

## Core instructions

Read both at every boot, before anything else in this folder.

| File | What it governs |
|---|---|
| [[_ai/global-instructions\|global-instructions.md]] | Behaviour and context for any task run in the vault — precedence, working principles, unattended runs, the owner's own preferences |
| [[_ai/document-conventions\|document-conventions.md]] | Sharing a document without corrupting it — frontmatter directives, zone markers, write-safety rules |

## Layout

| Folder | Purpose | Read at boot? |
|---|---|---|
| [[_ai/config/index]] | Configuration, credentials, endpoints | No — only when a tool needs it |
| [[_ai/memory/index]] | Long-term agent memory | Transient index: yes. Permanent: on demand |
| [[_ai/modules/index]] | Agents and skills | Registry yes, module bodies on demand |
| [[_ai/tools/index]] | Scripts the agent runs in its sandbox | No — only when invoking one |

## Module registry

Modules are skills and agents in the open `SKILL.md` format, defined as files here rather than installed into any client. Load a module by reading its file; load only what the current task needs.

| Module | Triggers on | Purpose | Updated |
|---|---|---|---|
| [[_ai/modules/vault/SKILL\|vault]] | First run, "set up the vault"; session start; "where is…", "file this", "save this conversation", "tidy up", "vault health", "archive this", end of session | Maintains the vault itself — setup, mount, capture, orient, audit, repair, checkpoint, archive | 2026-11-17 |

## Tool registry

| Tool | Language | What it does | Used by | Updated |
|---|---|---|---|---|
| `vault-audit.py` | Python 3 (no deps) | Read-only health scan: unregistered files, phantom rows, broken links, frontmatter gaps, stale items, misplaced secrets | vault / audit | 2026-11-17 |

## Loading protocol

1. Read this index.
2. Match the task against the **Triggers on** column above.
3. Read only the matching module files. If nothing matches, proceed without a module — do not load everything as a fallback.
4. If a module names a tool, check the tool registry before writing new code. Do not reimplement a tool that already exists.
5. If you find yourself doing the same multi-step procedure a second time, propose a module for it.

## Rules for this folder

Editing anything under `_ai/` changes how every future session behaves. Per root `AGENTS.md` §9:

- Announce that you are changing the agent system before you write.
- Propose changes to modules, permanent memory and instruction files rather than making them silently.
- Every module and tool carries frontmatter with an `updated` date and a changelog section.
- Secrets live only in `_ai/config/`, and their contents are never echoed into chat.
- Register a new module or tool in the tables above **in the same turn** you create it.
