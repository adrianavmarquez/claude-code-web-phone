---
title: "format-06-news"
project: "Advertising Copywritting"
source: claude.ai-project-knowledge
tags: [claude, project-knowledge]
---

# format-06-news

> Project knowledge · `format-06-news.md`

# Format 06: News

## What This Format IS
A lifestyle/usage photo with a "breaking news" banner overlaid. The format borrows credibility and urgency from news media aesthetics. Works best for product launches, new formulations, or any announcement-worthy moment. Should feel like a product story, not a traditional ad.

## Copy Slots & Word Counts
| Element | Requirement |
|---|---|
| Breaking News Banner | "JUST ANNOUNCED" or similar. Uppercase. Short strip in brand primary color. |
| Headline | 6–12 words. Newsworthy framing of the winning message. Pull from `news_hooks` in research brief. |
| Subhead | 8–15 words. Supporting detail from product intelligence. |
| CTA | 2–5 words. |

## Image Direction
- **Photo:** Close-up lifestyle/usage photograph per photography direction from brief. Someone using the product, applying it, holding it. Real skin/hands, natural light, shallow depth of field. Editorial and intimate, not staged.
- **Text:** Overlaid with subtle shadow for legibility. No background panels.
- **Safe Zones:** No critical content in top 250px or bottom 340px.

## Generation Prompt Template
```
Create a static ad for [BRAND NAME]'s [PRODUCT NAME]. 1080x1920px (9:16 ratio).

One continuous image filling the entire 1080x1920 frame with no panels, boxes, borders, or overlays.

[DESCRIBE A CLOSE-UP LIFESTYLE/USAGE PHOTOGRAPH per photography direction from brief - someone using the product, applying it, holding it. Real skin/hands, natural light, shallow depth of field. Editorial and intimate, not staged.]

TEXT positioned in the center area of the image, not in the top 250px or bottom 340px:

Breaking news banner in [BRAND ACCENT TYPOGRAPHY from brief], uppercase, on a thin strip in [BRAND PRIMARY COLOR from brief]:
JUST ANNOUNCED

Headline in [BRAND HEADLINE TYPOGRAPHY from brief], with subtle shadow for legibility:
[NEWSWORTHY VERSION OF YOUR WINNING AD MESSAGE - pull from news_hooks in research brief]

Subhead in [BRAND BODY TYPOGRAPHY from brief]:
[SUPPORTING DETAIL from product intelligence. E.g., "X options. 1 quiz. Zero guessing."]

CTA styled per [BRAND CTA STYLE from brief]:
[YOUR WINNING AD CTA]

Brand mark: [BRAND LOGO per brief placement rules]

Style: [PHOTOGRAPHY DIRECTION from brief]. Should feel like a breaking product news story, not a traditional ad.
```

## Research Brief Fields Required
- `ad_hooks.news_hooks` (for headline)
- `product_details` (for subhead supporting detail)
- `visual_system.primary_color_hex` (for banner strip)
- `visual_system.imagery_style` (for lifestyle photo direction)
- `visual_system` (all typography fields)

