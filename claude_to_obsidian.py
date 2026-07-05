#!/usr/bin/env python3
"""
claude_to_obsidian.py — turn a Claude.ai data export into an Obsidian vault.

Claude.ai's Project "memory" is a lossy condensed summary. The *full* chat
transcripts live in your account data export instead:

    claude.ai -> Settings -> Privacy -> Export data  (arrives by email as a .zip)

This script reads that export and writes one Markdown file per chat, grouped
into per-project folders, with YAML frontmatter Obsidian understands. Project
knowledge docs are exported too, each as its own note.

Usage:
    python3 claude_to_obsidian.py <export.zip | export_dir | conversations.json> \\
        [--out ObsidianVault] [--projects projects.json]

Examples:
    python3 claude_to_obsidian.py data-2026-07-05.zip
    python3 claude_to_obsidian.py ./unzipped-export --out ~/Obsidian/Claude
    python3 claude_to_obsidian.py conversations.json --projects projects.json

No third-party dependencies. Python 3.8+.
"""
from __future__ import annotations

import argparse
import io
import json
import os
import re
import sys
import zipfile
from datetime import datetime


# --------------------------------------------------------------------------- #
# Loading the export (zip / dir / single json — all handled the same way)
# --------------------------------------------------------------------------- #

def _load_json_bytes(raw: bytes):
    return json.loads(raw.decode("utf-8"))


def load_export(path: str, projects_override: str | None):
    """Return (conversations, projects) from whatever form the export is in."""
    conversations, projects = [], []

    if zipfile.is_zipfile(path):
        with zipfile.ZipFile(path) as zf:
            for name in zf.namelist():
                base = os.path.basename(name).lower()
                if base == "conversations.json":
                    conversations = _load_json_bytes(zf.read(name))
                elif base == "projects.json":
                    projects = _load_json_bytes(zf.read(name))
    elif os.path.isdir(path):
        conv_p = os.path.join(path, "conversations.json")
        proj_p = os.path.join(path, "projects.json")
        if os.path.exists(conv_p):
            with open(conv_p, "rb") as f:
                conversations = _load_json_bytes(f.read())
        if os.path.exists(proj_p):
            with open(proj_p, "rb") as f:
                projects = _load_json_bytes(f.read())
    elif os.path.isfile(path):
        with open(path, "rb") as f:
            data = _load_json_bytes(f.read())
        # A single json file could be either list; sniff by content.
        if _looks_like_conversations(data):
            conversations = data
        elif _looks_like_projects(data):
            projects = data
        else:
            conversations = data  # best effort
    else:
        raise FileNotFoundError(f"Not a zip, directory, or file: {path}")

    if projects_override:
        with open(projects_override, "rb") as f:
            projects = _load_json_bytes(f.read())

    return conversations, projects


def _looks_like_conversations(data) -> bool:
    return (
        isinstance(data, list)
        and data
        and isinstance(data[0], dict)
        and ("chat_messages" in data[0] or "messages" in data[0])
    )


def _looks_like_projects(data) -> bool:
    return (
        isinstance(data, list)
        and data
        and isinstance(data[0], dict)
        and "docs" in data[0]
    )


# --------------------------------------------------------------------------- #
# Small helpers
# --------------------------------------------------------------------------- #

_SLUG_RE = re.compile(r"[^\w\- ]+", re.UNICODE)
_WS_RE = re.compile(r"\s+")


def slugify(text: str, fallback: str = "untitled", maxlen: int = 80) -> str:
    text = (text or "").strip()
    text = _SLUG_RE.sub("", text)
    text = _WS_RE.sub(" ", text).strip()
    text = text.replace(" ", "-")
    text = text[:maxlen].strip("-.")
    return text or fallback


def yaml_escape(value: str) -> str:
    """Quote a scalar for YAML frontmatter."""
    value = (value or "").replace('"', '\\"').replace("\n", " ")
    return f'"{value}"'


def norm_date(value: str | None) -> str:
    """Best-effort ISO -> 'YYYY-MM-DD HH:MM' for readable frontmatter."""
    if not value:
        return ""
    try:
        cleaned = value.replace("Z", "+00:00")
        return datetime.fromisoformat(cleaned).strftime("%Y-%m-%d %H:%M")
    except Exception:
        return value


