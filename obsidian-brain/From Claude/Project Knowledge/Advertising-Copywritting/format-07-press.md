---
title: "format-07-press"
project: "Advertising Copywritting"
source: claude.ai-project-knowledge
tags: [claude, project-knowledge]
---

# format-07-press

> Project knowledge · `format-07-press.md`

# Format 07: Press

## What This Format IS
A clean, editorial layout that leads with media credibility. Publication names, a headline, and a pull quote from an actual press mention. Works best for brands with real press coverage. Soft, airy, magazine-inspired aesthetic. Prestigious and elevated.

## Copy Slots & Word Counts
| Element | Requirement |
|---|---|
| Publication Names | 2–4 publication names in a horizontal row. Muted styling. |
| Headline | 4–10 words. Centered. |
| Pull Quote | 15–30 words. An actual quote from a press mention. In quotation marks. Serif font. |
| Attribution | Publication name. Muted. |
| CTA | 2–5 words. |

## Image Direction
- **Background:** Brand secondary/accent background color. Fills entire frame. Clean, airy.
- **Product:** Positioned in the lower-center area. Shot from above with soft shadows.
- **Typography:** Clean, generous spacing. Magazine-inspired layout.
- **Safe Zones:** No critical content in top 250px or bottom 340px.

## Generation Prompt Template
```
Create a static ad for [BRAND NAME]'s [PRODUCT NAME]. 1080x1920px (9:16 ratio).

One continuous image filling the entire 1080x1920 frame with no panels, boxes, borders, or overlays.

[BRAND SECONDARY/ACCENT BACKGROUND COLOR from brief] background filling the entire frame. [PRODUCT(S) positioned in the lower-center area]. Shot from above with soft shadows. Clean, airy, editorial.

Use the product reference image to match the product styling precisely.

TEXT positioned in the center area of the image, not in the top 250px or bottom 340px:

Publication names in a horizontal row in [BRAND ACCENT TYPOGRAPHY from brief], muted, evenly spaced:
[PUBLICATIONS from press_mentions in research brief]

Headline in [BRAND HEADLINE TYPOGRAPHY from brief], centered:
[YOUR WINNING AD HEADLINE]

Pull quote in serif, centered, with quotation marks:
"[ACTUAL PRESS QUOTE from press_mentions in research brief]"

Attribution in [BRAND ACCENT TYPOGRAPHY from brief], muted:
[PUBLICATION NAME from research brief]

CTA styled per [BRAND CTA STYLE from brief]:
[YOUR WINNING AD CTA]

Brand mark: [BRAND LOGO per brief placement rules]

Style: soft, editorial, magazine-inspired. Prestigious and elevated. Clean typography, generous spacing per [BRAND VISUAL SYSTEM from brief].
```

## Research Brief Fields Required
- `press_mentions` (for publication names and pull quote)
- `ad_hooks.press_hooks` (for headline)
- `visual_system.secondary_color_hex` or `accent_color_hex` (for background)
- `visual_system` (all typography fields)

