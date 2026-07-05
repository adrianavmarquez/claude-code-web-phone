---
title: "MISC — Condensed Memory"
project: "MISC"
source: claude.ai-memory
tags: [claude, condensed-memory]
---

# MISC — Condensed Memory

> Claude's auto-condensed memory for this project. The full chats live in `Chat Archive/`; this is the summary layer.

**Purpose & context**

Adri is a digital marketing strategy consultant who advises clients on social media marketing across YouTube, TikTok, Instagram, Twitter/X, and LinkedIn. Adri also conducts market research for personal use. A key goal is building repeatable market research workflows — both for ad hoc use and potentially for clients.

**Current state**

Adri is evaluating tools and workflows for market research across social platforms. A recent area of exploration was Composio (an MCP-based integration platform) and whether its social connectors could support competitive intelligence gathering. Key finding: Composio's connectors are primarily built for managing authenticated accounts, not competitive research — YouTube is the strongest platform for public data via its Data API, while LinkedIn, TikTok, and Instagram are significantly more restricted. Platform ToS constraints around scraping are a relevant consideration given the client-facing nature of Adri's work.

An open question from the Composio evaluation: whether Adri's primary need is ad hoc research within a chat interface or an automated, recurring pipeline — since the answer significantly affects whether a tool like Composio would be appropriate or over-engineered.

Adri also works with video production, recently exploring LUT workflows in Adobe Premiere Pro (per-clip application via Lumetri Color vs. permanent installation, Input LUT vs. Creative Look distinction, batch application via Paste Attributes and adjustment layers).

**On the horizon**

- Determining the right architecture for a repeatable market research workflow (ad hoc vs. automated pipeline)
- Potentially deeper evaluation of MCP-based tools depending on workflow needs

**Key learnings & principles**

- Composio's Search and Browser tools differ from native Claude capabilities in that they support autonomous, persistent pipelines running without the user present — useful for automation but potentially redundant for in-chat research
- Scraping outside official APIs violates platform ToS — a meaningful risk for client deliverables
- For Premiere Pro LUT work: the Creative section's Intensity slider enables blending control; Input LUT is suited for technical/log-conversion use cases while Look is better for stylistic applications

**Tools & resources**

- Platforms actively discussed: YouTube, TikTok, Instagram, Twitter/X, LinkedIn
- Tools evaluated: Composio (MCP-based integration), Adobe Premiere Pro (Lumetri Color panel)
- Protocol context: MCP (Model Context Protocol)
