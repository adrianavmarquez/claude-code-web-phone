---
title: "format-04-handwriting"
project: "Advertising Copywritting"
source: claude.ai-project-knowledge
tags: [claude, project-knowledge]
---

# format-04-handwriting

> Project knowledge · `format-04-handwriting.md`

# Format 04: Handwriting / Sticky Note

## What This Format IS
A flat lay lifestyle photo with a sticky note in the scene. The handwritten message on the note delivers the ad copy in a casual, personal tone — like a note from a friend. The format breaks the "this is an ad" pattern by mimicking real life.

## Copy Slots & Word Counts
| Element | Requirement |
|---|---|
| Handwritten Note | 15–30 words. Casual, lowercase, personal. Rewrite the winning message as if writing to a friend. Pull from `handwriting_hooks` in research brief. |
| CTA | 2–5 words. Overlaid directly on the photo below the note. |

## Image Direction
- **Scene:** A contextual surface aligned with brand photography direction (e.g., kitchen counter, linen, wood). Shot from above.
- **Props:** Sticky note (cream-colored, slightly angled) + product(s) positioned next to the note.
- **Lighting:** Per photography direction from brief. Warm, intimate.
- **Text on note:** Casual black handwritten script. Real and slightly imperfect. Lowercase.
- **No background panels** behind any text — all text overlays directly on the photograph.
- **Safe Zones:** CTA and brand mark in lower portion, not in bottom 340px.

## Generation Prompt Template
```
Create a static ad for [BRAND NAME]'s [PRODUCT NAME]. 1080x1920px (9:16 ratio).

One continuous photograph filling the entire 1080x1920 frame with no panels, boxes, borders, or overlays of any kind.

The scene: a [CONTEXTUAL SURFACE aligned with brand photography direction] photographed from above. Sitting on the surface is a sticky note (cream-colored, slightly angled) and [PRODUCT(S) positioned next to the note, showing enough variants to support the copy]. [LIGHTING per photography direction from brief]. The surface fills the entire frame edge to edge.

Use the product reference image to match the product styling precisely.

On the sticky note, in casual black handwritten script:

"[HANDWRITTEN VERSION OF YOUR WINNING AD MESSAGE - rewritten to feel casual and personal, like a note to a friend. Pull from handwriting_hooks in research brief.]"

The handwriting should feel real and slightly imperfect. Lowercase, casual.

In the lower portion of the image, directly over the photograph:

CTA styled per [BRAND CTA STYLE from brief]:
[YOUR WINNING AD CTA]

Brand mark: [BRAND LOGO per brief placement rules]

No background panels behind any text. Style: overhead flat lay lifestyle photography per [PHOTOGRAPHY DIRECTION from brief]. One seamless surface. Warm, intimate, casual.
```

## Research Brief Fields Required
- `ad_hooks.handwriting_hooks` (for the note copy)
- `visual_system.imagery_style` (for surface and lighting)
- `visual_system.cta_font` / `cta_style`
- `brand_identity.tone_notes` (to calibrate casual voice)

