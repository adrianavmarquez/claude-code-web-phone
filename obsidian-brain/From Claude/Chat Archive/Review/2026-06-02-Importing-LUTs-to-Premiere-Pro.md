---
title: "Importing LUTs to Premiere Pro"
source: claude.ai-chat
created: "2026-06-02 21:48"
summary: "**Conversation Overview**  The person asked for instructions on how to import LUTs (Look Up Tables) into Adobe Premiere Pro. Claude provided a comprehensive walkthrough covering two main methods: applying LUTs per-clip via the Lumetri Color panel, and installing LUTs permanently into Premiere's system folders so they appear in dropdown menus without browsing. Claude explained the distinction between the Input LUT option (under Basic Correction, suited for technical/log-conversion LUTs) and the Look option (under Creative, suited for stylistic LUTs), noting that the Creative section includes an Intensity slider for blending control. File path locations for both Windows and Mac were provided, along with a note about accessing Mac app package contents. Claude also covered workflow efficiency tips including using Paste Attributes to apply a LUT across multiple clips and using adjustment layers. Claude closed by asking whether the person was working with a creative look or a log conversion LUT to potentially tailor the workflow further, though the person did not respond with additional detail."
messages: 2
claude_uuid: "7d7ea5b6-1165-4561-b9e8-a15897c97b3d"
tags: [claude, chat, archive]
---
# Importing LUTs to Premiere Pro

> **Conversation Overview**

The person asked for instructions on how to import LUTs (Look Up Tables) into Adobe Premiere Pro. Claude provided a comprehensive walkthrough covering two main methods: applying LUTs per-clip via the Lumetri Color panel, and installing LUTs permanently into Premiere's system folders so they appear in dropdown menus without browsing. Claude explained the distinction between the Input LUT option (under Basic Correction, suited for technical/log-conversion LUTs) and the Look option (under Creative, suited for stylistic LUTs), noting that the Creative section includes an Intensity slider for blending control. File path locations for both Windows and Mac were provided, along with a note about accessing Mac app package contents. Claude also covered workflow efficiency tips including using Paste Attributes to apply a LUT across multiple clips and using adjustment layers. Claude closed by asking whether the person was working with a creative look or a log conversion LUT to potentially tailor the workflow further, though the person did not respond with additional detail.

## 🧑 Adriana · 2026-06-02 21:48
HOW DO I IMPORT LUTS TO PREMIERE PRO?

## 🤖 Claude · 2026-06-02 21:48
Importing LUTs into Premiere Pro is straightforward. Here's how:

**The quick method (per-clip):**

1. Select your clip in the timeline
2. Open the **Lumetri Color** panel (Window → Lumetri Color)
3. Expand the **Basic Correction** section and use the **Input LUT** dropdown, or scroll down to the **Creative** section and use the **Look** dropdown
4. Click the dropdown and choose **Browse...**
5. Navigate to your `.cube` or `.3dl` file and select it

The difference between the two: use **Input LUT** (Basic Correction) for technical/conversion LUTs like Log-to-Rec709 corrections, and use **Look** (Creative) for stylistic/creative LUTs.

**To make LUTs permanently available in the dropdown menu:**

If you want your LUTs to show up in the dropdown list instead of browsing every time, drop them into Premiere's LUT folders:

- **Windows:** `C:\Program Files\Adobe\Adobe Premiere Pro [version]\Lumetri\LUTs\Creative` (or `\Technical`)
- **Mac:** `/Applications/Adobe Premiere Pro [version]/Contents/Lumetri/LUTs/Creative`

On Mac you may need to right-click the app → Show Package Contents to reach that folder. After dropping the files in, restart Premiere and they'll appear in the Input LUT / Look dropdowns by name.

**A couple of tips:**

- The **Creative → Look** section has an **Intensity** slider so you can dial the strength of a creative LUT up or down. Input LUTs don't have this, so apply creative LUTs through the Look dropdown if you want that control.
- To apply one LUT across many clips, apply it to one clip, then copy the clip (Ctrl/Cmd+C) and use **Paste Attributes** (Ctrl/Cmd+Alt/Opt+V) on the others. Or use an adjustment layer above your footage.

Which type of LUT are you working with — a creative look or a log conversion? I can tailor the workflow if you let me know.
