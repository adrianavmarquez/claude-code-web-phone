---
title: "format-09-statistics"
project: "Advertising Copywritting"
source: claude.ai-project-knowledge
tags: [claude, project-knowledge]
---

# format-09-statistics

> Project knowledge · `format-09-statistics.md`

# Format 09: Statistics

## What This Format IS
A typographic, data-forward layout where three stacked statistics dominate the visual. Minimal imagery — the product is small and secondary. Should feel like an infographic. Best for brands with clinical studies, certifications, or strong quantitative proof points.

## Copy Slots & Word Counts
| Element | Requirement |
|---|---|
| Headline | 4–10 words. Top of safe zone. Sets up the data. |
| Stat 1 | Big number (very large type) + 3–6 word descriptor (muted). |
| Stat 2 | Big number + 3–6 word descriptor. |
| Stat 3 | Big number + 3–6 word descriptor. |
| CTA | 2–5 words. |

## Image Direction
- **Background:** Brand background color (muted/neutral version). Fills entire frame.
- **Product:** A single product positioned small in the bottom-center of the safe zone. The focus is on the numbers, not the product.
- **Typography:** Numbers very large in brand headline font. Descriptors in brand accent font. Generous vertical spacing between stats.
- **Style:** Typographic and data-forward. Should feel like an infographic.
- **Safe Zones:** No critical content in top 250px or bottom 340px.

## Generation Prompt Template
```
Create a static ad for [BRAND NAME]'s [PRODUCT NAME]. 1080x1920px (9:16 ratio).

One continuous image filling the entire 1080x1920 frame with no panels, boxes, borders, or overlays.

[BRAND BACKGROUND COLOR from brief, muted/neutral version] background filling the entire frame. A single product positioned small in the bottom-center of the safe zone. The focus is on the numbers, not the product.

Headline in [BRAND HEADLINE TYPOGRAPHY from brief], top of safe zone:
[YOUR WINNING AD HEADLINE]

Three statistics stacked vertically with generous spacing, pulled from [statistics_and_data in research brief]:

[BIG NUMBER 1]
[DESCRIPTOR in BRAND ACCENT TYPOGRAPHY from brief, muted]

[BIG NUMBER 2]
[DESCRIPTOR]

[BIG NUMBER 3]
[DESCRIPTOR]

Numbers in [BRAND HEADLINE TYPOGRAPHY from brief], very large. Descriptors in [BRAND ACCENT TYPOGRAPHY from brief].

CTA styled per [BRAND CTA STYLE from brief]:
[YOUR WINNING AD CTA]

Brand mark: [BRAND LOGO per brief placement rules]

Style: typographic and data-forward. Big numbers dominate. Minimal imagery. Should feel like an infographic.
```

## Research Brief Fields Required
- `statistics_and_data` (for all three stats)
- `ad_hooks.statistic_hooks` (for headline)
- `visual_system.background_preference`
- `visual_system` (all typography fields)

