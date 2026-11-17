---
type: skill
name: export-conversation
module: vault
status: active
created: 2026-09-14
updated: 2026-11-17
triggers: [save this conversation, export this chat, persist this discussion, write this up, capture this thread, turn this into a document, this needs to go in the vault, don't lose this]
summary: Turn a live conversation into a filed document, choosing its shape and its home rather than dumping a transcript.
---

# export-conversation

Takes work that happened **in conversation** and makes it a document in the vault. The ad-hoc case: no project was open, no module owned it, but something worth keeping got said.

The failure this skill exists to prevent is the transcript dump — a wall of dialogue filed under a date, which nobody reads again and which no registry row can honestly summarise. A conversation that mattered becomes a document that stands on its own, or it does not get exported.

## Which skill is this, actually

Three skills write at the end of a conversation. They write different things and are not interchangeable:

| If what matters is… | Use | It produces |
|---|---|---|
| Something the owner handed you, already formed | [[_ai/modules/vault/skills/capture\|capture]] | That thing, filed |
| **The thinking that happened in the conversation** | **export-conversation** | **A new document that stands alone** |
| Where the work got to, so the next session continues | [[_ai/modules/vault/skills/checkpoint\|checkpoint]] | Task state and handoffs in `_ai/memory/` |

They compose. A long working session commonly exports a document *and* checkpoints. Run export first — the checkpoint should be able to point at the document you just filed.

Once the destination is chosen, the filing mechanics are `capture`'s: frontmatter, naming, same-turn registration, linking. Do not reinvent them here.

## Procedure

1. **Decide it is worth exporting.** Not every conversation is. If it reached no conclusion, produced no reusable reasoning, and changed no decision, say so and offer a `checkpoint` instead. Exporting nothing costs the owner a registry row and a file they will open once.

2. **Decide how many documents it is.** This is the step that gets skipped, and it is the one that determines whether the export is any good. A single conversation frequently contains:
   - a **decision** (with its alternatives and reasoning) → `_ai/memory/permanent/` if it governs how you behave, `home/` if it governs their work
   - **reference material** worked out along the way → `home/documents/`
   - the **start of a piece of work** → a new project or activity folder
   - **preferences** the owner stated in passing → `_ai/memory/permanent/`

   One idea per file (`AGENTS.md` §7). Say what you found and how you intend to split it before you write.

3. **Propose the destination.** Route with the decision list in `AGENTS.md` §8 and state the reasoning in one line: *"This is reference they'll look up, not work with an end — `home/documents/`."* Recommendation first, then the alternative you rejected. If the owner is unavailable (scheduled or unattended run), file to `_ai/memory/transient/`, register it, and flag that it needs a home. Never guess a permanent location unattended.

4. **Write the document** in the shape below — not as dialogue.

5. **File it** per [[_ai/modules/vault/skills/capture\|capture]]: frontmatter, hyphenated name, registry row in the parent `index.md` **in the same turn**, `[[wikilinks]]` out to related notes and back from them where it matters.

6. **Close the loop.** If the conversation opened work that continues, run `checkpoint` and link the new document from the transient row. Tell the owner in one line: what you wrote, where, and why there.

## The shape of an exported conversation

Write for a reader who was not in the room — which includes the owner in six months, and every future agent. Prose and headings, not speaker turns.

- **What this was** — one paragraph of context. Why the conversation happened at all.
- **What was concluded** — the substance. Lead with it.
- **Why** — the reasoning, and what was considered and rejected. A conclusion without its alternatives looks authoritative and cannot be revisited safely; this is the part a transcript preserves by accident and a bad summary destroys.
- **Open questions** — what was not settled. Name it rather than rounding it off to a conclusion.
- **Next actions** — only if there are real ones. An empty section is noise.

Frontmatter `summary` is the registry row, so write it as a claim about the content, not a label: *"Decided the vault module stays single; split trigger recorded"* beats *"Notes from a conversation about modules."*

## Verbatim text

Distil by default. Keep exact wording only where the wording itself is the artifact — a sentence they want to reuse, a name or phrase that was argued over, an instruction to be quoted back later. Put it in a `> quote` inline where it belongs, attributed and dated.

Append a full transcript only when the owner asks for one, and then as a separate `-transcript` file linked from the document, so the useful half stays readable. Never let the transcript *be* the document.

## Rules

- **Distinguish what was said from what was decided.** Half a conversation is exploration that was abandoned. Exporting a discarded idea as a conclusion puts a false fact in the vault, and the vault is the memory — a false document is a false memory.
- **Do not invent tidiness.** If the conversation ended mid-thought, the document says so. A clean write-up of an unresolved discussion is worse than an honest messy one.
- Attribute properly: what the owner decided, what you proposed, what is still open. In six months the distinction matters and nothing else records it.
- Date it in the frontmatter and in the opening paragraph. An exported conversation is a snapshot of what was known then.
- If the conversation changed something already in the vault, **update that file too** — and say you did. An export that leaves a superseded note standing creates two answers to the same question. Supersede per `AGENTS.md`: `status: archived` plus `Superseded by [[...]]`, never a silent overwrite.
- Never write conversational scratch into `home/`. If it is not finished enough to be their document, it goes in `_ai/memory/transient/` until it is.

## Changelog

- **2026-09-14** — created. Splits the ad-hoc conversation case out of `capture`, which assumed a formed artifact.
