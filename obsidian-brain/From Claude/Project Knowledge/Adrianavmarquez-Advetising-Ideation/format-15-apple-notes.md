---
title: "format-15-apple-notes"
project: "Adrianavmarquez Advetising Ideation"
source: claude.ai-project-knowledge
tags: [claude, project-knowledge]
---

# format-15-apple-notes

> Project knowledge · `format-15-apple-notes.md`

# Format 15: Apple Notes

## What This Format IS
A simulated screenshot of the Apple Notes app on an iPhone. Pure text on white, with a bulleted list of real customer pain points. Unlike the Ugly Ad, this format uses real customer language from the research brief — it works because the pain points feel uncomfortably accurate. Should be indistinguishable from an actual iPhone Notes screenshot.

## Copy Slots & Word Counts
| Element | Requirement |
|---|---|
| Notes Title (bold) | 6–12 words. List-style headline. E.g., "Signs you're [DOING THE WRONG THING based on pain points]:" Pull from `ad_hooks` in research brief. |
| Bullet 1–5 | 5–12 words each. Real customer pain points in customer language. Pull from `customer_pain_points` in research brief. |
| CTA Setup Text | 10–20 words. Casual, first person, like someone typing a note to themselves. References the CTA action. |
| Brand Name | Small, bottom right corner. |

## Image Direction
- **Style:** Exact replica of iPhone Notes app screenshot. Same padding, font sizes (San Francisco / system font), spacing as the real app.
- **Background:** White. No photographs except one small product image.
- **Product image:** Small photo of product(s) pasted into the note, as if dragged from camera roll. Small, casual, not centered perfectly.
- **iOS elements:** Yellow "< Notes" back arrow and text at the very top left, exactly as it appears in iOS.
- **Key rule:** Should be completely indistinguishable from a real iPhone Notes screenshot.

## Generation Prompt Template
```
Create a static ad for [BRAND NAME]'s [PRODUCT NAME]. 1080x1920px (9:16 ratio).

This should look exactly like a screenshot of the Apple Notes app on an iPhone. White background. No photographs except one small product image pasted in.

At the very top left, the yellow "< Notes" back arrow and text, exactly as it appears in iOS.

Below that, text in the Notes app default font (San Francisco / system font), left-aligned:

Large bold text (Notes title style):
[LIST-STYLE HEADLINE from research brief hooks - e.g., "Signs you're [DOING THE WRONG THING based on pain_points]:"]

Bulleted list in regular weight:
• [PAIN POINT 1 from customer_pain_points in research brief, in customer language]
• [PAIN POINT 2]
• [PAIN POINT 3]
• [PAIN POINT 4]
• [PAIN POINT 5]

Line break, then regular text:
[CTA SETUP - casual, first person, like someone typing a note to themselves. Reference your CTA action.]

Below, a small photo of [PRODUCT(S)] pasted into the note, as if dragged from camera roll. Small, casual, not centered perfectly.

At the bottom right corner, small:
[BRAND NAME]

The entire image should be indistinguishable from an actual iPhone Notes screenshot. Same padding, font sizes, spacing. Pure text on white.
```

## Research Brief Fields Required
- `customer_pain_points` (for the bulleted list — must use real customer language)
- `ad_hooks` (for the title/headline)
- `brand_identity.tone_notes` (to calibrate the casual CTA setup text)

## Important Note
Like the Ugly Ad (Format 14), this format intentionally breaks brand visual guidelines. No Figtree, no Morguns, no brand colors. The power is in the pain point accuracy, not the design. Both formats are pattern-interrupt tools — use them when polished formats plateau.

