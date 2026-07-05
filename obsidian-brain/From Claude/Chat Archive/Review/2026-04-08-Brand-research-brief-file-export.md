---
title: "Brand research brief file export"
source: claude.ai-chat
created: "2026-04-08 17:12"
summary: "**Conversation Overview**  The conversation began with an incomplete task from a prior session where Claude had been asked to output a brand research brief as a JSON file. The person dismissed that thread and redirected the conversation entirely toward building a new reusable skill. The person, who works in AI-assisted creative and design work, wanted to create a skill that functions as a structured prompt builder for any AI collaborative design task, not limited to a specific ad format or use case.  The person clarified their vision across several exchanges: the skill should present a structured intake form with numbered questions all at once (rather than one at a time), covering elements like headline, subhead, body copy, CTA, visual elements, composition, graphic design style, sentiment, variation vectors, goal, and target audience. The skill should automatically pull brand context (colors, fonts, tone, imagery style, persona) from files already uploaded to each project, so brand information never needs to be re-entered manually. Each project would have its own brand files serving as the context layer.  Claude built and packaged the skill as a `.skill` file, structured around three stages: silent brand context extraction from project files, an 18-question intake form across five sections (The Piece, The Message, The Visual, Style and Energy, Technical), and a full JSON output including a `full_image_generation_prompt` field containing a richly formatted, ready-to-paste paragraph for any AI image generation tool such as Midjourney, Firefly, or Ideogram. Claude offered to run a live test of the intake form to demonstrate the output format."
messages: 8
claude_uuid: "c101842c-64e3-4437-ba21-f843b4bf0b49"
tags: [claude, chat, archive]
---
# Brand research brief file export

> **Conversation Overview**

The conversation began with an incomplete task from a prior session where Claude had been asked to output a brand research brief as a JSON file. The person dismissed that thread and redirected the conversation entirely toward building a new reusable skill. The person, who works in AI-assisted creative and design work, wanted to create a skill that functions as a structured prompt builder for any AI collaborative design task, not limited to a specific ad format or use case.

The person clarified their vision across several exchanges: the skill should present a structured intake form with numbered questions all at once (rather than one at a time), covering elements like headline, subhead, body copy, CTA, visual elements, composition, graphic design style, sentiment, variation vectors, goal, and target audience. The skill should automatically pull brand context (colors, fonts, tone, imagery style, persona) from files already uploaded to each project, so brand information never needs to be re-entered manually. Each project would have its own brand files serving as the context layer.

Claude built and packaged the skill as a `.skill` file, structured around three stages: silent brand context extraction from project files, an 18-question intake form across five sections (The Piece, The Message, The Visual, Style and Energy, Technical), and a full JSON output including a `full_image_generation_prompt` field containing a richly formatted, ready-to-paste paragraph for any AI image generation tool such as Midjourney, Firefly, or Ideogram. Claude offered to run a live test of the intake form to demonstrate the output format.

## 🧑 Adriana · 2026-04-08 17:12
Output this as a file called brand-research-brief.json
> 📎 

## 🤖 Claude · 2026-04-08 17:12
I see the template, but there's no brand filled in yet. Before I build the file, a couple quick things:

Let me know your answers and I'll get started on the full research brief right away.

## 🧑 Adriana · 2026-04-08 17:12
[User dismissed — do not proceed, wait for next instruction]

## 🤖 Claude · 2026-04-08 17:12
Got it, I'll wait! Just say the word whenever you're ready.

## 🧑 Adriana · 2026-04-08 17:19
dismiss that, i want to create a skill that helps me generate the best json style prompts. this is like the abc step by step that i need to fullfill in order to give you enoguh concept to ocme up with a great acctionable prompt, de construct this and lets start there:
> 📎 

## 🤖 Claude · 2026-04-08 17:19
Okay, I've got the full picture. Let me make sure I understand what you want to build before I write anything.

You shared the **Headline ad format doc** as the source material. The skill you want is something that takes a concept and helps you build a complete, structured JSON prompt for any of the static ad styles (A, B, or C in that format, and presumably the others you have too).

So the skill would essentially be an **interactive intake flow**: it asks you the right questions step by step (brand, product, style, persona, energy, etc.), then assembles a fully formed, ready-to-use image generation prompt in JSON.

A few things I want to nail down before drafting:

**1. Scope of the skill right now:** Is this just for the Headline format (Styles A/B/C), or do you want the skill to eventually cover all 15 formats from the brief (Before & After, Bullet Points, Carousel, etc.)? I want to know if I'm building a Headline-specific skill or a universal prompt builder that the Headline doc is just the first module of.

**2. What the JSON output actually looks like:** The doc has image generation prompts written in plain text with bracketed variables. Do you want the output to be a JSON object with fields like `headline`, `subhead`, `cta`, `image_prompt`, `variation_vectors` etc. all filled in? Or more like the raw prompt text ready to paste into Midjourney/Firefly?

**3. The intake flow:** Do you want the skill to ask you questions one at a time (conversational), or present a structured form all at once and let you fill in what you know?

**4. Brand context:** Should this skill pull from an existing brand brief/research doc (like the brand-research-brief.json you were going to build), or does it work standalone and ask for brand info fresh each time?

## 🧑 Adriana · 2026-04-08 17:26
1. not for static ad style, to do any Ai collaborative design related task. I want it to ask me the right questions in order to then spit out a perfectly made json prompt for ai design generation.
2. i want the skill to ask me question by question what it needs in order to give me a filled in json prompt. For example: what is the main heading? what us the subheacing? what is the body? does it have a CTA? what elements you want to incorporate? variation vectors? graphic design style? sentiment? goal of this design? who are we talking to? etc etc. And then with my answers ut gives me back a perfectly well done json prompt
3. present a structured form all at once, like question 1,2,3,4,5,6
4. I would ask these questions and run this prompts inside each project individually so it would use as context previously uploaded files to the project to extract the brand info context tone style aesthetics etc etc from

## 🤖 Claude · 2026-04-08 17:28
Perfect, I have everything I need. Let me build this.

The skill is a **structured intake form** that collects everything needed to generate a JSON prompt for any AI-assisted design task, pulling brand context from whatever files are in the project. Let me draft it now.

Here's what the skill does, broken down:

**On trigger:** The moment you say anything like "build me a prompt for..." or "I want to generate a [design thing]," it activates. It silently reads whatever brand files are already in your project, extracts all visual identity info, and pre-loads it as defaults so you never have to re-explain the brand.

**The intake form:** 18 questions across 5 sections, presented all at once. You answer what's relevant, skip the rest. The sections are: The Piece, The Message, The Visual, Style and Energy, and Technical.

**The output:** A fully filled JSON prompt with every field named and populated, plus one final `full_image_generation_prompt` field that writes everything into a single, rich, ready-to-paste paragraph formatted for any AI image tool (Midjourney, Firefly, Ideogram, etc.).

**To install it:** Go to your Claude settings, find Skills, and upload the `.skill` file. Once installed, it'll be available in any project you add it to. When you drop a brand brief or guidelines doc into a project, it'll use those as the brand context layer automatically.

Want me to do a test run right now, where I run the intake form as if you were a client and show you what the JSON output looks like?
