---
type: skill
name: orient
module: vault
status: active
created: 2026-09-14
updated: 2026-11-17
triggers: [where is, where does this go, what is in my vault, what am I working on, show me, remind me about, explain my vault]
summary: Answer where things are and what state they are in, from the indexes, without scanning the vault.
---

# orient

Read-only. Answers questions about the vault from its registries. **Writes nothing** except a stale-index fix (see below).

The discipline that matters here: the answer comes from indexes, not from reading files. Reading twenty notes to answer "what am I working on" defeats the entire structure.

## Four question shapes

**"Where does this go?"** — Answer from the decision list in `AGENTS.md` §8. State the folder and why. No files need to be read at all.

**"Where is X?" / "What do I know about X?"** — Route via `AGENTS.md` §4 to one area index, scan its registry, name the file and its path. Open the file only if the owner wants the contents rather than the location.

**"What am I working on?" / "What's the state of things?"** — Read `home/projects/index.md` and `home/activities/index.md`. Report **active items only**, with their next action. Mention paused or blocked items in one line if any exist. Do not open individual project files.

**"Explain my vault"** — Describe it in terms of *their work*, not the folder tree. Which projects are live, what ongoing activities exist, what's being catalogued. A directory listing is not an orientation.

## Rules

- Always give the path alongside the answer, so the owner can open it in Obsidian themselves.
- Never scan `home/archives/` unless the owner asked about something archived, or every other tier failed — and say so before you do.
- Never enter `home/personal/` unless the question is personal. If personal content is relevant to a work question, say relevant personal context exists and ask before using it.
- Prefer one deep read over five shallow ones. If a registry row looks like the answer, open that file rather than opening its neighbours to compare.
- When answering from memory rather than from a registry, cite the memory file.

## When the registry can't answer

1. Search, scoped to the single relevant folder. Never vault-wide.
2. If the search finds something the registry did not list, **the registry is stale.** Add the missing row before you continue, and tell the owner you did. This is the one write `orient` is allowed to make.
3. If nothing is found anywhere, say so plainly. Do not widen into archives or personal to manufacture an answer.
