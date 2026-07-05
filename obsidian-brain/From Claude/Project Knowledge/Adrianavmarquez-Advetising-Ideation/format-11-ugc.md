---
title: "format-11-ugc"
project: "Adrianavmarquez Advetising Ideation"
source: claude.ai-project-knowledge
tags: [claude, project-knowledge]
---

# format-11-ugc

> Project knowledge · `format-11-ugc.md`

# Format 11: UGC (User-Generated Content)

## What This Format IS
A simulated iPhone selfie or casual phone photo that looks indistinguishable from real user content. Text overlays styled like Instagram story stickers. The format works because it doesn't look like an ad — it looks like something a real person posted. Raw, authentic, unpolished on purpose.

## Copy Slots & Word Counts
| Element | Requirement |
|---|---|
| Top Text Overlay | 5–12 words. Casual, first person. Pull from `ugc_hooks` in research brief. |
| Middle Text Overlay | 5–12 words. Ties to winning ad message. |
| Bottom Text Overlay | 5–10 words. Smaller. References the CTA action. |
| CTA | 2–5 words. Styled per brand CTA style. |

## Image Direction
- **Style:** Looks like a real iPhone selfie. Slightly overexposed like a phone camera. Real skin, no filter.
- **Setting:** Contextual and lived-in (bathroom mirror, kitchen counter, gym locker). Not staged.
- **Person:** Matches target_audience from research brief. Natural interaction with product — holding it up, showing it to camera, mid-use.
- **Text overlays:** Styled like Instagram story text — slightly rounded white background boxes. NOT brand typography.
- **iPhone/mirror edge:** Partially visible to reinforce authenticity.

## Generation Prompt Template
```
Create a static ad for [BRAND NAME]'s [PRODUCT NAME]. 1080x1920px (9:16 ratio).

One continuous image filling the entire 1080x1920 frame with no panels, boxes, borders, or overlays.

This should look like a [CONTEXTUAL SELFIE - bathroom mirror, kitchen counter, gym locker] taken with an iPhone. A [PERSON DESCRIPTION matching target_audience from research brief] is [DESCRIBE NATURAL INTERACTION WITH PRODUCT - holding it up, showing it to camera, mid-use]. The setting is real and lived-in, not staged. Warm imperfect lighting. Slightly overexposed like a phone camera. Real skin, no filter. The iPhone and mirror edge are partially visible.

TEXT styled like Instagram story text overlays with slightly rounded white background boxes:

Top text: "[CASUAL LINE 1 - pull from ugc_hooks in research brief]"
Middle text: "[CASUAL LINE 2 - ties to winning ad message]"
Bottom text (smaller): "[CASUAL LINE 3 - references the CTA action]"

CTA styled per [BRAND CTA STYLE from brief]:
[YOUR WINNING AD CTA]

Brand mark: [BRAND NAME]

Style: raw iPhone selfie UGC. Should be indistinguishable from a real person's Instagram story. Casual, authentic, unpolished on purpose.
```

## Research Brief Fields Required
- `ad_hooks.ugc_hooks` (for text overlay copy)
- `target_audience` (for person description)
- `brand_identity.tone_notes` (to calibrate casual voice)
- `visual_system.cta_font` / `cta_style`

## Important Note
This format intentionally breaks brand visual guidelines (no Figtree, no Morguns, no brand colors in the overlays). That is by design. The goal is authenticity, not brand consistency. The only brand element present is the brand name as a simple text mark.

