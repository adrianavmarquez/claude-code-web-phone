---
title: "format-10-testimonial"
project: "Advertising Copywritting"
source: claude.ai-project-knowledge
tags: [claude, project-knowledge]
---

# format-10-testimonial

> Project knowledge · `format-10-testimonial.md`

# Format 10: Testimonial

## What This Format IS
An intimate product-in-hand or product-in-use photograph with a real customer review overlaid. The review is the hero copy — the headline supports it. Works best when the testimonial directly mirrors the winning ad's message. Warm, tactile, personal.

## Copy Slots & Word Counts
| Element | Requirement |
|---|---|
| Star Rating | Five stars (★★★★★). |
| Review Quote | 20–40 words. A real testimonial from `testimonials` in research brief. Choose one that ties directly to the winning ad's message. In quotation marks. |
| Reviewer Attribution | "VERIFIED CUSTOMER". Muted. |
| Headline | 4–10 words. Supports or echoes the testimonial. |
| CTA | 2–5 words. |

## Image Direction
- **Photo:** Intimate product-in-hand or product-in-use. Someone holding the product, touching it, using it. Natural skin texture visible. Warm interior background, shallow depth of field. Editorial, not studio.
- **Lighting:** Per photography direction from brief. Warm, tactile.
- **Text:** Overlaid directly on photo. No background panels.
- **Safe Zones:** No critical content in top 250px or bottom 340px.

## Generation Prompt Template
```
Create a static ad for [BRAND NAME]'s [PRODUCT NAME]. 1080x1920px (9:16 ratio).

One continuous image filling the entire 1080x1920 frame with no panels, boxes, borders, or overlays.

[DESCRIBE AN INTIMATE PRODUCT-IN-HAND OR PRODUCT-IN-USE PHOTOGRAPH per photography direction from brief - someone holding the product, touching it, using it. Natural skin texture visible. Warm interior background, shallow depth of field. Editorial, not studio.]

Use the product reference image to match the product styling precisely.

TEXT positioned in the center area, not in the top 250px or bottom 340px:

Five stars: ★★★★★

Review quote in [BRAND BODY TYPOGRAPHY from brief]:
"[TESTIMONIAL from testimonials in research brief - choose one that ties to your winning ad's message]"

Reviewer in [BRAND ACCENT TYPOGRAPHY from brief], muted:
VERIFIED CUSTOMER

Headline in [BRAND HEADLINE TYPOGRAPHY from brief]:
[YOUR WINNING AD HEADLINE]

CTA styled per [BRAND CTA STYLE from brief]:
[YOUR WINNING AD CTA]

Brand mark: [BRAND LOGO per brief placement rules]

Style: intimate product-in-hand photography per [PHOTOGRAPHY DIRECTION from brief]. Warm, tactile, personal. The review feels authentic.
```

## Research Brief Fields Required
- `testimonials` (for the review quote — pick one that matches the winning message)
- `ad_hooks.testimonial_hooks` (for headline)
- `visual_system.imagery_style` (for photo direction)
- `visual_system` (all typography fields)

