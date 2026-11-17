---
type: index
status: active
created: 2026-09-14
updated: 2026-11-17
summary: Externalised configuration, credentials and connection settings for agents and tools.
---

# _ai/config — Configuration

Centralised settings so that modules and tools do not hard-code connection details. Read a config file only when a tool or module you are actually running needs it.

## Handling rules

- **Never echo the contents of a file in this folder into chat**, into a log, into a commit message, or into any file outside this folder. Refer to values by their key name.
- **Never write a secret anywhere else in the vault.** If you find a credential outside this folder, tell the owner and offer to move it.
- Treat every file here as sensitive even if it looks like it only contains a URL.
- When a module needs a new setting, add the key with a placeholder value and ask the owner to fill it in. Do not invent credentials.
- Prefer one file per service or integration.

## Conventions

- Name files after the service: `google-drive.md`, `email.md`, `obsidian.md`.
- Document every key: what it is, what needs it, where to obtain it.
- Never commit real secrets to any sync or backup that leaves the vault without the owner's explicit say-so.

## Registry

| File | Service / scope | Used by | Updated |
|---|---|---|---|
| _(none yet)_ | | | |
