---
title: "format-14-ugly-ad-ms-paint"
project: "Adrianavmarquez Advetising Ideation"
source: claude.ai-project-knowledge
tags: [claude, project-knowledge]
---

# format-14-ugly-ad-ms-paint

> Project knowledge · `format-14-ugly-ad-ms-paint.md`

# Format 14: Ugly Ad / MS Paint

## What This Format IS
An intentionally terrible-looking ad that mimics something made in 5 minutes in Microsoft Paint. The ugliness is the strategy — maximum pattern interrupt. It stops the scroll because it looks nothing like a real ad. Best used as a testing wildcard when polished ads are underperforming or when you want to test raw message strength without design.

## Copy Slots & Word Counts
| Element | Requirement |
|---|---|
| Top Headline | 5–10 words. Casual, direct. Arial Bold, slightly off-center. |
| Pointer Text | 3–6 words. Red, Comic Sans. Next to the crude arrows pointing at the product. |
| CTA Setup Line | 5–10 words. Blue underlined text like a hyperlink. Times New Roman. |
| CTA | 2–5 words. In a crude rectangle. |
| Brand Name | Lowercase, tiny, gray, bottom of image. |

## Image Direction
- **Background:** White. Flat.
- **Product:** Poorly cut-out photo of the product pasted in the center. Visible rough edges around the cutout (like someone used the lasso tool badly). Slightly crooked.
- **Arrows:** Crude red arrows drawn in a wobbly MS Paint style pointing at the products.
- **Typography:** Mix of ugly default system fonts (Arial, Comic Sans, Times New Roman). Mismatched sizes. Some text slightly crooked. Nothing perfectly centered.
- **Yellow highlight:** A yellow highlighted box around a key word, like the MS Paint highlighter tool.
- **CTA box:** Crude rectangle, white fill, not perfectly shaped.
- **Key rule:** NO polish. NO brand guidelines. The ugliness is intentional and total.

## Generation Prompt Template
```
Create a static ad for [BRAND NAME]'s [PRODUCT NAME]. 1080x1920px (9:16 ratio).

This ad should look like it was made in 5 minutes in Microsoft Paint by someone who has never designed an ad before. Intentionally ugly, low-fi, amateur.

White background. A poorly cut-out photo of [PRODUCT(S)] pasted in the center with visible rough edges around the cutout, like someone used the lasso tool badly. Slightly crooked.

Crude red arrows drawn in a wobbly MS Paint style pointing at the products.

TEXT in a mix of ugly default system fonts (Arial, Comic Sans, Times New Roman). Mismatched sizes. Some text slightly crooked. Nothing perfectly centered:

Top text (large, black, Arial Bold, slightly off-center):
[CASUAL VERSION OF YOUR HEADLINE]

Middle text (red, Comic Sans, smaller, next to arrows):
[POINTER TEXT]

Below products (blue underlined text like a hyperlink, Times New Roman):
[CASUAL CTA SETUP LINE]

A yellow highlighted box around a key word like the MS Paint highlighter tool.

CTA (black text in a crude rectangle, white fill, not perfectly shaped):
[YOUR CTA]

Small text at bottom (tiny, gray, Arial):
[brand name in lowercase]

NO polish. NO brand guidelines. The ugliness is the strategy. Maximum pattern interrupt.
```

## Research Brief Fields Required
- `customer_pain_points` (for the casual headline — raw, unpolished version)
- `brand_identity.tone_notes` (to understand what to intentionally break)
- `ad_hooks` (any hook works — the format tests message strength, not design)

## Important Note
This format intentionally violates every brand guideline. That is by design. It is used specifically to test whether the message itself resonates, independent of design quality. Use it as a testing wildcard, not as a primary creative.

