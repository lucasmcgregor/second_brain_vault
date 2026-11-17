---
type: index
status: active
created: 2026-09-14
updated: 2026-11-17
summary: Ongoing commitments with no end date — the registry of continuing activities.
---

# home/activities — Activities

Things the owner does **on an ongoing basis, with no end date**. Unlike projects, activities are not completed — they continue, pause, or eventually stop. They are the long-running threads of their life and work, and often the place where projects are born.

## Active activities

| Activity | What it is | Cadence | Current focus | Updated |
|---|---|---|---|---|
| _(none yet)_ | | | | |

Statuses live in each activity's frontmatter: `active` · `paused` · `stopped`

## Structure of an activity

One folder per activity, named for the thing itself: `activities/writing/`, `activities/finances/`. Each has an `index.md`:

```yaml
---
type: activity
status: active
created: 2026-09-14
updated: 2026-09-14
cadence: weekly | monthly | ad hoc | continuous
summary: One line for the registry row above.
---
```

The body carries: what the activity is and why it matters, how it runs, current focus, a running log of sessions or entries, and links to projects it has spawned.

## Working rules

- Activities accumulate. Expect long logs — keep them **reverse-chronological**, newest at the top, so the current state is the first thing read.
- When an activity generates work with a defined end, create a **project** for it and link both ways. Do not let projects hide inside activity logs.
- When a log or reference inside an activity grows big enough to stand alone, move it to [[home/documents/index]] and link it.
- Update "current focus" whenever it changes — that field is what makes this table worth reading.
- An activity that has not moved in months is a candidate for `paused` or archiving. Raise it rather than deciding it.

## Scanning

Read this index first, then the one activity that matters. Never read an entire activity log when the current focus line answers the question — and if an activity's log is long, read its top section before reading further back.
