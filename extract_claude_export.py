#!/usr/bin/env python3
"""
extract_claude_export.py — turn a Claude.ai data export into the Obsidian brain.

Handles the newer export layout:
    export/
      conversations.json          (list; chats have no project link)
      projects/<uuid>.json         (one file per project, with .docs)
      memories.json                (condensed per-project + account memory)

Writes, filtered to Adriana's in-scope areas only:
  <out>/From Claude/Project Knowledge/<Project>/<doc>.md   (durable project docs)
  <out>/From Claude/Condensed Memory/<Project>.md          (the summary layer)
  <out>/From Claude/Chat Archive/In-scope/<date-title>.md  (one md per chat)
  <out>/From Claude/Chat Archive/Review/<date-title>.md     (uncertain -> for review)
  <out>/From Claude/_Extraction Report.md                   (counts + what was excluded)

Excluded businesses (Ricos Açaí, Celestina, Sparked Reactions, Bulk HVAC and their
clients) are walled off: their project docs/memories are skipped, and any chat that
mentions them is left out of the brain and only listed by title in the report.

Usage: python3 extract_claude_export.py <export_dir> --out obsidian-brain
"""
from __future__ import annotations
import argparse, json, os, re, sys
from datetime import datetime

# ---- project scope by uuid (from the export's project names) ----------------
EXCLUDED_PROJECTS = {
    "019a5b3d-b768-732a-918b-b65f79bdbd40",  # @celestinajewels
    "019de1cd-717b-700c-b890-a0d9f1bec0c0",  # Celestina Advetising Ideation
    "019efa23-55a9-7372-b0cd-f6af08799928",  # Ricos Acai
    "019def06-0420-71be-978d-61ef8e05e8c1",  # @sparkedreactions
    "019dfea5-fe57-7290-8431-de7ca4bf10b9",  # @bulkhvac
    "019d4084-5d50-710d-91fb-fe6b66a65866",  # Remodeling Company (agency client)
}

# ---- content-based chat classification --------------------------------------
# Strong business identities -> exclude outright (honor "nothing related to these").
EXCLUDE_TERMS = [
    "celestina", "ricos", "rico's", "rico’s", "acai", "açaí", "açai", "acaí",
    "sparked reaction", "sparkedreactions", "bulkhvac", "bulk hvac", " hvac",
    "bulk buyer", "remodel", "doga", "together design", "jewel", "joyer",
    "anillo", "silver ring", "aretes", "collar",
]
INCLUDE_TERMS = [
    "adrianavmarquez", "adriana", "creatividad", "creativity2", "creador de contenido",
    "content creator", "reel", "tiktok", "instagram", "hook", "guion", "guión",
    "caption", "asesor", "consulting", "assesment", "assessment", "motion",
    "copywrit", "advertis", "pinterest", "youtube", "personal brand", "thumbnail",
    "ugc", "pitch", "brand deal", "colabora",
]

SLUG_RE = re.compile(r"[^\w\- ]+", re.UNICODE)
WS_RE = re.compile(r"\s+")


def slugify(text, fallback="untitled", maxlen=70):
    text = SLUG_RE.sub("", (text or "").strip())
    text = WS_RE.sub(" ", text).strip().replace(" ", "-")[:maxlen].strip("-.")
    return text or fallback


def yesc(v):
    return '"' + (v or "").replace('"', "'").replace("\n", " ") + '"'


def norm_date(v):
    if not v:
        return ""
    try:
        return datetime.fromisoformat(v.replace("Z", "+00:00")).strftime("%Y-%m-%d %H:%M")
    except Exception:
        return v


def date_only(v):
    d = norm_date(v)
    return d.split(" ")[0] if d else ""


def unique(path_dir, base, ext=".md"):
    cand = os.path.join(path_dir, base + ext)
    n = 2
    while os.path.exists(cand):
        cand = os.path.join(path_dir, f"{base}-{n}{ext}")
        n += 1
    return cand


def msg_text(m):
    parts = []
    for b in (m.get("content") or []):
        if isinstance(b, dict) and b.get("type") == "text" and b.get("text"):
            parts.append(b["text"])
    return ("\n\n".join(parts) or (m.get("text") or "")).strip()


def chat_blob(c):
    t = (c.get("name") or "") + " \n " + (c.get("summary") or "")
    for m in (c.get("chat_messages") or [])[:3]:
        t += " " + (m.get("text") or "")[:500]
    return t.lower()


def classify(c):
    b = chat_blob(c)
    ex = any(k in b for k in EXCLUDE_TERMS)
    inc = any(k in b for k in INCLUDE_TERMS)
    if ex:
        return "EXCLUDED"        # any excluded-business mention -> out of the brain
    if inc:
        return "IN"
    return "REVIEW"              # untitled / ambiguous -> quarantine for user review


