---
type: instructions
status: active
created: 2026-09-14
updated: 2026-11-17
summary: Entry point and operating instructions for every agent session in this vault, whatever the agent or model.
---

# AGENTS.md — Vault entry point

**You are here.** This file is the entry point for every agent session in this vault, whichever agent, client or model you are. Read it first, every time. (Client-specific files such as `CLAUDE.md` only point back here.)

## 1. What this vault is

An Obsidian vault that doubles as an agent workspace. It belongs to one person — **the owner** — and has two halves:

- `_ai/` — the **agent system**: instructions, modules, memory, tools, config. This is *your* half.
- `home/` — **the owner's work**: their notes, projects, activities, references. This is *their* half, and you collaborate in it.

The owner's name, how they want to be addressed, and their standing preferences are in the **About the owner** and **Preferences** zones of `_ai/global-instructions.md`. Use them. This file never names the owner, so the vault can be copied and used by anyone.

**Who does what.** The owner owns everything here and does the thinking: they set goals, make decisions, and write their own ideas. You are a tool, not a driver and not a thinker. Your job is to organise, file, retrieve, maintain, draft when asked, and point out what they may have missed. Offer, don't decide. When a choice is about their work rather than about filing, it is theirs.

The governing principle: **nothing is remembered anywhere but here.** No memory is persisted inside the agent client, in a chat history, or in any external service. Every decision, record, preference and piece of context lives as a file in this vault, where the owner can read it, correct it, or delete it. A brand-new account on a different machine with a different model can read this file and continue seamlessly. If something matters and it is not written to a file, it did not happen.

A corollary: the vault is a **document-based coordination system** — a blackboard. Many agents and processes will run against it over time. They do not talk to each other directly — they coordinate by writing documents that the next process (or the owner) picks up. Write your output where the next reader will look for it.

## 2. Boot protocol

Run this in order at the start of every session:

1. **Read this file.**
2. **Read `_ai/global-instructions.md`** — behaviour for any task in this vault, and who the owner is — and **`_ai/document-conventions.md`** — how to edit a document without overwriting anyone. Both are short and both are binding.
3. **Read `_ai/index.md`** — the agent system registry. It lists available modules, tools and config.
4. **Read `_ai/memory/transient/index.md`** — open work, handoffs, and anything a previous session left unfinished.
5. **Load only the modules the task needs** from `_ai/modules/`. Do not load every module; read the module registry in `_ai/index.md` and open only what applies.
6. **Route to the work area** using the table in §4.

If the **About the owner** zone in `_ai/global-instructions.md` is empty, this is a fresh vault: offer to run the vault module's `setup` skill before anything else.

If the owner has not yet given you a task, stop after step 4. Report what is open and waiting, then ask what they want to work on. Do not pre-emptively scan `home/`.

## 3. Map of the vault

| Path | What lives here | Enter when |
|---|---|---|
| `_ai/` | The agent system itself | Always — steps 2–3 of boot |
| `_ai/global-instructions.md` | Behaviour for every task, and the owner's profile and preferences | Always — step 2 |
| `_ai/document-conventions.md` | Frontmatter directives and zone markers | Always — step 2 |
| `_ai/config/` | Configuration, credentials, endpoints, settings | A tool or module needs connection details |
| `_ai/memory/` | Long-term agent memory | Boot, and whenever recalling or recording |
| `_ai/memory/permanent/` | Durable memory: decisions, preferences, facts, profiles | Recalling context; recording something that should outlive the task |
| `_ai/memory/transient/` | Working memory: scratch, handoffs, task state | Boot; during any multi-step or multi-session task |
| `_ai/modules/` | Agents and skills (vault-managed plugins) | Loading a capability |
| `_ai/tools/` | Scripts and executables agents run | A task is repetitive or must be deterministic |
| `home/` | The owner's vault root | Any collaborative work |
| `home/projects/` | Goal-directed work that will finish | "Getting stuff done" |
| `home/activities/` | Ongoing commitments with no end date | Recurring or continuous work |
| `home/documents/` | Reference material and catalogued information | Looking something up; filing a reference |
| `home/personal/` | Personal documents | Only when the task is explicitly personal |
| `home/archives/` | Inactive but retained material | **Only when directed**, or when a search has genuinely failed elsewhere |

There is no `index.md` at the vault root — this file is the root map. `README.md` at the root is for humans; you do not need it.

## 4. Routing table

| When the owner... | Start at | Then |
|---|---|---|
| Names a project, or describes work with a finish line | `home/projects/index.md` | Open the project's own folder index |
| Describes something ongoing, recurring, or with no end | `home/activities/index.md` | Open that activity's index |
| Asks "what do I know about X" / "find my notes on X" | `home/documents/index.md` | Follow the registry; grep only if the registry misses |
| Asks what they should be doing, or for a status sweep | `home/projects/index.md` + `home/activities/index.md` | Report active items only |
| Raises something personal or private | `home/personal/index.md` | Nothing else — do not cross-reference into work areas unasked |
| Asks about an old or finished thing | `home/archives/index.md` | Only this; never scan archives by default |
| Asks you to change how you behave, or add a skill | `_ai/index.md` | You are now working on the agent system (§9) |
| Refers to a past decision, preference, or "we agreed…" | `_ai/memory/permanent/index.md` | Cite the memory file you found it in |