def date_only(value: str | None) -> str:
    d = norm_date(value)
    return d.split(" ")[0] if d else ""


def unique_path(directory: str, base: str, ext: str = ".md") -> str:
    """Avoid clobbering when two chats slugify to the same name."""
    candidate = os.path.join(directory, base + ext)
    n = 2
    while os.path.exists(candidate):
        candidate = os.path.join(directory, f"{base}-{n}{ext}")
        n += 1
    return candidate


# --------------------------------------------------------------------------- #
# Message rendering
# --------------------------------------------------------------------------- #

def message_text(msg: dict) -> str:
    """Pull the fullest available text out of a message record."""
    parts = []
    content = msg.get("content")
    if isinstance(content, list):
        for block in content:
            if not isinstance(block, dict):
                continue
            if block.get("type") == "text" and block.get("text"):
                parts.append(block["text"])
            elif block.get("type") == "tool_use":
                parts.append(f"*[tool use: {block.get('name', 'tool')}]*")
            elif block.get("type") == "tool_result" and block.get("content"):
                parts.append(str(block["content"]))
    if parts:
        return "\n\n".join(parts).strip()
    # Fall back to the flat `text` field.
    return (msg.get("text") or "").strip()


def render_attachments(msg: dict) -> str:
    lines = []
    for att in msg.get("attachments") or []:
        name = att.get("file_name") or att.get("filename") or "attachment"
        lines.append(f"> 📎 **Attachment:** {name}")
        extracted = att.get("extracted_content")
        if extracted:
            snippet = extracted.strip()
            lines.append("> " + snippet.replace("\n", "\n> "))
    for f in msg.get("files") or []:
        name = f.get("file_name") or f.get("filename") or "file"
        lines.append(f"> 🖼️ **File:** {name}")
    return "\n".join(lines)


def render_conversation(conv: dict, project_name: str | None) -> tuple[str, str]:
    """Return (title, markdown) for a single conversation."""
    title = conv.get("name") or "Untitled chat"
    created = conv.get("created_at")
    updated = conv.get("updated_at")
    uuid = conv.get("uuid", "")
    messages = conv.get("chat_messages") or conv.get("messages") or []

    fm = ["---"]
    fm.append(f"title: {yaml_escape(title)}")
    if project_name:
        fm.append(f"project: {yaml_escape(project_name)}")
    if created:
        fm.append(f"created: {yaml_escape(norm_date(created))}")
    if updated:
        fm.append(f"updated: {yaml_escape(norm_date(updated))}")
    if uuid:
        fm.append(f"claude_uuid: {yaml_escape(uuid)}")
    fm.append(f"message_count: {len(messages)}")
    fm.append("source: claude.ai")
    fm.append("tags: [claude, chat]")
    fm.append("---")

    body = [f"# {title}\n"]
    if project_name:
        body.append(f"> Project: **{project_name}**\n")

    for msg in messages:
        sender = (msg.get("sender") or msg.get("role") or "").lower()
        who = "🧑 You" if sender in ("human", "user") else "🤖 Claude"
        stamp = norm_date(msg.get("created_at"))
        header = f"## {who}" + (f" · {stamp}" if stamp else "")
        body.append(header)
        text = message_text(msg)
        if text:
            body.append(text)
        atts = render_attachments(msg)
        if atts:
            body.append(atts)
        body.append("")  # spacer

    return title, "\n".join(fm) + "\n\n" + "\n".join(body).rstrip() + "\n"


def render_project_doc(doc: dict, project_name: str) -> tuple[str, str]:
    filename = doc.get("filename") or doc.get("file_name") or "document"
    title = os.path.splitext(filename)[0] or filename
    content = doc.get("content") or doc.get("extracted_content") or ""
    created = doc.get("created_at")

    fm = [
        "---",
        f"title: {yaml_escape(title)}",
        f"project: {yaml_escape(project_name)}",
    ]
    if created:
        fm.append(f"created: {yaml_escape(norm_date(created))}")
    fm.append("source: claude.ai")
    fm.append("tags: [claude, project-knowledge]")
    fm.append("---")

    body = f"# {title}\n\n> Project knowledge · original file: `{filename}`\n\n{content}\n"
    return title, "\n".join(fm) + "\n\n" + body


