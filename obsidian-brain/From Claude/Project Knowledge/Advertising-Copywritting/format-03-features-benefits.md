---
title: "format-03-features-benefits"
project: "Advertising Copywritting"
source: claude.ai-project-knowledge
tags: [claude, project-knowledge]
---

# format-03-features-benefits

> Project knowledge · `format-03-features-benefits.md`

# Format 03: Features & Benefits (Product Diagram)

## What This Format IS
An annotated product diagram that showcases multiple variants or components with thin callout lines pointing to each one. Works like a product guide or editorial spread. Best for products with distinct variants, shades, flavors, or components worth naming individually.

## Copy Slots & Word Counts
| Element | Requirement |
|---|---|
| Headline | 4–10 words. Top of safe zone. |
| Variant Name (×3–5) | 2–5 words each. Label connected to product by thin line. |
| Variant Description (×3–5) | 5–10 words each. Who it's for or what it does. |
| CTA | 2–5 words. Bottom of safe zone. |

## Image Direction
- **Background:** Clean brand background color, filling entire frame edge to edge. No texture, no props.
- **Composition:** Multiple product variants in a staggered diagonal layout. Each with generous space for callout labels.
- **Shot:** Directly above. Soft natural shadows.
- **Callout lines:** Thin lines in brand accent color extending from each product to its label.
- **CRITICAL LAYOUT RULE:** Top 250px and bottom 340px are background-only zones. ALL text, callout lines, and key product imagery must be placed within the center 1330px (y:250 to y:1580).

## Generation Prompt Template
```
Create a static ad for [BRAND NAME]'s [PRODUCT NAME]. 1080x1920px (9:16 ratio).

CRITICAL LAYOUT RULE: The top 250px and bottom 340px are background-only zones. ALL text, callout lines, and key product imagery must be placed within the center 1330px (from y:250 to y:1580). The background extends seamlessly into those zones.

Clean [BRAND BACKGROUND COLOR from brief] background filling the entire frame edge to edge. [DESCRIBE MULTIPLE PRODUCT VARIANTS arranged in a staggered diagonal layout, each showing a different variant/shade/flavor]. Shot from directly above. Soft natural shadows. Generous space between products for callout labels.

Thin lines in [BRAND ACCENT COLOR from brief] extend from each product to a text callout nearby:

[VARIANT 1 NAME from product intelligence]
[Who it's for or what it does]

[VARIANT 2 NAME]
[Who it's for or what it does]

[VARIANT 3 NAME]
[Who it's for or what it does]

[VARIANT 4 NAME]
[Who it's for or what it does]

[VARIANT 5 NAME]
[Who it's for or what it does]

Labels in [BRAND ACCENT TYPOGRAPHY from brief]. Descriptions in [BRAND BODY TYPOGRAPHY from brief].

Headline in [BRAND HEADLINE TYPOGRAPHY from brief], top of safe zone:
[YOUR WINNING AD HEADLINE]

CTA styled per [BRAND CTA STYLE from brief], bottom of safe zone:
[YOUR WINNING AD CTA]

Brand mark: [BRAND LOGO per brief placement rules]

Style: clean product diagram aesthetic. Flat background, no texture or props. Callout lines are thin, precise. Reads like an annotated product guide.
```

## Research Brief Fields Required
- `product_details.key_ingredients_or_specs` (for variant names and descriptions)
- `visual_system.accent_color_hex` (for callout lines)
- `visual_system.background_preference`
- `visual_system` (all typography fields)

