---
title: "Alternative AI tools for social media dashboard setup"
source: claude.ai-chat
created: "2026-05-19 12:51"
summary: "**Conversation Overview**  Adriana V. Marquez (@adrianavmarquez) is a bilingual (Spanish/English) content creator running the brand 'Motus,' creating content for Spanish-speaking women 25+ across USA, Mexico, Venezuela, Spain, and Colombia. Her brand has three content pillars: Content Creation & Creativity, Tech & Gear, and Lifestyle (beauty, fashion, wellness). She is active on Instagram, TikTok, YouTube, Pinterest, and X. Adriana has a sophisticated existing tech stack including n8n cloud, Notion, Airtable, Motion MCP, and Manus AI, and communicates naturally in Spanglish throughout the conversation.  The conversation centered on building an organic content intelligence dashboard, starting from a Perplexity Computer guide Adriana had found. Claude walked her through comparing Perplexity Computer, Claude Code with Playwright, Claude in Chrome (discarded due to lag and beta instability), Codex, and Manus AI as build options. Adriana ultimately decided to test Perplexity Computer against Manus AI head-to-head, with Manus's key weaknesses identified as high credit consumption, text-report-only output, and no live-reloading visual interface. Claude clarified that Perplexity Computer produces scheduled snapshot redeploys rather than truly live data, and recommended Claude Code plus n8n as the only architecture that delivers genuinely live-reloading data without per-run credit costs, though Adriana chose to proceed with Perplexity Computer for now given she can schedule redeploys.  Claude pulled Adriana's real creator database from her Notion page (ID: 3269c084f04180c7af1ecdbc26910367), which contains 37-40 tracked creators across eight categories: Filmmakers, Content/Editing Coaches, Fashion & Lifestyle, Vlogs, Tech & AI, Social Media & Marketing, Creative Storytellers, and Business Owners, with handles across YouTube, Instagram, TikTok, and other platforms. This real creator list and Motus brand context (hex colors: #D72323, #3846C4, #FFBA35, #000000, #FFFFFF, #F2E9FF, #2EA4FB; typography: Poppins throughout; em-dashes banned across all outputs) were baked into the Perplexity Computer build prompt. A key correction mid-conversation: 'Im motus' clarified that Motus is not a typo but the actual brand name, eliminating a dual-brand framing Claude had constructed. The conversation also covered API connections for the 'My Performance' dashboard section, with Claude guiding Adriana through Meta's developer portal (selecting 'Manage messaging & content on Instagram' use case, noting the Instagram Basic Display API was deprecated December 2024), Pinterest token setup (selecting Producción limitada over Sandbox), and explaining TikTok API limitations. Claude consistently recommended n8n as the right place to store and auto-refresh OAuth tokens (which expire every 60 days for Instagram) rather than Perplexity, and suggested YouTube Data API v3 as the easiest starting point and TikTok API as lowest priority due to approval complexity and analytics access limitations.  **Tool Knowledge**  Claude used the Notion MCP tool to fetch Adriana's creator database using the page ID `3269c084f04180c7af1ecdbc26910367` directly, which successfully returned the full creator list with cross-platform handles organized by category. This page also serves as the parent page where Manus writes her weekly digest newsletter as child pages. The creator data is also stored as a JSON file at `/home/ubuntu/creator_platform_research.json` on the Manus environment, which Manus loads directly for its newsletter generation tasks. For future Notion fetches related to Adriana's creator intelligence work, fetching by this specific page ID is the reliable path to her tracked creator database."
messages: 28
claude_uuid: "30a2b248-5fbf-4a09-9563-c295f991aae6"
tags: [claude, chat, archive]
---
# Alternative AI tools for social media dashboard setup

> **Conversation Overview**

Adriana V. Marquez (@adrianavmarquez) is a bilingual (Spanish/English) content creator running the brand "Motus," creating content for Spanish-speaking women 25+ across USA, Mexico, Venezuela, Spain, and Colombia. Her brand has three content pillars: Content Creation & Creativity, Tech & Gear, and Lifestyle (beauty, fashion, wellness). She is active on Instagram, TikTok, YouTube, Pinterest, and X. Adriana has a sophisticated existing tech stack including n8n cloud, Notion, Airtable, Motion MCP, and Manus AI, and communicates naturally in Spanglish throughout the conversation.

The conversation centered on building an organic content intelligence dashboard, starting from a Perplexity Computer guide Adriana had found. Claude walked her through comparing Perplexity Computer, Claude Code with Playwright, Claude in Chrome (discarded due to lag and beta instability), Codex, and Manus AI as build options. Adriana ultimately decided to test Perplexity Computer against Manus AI head-to-head, with Manus's key weaknesses identified as high credit consumption, text-report-only output, and no live-reloading visual interface. Claude clarified that Perplexity Computer produces scheduled snapshot redeploys rather than truly live data, and recommended Claude Code plus n8n as the only architecture that delivers genuinely live-reloading data without per-run credit costs, though Adriana chose to proceed with Perplexity Computer for now given she can schedule redeploys.

Claude pulled Adriana's real creator database from her Notion page (ID: 3269c084f04180c7af1ecdbc26910367), which contains 37-40 tracked creators across eight categories: Filmmakers, Content/Editing Coaches, Fashion & Lifestyle, Vlogs, Tech & AI, Social Media & Marketing, Creative Storytellers, and Business Owners, with handles across YouTube, Instagram, TikTok, and other platforms. This real creator list and Motus brand context (hex colors: #D72323, #3846C4, #FFBA35, #000000, #FFFFFF, #F2E9FF, #2EA4FB; typography: Poppins throughout; em-dashes banned across all outputs) were baked into the Perplexity Computer build prompt. A key correction mid-conversation: "Im motus" clarified that Motus is not a typo but the actual brand name, eliminating a dual-brand framing Claude had constructed. The conversation also covered API connections for the "My Performance" dashboard section, with Claude guiding Adriana through Meta's developer portal (selecting "Manage messaging & content on Instagram" use case, noting the Instagram Basic Display API was deprecated December 2024), Pinterest token setup (selecting Producción limitada over Sandbox), and explaining TikTok API limitations. Claude consistently recommended n8n as the right place to store and auto-refresh OAuth tokens (which expire every 60 days for Instagram) rather than Perplexity, and suggested YouTube Data API v3 as the easiest starting point and TikTok API as lowest priority due to approval complexity and analytics access limitations.

**Tool Knowledge**

Claude used the Notion MCP tool to fetch Adriana's creator database using the page ID `3269c084f04180c7af1ecdbc26910367` directly, which successfully returned the full creator list with cross-platform handles organized by category. This page also serves as the parent page where Manus writes her weekly digest newsletter as child pages. The creator data is also stored as a JSON file at `/home/ubuntu/creator_platform_research.json` on the Manus environment, which Manus loads directly for its newsletter generation tasks. For future Notion fetches related to Adriana's creator intelligence work, fetching by this specific page ID is the reliable path to her tracked creator database.

## 🧑 Adriana · 2026-05-19 12:51
i got this free guide to setup my own social media dahsboard, this uses perpelexity computer, do i have any other slternstives to building this either with codex, claude code or manus ai?
> 📎 

## 🤖 Claude · 2026-05-19 12:51
Looking at this guide, you've got solid alternatives. Let me break down how each compares for what you're actually trying to build:

**Claude Code** *(your strongest option given your setup)*

You already have the ecosystem dialed in: SKILL.md files, brand system locked, n8n connected, Notion, Airtable, Motion MCP, the works. Claude Code runs in your terminal and can build the full dashboard, deploy it, *and* tie it into your existing n8n flows for the weekly refresh. The Perplexity guide's "schedule a weekly run" step becomes a real n8n workflow that pings APIs and updates a Notion DB or Airtable, which then feeds the dashboard. That's a more durable system than Perplexity's scheduled agent because you own the pipes.

What you'd build differently: skip the demo-data-with-banner pattern. Go straight to API-connected since you already have Motion MCP for ad performance and could wire Instagram Graph / TikTok / YouTube APIs through n8n.

