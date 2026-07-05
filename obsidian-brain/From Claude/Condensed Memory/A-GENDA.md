---
title: "A-GENDA — Condensed Memory"
project: "A-GENDA"
source: claude.ai-memory
tags: [claude, condensed-memory]
---

# A-GENDA — Condensed Memory

> Claude's auto-condensed memory for this project. The full chats live in `Chat Archive/`; this is the summary layer.

**Purpose & context**

Adri (hello@adrianavmarquez.com) is a content creator and influencer who runs her own creator business across beauty, health, and lifestyle categories. She manages brand partnerships, paid campaigns, gifting arrangements, and affiliate relationships. A virtual assistant forwards emails on her behalf. Her primary communication channels are Gmail and Slack.

The core recurring need is a **morning inbox triage workflow** that surfaces who is waiting on a response and what is due within 48 hours — cutting through noise to produce a clear, printable daily action list.

**Current state**

Adri runs this triage workflow regularly, with Gmail as the sole active communication channel (Slack DMs have consistently returned empty results across multiple sessions). Active partnership categories tracked across sessions include:

- **Braun/Peyton** – Smart IPL campaign via brandmail platform; draft deadlines recur
- **Manychat/Steph** – Q2 Reels campaign with specific posting dates
- **Nuvadermis/Annie** – Scar cream content; has been repeatedly overdue
- **YADAH** – Camellia serum content
- **PartnerForward/Nanda**, **Markable/Heidi** – Ongoing partnership contacts
- Cold outreach brands and higher-value always-on campaign evaluations surface periodically

**Key learnings & principles**

- **Always exclude `from:hello@adrianavmarquez.com`** from Gmail filters — without this, subscriber notification floods surface as actionable items
- Slack empty results likely reflect search index limitations, not a truly empty inbox; do not spend multiple retry attempts confirming this — note clear status quickly and move on
- A secondary broad pass (e.g., `from:braun OR from:brandmail`) catches campaign-platform emails that Gmail's category filters sometimes misclassify
- `FULL_CONTENT` is required to determine whether a reply has been sent; `MINIMAL` is sufficient only for extracting sender/subject metadata during triage scanning

**Approach & patterns**

**Gmail triage filter (primary):**
```
is:unread newer_than:7d -category:promotions -category:social -category:updates -category:forums -in:sent -from:hello@adrianavmarquez.com
```

**Secondary pass (read-but-unreplied):**
```
collab OR campaign OR partnership OR meeting OR review
```

**Slack DM search:**
```
* after:[date]  |  channel_types: im,mpim  |  include_bots: False
```
Empty results should be noted without extended retries.

**Urgency ranking:** Urgent / Today / 48 Hours — based on who is waiting and what action is required. Filtered noise (newsletters, notifications, auto-emails, CC-only messages) is listed at the bottom of the output, not discarded silently.

**Output format:** Landscape DOCX with two pages:
1. Color-coded urgency triage table — columns: rank, urgency badge, source (Gmail/Slack), sender, subject + action description, physical checkbox
2. Week-ahead day-by-day plan table, with hard deadline callout line at the footer

**Tools & resources**

- **Gmail** – primary active channel
- **Slack** – secondary channel (consistently clear; check quickly)
- **DOCX generation:** `docx` npm package in Node.js
  - Landscape orientation: `PageOrientation.LANDSCAPE` with `{ width: 15840, height: 12240 }`
  - Save to `/home/claude/`
  - Validate at `/mnt/skills/public/docx/scripts/office/validate.py`
  - Deliver to `/mnt/user-data/outputs/`
- **Brandmail platform** – used by some brand partners (e.g., Braun) for campaign coordination
