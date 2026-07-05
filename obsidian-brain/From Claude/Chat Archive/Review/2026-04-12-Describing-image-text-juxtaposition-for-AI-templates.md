---
title: "Describing image-text juxtaposition for AI templates"
source: claude.ai-chat
created: "2026-04-12 04:58"
summary: "**Conversation Overview**  The person is working on a portfolio landing page and sought help generating AI prompts to recreate specific sections of it for the tool Emergent. The conversation focused on two distinct sections: a hero/intro section and a work categories section. Rather than building from scratch, the person clarified they only needed to adjust or recreate specific sections of an already-built portfolio.  For the hero section, key details established included the font 'Heading Now' (heavy/black weight), an asymmetric editorial grid where large text fragments and image placeholders alternate as equal-weight elements, five image placeholders of specified shapes and sizes on a white background, and an intentional off-balance layout. The person clarified that image curation was irrelevant — only placeholder shapes and sizes mattered.  For the work categories section, the defining characteristic was a zigzag layout — items intentionally staggered left and right in an off-balance diagonal rhythm rather than aligned to a grid. This section included four category items (Technology, Fashion, Hair, Beauty) with image placeholders, small scattered star decorative elements in a specific blue (#3846C4), and the bracketed heading '[my work]' in Heading Now font. Claude generated detailed AI prompts for Emergent for both sections, incorporating the zigzag and asymmetric layout logic as the core structural concept. The person's working preference was precise and correction-oriented, clarifying misunderstandings directly and efficiently."
messages: 14
claude_uuid: "83bcb22c-5302-49ef-bc75-29d407e22462"
tags: [claude, chat, archive]
---
# Describing image-text juxtaposition for AI templates

> **Conversation Overview**

The person is working on a portfolio landing page and sought help generating AI prompts to recreate specific sections of it for the tool Emergent. The conversation focused on two distinct sections: a hero/intro section and a work categories section. Rather than building from scratch, the person clarified they only needed to adjust or recreate specific sections of an already-built portfolio.

For the hero section, key details established included the font "Heading Now" (heavy/black weight), an asymmetric editorial grid where large text fragments and image placeholders alternate as equal-weight elements, five image placeholders of specified shapes and sizes on a white background, and an intentional off-balance layout. The person clarified that image curation was irrelevant — only placeholder shapes and sizes mattered.

