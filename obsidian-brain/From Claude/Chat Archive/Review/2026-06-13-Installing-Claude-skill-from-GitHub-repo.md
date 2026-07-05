---
title: "Installing Claude skill from GitHub repo"
source: claude.ai-chat
created: "2026-06-13 18:28"
summary: "**Conversation Overview**  The person asked Claude to install a custom Claude skill from a specific GitHub repository (github.com/aiwithremy/claude-skills-llm-council). The goal was to get the LLM Council skill — a reasoning methodology based on Karpathy's LLM Council concept — installed into their Claude account.  Claude cloned the repository, inspected the two files present (SKILL.md and README.md), and identified a blocking issue: claude.ai enforces a 200-character limit on a skill's `description` field, and the original description was 908 characters. Claude also identified an internal contradiction in the original file where step 5 specified in-chat output only, but a later note referenced generating an HTML report. Claude rebuilt the SKILL.md to fix both issues — trimming the description to fit within the 200-character limit while relocating the full trigger routing logic (mandatory triggers, strong triggers, and exclusion conditions) into the skill body so no nuance was lost, and aligning the HTML contradiction to in-chat markdown output. The person then asked Claude to use the full 200-character budget, prompting Claude to run a combinatorial search across phrasings and trigger orderings to maximize the character count, landing at 199/200 with four trigger phrases included ('council this', 'run the council', 'pressure-test this', 'debate this'), with all six canonical triggers preserved in the skill body.  Claude packaged the final SKILL.md into a ZIP archive with the correct folder structure (llm-council/SKILL.md) and delivered it as a downloadable file, along with installation instructions: enable code execution in Settings > Capabilities, then upload the ZIP under Settings > Capabilities > Skills. Claude also clarified that direct installation from chat is not possible in the claude.ai web interface — that capability exists only in Claude Code and Cowork — so the final upload step requires the person to act through their settings UI."
messages: 4
claude_uuid: "980fa0d6-2118-43e3-8b17-a0be51226ba8"
tags: [claude, chat, archive]
---
# Installing Claude skill from GitHub repo

> **Conversation Overview**

The person asked Claude to install a custom Claude skill from a specific GitHub repository (github.com/aiwithremy/claude-skills-llm-council). The goal was to get the LLM Council skill — a reasoning methodology based on Karpathy's LLM Council concept — installed into their Claude account.

Claude cloned the repository, inspected the two files present (SKILL.md and README.md), and identified a blocking issue: claude.ai enforces a 200-character limit on a skill's `description` field, and the original description was 908 characters. Claude also identified an internal contradiction in the original file where step 5 specified in-chat output only, but a later note referenced generating an HTML report. Claude rebuilt the SKILL.md to fix both issues — trimming the description to fit within the 200-character limit while relocating the full trigger routing logic (mandatory triggers, strong triggers, and exclusion conditions) into the skill body so no nuance was lost, and aligning the HTML contradiction to in-chat markdown output. The person then asked Claude to use the full 200-character budget, prompting Claude to run a combinatorial search across phrasings and trigger orderings to maximize the character count, landing at 199/200 with four trigger phrases included ("council this", "run the council", "pressure-test this", "debate this"), with all six canonical triggers preserved in the skill body.

Claude packaged the final SKILL.md into a ZIP archive with the correct folder structure (llm-council/SKILL.md) and delivered it as a downloadable file, along with installation instructions: enable code execution in Settings > Capabilities, then upload the ZIP under Settings > Capabilities > Skills. Claude also clarified that direct installation from chat is not possible in the claude.ai web interface — that capability exists only in Claude Code and Cowork — so the final upload step requires the person to act through their settings UI.

## 🧑 Adriana · 2026-06-13 18:28
Please install this Claude skill for me. The SKILL.md file lives in this GitHub repo: https://github.com/aiwithremy/claude-skills-llm-council

## 🤖 Claude · 2026-06-13 18:31
I'll grab the repo, look at what's actually in it, and then get it into a form you can install. Let me start by cloning it and inspecting the contents.

Just two files. Let me read both so I understand what the skill does and can check it's safe before installing.

This is a clean, safe skill: it's pure instructions (a "council of 5 advisors" reasoning method based on Karpathy's LLM Council), with no code, shell commands, or network calls. Nothing to worry about installing.

