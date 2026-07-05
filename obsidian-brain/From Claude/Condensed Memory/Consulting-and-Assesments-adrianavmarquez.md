---
title: "Consulting and Assesments @adrianavmarquez — Condensed Memory"
project: "Consulting and Assesments @adrianavmarquez"
source: claude.ai-memory
tags: [claude, condensed-memory]
---

# Consulting and Assesments @adrianavmarquez — Condensed Memory

> Claude's auto-condensed memory for this project. The full chats live in `Chat Archive/`; this is the summary layer.

**Purpose & context**

Adri (adrianavmarquez.com) is a content strategist, brand consultant, and coach working primarily with personal brands, creators, and founders — predominantly in Latin America and the US Latino market. Her work spans brand voice development, VOC-driven copywriting, content strategy, and social media growth. She also develops proprietary consulting frameworks and educational resources (like the Brand Brain) for her own coaching clients ("asesorados").

Her central brand philosophy is **"te sacudo, no te consiento"** — direct, experience-grounded challenge rather than coddling or performance. This ethos shapes both her personal voice and how she directs client content.

**Active client roster:**
- **Daniela Alsina** — Venezuelan-trained architectural/interior designer based in Miami; brand built around end-to-end design process ("de planos a entrega"), positioning away from generic motivational/guru tone
- **Claudia Grice ("Clau")** — Ecuadorian creator in Arizona; content covers migration, spirituality (framed as accessible, anti-postureo), and personal growth; target audience persona is "María," a Latina migrant navigating identity; brand seal: "Pertenezco a donde voy"
- **Mariana Salas ("Maleah/Male")** — Costa Rican creator in Brazil; transitioning from engineering to content creation; brand: "the sister who motivates you to shine with fear included"; five defined content pillars with specific virality levels and narrative structures
- **Luz (luzchapeton)** — Founder building a personal brand on Instagram; content in English
- **Julieth Ferreira** — Creator behind a 28-day digital journaling method ("Volver a mí"); product sold via Shopify

**Consulting/business development:** Adri is also building her own fractional CMO / strategic partner practice targeting mid-sized service businesses, with proprietary systems and documented results as the core differentiator.

---

**Current state**

- Actively managing multiple client content workflows in Notion via MCP integration (hooks, scripts, idea banks, 30-day content maps)
- VOC pressure-testing and rewriting hooks/scripts is the dominant recurring task across clients
- Recently consolidated her full brand knowledge into a structured markdown archive (brand identity, methodology, client roster, visual standards, operational preferences)
- "Volver a mí" Shopify store was in active launch phase; pending unresolved question about whether a Telegram community bonus exists

---

**On the horizon**

- Brand Brain template (Notion-based) has an English version in progress; Spanish version planned as a separate phase
- Master glossary of technical terms (AOV, CAC, LTV, CPM, etc.) to be compiled once full Brand Brain document is live in Notion
- Ongoing post-consultation tracking of Mariana Salas's content performance (pro-bono follow-up)

---

**Key learnings & principles**

**VOC methodology — three golden rules for all copy:**
1. **Visualizable** — the reader/viewer can picture it
2. **Falsifiable** — contains a specific, verifiable claim (not vague aspiration)
3. **Uniquely ownable** — could only come from this specific person/brand

**Dominant copy failure patterns Adri diagnoses:**
- Third-person or aspirational framing instead of first-person confession
- Generic "guru-speak" any creator could sign
- Value buried behind vague CTAs ("te explico," "haz esto")
- Hooks that open no curiosity gap and create no mirror moment for the audience
- Motivational/abstract language where concrete, lived detail is needed

**Proprietary frameworks in use:**
- **Cinematic Confessional** — storytime scripting method (visual contradiction opening → concrete sensory anchors → mirror moment for audience)
- **POV formula**: (Lived Experience + Psychological Insight) × Negation of Mass Consensus
- **Pillar vs. Concept vs. Angle** — framework for organizing creative strategy
- **Account Health Check Framework** — 7-step diagnostic across multiple platforms and business models
- Skill files stored at `/mnt/skills/user/` with subdirectories per skill (e.g., `storytime-scripting/SKILL.md`, `copywriting-pressure-test/SKILL.md`) — Claude should read these before executing creative tasks

**Content strategy principles:**
- Strongest personal brand content positions the creator as protagonist of their own story, not as instructor
- Tutorial/teaching content should come after messaging clarity is established, not before
- CTAs should route to owned properties (newsletter, YouTube) rather than bare follow requests
- Placeholders with brackets should be preserved for real data rather than inventing specifics
- Humor and emotion land harder from truth — flag when real memories or metrics are needed

---

**Approach & patterns**

**Output preferences (non-negotiable):**
- **Paste-ready deliverables** — no follow-up questions gating the output
- **No explanations pushed to Notion pages** — reasoning and strategic notes stay in the Claude chat only
- **Light formatting** — no heavy template structures or over-formatting
- Always include **2–4 alternate hooks** for A/B testing
- Flag gaps and out-of-scope edits **transparently** rather than silently resolving them
- Markdown compatible with Notion

**Language & voice:**
- Communicates in Spanish and Spanglish
- Uses **tuteo** (not voseo) — important for client-facing copy in her voice
- Client content language varies (Spanish for most clients, English for Luz)

**Workflow pattern:**
- Fetch full brand context from Notion before touching any copy (intake, brand voice, market research, pillars, strategy)
- Apply proprietary skill files before executing creative tasks
- Batch Notion updates in a single call; exact string matching required (accents, punctuation, emoji, quotation mark style must match source precisely)
- Flag bracketed placeholders needing real data before publishing

**Consulting positioning:**
- Fractional CMO / strategic partner (not executor or traditional agency)
- Value-based pricing anchored to proprietary systems and documented results, not hours

---

**Tools & resources**

- **Notion** (primary client workspace and knowledge management) — accessed via MCP integration; workspace under `adrianavmarquez` namespace
- **Shopify / Liquid** — used for client e-commerce builds (Volver a mí store)
- **Basecamp** — resource hub for coaching clients alongside Brand Brain
- **Skill files** — `/mnt/skills/user/` subdirectories for storytime-scripting, copywriting-pressure-test, and other proprietary methods
- **Notion MCP tools:** `notion-fetch` (full URLs or page IDs both work), `notion-update-page` with `update_content` + batch `content_updates` arrays, `insert_content` with `position: {type: 'end'}` for appending sections
