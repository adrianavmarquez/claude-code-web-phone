---
title: "Creatividad2 — Condensed Memory"
project: "Creatividad2"
source: claude.ai-memory
tags: [claude, condensed-memory]
---

# Creatividad2 — Condensed Memory

> Claude's auto-condensed memory for this project. The full chats live in `Chat Archive/`; this is the summary layer.

**Purpose & context**

Adri (Adriana V. Márquez) is a creative director, creative strategist, and personal brand consultant operating at the intersection of content creation, brand development, and creator education. Her work centers on two primary brands:

- **Creatividad²** — her main educational and strategic hub offering creative strategy, short-form video, brand development, and advertising. It includes a developing ecosystem of digital resources, AI agents, workshops, a low-ticket pre-recorded brand fundamentals course, a Notion-based CRM ("Brand Brain"), and personalized consulting. The community platform (Circle) is newly established. She has a significant social following (50K+) and Manychat contact base, but a smaller email list she is actively growing.
> *[line redacted — references an out-of-scope venture]*

Her client base splits into two segments: **Client A** (early-stage creators and small businesses growing on social but not yet monetizing) and **Client B** (established brands and creators running campaigns but lacking creative strategy structure). Current launch focus is directed at Client B. She also does website audits and strategic analysis for clients and references in the creator economy space across both English and Spanish markets.

Adri positions herself as a **visual curator and creative direction reference** — her content and brand are explicitly distinguished from generic creator tips. This positioning is a non-negotiable filter across all content and copy decisions.

**Current state**

- **Creatividad² community (Circle):** Newly created with zero spaces configured; content adaptation work (from MailerLite campaigns) is underway. A scriptwriting template (Notion-hosted) is live as a pre-access offer while the main framework is still being built.
- **Content pillar series ("Recursos con Criterio" / "Pasa el Filtro" — name TBD):** First episode scripted and production-ready in Spanish. The Pinterest episode leads the series. The pillar name only appears as a text overlay and does not block production.
- **Coming soon page:** Launched at adrianavmarquez.com with finalized copy and visual identity. Email capture is active; transitioning from Gumroad to her own website for product sales.
- **Course platform:** Teachable selected (Pro plan recommended for custom subdomain and branding removal) over a custom Wistia hub.
- **Operational skill library (SKILL.md system):** 16 skills built and iteratively refined within Claude projects, covering identity/positioning, monthly content architecture, format-specific scripting (reels, carousels, voiceover, storytime, talking head, text screen, YouTube essay/vlog, tweet snippets, Substack, email, LinkedIn), and a website audit framework. All skills are written creator-agnostic ("el creador") to work across brands.
- **MailerLite ↔ Circle workflow:** Established process for adapting email campaigns to Circle post format (text-only adaptation, no publishing).

**On the horizon**

- Finalizing the content pillar series name ("Recursos con Criterio" vs. "Pasa el Filtro")
- Building out Circle community spaces before content can be published
- Developing the Creatividad² operating document as a single source of truth (offers, funnel, quiz spec, automations) — recommended as the step before considering a dedicated Claude project split
- Expanding the offer ladder: digital resources, AI agents, workshops, Brand Brain CRM
- Potential workshop on storytelling (structured around Ben Watkins' framework + pedagogical model from analyzed transcript)

**Key learnings & principles**

- **Positioning over generic tips:** Content must read as creative direction expertise, not creator advice. The distinction is sharp and enforced at the scripting level.
- **Pinterest nuance as editorial model:** Adri didn't abandon Pinterest — she removed it from her creative direction process while keeping it recreational. Precision like this shapes entire episodes and should be preserved in content work.
- **Core thesis on creative direction:** Pinterest delivers pre-composed references; creative direction requires raw material so the creator's own mind connects the dots. Seeking CD references on Pinterest is like trying to dress differently by shopping at the same store.
- **Context mismatch awareness:** Email campaigns written for cold subscribers need reframing before being adapted for an existing community audience (Circle members have already joined — the hook and premise change).
- **Project architecture principle:** A Claude project boundary moves memory pools and search scope, not skills or account-level connectors. Creatividad²'s content layer is deeply fused with Adri's personal brand engine, making a hard silo counterproductive. Hard splits should wait until memory noise becomes documented friction.
- **Website audit pattern:** The single most universal and correctable UX gap across audited sites is pricing not being in real HTML.
- **MailerLite API:** Preview URL IDs do not map to campaign IDs. Always call `list_campaigns` first and match by name/subject. Use `status: draft` + `limit: 25` as reliable starting parameters.
- **Circle API:** `list_space_groups` is the reliable entry point for understanding community structure. Always verify spaces exist before attempting to create or publish content.

**Approach & patterns**

- **Communication style:** Direct, high-density, no softening or preamble. Adri corrects quickly and specifically; she provides her own rewrites when she has a clearer version. She distinguishes immediately between content that positions her correctly versus content that reads as generic.
- **Information delivery:** Sends context in sequential parts and expects Claude to wait before processing the full picture.
- **Scripting protocol:** Five-round maximum revision cap. Requires five small creator reference links before drafting. Rhythm mapping for breath points. Hooks are often written or heavily rewritten by Adri herself — her language is the standard.
- **Content philosophy:** Only references tools she has personally used. "What I don't use and why" beat appears in select episodes, not all. Spanish is the primary content language.
- **Copy standards:** Rejects AI-sounding language (e.g., "convertir" and conjugations flagged explicitly). Co-develops copy through iteration, not hand-off.
- **Workshop/education design:** Prefers frameworks where participants produce something concrete rather than accumulate theory. Anchors to vivid, specific examples before introducing abstraction.

**Tools & resources**

- **Platforms:** Circle (community), MailerLite (email), Manychat, Teachable (courses), Notion (resources, Brand Brain CRM), N8n (automations), Gumroad (transitioning away from)
- **Camera/lens kit:** Sony ZV-E1, Sony A7CII, Sony A7RV (photos only — video grain issue), Osmo Pocket 3, Osmo Action 6, Fujifilm XE5 + Fujinon 23mm, Sony RX100VII, Canon ELPH 360, iPhone 17 Pro Max; lenses: 14mm GM f/1.8, 11mm APS-C f/1.8 (vignette noted), 20mm GM f/1.8, 28-60mm f/4-5.6, 50mm Prime f/1.8, 24-70mm GM f/2.8, 90mm Macro G OSS f/2.8
- **Brand identity:** Colors — red #D72323, blue #3846C4, yellow #FFBA35, black #080808. Fonts — Poppins Bold, Glenda Sans, Plunct (hand-drawn), Heading Now
- **Professional tools referenced:** Shotdeck, Frameset, Eyecannndy, Cosmos, Savee, Are.na
- **Skill system:** 16 SKILL.md files built within Claude projects (descriptions collapsed to single paragraphs, all under 1024-byte limit after troubleshooting YAML field rejection)
- **Creator economy references:** Audited sites span Hispanic creator education market and English-language digital product creators
