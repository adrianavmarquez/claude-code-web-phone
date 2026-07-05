---
title: "AI video generation explained visually"
source: claude.ai-chat
created: "2026-07-03 02:47"
summary: "**Conversation Overview**  The person asked Claude to create a narrated, animated pop-science explainer video about how AI video generation works, using the Higgsfield MCP integration. Claude followed a structured multi-step pipeline: first loading workflow instructions for the video-explainer format, then surfacing available visual style presets for the person to choose from. The person selected the 'Fluffy Toy' preset style (preset ID: 1fde6c92-721b-4824-b490-4ea75ad0665f). Claude then established two working defaults—English narration and no burned-in subtitles—while noting subtitles could be enabled if desired, and proceeded to collect the remaining required parameters (video duration, host type, and orientation) via an interactive input widget before beginning production.  **Tool Knowledge**  The Higgsfield explainer video pipeline follows a strict sequential structure: `get_workflow_instructions` for the video-explainer workflow must be called first to understand the pipeline, followed by `get_youtube_explainer_presets` to display the style gallery before any user selections are made. The style preset ID must be captured exactly as provided by the gallery (e.g., `1fde6c92-721b-4824-b490-4ea75ad0665f`) for use in downstream generation calls. Duration is calculated in whole minutes mapped to 10-second scene blocks (1 min = 6 scenes, 2 min = 12 scenes, 3 min = 18 scenes), and scene count directly drives credit cost. The `ask_user_input_v0` tool accepts a maximum of 3 questions per call, so remaining parameters beyond the initial three (duration, character type, orientation) should be batched in a follow-up call or handled via stated defaults to avoid exceeding the limit."
messages: 4
claude_uuid: "0fb207d3-0a06-46b4-b65b-3ebf42df7ce6"
tags: [claude, chat, archive]
---
# AI video generation explained visually

> **Conversation Overview**

The person asked Claude to create a narrated, animated pop-science explainer video about how AI video generation works, using the Higgsfield MCP integration. Claude followed a structured multi-step pipeline: first loading workflow instructions for the video-explainer format, then surfacing available visual style presets for the person to choose from. The person selected the "Fluffy Toy" preset style (preset ID: 1fde6c92-721b-4824-b490-4ea75ad0665f). Claude then established two working defaults—English narration and no burned-in subtitles—while noting subtitles could be enabled if desired, and proceeded to collect the remaining required parameters (video duration, host type, and orientation) via an interactive input widget before beginning production.

**Tool Knowledge**

The Higgsfield explainer video pipeline follows a strict sequential structure: `get_workflow_instructions` for the video-explainer workflow must be called first to understand the pipeline, followed by `get_youtube_explainer_presets` to display the style gallery before any user selections are made. The style preset ID must be captured exactly as provided by the gallery (e.g., `1fde6c92-721b-4824-b490-4ea75ad0665f`) for use in downstream generation calls. Duration is calculated in whole minutes mapped to 10-second scene blocks (1 min = 6 scenes, 2 min = 12 scenes, 3 min = 18 scenes), and scene count directly drives credit cost. The `ask_user_input_v0` tool accepts a maximum of 3 questions per call, so remaining parameters beyond the initial three (duration, character type, orientation) should be batched in a follow-up call or handled via stated defaults to avoid exceeding the limit.

## 🧑 Adriana · 2026-07-03 02:47
Turn how AI video generation works into a narrated, animated pop-science explainer video using Higgsfield MCP.

## 🤖 Claude · 2026-07-03 02:53
I'll build this properly using Higgsfield's explainer pipeline: one narrator over stylized 10-second animated blocks, a single style key locking the look, assembled into one MP4. First step is locking the visual style.

Pick a visual style from the gallery above, whatever look you want for "how AI video generation works": Isometric Flat Vector and 2D Illustrator read very pop-science, Whiteboard Doodle leans explainer-classic, Low Poly / 3D Mix feel more techy. Or describe your own, or drop reference photos.

Once you pick the style, I'll grab a couple quick calls (length, narration language, mascot or faceless, orientation, subtitles) and then build the whole thing.

## 🧑 Adriana · 2026-07-03 02:53
Create an explainer video in the "Fluffy Toy" preset style (explainer preset id: 1fde6c92-721b-4824-b490-4ea75ad0665f).

## 🤖 Claude · 2026-07-03 02:54
Locked: **Fluffy Toy** style. Two defaults I'll run with unless you say otherwise, **English narration** and **no burned-in subtitles** (captions add a small cost per scene, and turn on nicely if you want reach on silent autoplay). Tell me in your reply if you want Spanish narration or subtitles on.

A few quick calls and I'll build the whole thing:
