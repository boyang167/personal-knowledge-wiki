#!/usr/bin/env python3
"""Build wiki/INDEX.llm.md from wiki frontmatter (stdlib only)."""

from __future__ import annotations

import argparse
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "wiki"
OUTPUT = WIKI / "INDEX.llm.md"

SKIP_DIR_NAMES = {"_meta", "_templates"}
SKIP_FILES = {"README.md", "MOC.md", "INDEX.llm.md"}


def parse_frontmatter(text: str) -> dict[str, object]:
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    block = text[3:end].strip()
    data: dict[str, object] = {}
    key: str | None = None
    list_mode = False
    list_items: list[str] = []

    def flush_list() -> None:
        nonlocal list_mode, list_items, key
        if key is not None and list_mode:
            data[key] = list_items
        list_mode = False
        list_items = []

    for line in block.splitlines():
        if re.match(r"^\s*-\s+", line) and key is not None and list_mode:
            list_items.append(re.sub(r"^\s*-\s+", "", line).strip())
            continue
        flush_list()
        m = re.match(r"^(\w+):\s*(.*)$", line)
        if not m:
            continue
        key = m.group(1)
        val = m.group(2).strip()
        if val == "" or val == "[]":
            list_mode = True
            list_items = []
            continue
        if val.startswith("[") and val.endswith("]"):
            inner = val[1:-1].strip()
            if not inner:
                data[key] = []
            else:
                data[key] = [x.strip().strip("'\"") for x in inner.split(",")]
            key = None
            continue
        data[key] = val.strip("'\"")
        key = None
    flush_list()
    return data


def collect_pages() -> list[tuple[Path, dict[str, object]]]:
    pages: list[tuple[Path, dict[str, object]]] = []
    for path in sorted(WIKI.rglob("*.md")):
        if path.name in SKIP_FILES:
            continue
        if any(part in SKIP_DIR_NAMES for part in path.parts):
            continue
        rel = path.relative_to(WIKI)
        text = path.read_text(encoding="utf-8", errors="replace")
        meta = parse_frontmatter(text)
        pages.append((rel, meta))
    return pages


def fmt_tags(meta: dict[str, object]) -> str:
    tags = meta.get("tags", [])
    if isinstance(tags, list):
        return ", ".join(str(t) for t in tags)
    return str(tags) if tags else ""


def build_markdown(pages: list[tuple[Path, dict[str, object]]]) -> str:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    lines = [
        "# Wiki LLM Index",
        "",
        f"自动生成，请勿手改。运行 `python scripts/build_llm_index.py` 更新。",
        "",
        f"**Generated:** {now}",
        "",
        "Agent 用法：先读本表定位路径，再打开对应 markdown 全文。",
        "",
        "| path | title | status | summary | tags |",
        "|------|-------|--------|---------|------|",
    ]
    for rel, meta in pages:
        title = str(meta.get("title", rel.stem))
        status = str(meta.get("status", "—"))
        summary = str(meta.get("summary", "")).replace("|", "\\|")
        tags = fmt_tags(meta).replace("|", "\\|")
        lines.append(f"| {rel.as_posix()} | {title} | {status} | {summary} | {tags} |")
    lines.append("")
    lines.append(f"**Total pages:** {len(pages)}")
    lines.append("")
    return "\n".join(lines)


def raw_stats() -> str:
    raw_root = ROOT / "raw" / "2-StudyMaterials"
    if not raw_root.is_dir():
        return ""
    lines = ["## raw/2-StudyMaterials 概览", ""]
    for child in sorted(raw_root.iterdir()):
        if not child.is_dir():
            continue
        md_count = sum(1 for _ in child.rglob("*.md"))
        pdf_count = sum(1 for _ in child.rglob("*.pdf"))
        lines.append(f"- `{child.name}`: {md_count} md, {pdf_count} pdf")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Build wiki/INDEX.llm.md")
    parser.add_argument(
        "--with-raw-stats",
        action="store_true",
        help="Append raw category file counts to INDEX.llm.md",
    )
    args = parser.parse_args()

    pages = collect_pages()
    body = build_markdown(pages)
    if args.with_raw_stats:
        body += "\n" + raw_stats()
    OUTPUT.write_text(body, encoding="utf-8")
    print(f"Wrote {OUTPUT.relative_to(ROOT)} ({len(pages)} pages)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