For the work categories section, the defining characteristic was a zigzag layout — items intentionally staggered left and right in an off-balance diagonal rhythm rather than aligned to a grid. This section included four category items (Technology, Fashion, Hair, Beauty) with image placeholders, small scattered star decorative elements in a specific blue (#3846C4), and the bracketed heading "[my work]" in Heading Now font. Claude generated detailed AI prompts for Emergent for both sections, incorporating the zigzag and asymmetric layout logic as the core structural concept. The person's working preference was precise and correction-oriented, clarifying misunderstandings directly and efficiently.

## 🧑 Adriana · 2026-04-12 04:58
how would you describe the juxtaposition of these images and the text? to give instructions to Ai to create a template

## 🤖 Claude · 2026-04-12 04:59
Here's a breakdown you can use as an AI prompt or brief:

**Layout logic:** The page uses an asymmetric grid where oversized, bold text fragments ("Hi, I'm Adri" / "& this is my" / "my portfolio.") are treated as visual objects — not headlines over images, but elements with the same visual weight as the photos. Text and image alternate across the grid without hierarchy: neither dominates.

**Image curation logic:** The photos are personal and unpolished — a childhood portrait, a messy paint-covered floor, sardines in a tin, a garden through a trellis structure, a hair-drawing illustration on pink. They share no consistent style, color palette, or subject. The juxtaposition is intentional: the variety signals "this person has range / texture / a life." Nothing is art-directed or brand-clean.

**The central tension:** The text is massive, confident, and sans-serif (feels institutional, bold, declarative). The images are intimate, raw, and eclectic. That contrast IS the concept: the bravado of the statement is undercut by the humanness of the objects shown. It says "portfolio" but feels like a person.

Here's prompt language you can give to an AI layout tool:

> "Create a portfolio landing page using an editorial grid where bold, large-scale text fragments and unedited personal photos alternate as equal-weight elements. The text is broken across 3 lines that read as a sentence when scanned top to bottom: 'Hi, I'm [Name] / & this is my / my portfolio.' Each line appears in a different grid zone, separated by images. Photos should feel uncurated and personal — different sizes, no unified palette, no professional staging. The visual logic is: personal intimacy held inside a confident structural grid. Use a white background. Typography is black, heavy, large — minimum 60px. Images sit without captions, borders, or drop shadows."

Want me to build this as an actual interactive HTML template where you can swap in your own photos?

## 🧑 Adriana · 2026-04-12 05:01
the image curation doesnt matter instead just needs to add image place holder to replace them but specify also the shapes, the font is heading now. the whole portfolio landing is made i just need to adjust this section

## 🤖 Claude · 2026-04-12 05:01
Got it. So this is just the **hero/intro section** of an existing portfolio, and you need a reusable layout spec with placeholders. Let me nail down a couple things first:

## 🧑 Adriana · 2026-04-12 05:01
[User dismissed — do not proceed, wait for next instruction]

## 🤖 Claude · 2026-04-12 05:01
Got it, waiting on you!

## 🧑 Adriana · 2026-04-12 05:02
headings now is the name of the font for that section

## 🤖 Claude · 2026-04-12 05:02
Oh perfect, so the font is literally called **"Heading Now"** — noted.

What do you need as output for this section?
- AI prompt to recreate it
- HTML/CSS code snippet to drop in
- Written spec / art direction doc

## 🧑 Adriana · 2026-04-12 05:02
* AI prompt to recreate it
*

## 🤖 Claude · 2026-04-12 05:02
Got it. One last thing before I write it:

## 🧑 Adriana · 2026-04-12 05:05
P: Which AI tool are you prompting?
R: emergent

## 🤖 Claude · 2026-04-12 05:05
Here's your prompt for Emergent:

---

**Section: Hero / Intro — Portfolio Landing Page**

Create a single section of a portfolio website with the following layout and specs. This is not a full page — only the intro/hero section.

**Typography**
Font: Heading Now. Weight: heavy/black. Size: very large (min 64px, ideally 80–100px). Color: #000000. The text is broken into 3 fragments that read as one sentence across the section:
- Fragment 1: "Hi, I'm [Name]"
- Fragment 2: "& this is my"
- Fragment 3: "my portfolio."

Each fragment sits in a different zone of the grid — they do not stack vertically as a single block. They are separated spatially by image placeholders.

**Grid logic**
Use an asymmetric 3-column grid. Text fragments and image placeholders alternate as equal-weight elements — neither dominates. The layout reads diagonally, not linearly. White background (#FFFFFF). No borders, no shadows, no decorative elements.

**Image placeholders**
5 placeholders total. Shapes and sizes as follows:
- Placeholder 1: landscape rectangle, large (approx 2:3 ratio, ~380x280px)
- Placeholder 2: landscape rectangle, slightly smaller (approx 3:2 ratio, ~220x160px)
- Placeholder 3: wide landscape rectangle, dominant (approx 16:9 ratio, ~380x220px)
- Placeholder 4: portrait square, small (approx 1:1, ~160x160px)
- Placeholder 5: square, medium (approx 1:1, ~240x240px)

Fill each placeholder with a flat neutral color (#E0E0E0 or similar). No icons, no "image" label inside them.

**Spacing**
Generous. Let the white space breathe. Do not center-align everything — the layout should feel editorial and off-balance intentionally.

**Do not add:** navigation, buttons, footer, captions, hover effects, or any decorative elements. Just the section.

---

Paste that in and adjust the name placeholder before generating. Want me to tweak anything before you run it?

## 🧑 Adriana · 2026-04-12 05:12
how would you describe the juxtaposition of these images and the text? they are not perfectly aligned, they are intentionally in like a "zigzag" like form to give instructions to Ai to create a template

## 🤖 Claude · 2026-04-12 05:13
Here's your prompt for this section:

---

**Section: Work Categories — Portfolio Landing Page**

Create a single section of a portfolio website. Not a full page — only this section.

**Heading**
Font: Heading Now. Weight: black/heavy. Size: ~80–90px. Color: #000000. Text: "[my work]" — include the brackets as part of the text, they are not decorative, they are typographic. Centered at the top of the section.

**Layout logic**
4 category items arranged in a loose zigzag — not a grid, not centered, not evenly spaced. Items drift left and right alternately as they go down, creating an intentional off-balance diagonal rhythm. Think of it as two columns that don't align: items stagger between left-center and right-center positions, with vertical gaps between them. Nothing snaps to a grid.

**Each category item**
One product image (PNG with transparent background, no frame, no card, no shadow) above a short label in plain text below it. Image sits floating on the white background. Label is small, ~16–18px, black, same font family or clean sans-serif, left-aligned under the image.

**Category items (4 total):**
- Technology — image placeholder, approx 160x130px
- Fashion — image placeholder, approx 160x110px
- Hair — image placeholder, approx 130x110px
- Beauty — image placeholder, approx 130x140px

Use flat #E0E0E0 rectangles as placeholders. No borders or labels inside the placeholder.

**Decorative elements**
Scatter 8–10 small solid 5-pointed stars in #3846C4 (dark blue) randomly around the section — different sizes between 16px and 28px. They sit behind the content, distributed across all corners and edges of the section, not clustered. No animation.

**Background:** #FFFFFF. No cards, no borders, no shadows, no hover effects.

---

Want me to adjust anything?
