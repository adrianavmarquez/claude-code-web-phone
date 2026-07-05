---
title: "format-13-new-creative-swatch-demo"
project: "Adrianavmarquez Advetising Ideation"
source: claude.ai-project-knowledge
tags: [claude, project-knowledge]
---

# format-13-new-creative-swatch-demo

> Project knowledge · `format-13-new-creative-swatch-demo.md`

# Format 13: New Creative Format (Swatch / Demo)

## What This Format IS
An experimental, pattern-interrupt format that shows the product in an unexpected, tangible, or interactive context — swatches on skin, product poured on a surface, ingredients laid out, the product in an unusual setting. This format should feel completely different from everything else in the creative set. The goal is to stop the scroll by showing something the viewer hasn't seen before.

## Copy Slots & Word Counts
| Element | Requirement |
|---|---|
| Headline | 4–10 words. |
| Demo Labels | 2–5 words each, connected to demo elements by thin lines (if applicable). |
| Bridge Line | 8–15 words. Connects the visual demo to the CTA. Pull from `new_format_hooks` in research brief. |
| CTA | 2–5 words. |

## Image Direction
- **Concept:** A creative product demonstration relevant to your product. Something tangible and interactive — swatches on skin, product spread on a surface, ingredients laid out, the product in an unexpected context.
- **Lighting:** Warm natural light per photography direction from brief.
- **Surface/context:** Extends to all edges.
- **Labels:** Connected to demo elements by thin lines in brand accent color (if applicable).
- **Safe Zones:** No critical content in top 250px or bottom 340px.
- **Key rule:** This format should be completely different from the other 14. If it could be mistaken for Format 01 or Format 03, rethink it.

## Generation Prompt Template
```
Create a static ad for [BRAND NAME]'s [PRODUCT NAME]. 1080x1920px (9:16 ratio).

One continuous image filling the entire 1080x1920 frame with no panels, boxes, borders, or overlays.

[DESCRIBE A CREATIVE PRODUCT DEMONSTRATION relevant to your product - swatches on skin, product poured/spread on a surface, ingredients laid out, the product in an unexpected context]. This format should feel interactive and tangible. Warm natural light per [PHOTOGRAPHY DIRECTION from brief]. Surface/context extends to all edges.

Use the product reference image to match the product styling precisely.

TEXT positioned in the center area, not in the top 250px or bottom 340px:

Headline in [BRAND HEADLINE TYPOGRAPHY from brief]:
[YOUR WINNING AD HEADLINE]

[LABELS FOR EACH DEMO ELEMENT in BRAND ACCENT TYPOGRAPHY from brief - connected by thin lines in BRAND COLOR if applicable]

Supporting text in [BRAND BODY TYPOGRAPHY from brief]:
[LINE THAT BRIDGES FROM THE DEMO TO THE CTA - pull from new_format_hooks in research brief]

CTA styled per [BRAND CTA STYLE from brief]:
[YOUR WINNING AD CTA]

Brand mark: [BRAND LOGO per brief placement rules]

Style: [UNIQUE VISUAL APPROACH]. This format should be completely different from everything else in the set.
```

## Research Brief Fields Required
- `ad_hooks.new_format_hooks` (for bridge line and headline)
- `product_details.key_ingredients_or_specs` (for demo elements and labels)
- `visual_system.accent_color_hex` (for callout lines)
- `visual_system.imagery_style`
- `visual_system` (all typography fields)

