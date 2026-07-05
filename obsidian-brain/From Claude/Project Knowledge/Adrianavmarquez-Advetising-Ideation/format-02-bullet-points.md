---
title: "format-02-bullet-points"
project: "Adrianavmarquez Advetising Ideation"
source: claude.ai-project-knowledge
tags: [claude, project-knowledge]
---

# format-02-bullet-points

> Project knowledge · `format-02-bullet-points.md`

# Format 02: Bullet Points

## What This Format IS
A product-forward layout that leads with a headline and supports it with 4–5 scannable bullet points. Works best for products with multiple distinct benefits or features. The product arrangement in the photo should visually support what the bullets say.

## Copy Slots & Word Counts
| Element | Requirement |
|---|---|
| Headline | 4–10 words. Sets up the list that follows. |
| Bullet 1–5 | 5–10 words each. Each bullet = one distinct, concrete benefit. No overlap. |
| CTA | 2–5 words. |

## Image Direction
- **Composition:** Multiple product variants or a product arrangement that supports the bullet copy (e.g., showing range/variety).
- **Shot:** From above. Lighting per photography direction from brief.
- **Surface:** Extends to all edges naturally.
- **Text:** Left-aligned bullet list with small arrow (→) before each line. Generous line spacing.
- **Safe Zones:** No critical content in top 250px or bottom 340px.

## Generation Prompt Template
```
Create a static ad for [BRAND NAME]'s [PRODUCT NAME]. 1080x1920px (9:16 ratio).

One continuous photograph filling the entire 1080x1920 frame with no panels, boxes, borders, or overlays of any kind.

[DESCRIBE A PRODUCT ARRANGEMENT THAT SUPPORTS THE BULLET COPY - e.g., multiple product variants arranged on a textured surface, showing range/variety]. Shot from above. [LIGHTING per photography direction from brief]. The surface extends to all edges naturally.

Use the product reference image to match the product styling precisely.

TEXT positioned in the center area of the image, not in the top 250px or bottom 340px:

Headline in [BRAND HEADLINE TYPOGRAPHY from brief], centered:
[YOUR WINNING AD HEADLINE]

Bullet list in [BRAND BODY TYPOGRAPHY from brief], left-aligned, generous line spacing, small arrow before each line:

→ [BULLET 1 from research brief - must be visually supported by what's shown]
→ [BULLET 2]
→ [BULLET 3]
→ [BULLET 4]
→ [BULLET 5]

CTA styled per [BRAND CTA STYLE from brief]:
[YOUR WINNING AD CTA]

Brand mark: [BRAND LOGO per brief placement rules]

Style: [PHOTOGRAPHY DIRECTION from brief]. The product arrangement is the hero. Text overlays feel designed, not pasted on.
```

## Research Brief Fields Required
- `product_details.key_ingredients_or_specs` (for bullets)
- `transformation_claims` (for headline)
- `visual_system` (all typography and color fields)
- `visual_system.imagery_style`

