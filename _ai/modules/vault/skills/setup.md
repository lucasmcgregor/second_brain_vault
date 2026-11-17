---
type: skill
name: setup
module: vault
status: active
created: 2026-11-17
updated: 2026-11-17
triggers: [set up the vault, set up my vault, first run, new vault, the About the owner zone is empty]
summary: First-run setup — ask the owner who they are and how they work, and record their answers in their own words.
---

# setup

Runs once, on a fresh copy of the vault. The vault ships with no owner: the **About the owner** and **Preferences** zones in `_ai/global-instructions.md` are empty. This skill fills them in so every later session knows who it is working for.

## When

- [[_ai/modules/vault/skills/mount|mount]] finds the About the owner zone empty, and the owner agrees to set up now.
- The owner asks to set up, or redo setup.

Never run it unattended. It only works with the owner present.

## Procedure

1. **Explain in two lines** what setup does: a few questions, the answers go into `_ai/global-instructions.md`, they can edit that file by hand at any time.
2. **Ask, one or two questions at a time**, and accept "skip" for any of them:
   - What should I call you? Which pronouns should I use?
   - What do you do, broadly? What will you mostly use this vault for?
   - How do you like answers: short or detailed, formal or casual?
   - Anything I should always do, or never do?
   - Are there projects or ongoing activities you want to start with?
3. **Draft the two zones** from their answers, keeping their words wherever possible. Do not embellish, infer traits, or add anything they did not say.
4. **Show the exact text** and ask for approval. Revise until they approve.
5. **Write it** into the `about-owner` and `preferences` zones, inside the existing markers. Leave the markers and zone status alone. This is the only time an agent writes in a `human` zone, and only with the text they approved.
6. **Starter work.** If they named projects or activities, offer to create each one with [[_ai/modules/vault/skills/capture|capture]]. Offer; don't assume.
7. **Point out the memory setting.** Tell them to check that their agent client's own memory is off — see [[_ai/modules/vault/bootstrap/connect-an-agent|connect-an-agent]].
8. **Confirm** in one line what was written and where.

## Rules

- These are the owner's words about themselves. Record them; do not interpret them.
- Do not put anything sensitive into these zones unasked. If the owner volunteers something private, ask whether it belongs in `home/personal/` instead.
- If the zones already have content, this is a re-run. Show what is there and ask what to change. Never overwrite silently.

## Changelog

- **2026-11-17** — created when the vault was made generic, replacing the hand-filled owner profile.
