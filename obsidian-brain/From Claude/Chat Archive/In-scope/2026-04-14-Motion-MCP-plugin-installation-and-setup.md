---
title: "Motion MCP plugin installation and setup"
source: claude.ai-chat
created: "2026-04-14 18:21"
summary: "**Conversation Overview**  The person asked Claude to install the Motion Creative plugin from the marketplace and the motion-mcp plugin, sharing documentation describing the Motion MCP server's capabilities. The Motion MCP is a read-only MCP server exposing Motion Creative Analytics data through 13 tools across five categories: creative performance analysis, competitor and brand research, saved reports and taxonomy access, and AI-assisted brief and concept generation. Authentication is handled via OAuth 2.0, and the server is accessible from any MCP-compatible client.  Claude attempted to locate and read plugin files from an uploaded zip archive (`motion-creative-plugin-main.zip`), exploring configuration files including `.mcp.json`, `marketplace.json`, and `plugin.json`, as well as the README. Claude then clarified a key distinction: the `motion-creative-plugin` is designed for **Claude Code** (the terminal-based environment), not Claude.ai chat, and therefore cannot be installed in the same way in this context. Claude outlined two paths forward: installing via Claude Code using `/plugin marketplace add Motion-Creative/motion-creative-plugin` and `/plugin install motion-creative@motion-mcp`, or connecting the MCP server directly to Claude.ai via Settings → Integrations using the server URL `https://projects.motionapp.com/mcp`. Claude also noted that 15 skill files from the plugin (covering tasks like ad analysis, hook writing, brief building, and competitor watching) could be loaded into the session as context in the interim, and recommended Claude Code as the appropriate tool for this workflow."
messages: 2
claude_uuid: "da720fed-96b3-45ea-bfab-7046ae28953e"
tags: [claude, chat, archive]
---
# Motion MCP plugin installation and setup

> **Conversation Overview**

The person asked Claude to install the Motion Creative plugin from the marketplace and the motion-mcp plugin, sharing documentation describing the Motion MCP server's capabilities. The Motion MCP is a read-only MCP server exposing Motion Creative Analytics data through 13 tools across five categories: creative performance analysis, competitor and brand research, saved reports and taxonomy access, and AI-assisted brief and concept generation. Authentication is handled via OAuth 2.0, and the server is accessible from any MCP-compatible client.

Claude attempted to locate and read plugin files from an uploaded zip archive (`motion-creative-plugin-main.zip`), exploring configuration files including `.mcp.json`, `marketplace.json`, and `plugin.json`, as well as the README. Claude then clarified a key distinction: the `motion-creative-plugin` is designed for **Claude Code** (the terminal-based environment), not Claude.ai chat, and therefore cannot be installed in the same way in this context. Claude outlined two paths forward: installing via Claude Code using `/plugin marketplace add Motion-Creative/motion-creative-plugin` and `/plugin install motion-creative@motion-mcp`, or connecting the MCP server directly to Claude.ai via Settings → Integrations using the server URL `https://projects.motionapp.com/mcp`. Claude also noted that 15 skill files from the plugin (covering tasks like ad analysis, hook writing, brief building, and competitor watching) could be loaded into the session as context in the interim, and recommended Claude Code as the appropriate tool for this workflow.

## 🧑 Adriana · 2026-04-14 18:21
Install the Motion Creative plugin add the marketplace and install the motion-mcp plugin.
❤️ The Motion MCP exposes Motion Creative Analytics data through a read-only MCP server with 13 tools across five categories, accessible from any MCP-compatible client. Once authenticated via OAuth 2.0, your AI tool can query creative performance, competitor analysis, saved reports, brand context, and workspace taxonomy directly. 
Think of it as a bridge between Motion and the AI tools you already use. Ask a question, get an answer powered by your actual account data. No copy-pasting, no context switching.

MCP (Model Context Protocol) is an open standard that works across AI platforms. Connect once and you're good to go. What you can do with the Motion MCP

The MCP connects your AI tool to 13 specialized tools across five categories. Here's what that unlocks:

Analyze your creative performance

Ask about your top ads, sort by any metric (ROAS, spend, CPA, CTR, and more), filter by date range, and get AI-generated summaries of what's working. Drill into individual creatives for detailed breakdowns, pull video transcripts to analyze hooks, and see demographic performance splits by age and gender.

Research competitors and brands

Browse any competitor's ad library, understand their creative strategy, messaging angles, and brand positioning. Search for any brand by name or domain. You're not limited to brands you already track in Motion.

Work with your saved reports and taxonomy

Access your saved Motion reports and your full glossary of creative tags. This lets the AI understand your team's taxonomy so it can filter and analyze creatives using the categories and labels you've already set up.

Generate briefs and concepts grounded in real data

Because the AI has access to both your performance data and competitor analysis, it can help you write creative briefs, suggest new concepts, or identify trends, all informed by what's actually working in market.

## 🤖 Claude · 2026-04-14 18:21
I need to clarify something important here. This plugin is designed for **Claude Code** (the terminal-based coding tool), not for Claude.ai chat. Let me explain what's going on and what you actually need to do.

---

**What this plugin is:**

The `motion-creative-plugin` is a Claude Code plugin. It adds slash commands like `/morning-briefing`, `/write-hooks`, `/build-brief` etc. directly into the Claude Code terminal environment, powered by the Motion MCP server at `https://projects.motionapp.com/mcp`.

**It cannot be installed here** in Claude.ai chat the same way. Claude.ai and Claude Code are separate environments.

---

**What you actually need to do:**

There are two paths depending on what you want:

**Path 1: Use it in Claude Code (what the plugin is built for)**

If you have Claude Code installed, run these two commands in your terminal:

```
/plugin marketplace add Motion-Creative/motion-creative-plugin
```
```
/plugin install motion-creative@motion-mcp
```

Then run `/customize` to configure your brand, KPIs, and competitors.

**Path 2: Connect Motion MCP to Claude.ai chat (this session)**

The MCP server URL is `https://projects.motionapp.com/mcp`. To use it here in Claude.ai, you'd go to **Settings → Integrations** (or the connector marketplace) and add that MCP server URL. Once authenticated via OAuth, Motion's 13 tools would be available in this chat.

---

**What I can do right now:**

The plugin also comes with 15 skill files (analyze-ad, write-hooks, build-brief, competitor-watch, etc.) that I can read and use as context. If you want, I can load those skills into our session so you can work with Motion strategy even before the MCP is connected. Just say the word.

Do you have Claude Code installed, or are you looking to connect Motion directly here in Claude.ai?
