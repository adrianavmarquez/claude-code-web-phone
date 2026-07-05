# 🧠 Adriana Márquez — Obsidian Brain

A **distilled, Claude-optimized memory** synthesized from Adriana Márquez's Notion
workspace. Built to *complement and categorize* — the opposite of a raw dump.

## How to use it

**In Obsidian:** *Open folder as vault* → point at this `obsidian-brain/` folder.
Open **`00 START HERE.md`** — it's the Map of Content and links to everything.

**With Claude / any LLM:** every note has YAML frontmatter and a one-line summary, so
the model can load only what a task needs. `00 START HERE` tells Claude which notes to
pull for identity vs. methodology vs. current goals.

## Why it's structured this way

The old Notion→Obsidian dump created thousands of disconnected "0 backlinks" notes — a
hairball. This brain fixes that:

- **Synthesis, not copy.** Durable knowledge (identity, voice, brand, frameworks,
  offers, goals) becomes clean notes; ephemera (template instances, per-client pages,
  per-video planners) is **linked, not duplicated**.
- **Everything is cross-linked** with `[[wikilinks]]`, so the graph is a real web.
- **Frontmatter on every note** (`teamspace`, `notion:` source link, `tags`) — nothing
  goes stale silently; follow the link to the source of truth.

## Structure

```
obsidian-brain/
├── 00 START HERE.md          ← the map, read this first
├── Identity/                 Who Is Adriana · Voice & Tone · Story & Self-Concept
├── Brand/                    Content Pillars · Brand Guide · Brand Analysis System
├── Methodology/              Content Creation Method · Creator Maturity Model ·
│                             Hook System · Coaching Framework
├── Offers/                   Creatividad2 Course · 1-1 Advising
├── Operating System/         Goals & Cadence · Weekly Content Schedule
└── Reference/                Notion Source Map  ← index + what's excluded + how to expand
```

## Scope

**Included:** 📱 Adriana Marquez · 🤳🏻 @adrianavmarquez · 🫂 community resources ·
👩🏻‍🏫 Asesorías 1:1 · 👩🏻‍💻 Marketing Strategist · 🎨 Creativity2.

**Excluded (by request):** Ricos Açaí · Sparked Reactions · Celestina · Bulk Buyers ·
Juyi (editor space) · individual 1:1 client data.

## Expanding it

`Reference/Notion Source Map.md` lists rich clusters not yet distilled, with pointers.
To add one: open its Notion page, create a note here with the same shape (frontmatter →
one-liner → distilled bullets → `See also` links), and link it from `00 START HERE`.