# --------------------------------------------------------------------------- #
# Project <-> conversation linkage
# --------------------------------------------------------------------------- #

def conversation_project_uuid(conv: dict) -> str | None:
    """Exports vary; try the fields that have carried project linkage."""
    for key in ("project_uuid", "project_id"):
        if conv.get(key):
            return conv[key]
    proj = conv.get("project")
    if isinstance(proj, dict):
        return proj.get("uuid") or proj.get("id")
    if isinstance(proj, str) and proj:
        return proj
    return None


# --------------------------------------------------------------------------- #
# Main
# --------------------------------------------------------------------------- #

def main() -> int:
    ap = argparse.ArgumentParser(
        description="Convert a Claude.ai data export into an Obsidian vault "
        "(one .md per chat, grouped by project)."
    )
    ap.add_argument("input", help="export .zip, unzipped dir, or conversations.json")
    ap.add_argument("--out", default="ObsidianVault", help="output vault folder")
    ap.add_argument("--projects", help="path to projects.json (if separate)")
    ap.add_argument(
        "--unfiled-name",
        default="_Unfiled",
        help="folder for chats with no detectable project",
    )
    args = ap.parse_args()

    try:
        conversations, projects = load_export(args.input, args.projects)
    except Exception as e:
        print(f"error: could not read export: {e}", file=sys.stderr)
        return 1

    if not conversations and not projects:
        print("error: found no conversations or projects in the input.", file=sys.stderr)
        return 1

    os.makedirs(args.out, exist_ok=True)

    # Map project uuid -> (name, folder) and write knowledge docs.
    uuid_to_name: dict[str, str] = {}
    docs_written = 0
    for proj in projects:
        name = proj.get("name") or "Untitled Project"
        puid = proj.get("uuid") or proj.get("id") or ""
        if puid:
            uuid_to_name[puid] = name
        folder = os.path.join(args.out, slugify(name, "project"))
        docs = proj.get("docs") or proj.get("documents") or []
        if docs:
            kfolder = os.path.join(folder, "Project Knowledge")
            os.makedirs(kfolder, exist_ok=True)
            for doc in docs:
                title, md = render_project_doc(doc, name)
                path = unique_path(kfolder, slugify(title, "document"))
                with open(path, "w", encoding="utf-8") as f:
                    f.write(md)
                docs_written += 1

    # Write conversations, grouped by project.
    chats_written = 0
    per_project_counts: dict[str, int] = {}
    for conv in conversations:
        puid = conversation_project_uuid(conv)
        project_name = uuid_to_name.get(puid) if puid else None
        folder_name = slugify(project_name, "project") if project_name else args.unfiled_name
        folder = os.path.join(args.out, folder_name)
        os.makedirs(folder, exist_ok=True)

        title, md = render_conversation(conv, project_name)
        prefix = date_only(conv.get("created_at") or conv.get("updated_at"))
        base = slugify(title, "chat")
        if prefix:
            base = f"{prefix}-{base}"
        path = unique_path(folder, base)
        with open(path, "w", encoding="utf-8") as f:
            f.write(md)
        chats_written += 1
        per_project_counts[folder_name] = per_project_counts.get(folder_name, 0) + 1

    # Summary.
    print(f"✅ Wrote vault to: {os.path.abspath(args.out)}")
    print(f"   {chats_written} chats, {docs_written} project-knowledge docs")
    for folder_name in sorted(per_project_counts):
        print(f"   - {folder_name}: {per_project_counts[folder_name]} chats")
    if args.unfiled_name in per_project_counts and projects:
        print(
            f"\nNote: {per_project_counts[args.unfiled_name]} chats landed in "
            f"'{args.unfiled_name}'. Claude's export doesn't always tag a chat "
            "with its project, so those couldn't be auto-grouped."
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
