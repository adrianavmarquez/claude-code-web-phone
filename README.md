# claude-code-web-phone

Adriana Márquez's **Obsidian brain** — a distilled, Claude-optimized memory built
from her Notion workspace and Claude.ai export — plus the tools that produce it.

## What's here

- **[`obsidian-brain/`](obsidian-brain/)** — the actual vault. Open it in Obsidian
  (*Open folder as vault*) and start at `00 START HERE.md`. A curated, cross-linked
  memory layer over a full `From Claude/` archive. Scope is Adriana's personal/brand
  areas only; other ventures are walled off.
- **`extract_claude_export.py`** — turns a Claude.ai data export (newer format:
  `conversations.json` + `projects/` + `memories.json`) into the `From Claude/` archive,
  classifying chats in-scope vs excluded so nothing off-limits leaks in.
- **`claude_to_obsidian.py`** — a general-purpose converter for the older single-file
  export shape (documented below).

---

## `claude_to_obsidian.py` — general Claude.ai chat → Obsidian converter

Export your Claude.ai chats into an **Obsidian vault** — one Markdown note per
chat, grouped into per-project folders — instead of settling for the lossy,
condensed Project "memory".

## Why

Inside a Claude.ai **Project**, the "memory" you see is a *condensed summary* of
your chats. It's lossy. The **full transcripts** of every chat still exist —
they just aren't exposed in the Project UI. They come out through your account
**data export**, and `claude_to_obsidian.py` turns that export into clean,
Obsidian-ready Markdown.

## Step 1 — get the raw export from Claude

1. On **claude.ai** (web, not the phone app) → **Settings → Privacy → Export data**.
2. Wait for the email, then download the `.zip`. Inside you'll find:
   - `conversations.json` — every chat, full transcript (the real, un-condensed thing)
   - `projects.json` — each project plus its uploaded knowledge docs
   - `users.json`

## Step 2 — convert to an Obsidian vault

No dependencies — just Python 3.8+.

```bash
# straight from the downloaded zip
python3 claude_to_obsidian.py data-2026-07-05.zip --out ~/Obsidian/Claude

# or from an unzipped folder
python3 claude_to_obsidian.py ./unzipped-export --out ~/Obsidian/Claude

# or from the individual json files
python3 claude_to_obsidian.py conversations.json --projects projects.json
```

Then in Obsidian: **Open folder as vault** → pick the `--out` folder.

## What you get

```
ObsidianVault/
├── Marketing-Brain/
│   ├── 2026-03-01-Launch-plan-for-spring.md
│   ├── 2026-03-04-Ad-copy-brainstorm.md
│   └── Project Knowledge/
│       └── brand-voice.md
├── Personal-Assistant/
│   └── 2026-02-18-Trip-itinerary.md
└── _Unfiled/
    └── 2026-02-10-Random-idea.md
```

Each chat note has YAML frontmatter Obsidian understands:

```markdown
---
title: "Launch plan for spring"
project: "Marketing Brain"
created: "2026-03-01 09:00"
updated: "2026-03-01 10:00"
claude_uuid: "c1"
message_count: 2
source: claude.ai
tags: [claude, chat]
---
```

- **One `.md` per chat**, filename prefixed with its date so notes sort chronologically.
- **Per-project folders**, so a project's chats live together.
- **Project knowledge docs** exported too, each as its own note under `Project Knowledge/`.
- **Attachments** are noted inline (with extracted text where the export includes it).

## Notes & limitations

- **`_Unfiled`:** Claude's export doesn't always tag a chat with the project it
  belonged to. Chats without a detectable project land in `_Unfiled/` — the
  script tells you how many. You can drag them into the right folder in Obsidian.
- The export is a point-in-time snapshot. Re-run the export + this script
  whenever you want to refresh your vault. Re-running writes into the same
  folder; existing filenames are never overwritten (duplicates get a numeric
  suffix), so delete the old vault first if you want a clean rebuild.
- Everything runs locally — nothing is uploaded anywhere.

## Options

| Flag | Default | Meaning |
| --- | --- | --- |
| `--out` | `ObsidianVault` | Output vault folder |
| `--projects` | — | Path to `projects.json` if passing `conversations.json` directly |
| `--unfiled-name` | `_Unfiled` | Folder name for chats with no detectable project |