def render_chat(c):
    title = c.get("name") or "Untitled chat"
    msgs = c.get("chat_messages") or []
    fm = ["---", f"title: {yesc(title)}", "source: claude.ai-chat"]
    if c.get("created_at"):
        fm.append(f"created: {yesc(norm_date(c['created_at']))}")
    if c.get("summary"):
        fm.append(f"summary: {yesc(c['summary'])}")
    fm += [f"messages: {len(msgs)}", f"claude_uuid: {yesc(c.get('uuid',''))}",
           "tags: [claude, chat, archive]", "---", ""]
    body = [f"# {title}", ""]
    if c.get("summary"):
        body += [f"> {c['summary']}", ""]
    for m in msgs:
        who = "🧑 Adriana" if (m.get("sender") or "").lower() in ("human", "user") else "🤖 Claude"
        stamp = norm_date(m.get("created_at"))
        body.append(f"## {who}" + (f" · {stamp}" if stamp else ""))
        txt = msg_text(m)
        if txt:
            body.append(txt)
        for a in (m.get("attachments") or []):
            body.append(f"> 📎 {a.get('file_name','attachment')}")
        body.append("")
    return title, "\n".join(fm) + "\n".join(body).rstrip() + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("export")
    ap.add_argument("--out", default="obsidian-brain")
    args = ap.parse_args()

    root = os.path.join(args.out, "From Claude")
    pk_dir = os.path.join(root, "Project Knowledge")
    mem_dir = os.path.join(root, "Condensed Memory")
    in_dir = os.path.join(root, "Chat Archive", "In-scope")
    rev_dir = os.path.join(root, "Chat Archive", "Review")
    for d in (pk_dir, mem_dir, in_dir, rev_dir):
        os.makedirs(d, exist_ok=True)

    report = {"projects_in": [], "projects_excluded": [], "docs": 0, "memories": 0,
              "chat_in": 0, "chat_review": 0, "chat_excluded": []}

    # ---- projects: names + docs ----
    uuid_name = {}
    pdir = os.path.join(args.export, "projects")
    for fn in sorted(os.listdir(pdir)):
        p = json.load(open(os.path.join(pdir, fn)))
        if not isinstance(p, dict):
            continue
        uuid = p.get("uuid") or fn.replace(".json", "")
        name = p.get("name") or "Untitled Project"
        uuid_name[uuid] = name
        if uuid in EXCLUDED_PROJECTS:
            report["projects_excluded"].append(name)
            continue
        report["projects_in"].append(name)
        docs = p.get("docs") or []
        real = [d for d in docs if (d.get("content") or "").strip()]
        if real:
            folder = os.path.join(pk_dir, slugify(name, "project"))
            os.makedirs(folder, exist_ok=True)
            for d in real:
                fnm = d.get("filename") or d.get("file_name") or "document"
                title = os.path.splitext(fnm)[0] or fnm
                md = (f"---\ntitle: {yesc(title)}\nproject: {yesc(name)}\n"
                      f"source: claude.ai-project-knowledge\ntags: [claude, project-knowledge]\n---\n\n"
                      f"# {title}\n\n> Project knowledge · `{fnm}`\n\n{d.get('content','')}\n")
                with open(unique(folder, slugify(title, "doc")), "w", encoding="utf-8") as f:
                    f.write(md)
                report["docs"] += 1

    # ---- memories (per-project condensed) ----
    mpath = os.path.join(args.export, "memories.json")
    if os.path.exists(mpath):
        mem = json.load(open(mpath))
        m0 = mem[0] if isinstance(mem, list) and mem else mem
        pm = (m0 or {}).get("project_memories") or {}
        if isinstance(pm, dict):
            for uuid, text in pm.items():
                if uuid in EXCLUDED_PROJECTS or not text:
                    continue
                name = uuid_name.get(uuid, uuid)
                md = (f"---\ntitle: {yesc(name + ' — Condensed Memory')}\nproject: {yesc(name)}\n"
                      f"source: claude.ai-memory\ntags: [claude, condensed-memory]\n---\n\n"
                      f"# {name} — Condensed Memory\n\n"
                      f"> Claude's auto-condensed memory for this project. The full chats live in "
                      f"`Chat Archive/`; this is the summary layer.\n\n{text}\n")
                with open(unique(mem_dir, slugify(name, "project")), "w", encoding="utf-8") as f:
                    f.write(md)
                report["memories"] += 1
        acct = (m0 or {}).get("conversations_memory")
        if acct:
            with open(os.path.join(mem_dir, "_Account-wide Memory.md"), "w", encoding="utf-8") as f:
                f.write(f"---\ntitle: \"Account-wide Memory\"\nsource: claude.ai-memory\n"
                        f"tags: [claude, condensed-memory]\n---\n\n# Account-wide Memory\n\n{acct}\n")
            report["memories"] += 1

    # ---- conversations ----
    conv = json.load(open(os.path.join(args.export, "conversations.json")))
    for c in conv:
        k = classify(c)
        if k == "EXCLUDED":
            report["chat_excluded"].append(c.get("name") or "(untitled)")
            continue
        title, md = render_chat(c)
        prefix = date_only(c.get("created_at"))
        base = (f"{prefix}-" if prefix else "") + slugify(title, "chat")
        folder = in_dir if k == "IN" else rev_dir
        with open(unique(folder, base), "w", encoding="utf-8") as f:
            f.write(md)
        report["chat_in" if k == "IN" else "chat_review"] += 1

    # ---- report ----
    lines = ["---", "title: Extraction Report", "tags: [claude, report]", "---", "",
             "# From Claude — Extraction Report", "",
             f"- Project knowledge docs written: **{report['docs']}**",
             f"- Condensed memory notes: **{report['memories']}**",
             f"- Chats → In-scope: **{report['chat_in']}**",
             f"- Chats → Review (ambiguous/untitled): **{report['chat_review']}**",
             f"- Chats excluded (mention excluded businesses): **{len(report['chat_excluded'])}**", "",
             "## In-scope projects mined", ""]
    lines += [f"- {n}" for n in sorted(set(report["projects_in"])) if n.strip()]
    lines += ["", "## Excluded projects (walled off)", ""]
    lines += [f"- {n}" for n in sorted(set(report["projects_excluded"]))]
    lines += ["", "## Excluded chats (left out — titles only, for transparency)", ""]
    lines += [f"- {t}" for t in report["chat_excluded"]]
    with open(os.path.join(root, "_Extraction Report.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

    print(json.dumps({k: (v if not isinstance(v, list) else len(v)) for k, v in report.items()}, indent=2))


if __name__ == "__main__":
    main()
