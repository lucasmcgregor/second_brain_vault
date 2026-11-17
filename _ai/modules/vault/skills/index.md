---
type: index
status: active
created: 2026-09-14
updated: 2026-11-17
summary: Skills belonging to the vault keeper module.
---

# vault / skills

Load only the skill that matches the task. The router in [[_ai/modules/vault/SKILL|SKILL.md]] decides which.

| Skill | Triggers on | Writes? |
|---|---|---|
| [[_ai/modules/vault/skills/setup\|setup]] | First run, "set up the vault" | Yes — owner profile, with approval |
| [[_ai/modules/vault/skills/mount\|mount]] | Session start, scheduled task start | Mount receipt only |
| [[_ai/modules/vault/skills/orient\|orient]] | "Where is…", "what's in…", "what should I be doing" | No |
| [[_ai/modules/vault/skills/capture\|capture]] | "File this", "save this", a loose note | Yes |
| [[_ai/modules/vault/skills/export-conversation\|export-conversation]] | "Save this conversation", "write this up", "don't lose this" | Yes |
| [[_ai/modules/vault/skills/audit\|audit]] | "Vault health", scheduled sweep | No |
| [[_ai/modules/vault/skills/maintain-indexes\|maintain-indexes]] | "Tidy up", audit found drift | Yes |
| [[_ai/modules/vault/skills/checkpoint\|checkpoint]] | End of session, handoff | Yes |
| [[_ai/modules/vault/skills/archive\|archive]] | "This is finished", "put this away" | Yes |