**Codex** *(GPT-5 / OpenAI's coding agent)*

Solid for the build itself. Will produce clean code, deploy to Vercel or similar. Where it falls short for you: no native connection to your existing stack. You'd be rebuilding the wiring (Notion, Airtable, Motion) from scratch instead of leveraging what's already running. Also no equivalent to your SKILL.md library, your brand system would need to live in the prompt every time.

**Manus AI**

Closer to Perplexity Computer in spirit, an autonomous agent that builds and deploys. Good for a one-shot polished prototype. Weaker for ongoing maintenance and integration with your specific stack. If you want "build it once, share the link, done," Manus is fine. If you want it to live and breathe with your business, it's not the move.

**My honest take for you specifically**

Claude Code is the right answer because:

1. You already have the Motion MCP plugin pulling ad performance data, that's literally one of the four dashboard sections done.
2. Your n8n cloud instance can handle the weekly refresh cron without paying for Perplexity scheduled tasks.
3. Your brand system (D72323, 3846C4, FFBA35, Poppins) is already documented in your skills, Claude Code can read it directly.
4. You can iterate in Spanglish, in your voice, with full context of your creator business.

The Perplexity guide is designed for someone starting from zero. You're not starting from zero.

Want me to draft the actual Claude Code prompt adapted to your stack? I'd structure it around: pulling competitor data via Motion, pulling your IG/TikTok metrics via n8n webhooks into Airtable, and rendering it all in a dashboard with your brand system baked in from the start.

## 🧑 Adriana · 2026-05-19 13:44
The idea is no tot be connected to my sdvertising aspects but for organic content creation instead and it woudl need to deploy browser scrapping and all on its own. How does the attached reference for perpelxity goes abou tthis?

## 🤖 Claude · 2026-05-19 13:45
Good catch, that changes the picture. Let me re-read what Perplexity is actually doing in the guide and then compare honestly.

**What Perplexity Computer is doing under the hood**

The guide is a little vague on this, but here's what's happening:

For the three sections that "work without setup" (trending topics, competitor signals, industry news), Perplexity Computer is doing autonomous web research. It's a browser agent. It can navigate sites, read content, summarize what it finds, and render the result into your dashboard. The weekly cron job ("every Monday 9am, refresh trending topics and competitor hooks") works because Computer can re-run that browsing task on a schedule without you supervising it.

That's the killer feature for organic content tracking: it's not scraping APIs, it's *browsing the live web* the way you would, looking at competitor profiles, reading industry newsletters, checking what's trending, then writing it up. No API tokens needed for those three sections because there's nothing to authenticate, it's just reading public content.

The fourth section (your own metrics) is the only piece that needs API tokens, because your private analytics aren't on the public web.

**So the real question: which tools can do autonomous browser-based research on a schedule?**

Let me compare honestly for your actual use case:

**Perplexity Computer** *(what the guide uses)*

Built for exactly this. Browser agent + scheduled runs + deploys to a URL. The weak spot: TikTok and Instagram aggressively block automated browsing. Computer will get further than most because it's a real headless browser with login support, but expect inconsistency on those two platforms specifically. YouTube, news sites, blogs, Substack, X, and Reddit work cleanly.

**Claude in Chrome** *(Anthropic's browser agent, currently beta)*

Okay, now I have a much clearer picture. Let me give you the real comparison.

**How Perplexity Computer handles the three "no setup" sections**

It's browsing the public web on autopilot. The agent navigates to competitor profiles, scans trending topics on TikTok/IG/news sites, reads industry newsletters, summarizes everything, then writes the results into your dashboard. The weekly cron just re-runs that browsing loop. The reason it "just works" is that there's nothing to authenticate, it's all public content being read by a real headless browser.

**Your three real alternatives for organic content scraping + scheduled refresh**

**1. Claude in Chrome (best alternative for your case)**

Same model as Perplexity Computer but it runs inside *your* Chrome with *your* logins. You record a workflow once (or describe it in plain English), schedule it via the clock icon, and it runs daily/weekly/monthly without you. Multi-tab orchestration is the killer feature, drag 15 competitor tabs into Claude's tab group and tell it to scrape hooks, formats, and posting cadence from all of them at once.

Important caveat for you on Pro plans: Claude in Chrome is limited to Haiku 4.5. For dashboard-style scraping that's fine, but if you want Sonnet or Opus running the browser, you'd need Max ($100+/month).

**2. Claude Code + Playwright MCP (most powerful, most setup)**

This is the "build it yourself with full control" route. Claude Code spawns headless Chromium instances, scrapes whatever you want, dumps results to a JSON file or Airtable, and you trigger refreshes via cron or n8n. Can run multiple browser agents in parallel, so it scales much further than Perplexity or Claude in Chrome. Downside: more upfront setup, and you're maintaining the scraping logic.

**3. Codex with Chrome extension**

OpenAI has a "Control Chrome with Codex" extension now too. Functionally similar to Claude in Chrome but in the OpenAI ecosystem. No major advantage over Claude in Chrome for your case, and you'd lose the ability to tie it back to your skills library and existing setup.

**The honest recommendation for organic-only, autonomous scraping**

For your specific use case, I'd actually rank them:

**Best fit: Claude in Chrome + Claude Code combo.** Claude in Chrome handles the recurring browser scrapes (logged into your IG, TikTok, X, Substack, newsletters). Claude Code builds and deploys the dashboard itself and writes the data-processing layer. They're designed to work together.

**Second choice: stay with Perplexity Computer.** If the only thing you want is the guide as written and you don't want to think about it. It's purpose-built for exactly this and it's the simplest path.

**Skip: Manus, Codex.** Both can do it, neither plays to your strengths.

One thing worth naming honestly: TikTok and Instagram actively detect and throttle browser agents on competitor profile views. All of these tools (Perplexity included) will hit walls there eventually. Public RSS, Substack, X, YouTube, news sites, Reddit, Google Trends, all of those scrape cleanly. The dashboard works best if you treat IG and TikTok as "best effort" sections and lean heavier on the platforms that don't fight back.

Want me to draft the equivalent of the Perplexity master prompt but for Claude in Chrome, organic content only, with your brand system baked in?

## 🧑 Adriana · 2026-05-19 13:48
i have found difficult the claude chrome extension it has issues and it lags so if the chrome extension its needed this would be my first one to discard

## 🤖 Claude · 2026-05-19 13:48
Fair, and honestly the lag complaint is legit. The extension is still in beta and people report exactly what you're describing. Let me re-rank without it.

**Your real options, Chrome extension out**

**1. Perplexity Computer (the guide as written)**

Still the cleanest path for your use case. It's not running in your browser, it spins up its own cloud browser, does the work server-side, and just delivers you the result. No extension lag, no Chrome tab management, no "is my computer awake at 9am Monday" question. You hand it the prompt, walk away, come back to a deployed dashboard.

The trade-off you accept: you're inside Perplexity's ecosystem. The dashboard lives at a Perplexity-hosted URL, the schedule lives in their system, and if you want to change something deep you're prompting Computer again rather than editing code.

For "I want this built and refreshed automatically with the least friction possible," this is still the answer.

**2. Claude Code + Playwright MCP (no Chrome extension involved)**

This is the route I'd actually push you toward given everything I know about your setup. Here's why it solves what you're describing without the lag problem:

Claude Code runs in your terminal. Playwright runs headless Chromium *in the background*, not in your visible Chrome. You never see a browser window unless you want to. The scraping happens on a server (your machine, a VPS, or a cloud function) on whatever schedule you set via n8n or cron. No extension, no lag, no UI bottleneck.

The flow looks like this:

- Claude Code builds the dashboard (Next.js or whatever, deployed to Vercel) with your brand system pulled from your skills library.
- Claude Code writes the Playwright scrapers for each source (competitor IG profiles, TikTok creator pages, Substack publications, X accounts, YouTube channels, Google Trends, industry newsletters).
- n8n triggers the scrapers on a weekly cron, dumps results into Airtable or Notion (both already connected for you), and the dashboard reads from there.
- You own every piece of it. No vendor lock-in.

The honest cost: it's a bigger upfront build than pasting the Perplexity prompt. Probably a full day instead of an afternoon. But the system is permanent, free to run after setup (no Perplexity credits burning), and lives natively inside the stack you've already built.

**3. n8n alone with a scraping node**

Worth naming because you already have n8n running. n8n has community nodes for Playwright/Puppeteer and Apify integration. You could build the scraping pipeline entirely in n8n with no Claude Code at all, and just use Claude to write the dashboard frontend separately. Less elegant than option 2, but worth considering if you want to keep everything visual and node-based instead of code-based.

**My actual recommendation**

If you want the guide experience: **Perplexity Computer.** Use the prompt as written, ship it this afternoon.

If you want the durable system that grows with your business and doesn't burn credits forever: **Claude Code + Playwright + your existing n8n.** One day of build, then it's yours.

Which trade-off do you want to make? The "ship today, rent the system" path or the "build it once, own it forever" path?

## 🧑 Adriana · 2026-05-19 13:51
i have subscribed an unsubscribed to perpelxity twice but bc i think i dint know how to use it it keeps telling me that memory is full and to continue in new web, what is like the best applications fo rit?

## 🤖 Claude · 2026-05-19 13:51
Ah, that's a totally different problem and it tells me you're hitting Perplexity's context window limit, not really a "memory full" issue in the way it sounds. Let me explain what's happening and then tell you honestly where Perplexity actually shines, because it sounds like you've been using it for the wrong things.

**What "memory is full, start a new thread" actually means**

Every AI tool has a context window: the amount of text it can hold in active memory in a single conversation. When you keep chatting in one thread, every message you've sent plus every response Perplexity has given is being re-read by the model every time you send a new message. Eventually it hits the ceiling and tells you to start fresh.

This isn't a Perplexity bug. Claude does it, ChatGPT does it, all of them do it. But Perplexity hits it faster than most because every search result it pulls in (full web pages, citations, sources) eats context window space aggressively. You can have a 10-message conversation in Perplexity and already be near the limit because behind the scenes it's loaded 40 web pages into memory.

**The mistake most people make with Perplexity**

People treat it like ChatGPT or Claude: "let me have a long conversation, iterate, brainstorm, refine." Perplexity is bad at that. It's not built for it.

Perplexity is built for one-shot research questions. You ask, it answers with cited sources, you screenshot or save the answer, you close the thread. It's a research engine wearing a chat interface, not a thinking partner.

**Where Perplexity actually shines (the right use cases)**

Quick fact-finding with sources: "What's the average CPM for beauty creators on Instagram in 2026?" One question, one cited answer, done.

Pre-meeting research: "Tell me everything about [brand name], their recent campaigns, leadership, recent news." Five minutes of reading, you walk in informed.

Comparing options: "Compare Riverside, Descript, and CapCut for podcast editing in 2026." It pulls fresh reviews from across the web, gives you a structured comparison.

Live market scans: "What are beauty creators on TikTok talking about this week?" It searches Twitter, Reddit, news, all in one query.

Deep Research mode (the underused feature): for bigger questions, switch to Research mode. It spends 5 to 10 minutes browsing 30+ sources and produces a long structured report. This is where Perplexity actually pulls ahead of Claude and ChatGPT for research-heavy work. Use it for things like "the state of the creator economy in 2026" or "what platforms are emerging for short-form video."

Perplexity Computer (the one in the guide): for the autonomous "build and deploy something" use case. Different product, runs in the cloud, lives in the same Perplexity app.

**Where Perplexity is the wrong tool**

Long-form writing or copywriting (Claude wins).

Iterating on a project over multiple sessions (Claude wins, especially with your skills setup).

Strategic thinking, brand work, creative direction (Claude wins by a lot).

Anything that requires it to remember your voice, brand, or context across sessions (Perplexity doesn't have persistent memory the way Claude does).

Coding (Claude Code or Codex).

**The honest take for you specifically**

You probably don't need Perplexity at all for the work you do day to day. Your strategy work, copywriting, scripting, brand thinking, all of that is better in Claude where your skills library lives and your voice is documented.

What Perplexity would genuinely add to your workflow: a research tab open in your browser for the moments when you need fast cited answers about the creator economy, platform updates, competitor news, or industry trends. Open it, ask the question, get the answer, close the tab. Don't try to live in it.

If you want the dashboard the guide describes, Perplexity Computer is worth subscribing for that specific project, build it in an afternoon, set the weekly cron, then either keep the sub for the research engine or cancel and just keep the dashboard URL alive.

Does that change how you're thinking about it? If the dashboard is the only reason you'd subscribe again, I'd still push you toward building it in Claude Code so you own it permanently. But if you'd actually use Perplexity for daily research too, then it earns its keep.

## 🧑 Adriana · 2026-05-19 13:59
ok giuve me the step by step adapted to my brand my setup on perplexity computer, its for organic remember not ads

## 🤖 Claude · 2026-05-19 14:00
Got it. Here's the full adapted plan for Perplexity Computer, organic content only, your brand, your voice. I'll give you the master prompt first, then the iteration prompts, then the schedule prompt. Copy-paste in order.

---

## STEP 1 · Build the dashboard

Open Perplexity Computer, paste this exact prompt, hit send. Let it run, it takes 15 to 30 minutes for the first build.

```
Build a polished prototype dashboard called "Adri's Creator Intelligence
Dashboard", a single-page app for me as a content creator and creative
strategist. This is for tracking ORGANIC content only, not paid ads.

Build four sections, each with realistic mock data I can replace later:

1. TRENDING TOPICS + CONTENT THEMES
   What's rising in the creator strategy + marketing psychology niche
   this week. Rising formats (carousel structures, voiceover trends,
   storytime hooks), viral angles, recurring themes ranked by momentum.
   Focus on what bilingual and Latina creators are doing, plus the
   broader English-speaking creator economy.

2. COMPETITOR + PEER SIGNALS
   Track these creators by handle (use mock data for now, I'll add
   real handles later): top 8 creator strategists and marketing
   educators on Instagram, TikTok, and YouTube. Show what they posted
   in the last 7 days, which hooks are working, posting cadence, and
   growth signals.

3. INDUSTRY NEWS + PLATFORM UPDATES
   Creator economy moves, platform algorithm changes (IG, TikTok,
   YouTube, Substack, LinkedIn), Meta and ByteDance announcements,
   monetization updates, new creator tools and AI launches relevant
   to content production.

4. MY ORGANIC PERFORMANCE METRICS
   Reach, engagement rate, saves, shares, profile visits, follower
   growth, top posts, and best-performing format across Instagram,
   TikTok, YouTube, LinkedIn, and Substack. Use realistic mock data
   for now with a banner that says "Connect accounts in Settings to
   see real numbers."

LAYOUT REQUIREMENTS

- Fixed left sidebar with clickable navigation that scrolls to each
  section. Items: Overview, Trending, Competitors, Industry News,
  My Performance, Content Calendar, AI Assistant, Settings.
- Dashboard header with my name "@adrianavmarquez" and a subtitle
  "Creator Intelligence, refreshed weekly".
- Top row of KPI cards: Total Reach, Avg Engagement Rate, Follower
  Growth (7d), Top Performing Format.
- Trend line chart showing weekly reach and engagement over the
  last 8 weeks.
- Competitor comparison table with columns: handle, platform, posts
  this week, top hook, engagement rate, growth.
- News feed as a vertical list of cards with source, headline, date,
  and a 2-sentence summary.
- Content Calendar section: monthly grid view with placeholders for
  scheduled posts across platforms, color-coded by platform.
- AI Assistant section: a chat interface placeholder where I can
  ask questions about my own data.
- Settings panel accessed from a gear icon top right, with sections
  for Instagram, TikTok, YouTube, LinkedIn, Substack account
  connections.

VISUAL STYLE, NON-NEGOTIABLE

Brand colors, use these exact hex codes:
- Primary red: #D72323
- Primary blue: #3846C4
- Primary yellow: #FFBA35
- Black: #000000
- White: #FFFFFF
- Lavender accent: #F2E9FF
- Sky blue accent: #2EA4FB

Use color sparingly and intentionally. White backgrounds, black body
text, brand colors only for titles, KPI numbers, accent strokes,
data viz, and call-to-action elements. Never use all brand colors at
once in the same section. Default accent is the red.

Typography: Poppins for everything.
- Titles: Poppins Bold, in brand red or brand blue
- Subtitles: Poppins Medium, black
- Body text: Poppins Regular, black on white
- KPI numbers: Poppins Bold, large, in brand color

Tables: black borders, header row text in brand color Poppins Medium,
body rows black text on white.

Feel: clean, editorial, bold, magazine-with-live-numbers. Not corporate
SaaS. Think New York Times editorial meets Notion.

CRITICAL FORMATTING RULE

Em-dashes are banned across the entire dashboard, no exceptions. The
character "—" must not appear anywhere in any UI copy, mock data,
headlines, descriptions, or labels. Replace with commas, colons, or
rewrite the phrase entirely.

DEPLOY

Deploy the dashboard to a live public URL I can bookmark and share.
Screenshot every section after deployment so I can review.
```

---

## STEP 2 · After the first build, iterate

Don't try to fix everything in the first prompt. Let it build, look at it, then send follow-ups one at a time. Examples of iteration prompts:

```
The competitor table looks too dense. Make rows taller, add 8px more
vertical padding, and change the header row background to #F2E9FF
with text in #3846C4. Keep the rest the same. Redeploy.
```

```
The trending topics section should display as cards in a 2-column
grid on desktop, single column on mobile. Each card needs: title,
3-bullet summary, source platform, and momentum indicator (rising,
peak, fading). Use the brand yellow for "rising" tags, red for
"peak", and gray for "fading". Redeploy.
```

```
Add an empty state to the Content Calendar that says "Click a date
to plan a post" with a small icon, and let me click any date to
open a simple modal where I can type the post idea, pick a platform,
and save. Keep saved data in localStorage for now. Redeploy.
```

Iterate until it looks right. Three to five rounds is normal.

---

## STEP 3 · Add your real competitor handles

Once the layout works, swap mock data for real targets:

```
Replace the mock competitor data with these real handles. Pull their
most recent 7 days of public posts, top hooks, posting cadence, and
estimated engagement. Update the competitor table and refresh the
deployed site.

Instagram: [paste 8 handles, e.g., @vanessalau.co, @maddyrosecass,
@joiingram, etc.]

TikTok: [paste handles]

YouTube: [paste channel names or URLs]
```

Pick competitors that are genuinely close to your positioning. Other bilingual creator strategists, marketing educators, creators teaching the psychology of content. Don't pick aspirational accounts way bigger than you, the signal gets noisy. Pick peers and one tier above.

---

## STEP 4 · Set the weekly schedule

This is what makes the whole thing worth it. Send this prompt:

```
Schedule the following recurring task to run every Monday at 8am
Eastern Time:

1. Refresh the trending topics section with what's rising in the
   creator strategy and marketing psychology niche over the last
   7 days. Pull from Instagram, TikTok, YouTube, Substack, Twitter,
   and Reddit creator communities.

2. Refresh the competitor signals section. For each tracked handle,
   pull their last 7 days of posts, identify the top-performing hook
   based on visible engagement, note posting cadence, and flag any
   significant shifts in their content strategy or follower growth.

3. Refresh the industry news section with 5 to 8 of the most
   important creator economy and platform updates from the last 7
   days. Prioritize Meta, ByteDance, YouTube, Substack, LinkedIn,
   and major AI tool launches relevant to content creators.

4. Redeploy the dashboard with updated data.

5. Send me a short "What changed this week" summary as a separate
   message. Format: 3 bullets max for trends, 3 bullets max for
   competitor moves, 3 bullets max for industry news. Bilingual is
   fine, write the way I'd write it, Spanglish where it lands. No
   em-dashes.

Keep my brand styling intact on every redeploy.
```

---

## STEP 5 · Skip the API connection step for now

The guide tells you to plug in Instagram Graph API, TikTok Display API, and YouTube Data API tokens to populate the "My Performance" section. That's the dev-portal heavy step the guide warns you about.

**My honest advice: don't bother yet.** Build the three organic-scraping sections first (trending, competitors, news), live with the dashboard for a few weeks, and decide if you actually use it before spending a Saturday on developer portals. If you find yourself opening it weekly, then go set up the IG and YouTube tokens. TikTok takes 1 to 3 business days to approve so do that one last.

In the meantime, leave the "My Performance" section showing mock data with the banner. The other three sections are where the real value lives.

---

## One thing to watch

Perplexity Computer credits burn faster on scheduled tasks than on one-off builds. Watch your usage the first two weeks. If a single weekly refresh is eating too much of your monthly allowance, you can:

- Drop the schedule to bi-weekly instead of weekly
- Reduce the number of competitors from 8 to 4
- Drop the industry news section to top 3 items instead of top 5 to 8

Trending and competitors are the two sections worth paying credits for. News you can get from your existing newsletter subs.

---

That's the whole flow. Send the master prompt, iterate three to five times, add real handles, schedule the cron, walk away. Ping me back if anything in the build comes out weird and I'll write you the fix prompt.

## 🧑 Adriana · 2026-05-20 21:04
step one i ready but i think the data being shown it has to be a sample bc it does not relate to the hashtags i need tobe looking for o keywords relevant to my brand, neither my competition:

for example these are scheduled tasks i have with manus ai:

> *[line redacted — references an out-of-scope venture]*
2. Generate and deliver the Manus Weekly Digest newsletter for Adriana V. Marquez (@adrianavmarquez). 
BRAND CONTEXT:
Adriana is a bilingual (Spanish/English) content creator for Spanish-speaking women 25+ from USA, Mexico, Venezuela, Spain, and Colombia. Her brand "Motus" has 3 content pillars: (1) Content Creation & Creativity, (2) Tech & Gear, (3) Lifestyle (beauty, fashion, wellness). She is active on Instagram, TikTok, YouTube, Pinterest, and X.
CREATOR LIST (from Notion page 3269c084f04180c7af1ecdbc26910367):
The creator database is stored at /home/ubuntu/creator_platform_research.json with cross-platform handles for all 40 creators across 7 categories: Filmmakers, Content/Editing Coaches, Fashion & Lifestyle, Vlogs, Tech & AI, Social Media & Marketing, Creative Storytellers, Business Owners.
NEWSLETTER GENERATION PROCESS:
1. Load the creator list from /home/ubuntu/creator_platform_research.json
2. For each YouTube creator, use the YouTube Data API (Youtube/get_channel_videos) to fetch videos published in the last 7 days. Use the channel handle from the json file.
3. For Instagram and TikTok creators, search the web for their recent posts from the past week (search "[creator handle] instagram new post this week" or browse their profile).
4. For each creator with new content, analyze: topic, hook strategy (first 3-5 seconds), script/visual breakdown, performance metrics (views/likes if available).
5. Research the latest trends in: content creation tools, AI/tech for creators, social media algorithm updates, pop culture moments relevant to women 25+ in Latin America/USA, beauty/fashion/wellness trends.
6. Generate the newsletter in this exact structure:
   - Header: "💌 Motus Weekly Digest: [Date]"
   - Executive Summary (2-3 sentences on the week's biggest patterns)
   - Creator Spotlight: Deep Dive (2 standout pieces with full analysis: topic, hook strategy, script breakdown, performance insights, clickable link)
   - Weekly Roundup by category (all creators with new content, each with: title, clickable link, quick take)
   - Trend Watch section (pop culture, tech/AI, platform updates, lifestyle trends relevant to Motus brand)
   - Actionable Takeaways for Motus (2-3 specific content ideas Adriana can act on)
7. Deliver the newsletter in TWO places:
   a. Create a new Notion page as a child of page ID 3269c084f04180c7af1ecdbc26910367 titled "Motus Weekly Digest: [Date]" with the full newsletter content
   b. Send the full newsletter as a message to the user in this chat
IMPORTANT NOTES:
- All links must be real, clickable URLs to the actual content
- Analyze ONLY content published in the last 7 days
- Keep the tone warm, smart, and encouraging — like a brilliant creative friend who did all the research for you
- The newsletter should feel like a curated magazine, not a data dump

## 🤖 Claude · 2026-05-20 21:04
You're exactly right, and this is the key insight: what you're seeing in Step 1 is **mock data**, sample placeholder content the dashboard generates to show you the layout. It was never going to match your real hashtags, keywords, or competitors because I deliberately told it to use realistic mock data so you could approve the design first.

But your Manus tasks reveal something important: **you already have the real strategic infrastructure built.** The creator database, the brand context, the pillars, the niche definition. That's the actual fuel. The Perplexity prompt I gave you was generic because I didn't have that context loaded into it. Now I do.

So let me reconcile two things, because there's a tension in your setup worth naming.

**You have two different brand frames running in parallel**

Your Manus tasks describe **Motus**: bilingual content creator for Spanish-speaking women 25+, three pillars (Content Creation & Creativity, Tech & Gear, Lifestyle), active on IG/TikTok/YouTube/Pinterest/X, audience across USA/Mexico/Venezuela/Spain/Colombia.

That's a *creator-facing lifestyle brand*. Different from the *creator strategist / marketing educator* positioning I built the Step 1 prompt around. Both are you, but they're different audiences, different competitors, different keywords. Before I rewrite the Perplexity prompt I need to know which brand this dashboard serves, because the trending topics, the competitor list, and the keywords all change depending on the answer.

The Manus task #1 says "creators who educate other creators." Task #2 says "Spanish-speaking women 25+, lifestyle." Those pull in different directions.

**The other thing worth naming honestly**

Looking at your two Manus tasks side by side with what you're trying to do in Perplexity Computer: Manus is already doing the harder, better-integrated version of this. It loads your real creator database from JSON, hits the YouTube Data API for actual recent videos, writes to your Notion, and delivers a curated newsletter. That's a more sophisticated pipeline than a Perplexity dashboard with scraped mock-to-real data.

So the real question isn't "how do I make Perplexity match Manus." It's "what does the Perplexity dashboard give me that Manus doesn't?" The answer is: a **visual, always-on dashboard URL** versus Manus's **scheduled report/newsletter**. Different output format, same underlying research. If you want the glanceable visual layer, Perplexity Computer is worth it. If you just want the intelligence delivered, Manus already wins and you might not need Perplexity at all.

Let me build you the right thing instead of guessing. Two quick questions:

It looks like the questions were sent to you but your selections didn't come through, the response came back empty. No problem, just tell me in your own words and we'll keep moving.

The two things I need from you:

**1. Which brand is this dashboard for?** Your Manus tasks blur two different positionings, Motus (lifestyle for Spanish-speaking women 25+) and the creator strategist who educates other creators. They have different competitors and different keywords, so the dashboard changes depending on which one. Or if you want both in one unified view, that works too, I'd just split it into two tracked segments.

**2. What is the Perplexity dashboard actually adding?** Because here's my honest read: your Manus setup is already doing the more sophisticated version of this. It loads your real 40-creator database from JSON, hits the YouTube Data API for actual recent videos, writes to Notion, and ships a curated newsletter. That's a real pipeline. A Perplexity dashboard would mostly add a *visual, glanceable URL* on top of intelligence you're already gathering. If that visual layer is what you want, great, it's worth building. If you're hoping Perplexity replaces Manus, I'd actually argue against it, Manus is winning on integration.

One more thing I can do that would make the Perplexity prompt genuinely yours instead of generic: that creator database lives in your Notion (page `3269c084f04180c7af1ecdbc26910367`). I have Notion connected. If you want, I can pull your actual creator list and brand context straight from there and bake the real handles, real categories, and real keywords into the Perplexity prompt, so Step 1 stops showing you sample data that doesn't relate to your niche.

Want me to pull the creator database from Notion first? That single move fixes the core complaint, the dashboard showing irrelevant mock hashtags and competitors, because we'll feed it your real targets from the start. Just confirm the brand frame and whether to pull from Notion, and I'll write you the corrected prompt.

## 🧑 Adriana · 2026-05-20 21:05
Q: Which brand should this Perplexity dashboard serve?
A: Both, unified view

Q: What's the dashboard actually adding on top of your Manus tasks?
A: Test if Perplexity beats Manus

## 🤖 Claude · 2026-05-20 21:06
Perfect, that's a clear frame: unified view across both brands, and you're running Perplexity as a head-to-head test against Manus. That actually sharpens the build, because for a fair test the Perplexity dashboard needs to be fed the *same real inputs* Manus uses, otherwise you're comparing Manus-with-real-data against Perplexity-with-mock-data and the test is rigged before it starts.

So the move is: pull your actual creator database and brand context from Notion, bake them into the Perplexity prompt, and let both tools run on identical fuel. Let me grab that Notion page first.

Got it, I have your real creator database now. This is the exact list Manus uses, so feeding it into Perplexity gives you a fair test. Let me organize what I pulled and then write you the corrected prompt.

**Your real tracked creators, by category (37 total)**

Filmmakers: dannygevirtz, lifeofriza, aliyahsimone, gakulange, damiansayaz, gawxart (YT) + artzenmedia, en.somniac, ignaciovasconez, andrews_life, omgadrian (IG)

Content/Editing/Influencer Coaches: suddinqg, happywithmeg, stevenwommack, justinescameraroll_, gannon.meyer (IG)

Fashion & Lifestyle: mariabottle (YT) + katharina.spielmann, lozvassallo, aish_2c, carlotamadrigal, noorieana, geeeramos (IG)

Blogs/Vlogs: moyamawhinney, nina.montagne, mickeyyyy4, claufernandezm (YT)

Tech & AI: benkaluza, johnbucog (IG)

Social Media & Marketing: agusbirch-mkt, tessbarclay, vanessalau (YT) + soymariamalagarrigaa, personalbrandlaunch, bonusfootage, justjaeden_, jason_swet, orenmeetsworld, li.gorbunova, itsryanto (IG)

Creative Storytellers: juanatempesta (IG)

Business Owners: inspiredmediaco, gracebeverley, juliabroome, jessijeanhome, nanadelrey, christy_ix (IG)

Now here's the honest structural problem you need to know before we build, because it directly affects your "does Perplexity beat Manus" test:

**Why your Manus setup has a built-in advantage Perplexity can't match**

Manus loads these handles from a JSON file *and hits the YouTube Data API* for the YouTube creators. That means for the ~13 YouTube channels in your list, Manus gets exact, structured, real video data from the last 7 days: titles, links, view counts. That's API-grade accuracy.

Perplexity Computer can't do that. For the same YouTube creators it has to *browse and read* the channel pages, which is less precise and sometimes stale. And for the Instagram creators (the majority of your list, ~24 handles), both tools are stuck browsing public profiles, where IG actively throttles agents. So neither tool will scrape IG cleanly, but only Manus gets the YouTube API edge.

What this means for your test: if you judge purely on "who got the most accurate recent data," Manus likely wins because of the YouTube API. So judge Perplexity on different criteria: **the visual dashboard, the synthesis quality, and whether the glanceable format changes how you actually use the intelligence.** That's where Perplexity could genuinely beat Manus, not on raw data accuracy.

Here's the corrected Step 1 prompt with your real creators and unified brand baked in:

```
Build a polished prototype dashboard called "Adri's Creator Intelligence
Dashboard", a single-page app for me, Adriana V. Marquez
(@adrianavmarquez). This tracks ORGANIC content only, not paid ads.

I run a unified creator brand with two faces that share one dashboard:
- MOTUS: bilingual (Spanish/English) lifestyle creator for Spanish-
  speaking women 25+ across USA, Mexico, Venezuela, Spain, Colombia.
  Three pillars: Content Creation & Creativity, Tech & Gear, Lifestyle
  (beauty, fashion, wellness).
- CREATOR STRATEGIST: I teach the psychological WHY behind content
  strategy to other creators and marketers.
Active on Instagram, TikTok, YouTube, LinkedIn, Pinterest, Substack, X.

Build five sections, each with realistic mock data I will replace with
real scrapes later:

1. TRENDING TOPICS + CONTENT THEMES
   What is rising this week across two lanes: (a) the creator-education
   and marketing-psychology niche, and (b) lifestyle content for Latina
   and Spanish-speaking women 25+. Rising formats, viral angles, hooks,
   themes ranked by momentum. Pull from IG, TikTok, YouTube, Substack,
   X, Reddit, and Pinterest.

2. COMPETITOR + PEER SIGNALS
   Track the creators listed below by category. For each, show last
   7 days of public posts, top working hook, posting cadence, and
   growth signal. Use mock data now, structured so I can swap in real
   scrapes.

3. INDUSTRY NEWS + PLATFORM UPDATES
   Creator economy moves and algorithm changes across IG, TikTok,
   YouTube, Substack, LinkedIn, Pinterest. Meta and ByteDance
   announcements, monetization updates, new creator and AI tools.

4. MY ORGANIC PERFORMANCE METRICS
   Reach, engagement rate, saves, shares, profile visits, follower
   growth, top posts, best format, across IG, TikTok, YouTube,
   LinkedIn, Substack. Mock data now with a banner: "Connect accounts
   in Settings to see real numbers."

5. CONTENT CALENDAR
   Monthly grid, color-coded by platform, click a date to plan a post.

TRACKED CREATORS, organize the competitor section by these categories:

Filmmakers: youtube.com/@dannygevirtz, @lifeofriza, @aliyahsimone,
@gakulange, @damiansayaz, @gawxart; instagram.com/artzenmedia,
en.somniac, ignaciovasconez, andrews_life, omgadrian

Content/Editing/Influencer Coaches: instagram.com/suddinqg,
happywithmeg, stevenwommack, justinescameraroll_, gannon.meyer

Fashion & Lifestyle: youtube.com/@mariabottle;
instagram.com/katharina.spielmann, lozvassallo, aish_2c,
carlotamadrigal, noorieana, geeeramos

Vlogs: youtube.com/@moyamawhinney, @nina.montagne, @mickeyyyy4,
@claufernandezm

Tech & AI: instagram.com/benkaluza, johnbucog

Social Media & Marketing: youtube.com/@agusbirch-mkt, @tessbarclay,
@vanessalau; instagram.com/soymariamalagarrigaa, personalbrandlaunch,
bonusfootage, justjaeden_, jason_swet, orenmeetsworld, li.gorbunova,
itsryanto

Creative Storytellers: instagram.com/juanatempesta

Business Owners: instagram.com/inspiredmediaco, gracebeverley,
juliabroome, jessijeanhome, nanadelrey, christy_ix

LAYOUT
- Fixed clickable left sidebar: Overview, Trending, Competitors,
  Industry News, My Performance, Content Calendar, AI Assistant,
  Settings.
- Header: "@adrianavmarquez" + subtitle "Creator Intelligence,
  refreshed weekly".
- KPI cards row: Total Reach, Avg Engagement Rate, Follower Growth
  (7d), Top Performing Format.
- Trend line chart: weekly reach + engagement, last 8 weeks.
- Competitor table grouped by category: handle, platform, posts this
  week, top hook, engagement, growth.
- News feed: vertical cards, source, headline, date, 2-sentence
  summary.
- Settings gear top right: connection panels for IG, TikTok, YouTube,
  LinkedIn, Substack.

VISUAL STYLE, NON-NEGOTIABLE
Brand colors, exact hex:
Primary red #D72323, primary blue #3846C4, primary yellow #FFBA35,
black #000000, white #FFFFFF, lavender #F2E9FF, sky blue #2EA4FB.
Use color sparingly and intentionally. White backgrounds, black body
text. Brand colors only for titles, KPI numbers, accent strokes, data
viz, CTAs. Never all colors at once in one section. Default accent red.
Typography: Poppins everywhere. Titles Poppins Bold in red or blue.
Subtitles Poppins Medium black. Body Poppins Regular black on white.
KPI numbers Poppins Bold large in brand color. Tables: black borders,
header row text in brand color Poppins Medium, body black on white.
Feel: clean, editorial, bold, magazine with live numbers.

CRITICAL RULE
Em-dashes are banned across the entire dashboard, no exceptions. The
character "—" must not appear anywhere in UI copy, mock data,
headlines, or labels. Use commas, colons, or rewrite.

DEPLOY
Deploy to a live public URL I can bookmark and share. Screenshot every
section after deployment so I can review.
```

Once it builds, the iteration prompts and the weekly schedule prompt from before still apply. When you schedule the refresh, point it at this same creator list and tell it to flag the YouTube creators as "verify against YouTube directly" since those are the ones where accurate recent data matters most.

One question to make the test cleaner: do you want me to write the weekly schedule prompt so its output mirrors your Manus newsletter structure (executive summary, creator spotlight, roundup by category, trend watch, takeaways)? That way both tools produce comparable output and you can judge them side by side on the same format.

## 🧑 Adriana · 2026-05-20 21:18
Im motus thats a typo

## 🤖 Claude · 2026-05-20 21:19
Ah, good, that simplifies everything. Scratch the dual-brand framing. You're Motus: bilingual lifestyle creator for Spanish-speaking women 25+, three pillars (Content Creation & Creativity, Tech & Gear, Lifestyle). One brand, one audience, clean.

That actually makes the dashboard tighter. Here's the corrected Step 1 prompt, Motus only, your real creators baked in:

```
Build a polished prototype dashboard called "Motus Creator Intelligence
Dashboard", a single-page app for me, Adriana V. Marquez
(@adrianavmarquez). This tracks ORGANIC content only, not paid ads.

BRAND CONTEXT
Motus is my bilingual (Spanish/English) content brand for Spanish-
speaking women 25+ across USA, Mexico, Venezuela, Spain, and Colombia.
Three content pillars:
1. Content Creation & Creativity
2. Tech & Gear
3. Lifestyle (beauty, fashion, wellness)
Active on Instagram, TikTok, YouTube, Pinterest, and X.

Build five sections, each with realistic mock data I will replace with
real scrapes later:

1. TRENDING TOPICS + CONTENT THEMES
   What is rising this week, mapped to my three pillars. Rising formats,
   viral angles, hooks, recurring themes ranked by momentum. Focus on
   content for Latina and Spanish-speaking women 25+, plus the broader
   creator-education and tech/gear conversation. Pull from IG, TikTok,
   YouTube, Pinterest, X, and Reddit.

2. COMPETITOR + PEER SIGNALS
   Track the creators listed below by category. For each, show last
   7 days of public posts, top working hook, posting cadence, and
   growth signal. Use mock data now, structured so I can swap in real
   scrapes.

3. INDUSTRY NEWS + PLATFORM UPDATES
   Creator economy moves and algorithm changes across IG, TikTok,
   YouTube, Pinterest, X. Meta and ByteDance announcements, monetization
   updates, new creator and AI tools, plus pop culture and beauty/
   fashion/wellness moments relevant to women 25+ in Latin America and
   the USA.

4. MY ORGANIC PERFORMANCE METRICS
   Reach, engagement rate, saves, shares, profile visits, follower
   growth, top posts, best format, across IG, TikTok, YouTube,
   Pinterest, X. Mock data now with a banner: "Connect accounts in
   Settings to see real numbers."

5. CONTENT CALENDAR
   Monthly grid, color-coded by platform, click a date to plan a post.

TRACKED CREATORS, organize the competitor section by these categories:

Filmmakers: youtube.com/@dannygevirtz, @lifeofriza, @aliyahsimone,
@gakulange, @damiansayaz, @gawxart; instagram.com/artzenmedia,
en.somniac, ignaciovasconez, andrews_life, omgadrian

Content/Editing/Influencer Coaches: instagram.com/suddinqg,
happywithmeg, stevenwommack, justinescameraroll_, gannon.meyer

Fashion & Lifestyle: youtube.com/@mariabottle;
instagram.com/katharina.spielmann, lozvassallo, aish_2c,
carlotamadrigal, noorieana, geeeramos

Vlogs: youtube.com/@moyamawhinney, @nina.montagne, @mickeyyyy4,
@claufernandezm

Tech & AI: instagram.com/benkaluza, johnbucog

Social Media & Marketing: youtube.com/@agusbirch-mkt, @tessbarclay,
@vanessalau; instagram.com/soymariamalagarrigaa, personalbrandlaunch,
bonusfootage, justjaeden_, jason_swet, orenmeetsworld, li.gorbunova,
itsryanto

Creative Storytellers: instagram.com/juanatempesta

Business Owners: instagram.com/inspiredmediaco, gracebeverley,
juliabroome, jessijeanhome, nanadelrey, christy_ix

LAYOUT
- Fixed clickable left sidebar: Overview, Trending, Competitors,
  Industry News, My Performance, Content Calendar, AI Assistant,
  Settings.
- Header: "@adrianavmarquez · Motus" + subtitle "Creator Intelligence,
  refreshed weekly".
- KPI cards row: Total Reach, Avg Engagement Rate, Follower Growth
  (7d), Top Performing Format.
- Trend line chart: weekly reach + engagement, last 8 weeks.
- Competitor table grouped by category: handle, platform, posts this
  week, top hook, engagement, growth.
- News feed: vertical cards, source, headline, date, 2-sentence
  summary.
- Settings gear top right: connection panels for IG, TikTok, YouTube,
  Pinterest, X.

VISUAL STYLE, NON-NEGOTIABLE
Brand colors, exact hex:
Primary red #D72323, primary blue #3846C4, primary yellow #FFBA35,
black #000000, white #FFFFFF, lavender #F2E9FF, sky blue #2EA4FB.
Use color sparingly and intentionally. White backgrounds, black body
text. Brand colors only for titles, KPI numbers, accent strokes, data
viz, CTAs. Never all colors at once in one section. Default accent red.
Typography: Poppins everywhere. Titles Poppins Bold in red or blue.
Subtitles Poppins Medium black. Body Poppins Regular black on white.
KPI numbers Poppins Bold large in brand color. Tables: black borders,
header row text in brand color Poppins Medium, body black on white.
Feel: clean, editorial, bold, magazine with live numbers.

CRITICAL RULE
Em-dashes are banned across the entire dashboard, no exceptions. The
character "—" must not appear anywhere in UI copy, mock data,
headlines, or labels. Use commas, colons, or rewrite.

DEPLOY
Deploy to a live public URL I can bookmark and share. Screenshot every
section after deployment so I can review.
```

That's the clean Motus version. The data you saw before was mock placeholder, so once this builds with your real creator list and the weekly schedule pointed at the same handles, you'll finally see relevant trends and real competitors instead of generic samples.

The honest test-fairness note from before still stands: for the ~13 YouTube creators in your list, Manus has an edge because it hits the YouTube Data API for exact recent video data, while Perplexity has to browse. So judge Perplexity on the visual dashboard, the synthesis quality, and whether the always-on glanceable format changes how you use the intel, not on raw data precision.

And my offer holds: want me to write the weekly schedule prompt so Perplexity's output mirrors your Manus newsletter structure (executive summary, creator spotlight, roundup by category, trend watch, Motus takeaways)? Same format on both tools makes the head-to-head actually comparable.

## 🧑 Adriana · 2026-05-20 21:20
manus takes too many credits its not a dashboard is just a written report its not as visual as i wante dto be and i wantes to actually reloading live

## 🤖 Claude · 2026-05-20 21:21
Right, now the picture is complete and it changes my recommendation. Let me say the honest thing first: **what you actually want, Perplexity Computer can't fully give you either.**

Let me break down the gap between what you want and what each tool does, because there's a mismatch worth naming before you spend more credits.

**What you're describing**

A visual dashboard that reloads live. "Live" meaning you open the URL and the numbers and trends are current, refreshing on their own, not a static snapshot from last Monday.

**What Perplexity Computer actually produces**

Not that. It builds a dashboard and deploys it to a URL, yes, but the data inside is frozen at the moment it last ran. It's a snapshot, not a live feed. To update it, the scheduled task re-runs (burning credits each time, same problem you have with Manus) and redeploys. So you'd be trading Manus's "expensive written report" for Perplexity's "expensive visual report." More visual, same credit-burn problem, still not truly live.

The "reloading live" part is the issue. No agent-based tool (Manus, Perplexity Computer, Claude in Chrome) gives you live-reloading data, because every refresh is an expensive agent run. Agents are the wrong architecture for "live."

**What "live reloading" actually requires**

A real dashboard with a backend. The page loads, calls APIs or a database, and shows current data every time you open it, no agent, no credits per view. This is the Claude Code + n8n route I mentioned earlier, and your frustration is exactly why it's the right fit:

- The dashboard is a real deployed web app (free to host on Vercel). Open it anytime, it loads fresh from your database. Truly "live" in the sense you mean.
- n8n does the scraping/fetching on a schedule (you already pay for n8n, no per-run agent credits). It writes to Airtable or Notion.
- The dashboard reads from that database every time it loads. So between scheduled fetches it shows the latest stored data, and the moment n8n updates the store, the dashboard reflects it on next load. No credits burned when you view it. No agent re-running to "redeploy."

That's the only architecture that gives you all three things you want at once: visual, live-reloading, and not bleeding credits.

**The honest tradeoff**

Perplexity Computer: ship it this afternoon, looks great, but it's a snapshot and every refresh costs credits. Same fundamental problem as Manus, just prettier.

Claude Code + n8n: a real build (think a day, not an afternoon), but then it's free to run forever, genuinely live, and yours. No vendor credits ever again.

Given that "too many credits" is the exact pain that made you abandon Manus, paying Perplexity credits to solve a credit problem doesn't really solve it. It just moves it.

**My recommendation**

Build the real thing in Claude Code, fed by your n8n instance. You already have n8n connected and running. The YouTube creators get real API data (same edge Manus had, but free through n8n's YouTube node). The dashboard reads from Airtable. You open the URL whenever, it's current, nobody charges you per view.

I can do two things right now to get you moving:

1. Write the Claude Code build prompt, adapted to Motus, your brand system, your real creator list, deploying a live dashboard that reads from Airtable.
2. Sketch the n8n workflow that does the weekly fetch (YouTube API for the channels, web scrape for the rest) and writes to Airtable, so the dashboard has something to read.

Want me to start with the Claude Code prompt? That's the piece that gives you the visual, live-reloading dashboard you've been trying to get this whole time. The credit problem disappears because the only thing that ever "runs" is your already-paid n8n, and only once a week.

## 🧑 Adriana · 2026-05-20 21:22
Ok i can chedule to rerun so its updated and re done i sent the step one and is aking to deploy make aprompt to fix it with all you just learnt

## 🤖 Claude · 2026-05-20 21:23
Before I write it, one thing to get right so this deploy actually lands the way you want.

You said you can schedule Perplexity to re-run and redeploy, and that's fine, that's the Perplexity model and it works. So this prompt's job is to get a clean, on-brand deploy out of the build you already started, and set it up so your scheduled re-runs refresh it properly. I'm not going to redirect you to Claude Code mid-flow, you're already in motion in Perplexity, let's finish strong here.

Paste this as your next message in the same Perplexity Computer thread (it continues the build you started, so don't start a new thread):

```
Yes, deploy it. Before and during deploy, apply these corrections and
requirements:

DEPLOY REQUIREMENTS
- Deploy to a live public URL I can bookmark and share.
- The deployed page must re-fetch and re-render its data fresh every
  time it loads, so when you re-run this task on a schedule and
  redeploy, the same URL shows the updated data without me needing a
  new link. Keep the URL stable across redeploys.
- After deploying, take a full screenshot of every section and give me
  the live URL at the top of your reply.

CONFIRM THE BRAND STYLING IS INTACT ON THE DEPLOYED VERSION
- Brand colors, exact hex only: red #D72323, blue #3846C4, yellow
  #FFBA35, black #000000, white #FFFFFF, lavender #F2E9FF, sky blue
  #2EA4FB. Color used sparingly: white backgrounds, black body text,
  brand color only for titles, KPI numbers, accent strokes, data viz,
  and CTAs. Never all colors at once in one section. Default accent red.
- Poppins everywhere. Titles Poppins Bold in red or blue. Subtitles
  Poppins Medium black. Body Poppins Regular black on white. KPI numbers
  Poppins Bold large in brand color. Tables: black borders, header row
  text in brand color Poppins Medium, body black on white.
- Em-dashes are banned everywhere on the dashboard. The character "—"
  must not appear in any copy, mock data, headline, or label. Use
  commas, colons, or rewrite. Scan the whole build and remove any.

CONFIRM ALL FIVE SECTIONS DEPLOYED CORRECTLY
1. Trending topics mapped to my three Motus pillars (Content Creation
   & Creativity, Tech & Gear, Lifestyle for Spanish-speaking women 25+).
2. Competitor signals, grouped by my real creator categories
   (Filmmakers, Content/Editing Coaches, Fashion & Lifestyle, Vlogs,
   Tech & AI, Social Media & Marketing, Creative Storytellers, Business
   Owners), each creator showing last 7 days, top hook, cadence, growth.
3. Industry news + platform updates.
4. My organic performance metrics, with the "Connect accounts in
   Settings to see real numbers" banner since these are still mock.
5. Content calendar, color-coded by platform, clickable dates.

LEFT SIDEBAR
Confirm the sidebar is fixed and every item scrolls to its section:
Overview, Trending, Competitors, Industry News, My Performance, Content
Calendar, AI Assistant, Settings.

DATA NOTE
The current data is mock placeholder, that is expected for this build.
Deploy with the mock data now. When I schedule the recurring refresh,
the real trending topics, competitor posts, and news will replace it.
Just make sure the layout, the brand styling, and the creator
categories are correct and locked so the scheduled re-runs only swap
the data, not the design.
```

That gets you deployed, on-brand, em-dash-free, with a stable URL your scheduled re-runs will keep refreshing.

Then, once it's live and you've eyeballed the screenshots, your very next message should be the schedule prompt so the mock data starts getting replaced with real scrapes. Want me to hand you that scheduled-refresh prompt now, written to mirror your Manus newsletter structure (executive summary, creator spotlight, roundup by category, trend watch, Motus takeaways) so you can judge Perplexity against Manus on equal footing? Say the word and I'll write it to drop in right after the deploy confirms.

## 🧑 Adriana · 2026-05-20 21:26
what apis or how ccna i connect my youtube, instagram, tiktok and pinterest to it so it can track my insights?

## 🤖 Claude · 2026-05-20 21:27
Good, this is the "My Performance" section, the one that needs real account connections instead of scraping. Let me be straight with you about each platform, because they range from "doable in an afternoon" to "genuinely painful," and one of them is basically not worth it for a solo creator.

Quick honest framing first: these APIs return *your own* analytics (your reach, your engagement, your followers). They're separate from the scraping that powers your trending/competitor/news sections. And inside Perplexity Computer specifically, wiring real API tokens into a deployed dashboard is fiddly, Perplexity isn't really built to hold persistent API credentials securely. So I'll tell you what each requires, then give you the honest verdict on whether to bother in Perplexity vs. doing this part in n8n.

Let me verify the current state of each platform's API since these change often.

I have what I need. Here's the honest, platform-by-platform breakdown for connecting *your own* insights, ranked from easiest to most painful.

**YouTube, easiest, do this first**

The YouTube Data API v3 is the friendliest of the four. Create a Google Cloud project, enable YouTube Data API v3, generate an API key (or OAuth for private channel metrics like watch time and revenue). Public stuff (views, likes, comments, subscriber count, recent videos) needs only the API key, no approval wait. For deeper private analytics you add OAuth. This is the one where you'll actually get clean data the same afternoon, and it's the same API your Manus setup already uses for the YouTube creators.

**Instagram, doable but a real project**

Two things to know up front. First, your account must be a Business or Creator account, not personal. The API only returns data for Instagram Business or Creator accounts that you own or manage. Yours is a creator account so you're fine. Second, the old simple path is dead: the Instagram Basic Display API was officially deprecated and shut down on December 4, 2024. Everything now goes through the Instagram Graph API.

The path: Meta developer account, create a Business-type app, add Instagram Graph API, authenticate via OAuth, request `instagram_basic` and `instagram_manage_insights`, generate a long-lived token. That token gives you reach, impressions, profile views, follower count, engagement. Two honest catches: long-lived tokens last about 60 days so you have to refresh them, and going fully live can require Meta app review, which takes around 4 to 6 weeks. For your own single account in development mode you can often skip the long review and use it just for yourself, which is the move here.

**Pinterest, middle difficulty**

Pinterest has its own API v5 with an analytics endpoint for your own account (impressions, saves, pin clicks, outbound clicks). Create a Pinterest developer app, OAuth in, request analytics scope. Less documented than the others but workable. Honestly, for Motus, Pinterest analytics are the lowest-stakes of the four, I'd connect it last or skip it unless Pinterest is a real traffic driver for you.

**TikTok, the painful one, and I'd tell you to skip the API**

Here's the thing nobody says clearly. TikTok's Display API gives you read-only access to your public content, profile details and publicly shared videos, but it cannot access analytics. It's a window, not a door. The actual analytics (views, watch time, audience demographics, follower growth) live in the **Business API**, and the Business API requires a registered developer app and approval from TikTok. Individual creators typically access it through authorized third-party platforms rather than building direct integrations. Approval also takes 3 to 7 days and there's no webhooks, so you'd have to build a polling system. For a solo creator, the TikTok API is the worst effort-to-payoff ratio of the four.

**My honest verdict for you**

Don't try to wire all four into Perplexity Computer. Two reasons: Perplexity isn't built to securely hold and refresh OAuth tokens that expire every 60 days, and you'd be re-doing the auth dance every time the dashboard rebuilds. This is exactly the kind of token-management plumbing that belongs in n8n, which you already pay for and which has built-in OAuth handling and credential storage.

So the realistic plan:

For the Perplexity dashboard you're shipping now: leave "My Performance" on mock data with the connect-accounts banner. Don't fight the API integration inside Perplexity, it's the wrong place for it.

For real insights tracking, do it in n8n: YouTube first (easy, today), Instagram second (a Saturday project), Pinterest third (optional), TikTok last or never (use TikTok's native analytics export manually instead, it's genuinely not worth the API pain for one creator). n8n stores the tokens, refreshes them on schedule, and writes the numbers somewhere your dashboard can read.

A faster shortcut worth naming: tools like Phyllo or getlate aggregate multiple platform APIs behind one connection, including the TikTok data that's otherwise a nightmare to get directly. If you want all four platforms' insights without four separate developer-portal ordeals, a creator-analytics aggregator is often the sane choice for a solo operator. Worth a look before you commit a weekend to Meta's developer portal.

Want me to map out the n8n side, which nodes pull YouTube and Instagram insights, how to store the tokens, and where to write the numbers so your dashboard reads them live? That's the piece that actually solves "track my insights" properly, separate from the Perplexity build.

## 🧑 Adriana · 2026-05-20 22:28
which of these options should i chose for the instagram ap token?

## 🤖 Claude · 2026-05-20 22:28
You're at the Meta app-creation "use case" picker. For pulling your own Instagram insights into a dashboard, the right choice is:

**"Manage messaging & content on Instagram"** (the one with the Instagram camera icon, second from the bottom). Its description says Publish posts, share stories, respond to comments, answer direct messages and more with the Instagram API. That's the Instagram Graph API use case, and it's the one that unlocks the insights/analytics endpoints (reach, impressions, profile views, follower count, engagement) for an account you own.

Don't pick these, even though they look tempting:

The four **Marketing API** options at the top are for *paid ads*. You said this is organic only, so skip all of them.

**"Authenticate and request data from users with Facebook Login"** is just the login layer. You'll actually end up using Facebook Login *as part of* the Instagram setup, but it's not the use case to start from on its own.

**"Create an app without a use case"** (very bottom) is the escape hatch. It gives you a blank app with no permissions, and then you manually add the Instagram product yourself. Some guides recommend this route because it gives you more control, but for your purpose the "Manage messaging & content on Instagram" use case is the cleaner, more guided path.

So: **Manage messaging & content on Instagram.**

One heads-up for what comes after you click it, so you're not caught off guard:

- It'll have you connect your Instagram (must be a Business or Creator account, yours is Creator, so you're good).
- When it asks for permissions, the ones you actually need for insights are `instagram_basic` and `instagram_manage_insights`. You can ignore the messaging and publishing permissions unless you want them later.
- You'll generate a token that's short-lived (about an hour) first, then exchange it for a long-lived one (about 60 days). The 60-day expiry is the reason I keep nudging you to let n8n hold and auto-refresh this token rather than pasting it into Perplexity, because in Perplexity you'd be redoing this dance every two months.

If the next screen looks confusing, screenshot it and send it over, I'll tell you exactly what to click. The Meta developer portal is genuinely the most disorienting part of this whole project, the guide you started with even warned you about it, so don't feel bad if it gets murky. We'll get through it one screen at a time.

## 🧑 Adriana · 2026-05-20 22:33
Ok in my meta key i included threads, facebook and instagram all at once

## 🤖 Claude · 2026-05-20 22:33
That's totally fine, no harm done. Including Threads, Facebook, and Instagram on one app is actually a normal setup, not a mistake. Let me explain what it means so you know where you stand.

**What having all three does**

Meta apps are containers that can hold multiple products. Adding all three just means your one app *can* talk to all three APIs if you set up the permissions for each. It doesn't break anything, doesn't slow down the Instagram piece, and doesn't cost anything. The extra two (Threads, Facebook) just sit there unused until you wire them up. Think of it like buying a tool kit with three drawers and only using one for now.

**Why it can actually help you**

Here's the upside for Motus specifically: Facebook is part of the chain whether you wanted it or not. Instagram's Graph API authenticates *through* a Facebook Page connected to your Instagram account. So having the Facebook product in there isn't clutter, it's part of how Instagram insights even work. And Threads, if Motus ever posts there, you'd already be set up to pull those insights too. So you've basically future-proofed yourself by accident. Not a bad accident.

**The one thing to watch**

The only place "too many products" causes friction is *app review*, if you ever submit this app to Meta for full Live mode. Each product/permission you request gets scrutinized, and asking for more than you use can slow approval or trigger questions. But you're not going there. For pulling your own single account's data, you stay in **development mode** and skip review entirely. In dev mode, all of this just works for you, the owner, no review needed. So the multi-product setup costs you nothing on the path you're actually taking.

**What to do next**

Don't remove anything. Leave all three. Just focus only on the Instagram piece and ignore the other two drawers for now. Your next moves:

1. Make sure your Instagram (Creator account) is connected to a Facebook Page. If it isn't, that's the one connection you do need to create, because Instagram insights route through that Page.
2. In the Instagram product settings, generate a User Access Token with the permissions `instagram_basic` and `instagram_manage_insights`.
3. Exchange the short-lived token (about 1 hour) for a long-lived one (about 60 days).
4. Test it before wiring it anywhere: paste a quick call into your browser to confirm it returns your data. Something like asking the Graph API for your account's `followers_count` and `reach`.

If you hit the screen where you generate the token, or the part about connecting the Facebook Page, screenshot it and I'll point you to the exact buttons. That token-generation screen is where most people get briefly lost because Meta buries it.

And the standing reminder, once you've got a working long-lived token: that 60-day expiry is exactly why I'd have n8n store and auto-refresh it rather than pasting it into Perplexity. Otherwise you're back on this screen every two months. But first, let's just get a token that works. Where are you in the flow right now, still on product setup, or did you reach the token screen?

## 🧑 Adriana · 2026-05-21 01:56
para el token de interest: Seleccionar entorno
Producción limitada
Sandbox?

## 🤖 Claude · 2026-05-21 01:56
Para el token de Pinterest, elige **Producción limitada** (Limited Production), no Sandbox.

Aquí está el por qué, rapidito:

**Sandbox** es un entorno de prueba con datos falsos. No te da tus números reales de Pinterest, solo data de mentira para que los desarrolladores prueben que su código funciona. Si eliges esto, tu dashboard te va a mostrar puras métricas inventadas, que es justo lo que estás tratando de evitar.

**Producción limitada** (Limited Production) sí te conecta a tu cuenta real y te devuelve tus analytics de verdad: impressions, saves, pin clicks, outbound clicks. El "limitada" se refiere a que tienes límites más bajos de llamadas a la API hasta que Pinterest apruebe tu app para producción completa, pero para una sola cuenta como la tuya, esos límites son más que suficientes. Ni los vas a tocar.

Entonces: **Producción limitada.**

Un par de cosas que te van a servir saber para los siguientes pasos:

Con Producción limitada vas a poder pedir el scope de analytics (busca algo como `user_accounts:read` y `pins:read`, y el de analytics si aparece por separado). Esos son los que te dan acceso a tus métricas.

El token de Pinterest también expira, igual que el de Instagram, así que aplica el mismo consejo: cuando lo tengas funcionando, lo ideal es que n8n lo guarde y lo refresque solo, no pegarlo directo en Perplexity donde lo vas a tener que renovar a cada rato.

Y honestamente, te lo recordé antes pero vale repetirlo ahora que estás metida en el portal de Pinterest: de las cuatro plataformas, Pinterest es la de menor prioridad para Motus a menos que Pinterest te esté mandando tráfico real. Si lo estás haciendo solo por completar el set, está bien, pero si te empiezas a frustrar, esta es la que puedes saltarte sin perder casi nada. YouTube e Instagram son las que de verdad mueven la aguja para ti.

Si llegas a la pantalla donde generas el token o donde pides los scopes y se ve confusa, mándame screenshot y te digo exactamente qué picar.