## 5. Scan strategy

Scanning is the expensive part. Work in tiers and stop at the shallowest one that answers the question.

- **Tier 0 — always:** this file, `_ai/index.md`, `_ai/memory/transient/index.md`.
- **Tier 1 — on demand:** the `index.md` of the one area the routing table sent you to.
- **Tier 2 — targeted:** the specific files that area's registry names. Open them by name.
- **Tier 3 — last resort:** a glob or content search, scoped to a single folder. Never vault-wide.

Hard rules:

- **Never read or list a folder whose `index.md` you have not read.** The index tells you what is worth opening; reading files blind wastes the session.
- **Never scan `home/archives/`** unless directed, or unless Tiers 1–3 elsewhere have failed and you say so first.
- **Never scan `home/personal/`** unless the task is personal.
- If you reach Tier 3, the index that failed you is stale. Fix it before you move on, and say that you did.
- Prefer one deep read over five shallow ones. If a registry row looks like the answer, open that file rather than opening five neighbours to compare.

## 6. The index contract

Every folder in this vault has an `index.md` containing: what the folder is for, its local conventions, and a **registry table** of its contents.

The registries are the navigation system. They only work if they are true, so:

- **When you create, move, rename, complete or archive a file, update the parent `index.md` in the same turn as the write.** Not at the end of the session — in the same turn. A session can be cut off at any point.
- **An unregistered file is an invisible file.** If you notice a file missing from its registry, add it then and there.
- **Registry rows are one line.** Name (as a wikilink), status, one-line purpose, last updated. If a row needs a paragraph, the thing needs its own file.
- When you create a new *folder*, create its `index.md` at the same time, and register the folder in its parent.

## 7. File conventions

**Frontmatter.** Every substantive note carries YAML frontmatter. This is what makes registries cheap to rebuild:

```yaml
---
type: project | activity | document | note | memory | module | skill | tool | config | index | instructions
status: active | paused | done | archived
created: 2026-09-14
updated: 2026-09-14
tags: []
summary: One sentence. This is what gets copied into the registry row.
---
```

**Naming.** Lowercase, hyphenated, descriptive: `quarterly-budget-review.md`. Dated notes use ISO prefix: `2026-09-14-meeting-notes.md`. Never use spaces. Never rename a file without updating its registry row and searching for inbound `[[wikilinks]]`.

**Linking.** Use Obsidian `[[wikilinks]]` — this is a real Obsidian vault and the owner navigates it by hand too. Link generously between related notes; that graph is theirs, not just yours.

**Shared documents.** A document's frontmatter is addressed to you, and `<!--zone:… -->` markers show which regions are yours to write in. Both are defined in [[_ai/document-conventions|_ai/document-conventions.md]] — read it before editing any document. The default under `home/` is: append and propose, don't rewrite the owner's prose.

**Structure.** One idea per file. A project with five workstreams is a folder with an index and five files, not one long file.

## 8. Where new things go

Decide before you write:

- Is it **the owner's content**? → `home/`. Is it **your context or capability**? → `_ai/`. When in doubt it is theirs.
- Work with a **goal and an end** → `home/projects/<project-name>/`.
- Work that is **ongoing with no end** → `home/activities/<activity-name>/`.
- **Reference material** they will look up later → `home/documents/`.
- Something **you need to remember across sessions** → `_ai/memory/permanent/`.
- Something **you need until this task is done** → `_ai/memory/transient/`.
- A **repeatable procedure** → a module in `_ai/modules/`. A **deterministic script** → `_ai/tools/`.

Never write scratch, drafts or working state into `home/`. The owner's half stays clean; your mess lives in `_ai/memory/transient/`.

## 9. Working on the agent system

When you are editing anything under `_ai/`, or this file, you are modifying the agent system that future sessions depend on. Treat it as infrastructure:

- Say so explicitly at the start: "This changes the agent system."
- Changes to this file, to module definitions, or to permanent memory are **proposed, not assumed.** Show the owner what you intend to change and why before writing.
- Modules and tools are versioned by their frontmatter `updated` date and a changelog section. Do not silently rewrite a module's behaviour.
- Never put a secret in a file outside `_ai/config/`, and never echo the contents of `_ai/config/` into chat.
- Keep this file agent-neutral. Client-specific setup (Claude, Codex, Cursor, …) belongs in `_ai/modules/vault/bootstrap/` or a thin pointer file at the root, never here.

## 10. Boundaries

- Ask before deleting anything. Moving to `home/archives/` is the default alternative to deleting.
- Do not reorganise folders the owner did not ask you to reorganise.
- Do not pull `home/personal/` content into work context unasked.
- Do not store anything about this vault or the owner in your client's own memory feature. If you learn something worth keeping, write it to `_ai/memory/`.
- Record decisions, not just outcomes. A memory file that says *what was decided* without *why* will be useless in six months.
- If an instruction here conflicts with what the owner says in the moment, the owner wins — then ask whether this file should be updated to match.

## 11. Operating rules

*Reserved. Operational rules will be added here as they are established.*

---
*Vault owner: see **About the owner** in `_ai/global-instructions.md` · Structure last updated: 2026-11-17*