Now I need to get the install path right for your setup. Let me check the current process.

The skill is safe and I've confirmed the install path. One thing to check before I package it: claude.ai enforces a 200-character limit on the skill `description`, and this one's description looks long. Let me verify so the upload doesn't get rejected.

Confirmed the issue: the skill's description is 908 characters, but claude.ai caps it at 200. Uploaded as-is, it would get rejected. So I'll package a version with a tight 200-char description, and move the full trigger logic (mandatory vs. strong triggers, what *not* to trigger on) into the body of the skill so none of that nuance is lost. I'll also fix one internal contradiction in the original (step 5 says "present in chat, no files," but a later note says "make the HTML report clean," I'm aligning it to in-chat output).

Description came out to 233 characters. Trimming further.

Now I'll package it into the ZIP format claude.ai expects (a folder containing the SKILL.md), and put it where you can grab it.

Done. The skill is packaged and ready to install. Here's where things landed.

**What it is:** LLM Council, a reasoning skill based on Karpathy's method. When you trigger it, Claude runs your question past five advisors with opposing thinking styles (Contrarian, First Principles, Expansionist, Outsider, Executor), has them anonymously peer-review each other, and a "chairman" synthesizes a final verdict. It's pure instructions, no code, no shell commands, no network calls, so nothing risky in it.

**Two things I fixed so it would actually install:**
- claude.ai caps a skill's `description` at 200 characters, and the original was 908. It would have been rejected on upload. I trimmed the description to 190 characters and moved the full trigger logic (mandatory vs. strong triggers, plus what *not* to trigger on) into the body of the skill, so none of that nuance is lost.
- The original contradicted itself: step 5 says "present in chat, no files," but a later note says "make the HTML report clean." I aligned it to in-chat markdown output.

**The honest part about "install it for me":** in this claude.ai chat I can prepare the file, but I can't push it into your account's skill registry. That registry is only reachable through your settings. (The repo's promise that "Claude will put it in the right place" is true in Claude Code and Cowork, which are filesystem-based, not in a regular chat.) So the last step is yours, and it's quick:

1. Make sure code execution is on: Settings > Capabilities, enable code execution (custom skills require it).
2. Go to Settings > Capabilities > Skills (your build may label it Customize > Skills or Settings > Features > Skills).
3. Click Upload skill / Add skill and select the `llm-council.zip` above.
4. Toggle it on once it appears.

**Using it:** in any chat, say "council this" or "pressure-test this" followed by a real decision, and it runs. One caveat for regular chat: the skill is written to spawn five advisors "in parallel" as sub-agents, which is a Claude Code / Cowork capability. In a normal claude.ai chat there are no true parallel sub-agents, so Claude will work through the five perspectives within one response instead. The output is the same; it just isn't literally parallel.

If you're actually in Claude Code or Cowork rather than the web chat, tell me and I'll give you the filesystem path version instead, which I can drop in directly.

## 🧑 Adriana · 2026-06-13 18:32
add what is missing use the full characters

## 🤖 Claude · 2026-06-13 18:33
You're right, no reason to leave characters on the table. Let me max out the 200-char budget and pack in more of the trigger phrases.

199 of 200, with four triggers now. Let me see if a slightly tighter phrasing fits a fifth.

The optimizer maxes at 4 triggers regardless of phrasing. Since all six triggers live in full in the body anyway, the description's only job is discovery breadth, so I'll pin the two canonical invocations ("council this", "run the council") and fill the rest to hit exactly 200.

199/200 with both canonical invocations plus two alternates. Repackaging the zip.

Updated. The description now uses 199 of the 200 characters and carries four triggers instead of three:

> Run a decision past a council of 5 AI advisors who analyze independently, peer-review anonymously, then synthesize a verdict. Triggers: council this, run the council, pressure-test this, debate this.

I pinned the two canonical invocations ("council this" and "run the council") and added "pressure-test this" and "debate this." The remaining two ("stress-test this," "war room this") didn't fit the 200-char limit, but all six still live verbatim in the body's triggers section, so discovery and routing lose nothing.

The zip above is the updated version. Same install path as before: enable code execution, then Settings > Capabilities > Skills, upload the zip, toggle it on.
