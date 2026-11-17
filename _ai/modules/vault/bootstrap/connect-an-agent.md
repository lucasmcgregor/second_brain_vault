---
type: document
status: active
created: 2026-11-17
updated: 2026-11-17
summary: How to point any agent client at this vault, and how to keep that client from storing memory of its own.
---

# Connecting an agent to the vault

The vault is agent-neutral. Its entry point is `AGENTS.md` at the vault root, and every client should boot from there. What changes between clients is only **how the client finds that file** and **how you stop the client keeping memory outside the vault**.

## Pointing the client at `AGENTS.md`

| Client | How it finds the vault's instructions |
|---|---|
| Claude Code (CLI, desktop Code tab, IDE) | Open the vault folder as the working directory. Claude Code reads `CLAUDE.md`, which imports `AGENTS.md`. |
| Claude Cowork / Claude desktop | Connect the folder, then install the loader stub — see [[_ai/modules/vault/bootstrap/cowork-loader\|cowork-loader]]. |
| OpenAI Codex, Cursor, and other clients that follow the `AGENTS.md` convention | Open the vault folder. They read `AGENTS.md` automatically. |
| Gemini CLI | Either set its context file name to `AGENTS.md` in its settings, or add a root `GEMINI.md` containing one line: "Read `AGENTS.md` and follow it." |
| Anything else | Start the session with: *"Read `AGENTS.md` at the root of this folder and follow its boot protocol."* |

A pointer file such as `CLAUDE.md` or `GEMINI.md` should **contain no rules**, only a pointer to `AGENTS.md`. Rules belong in one place, so they cannot drift apart.

## Keep memory in the vault

The design rule is that **nothing is remembered anywhere but here** (`AGENTS.md` §1). Many agent clients have their own memory feature that quietly saves facts about you on the provider's side. Turn it off for vault work, so that everything the agent knows is in a file the owner can read, correct and delete.

### Claude Code

- The vault ships with `.claude/settings.json` at its root, which sets `"autoMemoryEnabled": false`. This turns off Claude Code's auto memory for this project.
- You can confirm the setting with the `/memory` command inside a Claude Code session.
- Keep vault-specific content out of your user-level `~/.claude/CLAUDE.md`. That file lives outside the vault.

### Claude apps (claude.ai, desktop, Cowork)

- In **Settings**, turn off the memory features (generating memory from chats, and searching or referencing past chats). Exact labels vary by version.
- Projects and chat history on claude.ai are stored with your account. Treat a chat as disposable: anything worth keeping gets written to the vault with the `checkpoint` or `export-conversation` skill before the session ends.

### Other clients

Look for a "memory", "personalisation" or "remember facts" setting and turn it off for this workspace. Clients that read `AGENTS.md` are also told not to use their own memory (`AGENTS.md` §10), but a setting is more reliable than an instruction.

## Scheduled and unattended runs

A scheduled task starts cold, so its prompt must mount the vault itself:

> Mount the vault at `<VAULT_PATH>` — read AGENTS.md and follow its boot protocol — then …

See [[_ai/modules/vault/skills/mount|mount]] for what an unattended run does and does not do.

## Changelog

- **2026-11-17** — created when the vault was made agent-neutral.
