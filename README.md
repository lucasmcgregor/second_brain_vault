
<h1 align="center">Second Brain Vault</h1>

<p align="center">
  <b>Capture everything. Let your AI agent organise it. Keep your life on your own computer.</b>
</p>

---

## 📑 Contents

- [🧠 What is a second brain?](#-what-is-a-second-brain)
- [💎 Why Obsidian](#-why-obsidian)
- [🤝 You drive, the agent assists](#-you-drive-the-agent-assists)
- [🔒 Your data stays yours](#-your-data-stays-yours)
- [🧩 What it's built on](#-what-its-built-on)
- [📦 What's in the box](#-whats-in-the-box)
- [🚀 Getting started](#-getting-started)
- [💬 Day to day](#-day-to-day)
- [🩺 Keeping it healthy](#-keeping-it-healthy)
- [🔧 Extending it](#-extending-it)
- [🙏 Credits](#-credits)

---

## 🧠 What is a second brain?

A **second brain** is a trusted place outside your head for everything you need to remember: notes, ideas, tasks, plans, reference material. You stop trying to hold it all in memory, and you can always find it again.

### The problem

- 📚 **You have a lot to keep track of.** Information, ideas and tasks arrive all day, from everywhere.
- 🗂️ **Organising systems end up organising you.** Most systems make you spend more time sorting, tagging and filing than doing the work, and you bend your habits around the tool instead of it working for you.
- ☁️ **You want the power of AI, without handing over your life.** An AI assistant could do the organising for you, but you don't feel comfortable uploading everything you know to someone else's cloud.

### The answer

This second brain combines two things:

1. **A knowledge base that runs on your own computer** — [Obsidian](https://obsidian.md).
2. **Whatever AI agent you want to help you** — Claude, Codex, Cursor, or another.

You just **capture what you need as it comes to you**. Your agent helps organise it after the fact: filing it in the right place, linking related notes, keeping track of open work, and finding things again when you ask.

**You drive. The agent assists.**

---

## 💎 Why Obsidian

[Obsidian](https://obsidian.md) is a free personal wiki that stores all of your documents **as plain files on your own computer**. No account is required, and nothing is uploaded unless you choose to sync.

It's also a powerful knowledge management system in its own right:

- 🔗 **Linked notes.** Connect ideas with `[[wikilinks]]` and explore them in a visual graph.
- 🧩 **Thousands of community plugins.** Add anything from [task management to templates, calendars and visualisation tools](https://obsidian.md/plugins).
- 📄 **Plain Markdown.** Your notes are ordinary text files. Any app can open them, today or in twenty years.

Second Brain Vault is a ready-made Obsidian vault with a folder structure and a set of agent instructions already in place. There's no app to install, no server and no database. The vault *is* the product.

---

## 🤝 You drive, the agent assists

This is built for collaboration between a person and an AI, with a clear division of labour:

- 👤 **You own everything.** Every note, project and decision in the vault is yours. You set the goals, make the calls, and write your own ideas.
- 🤖 **The agent is a tool, not a driver and not a thinker.** It organises, files, retrieves, keeps the indexes up to date, drafts when asked, and points out what you may have missed. It offers; it doesn't decide.

The agent's instructions say this in writing. It's told to add to your notes rather than rewrite them, to ask before moving or deleting anything, and to treat what you say in the moment as overriding any written rule.

---

## 🔒 Your data stays yours

Most AI assistants remember you by storing facts about you on the provider's servers, where you can't easily see, check or correct them. This vault turns that around.

**Your agent's memory lives on your computer, in the vault.** What it knows about your past decisions, your preferences and your work in progress is a set of plain files in `_ai/memory/`. You turn off the AI client's own memory feature, so the vault is the only place anything is kept long-term.

That brings three benefits:

- 🛡️ **Privacy and control.** Your knowledge is a folder on your disk. Back it up, sync it, encrypt it or delete it, on your own terms.
- 👀 **Transparency.** You can see exactly what the agent knows and what it's doing, because its memory, its open tasks and its notes to its next session are files you can open in Obsidian. If it remembers something wrong, you edit the file.
- 🔄 **Freedom to switch.** Nothing ties you to one AI provider. A different model, on a different account or machine, can read the vault and pick up where the last one stopped.

### What happens during a session

To help you, the agent reads the notes it needs and sends them to the AI provider's servers for processing, for that session only. With the client's memory turned off, and a private or incognito session where your client offers one, that working memory should be short-lived and end with the session. Your life stays on your machine.

> [!NOTE]
> Providers may still keep conversation records for a period under their own data policies. Check your provider's retention settings if this matters to you. The `home/personal/` folder is off-limits to the agent unless you explicitly ask it to work there.

---

## 🧩 What it's built on

Second Brain Vault combines three proven ideas.

### 1. 🗂️ PARA — how your notes are organised

Tiago Forte's [PARA method](https://fortelabs.com/blog/para/) sorts everything by how actionable it is: **P**rojects, **A**reas, **R**esources, **A**rchives. Your half of the vault, `home/`, follows it closely:

| PARA | In this vault | What goes there |
|---|---|---|
| Projects | `home/projects/` | Work with a goal and a finish line: plan a trip, write a report, move house |
| Areas | `home/activities/` | Ongoing commitments with no end date: finances, health, a writing practice |
| Resources | `home/documents/` | Reference material you'll look things up in |
| Archives | `home/archives/` | Finished or dormant material you want to keep |
| *(added)* | `home/personal/` | Private material the agent stays out of unless asked |

One question sorts almost anything: **does this work end?**

### 2. 🧰 Modules — what the agent can do

The agent's abilities are packaged as **modules**: folders of plain-text instructions in the [Agent Skills](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview) `SKILL.md` format that Anthropic introduced for Claude. Each one says when to use it and how. The agent loads only the modules a task needs, so it stays focused and quick.

Because modules live *in the vault* rather than being installed into an app, your agent's abilities travel with your notes. The vault ships with one module, **vault**, which looks after the vault itself:

| Skill | What it does |
|---|---|
| `setup` | First run: asks who you are and how you like to work |
| `mount` | Starts a session: reads the rules, finds open work |
| `orient` | Answers "where is…" and "what am I working on?" |
| `capture` | Files something new in the right place |
| `export-conversation` | Turns a useful chat into a proper document |
| `checkpoint` | Saves where you got to before a session ends |
| `audit` | Runs a health check on the vault |
| `maintain-indexes` | Repairs what the audit found |
| `archive` | Retires finished work cleanly |

You can add your own modules too: a weekly review, a reading-notes workflow, a meeting-prep routine.

### 3. 📋 The blackboard — how agents remember and coordinate

In AI research, a [blackboard system](https://en.wikipedia.org/wiki/Blackboard_system) is a shared workspace that several specialists read from and write to. They don't talk to each other directly. Each one posts what it found, and the next picks up from there.

The vault works the same way. A chat session, a scheduled overnight task and a different AI model never speak to each other. They coordinate by writing documents: task state, handoff notes, decisions. The file `_ai/memory/transient/index.md` is the blackboard. Every session reads it first to see what's open, and writes to it before it ends. You're one of the specialists too: you can read and write the same board.

---

## 📦 What's in the box

```
your-vault/
├── README.md             ← you are here (for humans)
├── AGENTS.md             ← the agent's entry point: rules, map, routing
├── CLAUDE.md             ← one-line pointer to AGENTS.md, for Claude
├── .claude/settings.json ← turns off Claude Code's own memory for this vault
│
├── home/                 ← YOUR half: your notes and work
│   ├── projects/
│   ├── activities/
│   ├── documents/
│   ├── personal/
│   └── archives/
│
└── _ai/                  ← the AGENT's half: its rules, memory and tools
    ├── global-instructions.md   ← how the agent behaves, plus your profile
    ├── document-conventions.md  ← how you and the agent share a document
    ├── memory/
    │   ├── permanent/    ← decisions and preferences that last
    │   └── transient/    ← open work and handoffs (the blackboard)
    ├── modules/          ← skills the agent can load
    ├── tools/            ← scripts, such as the vault health check
    └── config/           ← settings and credentials (kept here and nowhere else)
```

Every folder has an `index.md` listing what's in it. Those indexes are how the agent finds things without reading your whole vault, and they double as a table of contents for you.

---

## 🚀 Getting started

### 1️⃣ Make your copy

Copy or clone this folder to wherever you keep your files. Rename it if you like; the name doesn't matter.

### 2️⃣ Open it in Obsidian

[Download Obsidian](https://obsidian.md) (free), choose **Open folder as vault**, and pick your copy. That's all the Obsidian setup there is. Start with `home/index.md`.

### 3️⃣ Point your agent at it

The agent's instructions live in `AGENTS.md`, a [convention](https://agents.md) that a growing number of AI agents read automatically.

**Claude Code** (terminal, desktop app Code tab, or IDE)
1. Start Claude Code with the vault folder as the working directory.
2. Claude reads `CLAUDE.md`, which pulls in `AGENTS.md`. Nothing else to configure.

**Claude desktop / Cowork**
1. Connect the vault folder.
2. Install the small loader skill described in `_ai/modules/vault/bootstrap/cowork-loader.md`. It tells Claude where the vault is and to read `AGENTS.md` first.

**Codex, Cursor and other `AGENTS.md`-aware agents**
Open the vault folder. They pick up `AGENTS.md` on their own.

**Anything else**
Start the session with: *"Read AGENTS.md in this folder and follow its boot protocol."*

More detail for each client is in `_ai/modules/vault/bootstrap/connect-an-agent.md`.

### 4️⃣ Turn off the agent's own memory

This is what keeps your memory in your vault rather than with the AI provider.

| Client | What to do |
|---|---|
| **Claude Code** | Already done. The vault's `.claude/settings.json` sets `"autoMemoryEnabled": false` for this folder. Check it with the `/memory` command. Keep anything about this vault out of your personal `~/.claude/CLAUDE.md`, which lives outside the vault. |
| **Claude apps** (claude.ai, desktop, Cowork) | In **Settings**, turn off the memory features: generating memory from your chats, and searching or referencing past chats. Labels vary a little between versions. Use incognito chats where available. |
| **Other agents** | Look for a "memory" or "personalisation" setting and turn it off for this workspace. |

The vault also tells every agent, in writing, not to use its own memory. A setting is more reliable than an instruction, so do both.

### 5️⃣ Run setup

Say **"set up the vault"**. The agent asks a few questions: what to call you, what you'll use the vault for, how you like answers, and anything to always or never do. It shows you exactly what it will write before writing it. Your answers go into `_ai/global-instructions.md` under **About the owner** and **Preferences**, and you can edit them by hand at any time.

---

## 💬 Day to day

Capture first, organise later. Talk to the agent normally; these phrases map onto the built-in skills:

| You say | What happens |
|---|---|
| "Mount the vault" (or just start a session) | It reads the rules and tells you what's open |
| "What am I working on?" | A status sweep of your active projects and activities |
| "File this" / "Make a note of…" | It files it in the right place, with links |
| "Where are my notes on X?" | It finds them through the indexes and gives you the path |
| "Save this conversation" | It writes the useful parts up as a proper document |
| "Checkpoint" / "Before we finish…" | It records where you got to, for next time |
| "Vault health" | It runs the audit and proposes fixes |
| "This project is done" | It proposes archiving it, and waits for your OK |

### ✍️ Working on the same document

Sometimes you and the agent both write in one note, for example a question you want answered or a draft you want reviewed. Two simple conventions stop you overwriting each other:

- **Frontmatter tells the agent how to treat a note.** Add `allow agent write: false` and it will read the note but never edit it.
- **Zones mark who owns which part.** Hidden HTML comments like `<!--zone:agent-answer: q1 -->` fence off where the agent may write. Everything outside a zone is yours.

By default, the agent only *adds* to notes in `home/` and never rewrites what you wrote. Full details are in `_ai/document-conventions.md`.

---

## 🩺 Keeping it healthy

A small Python script checks the vault for drift: files missing from their index, broken links, missing frontmatter, credentials in the wrong place.

```bash
python3 _ai/tools/vault-audit.py .
```

It only reads; it never changes anything. Ask the agent for a "vault health" check and it will run the script, explain the results and offer fixes.

---

## 🔧 Extending it

- 🧰 **Add a module.** Once you've done the same multi-step task with the agent twice, ask it to propose a module for it. Modules live in `_ai/modules/` and are registered in `_ai/index.md`.
- ⚙️ **Add a tool.** For anything that must be exact and repeatable, a script in `_ai/tools/` beats re-explaining it every session.
- 📝 **Change the rules.** `AGENTS.md` and everything in `_ai/` are plain text. Edit them yourself, or ask the agent: it will propose the change and wait for your approval before touching its own instructions.
- ⏰ **Schedule work.** A scheduled agent task, such as a weekly health check, starts with *"Mount the vault at &lt;path&gt;…"* and leaves its results on the blackboard for you and your next session.
- 🔌 **Add Obsidian plugins.** Tasks, calendars, templates, dashboards: Obsidian's [community plugins](https://obsidian.md/plugins) work alongside the agent.

---

## 🙏 Credits

- **PARA** — Tiago Forte, [*The PARA Method*](https://fortelabs.com/blog/para/) and *Building a Second Brain*.
- **Obsidian** — the [Obsidian](https://obsidian.md) knowledge base. The Obsidian name and logo belong to their owners; this project is not affiliated with Obsidian.
- **Modules** — modelled on Anthropic's [Agent Skills](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview) for Claude.
- **Blackboard architecture** — the classic AI coordination pattern; see [Blackboard system](https://en.wikipedia.org/wiki/Blackboard_system).
- **`AGENTS.md`** — the open [agents.md](https://agents.md) convention for agent instructions.
