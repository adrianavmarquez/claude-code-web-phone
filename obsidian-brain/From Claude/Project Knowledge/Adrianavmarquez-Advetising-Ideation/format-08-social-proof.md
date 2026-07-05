---
title: "format-08-social-proof"
project: "Adrianavmarquez Advetising Ideation"
source: claude.ai-project-knowledge
tags: [claude, project-knowledge]
---

# format-08-social-proof

> Project knowledge · `format-08-social-proof.md`

# Format 08: Social Proof

## What This Format IS
A lifestyle flat lay where the scroll-stopper is a large, impressive number (reviews, customers, units sold, etc.). The big number dominates the visual hierarchy and the copy supports it. Best for brands with strong review metrics or notable community size.

## Copy Slots & Word Counts
| Element | Requirement |
|---|---|
| Big Number | The most impressive number from `statistics_and_data` or `review_metrics`. Very large type. |
| Supporting Text | 5–10 words. What that number means. |
| Headline | 4–10 words. |
| Source | 2–5 words. Muted. Where the number comes from. |
| CTA | 2–5 words. |

## Image Direction
- **Composition:** Lifestyle flat lay per photography direction from brief. Products on a textured, warm, tactile surface (linen, bedsheet, towel, wood). Multiple product variants visible showing range.
- **Lighting:** Warm natural lighting. Surface extends to all edges naturally.
- **Text:** The big number is the visual anchor. Everything else is secondary.
- **Safe Zones:** No critical content in top 250px or bottom 340px.

## Generation Prompt Template
```
Create a static ad for [BRAND NAME]'s [PRODUCT NAME]. 1080x1920px (9:16 ratio).

One continuous image filling the entire 1080x1920 frame with no panels, boxes, borders, or overlays.

[DESCRIBE A LIFESTYLE FLAT LAY per photography direction from brief - products on a textured surface like linen, bedsheet, towel, wood, something warm and tactile]. Multiple product variants visible showing range. Warm natural lighting. The surface extends to all edges naturally.

Use the product reference image to match the product styling precisely.

TEXT positioned in the center area, not in the top 250px or bottom 340px:

Large number in [BRAND HEADLINE TYPOGRAPHY from brief], very large, centered:
[BIG IMPRESSIVE NUMBER from statistics_and_data in research brief]

Supporting text in [BRAND BODY TYPOGRAPHY from brief]:
[What that number means]

Headline in [BRAND HEADLINE TYPOGRAPHY from brief]:
[YOUR WINNING AD HEADLINE]

Small text in [BRAND ACCENT TYPOGRAPHY from brief], muted:
[SOURCE from statistics_and_data in research brief]

CTA styled per [BRAND CTA STYLE from brief]:
[YOUR WINNING AD CTA]

Brand mark: [BRAND LOGO per brief placement rules]

Style: lifestyle flat lay per [PHOTOGRAPHY DIRECTION from brief]. The big number is the scroll-stopper.
```

## Research Brief Fields Required
- `statistics_and_data` (for the big number and source)
- `review_metrics` (alternative source for big number)
- `ad_hooks.social_proof_hooks` (for headline)
- `visual_system.imagery_style` (for flat lay direction)
- `visual_system` (all typography fields)

