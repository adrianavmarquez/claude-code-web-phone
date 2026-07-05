---
title: "format-01-before-after"
project: "Advertising Copywritting"
source: claude.ai-project-knowledge
tags: [claude, project-knowledge]
---

# format-01-before-after

> Project knowledge · `format-01-before-after.md`

# Format 01: From This to This (Before & After)

## What This Format IS
A side-by-side split composition that contrasts the "problem state" (left) with the "solution state" (right). It works by making the transformation visceral and immediate — the viewer sees the before and after in a single glance without reading a word.

## Copy Slots & Word Counts
| Element | Requirement |
|---|---|
| Headline | 4–10 words. States the transformation directly. |
| Left Label | 2–4 words. Names the "before" state. Muted/subdued styling. |
| Right Label | 2–4 words. Names the "after" state. Accent color. |
| CTA | 2–5 words. Action-oriented. |

## Image Direction
- **Composition:** Side-by-side split. Left = problem (cluttered, chaotic, generic competitors). Right = hero product (centered, generous space, clean).
- **Divider:** Thin vertical line separating the two halves.
- **Shot:** Directly overhead. Soft natural light, gentle shadows.
- **Surface:** Brand background surface from brief, extending seamlessly to all edges.
- **Safe Zones:** No critical content in top 250px or bottom 340px.
- **Text placement:** Center area of the image only (y:250 to y:1580).

## Generation Prompt Template
```
Create a static ad for [BRAND NAME]'s [PRODUCT NAME]. 1080x1920px (9:16 ratio).

One continuous photograph filling the entire 1080x1920 frame with no panels, boxes, borders, or overlays of any kind.

Side-by-side split composition on a [BACKGROUND SURFACE from brand brief] surface. Left side: [DESCRIBE 6-8 COMPETITOR/GENERIC PRODUCTS scattered and cluttered, representing the "problem" state]. Right side: [HERO PRODUCT centered with generous space, representing the "solution" state]. A thin vertical divider line separates the two halves. Shot from directly overhead. Soft natural light, gentle shadows. The surface extends to all edges seamlessly.

Use the product reference image to match the product styling precisely.

TEXT positioned in the center area of the image, not in the top 250px or bottom 340px:

Headline in [BRAND HEADLINE TYPOGRAPHY from brief], centered:
[YOUR WINNING AD HEADLINE]

Left label in [BRAND ACCENT TYPOGRAPHY from brief], muted: [PROBLEM LABEL]
Right label in [BRAND ACCENT TYPOGRAPHY from brief]: [SOLUTION LABEL]

CTA styled per [BRAND CTA STYLE from brief]:
[YOUR WINNING AD CTA]

Brand mark: [BRAND LOGO per brief placement rules]

Style: [PHOTOGRAPHY DIRECTION from brief]. The left side should feel chaotic, the right side should feel like relief.
```

## Research Brief Fields Required
- `visual_system.background_preference`
- `visual_system.imagery_style`
- `visual_system.primary_font` / `labels_font` / `cta_font`
- `competitive_landscape.top_competitors` (for left side)
- `transformation_claims` (for headline and labels)

