---
title: "format-05-negative-marketing"
project: "Advertising Copywritting"
source: claude.ai-project-knowledge
tags: [claude, project-knowledge]
---

# format-05-negative-marketing

> Project knowledge · `format-05-negative-marketing.md`

# Format 05: Negative Marketing

## What This Format IS
A fake one-star review that flips into a compliment. The "negative" framing is the scroll-stopper — the viewer expects a complaint and gets a confession of obsession. Dark, dramatic background makes the product pop. Best used for products with strong loyalty and repeat purchase behavior.

## Copy Slots & Word Counts
| Element | Requirement |
|---|---|
| Star Rating | One filled star, four empty stars (★☆☆☆☆). |
| Review Text | 25–45 words. Starts as a complaint, ends as an admission of love. Pull from `negative_marketing` hooks in research brief. E.g., "Worst purchase I've ever made. Now I'm spending $X/month because nothing else compares." |
| Reviewer Name | First name + "VERIFIED PURCHASE". Muted styling. |
| CTA | 2–5 words. Color-inverted for dark background. |

## Image Direction
- **Background:** Dark/contrasting (opposite of brand background preference). Fills entire frame.
- **Product:** Centered, lit dramatically with warm directional light from one side. Strong shadow against dark background. Product pops against darkness.
- **Text:** Light text on dark background. Fake review graphic styled simply — no boxes or panels.
- **Safe Zones:** No critical content in top 250px or bottom 340px.

## Generation Prompt Template
```
Create a static ad for [BRAND NAME]'s [PRODUCT NAME]. 1080x1920px (9:16 ratio).

One continuous image filling the entire 1080x1920 frame with no panels, boxes, borders, or overlays.

Dark/contrasting background color (opposite of [BRAND BACKGROUND PREFERENCE from brief]) filling the entire frame. [PRODUCT centered, lit dramatically with warm directional light from one side creating a strong shadow against the dark background]. The product pops against the darkness.

Use the product reference image to match the product styling precisely.

TEXT positioned in the center area of the image, not in the top 250px or bottom 340px:

A fake one-star review graphic. Light text on the dark background:

One star (one filled star, four empty stars)

Review text in [BRAND BODY TYPOGRAPHY from brief], sentence case:
"[NEGATIVE HOOK THAT FLIPS INTO A COMPLIMENT - pull from negative_marketing hooks in research brief. E.g., 'Worst purchase I've ever made. Now I'm spending $X/month because nothing else compares. I'll never be able to go back to [OLD WAY from pain points].']"

Reviewer name in [BRAND ACCENT TYPOGRAPHY from brief], muted:
[NAME] / VERIFIED PURCHASE

CTA styled per [BRAND CTA STYLE from brief] but color-inverted for dark background:
[YOUR WINNING AD CTA]

Brand mark: [BRAND LOGO per brief placement rules]

Style: dark, dramatic, editorial. High contrast. The product glows against the background. The fake negative review is the scroll-stopper.
```

## Research Brief Fields Required
- `ad_hooks.negative_marketing` (for review copy)
- `customer_pain_points` (for the "old way" reference)
- `visual_system.background_preference` (to invert it)
- `visual_system` (all typography fields)

