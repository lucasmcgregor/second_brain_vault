---
type: index
status: active
created: 2026-09-14
updated: 2026-11-17
summary: Goal-directed work with a finish line — the registry of active, paused and completed projects.
---

# home/projects — Projects

Work with a **goal and an end**. This is the "getting stuff done" half of the vault. A project is finished when its goal is met; then it moves to [[home/archives/index]].

## Active projects

| Project | Goal | Status | Next action | Updated |
|---|---|---|---|---|
| _(none yet)_ | | | | |

Statuses: `active` · `paused` · `blocked` · `done`

## Completed, not yet archived

| Project | Finished | Outcome |
|---|---|---|
| _(none)_ | | |

## Structure of a project

One folder per project, named for the goal: `projects/redesign-website/`. Every project folder has an `index.md`:

```yaml
---
type: project
status: active
created: 2026-09-14
updated: 2026-09-14
goal: What "done" looks like, in one sentence.
due: 2026-12-01   # omit if none
summary: One line for the registry row above.
---
```

The body carries: the goal and what done looks like, current status, next actions, open questions and decisions, and links to related documents and activities. Small projects can be a single file rather than a folder — promote to a folder as soon as there is a second file.

## Working rules

- **Update the project index in the same turn you change the project.** Status and next action going stale is how a project quietly dies.
- `next action` is a specific thing someone could do today, not a restatement of the goal.
- Record decisions in the project index as they are made; promote the ones that outlive the project into `_ai/memory/permanent/`.
- When a project finishes: write its outcome, promote anything durable to memory or documents, then ask before archiving.
- If a "project" is still running with no end in sight after a few months, it is probably an activity. Say so.

## Scanning

Read this index first. Open individual project indexes only for the projects the task concerns. For a status sweep, this table alone should be enough — if it is not, the table is stale and fixing it is the first task.
