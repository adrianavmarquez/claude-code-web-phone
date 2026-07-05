---
title: "format-12-us-vs-them"
project: "Adrianavmarquez Advetising Ideation"
source: claude.ai-project-knowledge
tags: [claude, project-knowledge]
---

# format-12-us-vs-them

> Project knowledge · `format-12-us-vs-them.md`

# Format 12: Us vs. Them

## What This Format IS
An overhead comparison flat lay that contrasts competitor/generic products (left, messy) with your product (right, clean). The visual contrast tells the story instantly without needing to read. Checkmarks and X marks reinforce the comparison. Best for brands with clear, defensible differentiators.

## Copy Slots & Word Counts
| Element | Requirement |
|---|---|
| Headline | 4–10 words. Top of safe zone. Sets up the comparison. |
| Left Side (✕ marks) | 3–4 competitor weaknesses. 4–8 words each. Pull from `us_vs_them_angles` in research brief. Muted styling. |
| Right Side (✓ marks) | 3–4 your advantages. 4–8 words each. Pull from `us_vs_them_angles` in research brief. Accent color. |
| CTA | 2–5 words. |

## Image Direction
- **Composition:** Overhead flat lay. Left = cluttered competitor/generic products (cheap packaging, messy, scattered). Right = your product(s) neatly placed with clean space. No hard divider line — the mess on the left naturally transitions to clean space on the right.
- **Lighting:** Bright, even. Surface extends to all edges.
- **Safe Zones:** No critical content in top 250px or bottom 340px.

## Generation Prompt Template
```
Create a static ad for [BRAND NAME]'s [PRODUCT NAME]. 1080x1920px (9:16 ratio).

One continuous image filling the entire 1080x1920 frame with no panels, boxes, borders, or overlays.

Overhead flat lay on a clean surface. Left side: [DESCRIBE CLUTTERED COMPETITOR/GENERIC PRODUCTS based on competitive_landscape from research brief - cheap packaging, messy, powder fallout, scattered tools]. Right side: [YOUR PRODUCT(S) neatly placed with clean space]. No hard divider line. The mess on the left naturally transitions to clean space on the right. Bright, even lighting. Surface extends to all edges.

Headline in [BRAND HEADLINE TYPOGRAPHY from brief], top of safe zone:
[YOUR WINNING AD HEADLINE]

Left side in [BRAND ACCENT TYPOGRAPHY from brief], muted, X marks:
✕ [COMPETITOR WEAKNESS 1 from us_vs_them_angles in research brief]
✕ [COMPETITOR WEAKNESS 2]
✕ [COMPETITOR WEAKNESS 3]
✕ [COMPETITOR WEAKNESS 4]

Right side in [BRAND ACCENT TYPOGRAPHY from brief], checkmarks:
✓ [YOUR ADVANTAGE 1 from us_vs_them_angles in research brief]
✓ [YOUR ADVANTAGE 2]
✓ [YOUR ADVANTAGE 3]
✓ [YOUR ADVANTAGE 4]

CTA styled per [BRAND CTA STYLE from brief]:
[YOUR WINNING AD CTA]

Brand mark: [BRAND LOGO per brief placement rules]

Style: overhead comparison flat lay per [PHOTOGRAPHY DIRECTION from brief]. The visual contrast between messy and clean tells the story instantly.
```

## Research Brief Fields Required
- `competitive_landscape.us_vs_them_angles` (for ✕ and ✓ copy)
- `competitive_landscape.top_competitors` (for left side visual description)
- `ad_hooks.us_vs_them_hooks` (for headline)
- `visual_system.imagery_style`
- `visual_system` (all typography fields)

