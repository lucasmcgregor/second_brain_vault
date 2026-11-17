---
type: index
status: active
created: 2026-09-14
updated: 2026-11-17
summary: Vault-managed agents and skills — capabilities defined as files rather than installed into a client.
---

# _ai/modules — Modules

Modules are the agents and skills available in this vault. They are skills in the open `SKILL.md` format, captured as **files in the vault**, not installations in any client. Mounting the vault mounts the modules, so capabilities travel with the vault across accounts, machines and models.

## Registry

Mirror every row into the module registry in [[_ai/index]] when you add one.

| Module | Triggers on | Purpose | Tools used | Updated |
|---|---|---|---|---|
| [[_ai/modules/vault/SKILL\|vault]] | First run, "set up the vault"; session start; "where is…", "file this", "save this conversation", "tidy up", "vault health", "archive this", end of session | The vault keeper — mounts the vault, files new material, keeps indexes true, reports health | `vault-audit.py` | 2026-11-17 |

## Anatomy of a module

One folder per module, containing at minimum a `SKILL.md`-style definition:

```yaml
---
type: module
name: module-name
status: active
created: 2026-09-14
updated: 2026-09-14
triggers: [phrases or situations that should load this module]
tools: [tools in _ai/tools this module calls]
summary: One sentence — what this module does.
---
```

The body covers: when to use it (and when not to), the procedure step by step, the inputs it expects, where it writes its output, and a changelog.

## Loading

Load a module by reading its definition. Load **only** modules whose triggers match the task at hand — loading everything defeats the point. If no module matches, work without one.

## Authoring rules

- A module earns its existence when a procedure has been done twice and will be done again. Do not pre-build modules speculatively.
- Modules write their output to a known location and say so in their definition, so other processes can pick it up.
- A module that needs a deterministic, repetitive step should call a tool from [[_ai/tools/index]] rather than regenerating logic each run.
- Changing a module changes future sessions' behaviour: propose it to the owner, bump `updated`, and append to the changelog.
- Register it in both this table and [[_ai/index]] in the same turn you create it.
