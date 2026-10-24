#!/usr/bin/env python3
"""Detect new raw files, update wiki stubs, refresh the index, then commit and push.

Already-seen files live in wiki/_meta/ingest-ledger.json. The first run without a
ledger records the current tree as a baseline and does not rewrite wiki pages.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
from datetime import date, datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "raw"
LEDGER_PATH = ROOT / "wiki" / "_meta" / "ingest-ledger.json"
MOC_PATH = ROOT / "wiki" / "MOC.md"
LOCK_PATH = ROOT / ".git" / "ingest.lock"

TEXT_EXT = {".md", ".txt", ".rst", ".csv"}
SKIP_DIR_NAMES = {".git"}

TOPIC_BY_PREFIX = (
    ("2-StudyMaterials/1-Biological", "biological", "生物 / 生信", "biological"),
    ("2-StudyMaterials/2-MachineLearning", "ml", "机器学习", "ml"),
    ("2-StudyMaterials/3-ReinforcementLearning", "ml", "机器学习", "ml"),
    ("2-StudyMaterials/4-DeepLearning", "ml", "机器学习", "ml"),
    ("2-StudyMaterials/5-Infrastructure", "infrastructure", "基础设施", "infrastructure"),
    ("2-StudyMaterials/6-Database", "database", "数据库", "database"),
    ("2-StudyMaterials/7-BigData", "big-data", "大数据", "big-data"),
    ("2-StudyMaterials/8-ProgramerLanguage", "programming", "编程语言", "programming"),
    ("2-StudyMaterials/9-Tech", "tech", "技术杂项", "tech"),
    ("2-StudyMaterials/10-KG", "kg", "知识图谱", "kg"),
    ("2-StudyMaterials/11-OpneSource", "opensource", "开源", "opensource"),
)

MOC_HEADING = {
    "biological": "## 生物 / 生信",
    "ml": "## 机器学习",
    "infrastructure": "## 基础设施",
    "database": "## 数据库",
    "big-data": "## 大数据",
    "programming": "## 编程语言",
    "tech": "## 技术杂项",
    "opensource": "## 开源",
    "kg": "## 知识图谱",
}

SECRET_PATTERNS = (
    re.compile(r"-----BEGIN (?:RSA |OPENSSH |EC |DSA )?PRIVATE KEY-----"),
    re.compile(
        r"(?i)\b(?:api[_-]?key|secret|access[_-]?token|password|passwd)\b\s*[:=]\s*['\"]?[A-Za-z0-9_\-+/=]{8,}"
    ),
    re.compile(r"密码\s*[:：]\s*[`'\" ]*[^\s`'\"，。,\n]{4,}"),
    re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    re.compile(r"(?i)\bBearer\s+[A-Za-z0-9\-._~+/]{20,}={0,2}"),
)


def rel_posix(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def run_git(args: list[str], check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args],
        cwd=ROOT,
        check=check,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )


def ignored_paths(paths: list[str]) -> set[str]:
    ignored: set[str] = set()
    for start in range(0, len(paths), 200):
        chunk = paths[start : start + 200]
        proc = subprocess.run(
            ["git", "check-ignore", "-z", "--stdin"],
            cwd=ROOT,
            input="\0".join(chunk) + "\0",
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
        )
        ignored.update(part for part in proc.stdout.split("\0") if part)
    return ignored


def iter_raw_files() -> list[Path]:
    found: list[Path] = []
    for dirpath, dirnames, filenames in os.walk(RAW):
        dirnames[:] = [name for name in dirnames if name not in SKIP_DIR_NAMES]
        current = Path(dirpath)
        rel_dirs = [rel_posix(current / name) for name in dirnames]
        if rel_dirs:
            skipped = ignored_paths(rel_dirs)
            dirnames[:] = [
                name for name in dirnames if rel_posix(current / name) not in skipped
            ]
        for name in filenames:
            found.append(current / name)
    if not found:
        return []
    skip_files = ignored_paths([rel_posix(path) for path in found])
    return [path for path in found if rel_posix(path) not in skip_files]


def file_record(path: Path) -> dict[str, object]:
    stat = path.stat()
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return {
        "sha256": digest.hexdigest(),
        "bytes": stat.st_size,
        "mtime_ns": stat.st_mtime_ns,
        "processed_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }


def yaml_quote(value: str) -> str:
    cleaned = value.replace("\n", " ").replace('"', "'")
    return f'"{cleaned}"'


def load_ledger() -> dict[str, object]:
    if not LEDGER_PATH.exists():
        return {"version": 1, "files": {}}
    data = json.loads(LEDGER_PATH.read_text(encoding="utf-8"))
    data.setdefault("version", 1)
    data.setdefault("files", {})
    return data


def save_ledger(ledger: dict[str, object]) -> None:
    LEDGER_PATH.parent.mkdir(parents=True, exist_ok=True)
    LEDGER_PATH.write_text(
        json.dumps(ledger, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def topic_for(rel: str) -> tuple[str, str, str] | None:
    marker = "raw/"
    suffix = rel[len(marker) :] if rel.startswith(marker) else rel
    for prefix, folder, heading, tag in TOPIC_BY_PREFIX:
        if suffix.startswith(prefix + "/") or suffix == prefix:
            return folder, heading, tag
    return None


def looks_secret(path: Path) -> bool:
    if path.suffix.lower() not in TEXT_EXT | {".json", ".yml", ".yaml", ".env", ".ini", ".toml", ".py"}:
        return False
    try:
        text = path.read_text(encoding="utf-8", errors="replace")[:262144]
    except OSError:
        return False
    return any(pattern.search(text) for pattern in SECRET_PATTERNS)


def slug_for(path: Path) -> str:
    stem = path.stem.lower()
    ascii_slug = re.sub(r"[^a-z0-9]+", "-", stem).strip("-")
    if len(ascii_slug) >= 3:
        return ascii_slug[:80]
    digest = hashlib.sha256(rel_posix(path).encode("utf-8")).hexdigest()[:8]
    return f"note-{digest}"


def wiki_mentions(rel: str) -> bool:
    needle = rel.replace("\\", "/")
    for page in (ROOT / "wiki").rglob("*.md"):
        if "_meta" in page.parts or "_templates" in page.parts:
            continue
        try:
            if needle in page.read_text(encoding="utf-8", errors="replace"):
                return True
        except OSError:
            continue
    return False


def strip_markup(text: str) -> str:
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)
    return re.sub(r"\s+", " ", text).strip()


def excerpt_markdown(path: Path) -> tuple[str, str, list[str], list[str]]:
    raw = path.read_text(encoding="utf-8", errors="replace").lstrip("\ufeff")[:12000]
    title = path.stem
    headings: list[str] = []
    bullets: list[str] = []
    summary = ""
    for line in raw.splitlines():
        stripped = line.strip().lstrip("\ufeff")
        if stripped.startswith("#"):
            heading = strip_markup(stripped.lstrip("#").strip())
            if heading and title == path.stem:
                title = heading
            if heading:
                headings.append(heading)
            continue
        if not stripped or stripped.startswith(("|", "!", "```", "<!--")):
            continue
        if stripped[0] in "-*•":
            content = strip_markup(stripped.lstrip("-*• ").strip())
            if len(content) >= 4 and len(bullets) < 6:
                bullets.append(content[:180])
            continue
        plain = strip_markup(stripped)
        if len(plain) < 12:
            continue
        if not summary:
            summary = plain[:120]
    if not summary:
        summary = f"自动摘录 {path.name} 的要点，尚未对照全文复核"
    return title[:80], summary, headings[:12], bullets


def ensure_moc_link(folder: str, title: str, page_rel: str) -> None:
    heading = MOC_HEADING[folder]
    text = MOC_PATH.read_text(encoding="utf-8")
    safe_title = title.replace("[", "").replace("]", "")
    link = f"- [{safe_title}](./{page_rel})"
    if f"](./{page_rel})" in text:
        return
    start = text.find(heading)
    if start < 0:
        text = text.rstrip() + f"\n\n{heading}\n\n{link}\n"
        MOC_PATH.write_text(text, encoding="utf-8")
        return
    next_heading = text.find("\n## ", start + len(heading))
    if next_heading < 0:
        updated = text.rstrip() + f"\n{link}\n"
    else:
        block = text[start:next_heading].rstrip()
        updated = text[:start] + block + f"\n{link}\n" + text[next_heading:]
    MOC_PATH.write_text(updated, encoding="utf-8")


def write_text_page(path: Path, folder: str, tag: str) -> Path | None:
    rel = rel_posix(path)
    if wiki_mentions(rel):
        return None
    title, summary, headings, bullets = excerpt_markdown(path)
    slug = slug_for(path)
    dest = ROOT / "wiki" / folder / f"{slug}.md"
    if dest.exists():
        dest = ROOT / "wiki" / folder / f"{slug}-{hashlib.sha256(rel.encode()).hexdigest()[:6]}.md"
    heading_lines = "\n".join(f"- {item}" for item in headings) or "- （原文没有清晰标题）"
    bullet_lines = "\n".join(f"- {item}" for item in bullets) or "- （没有可直接摘出的短句）"
    today = date.today().isoformat()
    body = f"""---
title: {yaml_quote(title)}
summary: {yaml_quote(summary)}
tags: [{tag}, ingest]
status: draft
ingest: auto
updated: {today}
sources:
  - path: {rel}
    note: 自动摘录标题、小节和少量原句，未对照全文复核
---

# {title}

## 结论摘要

- 本页由 raw 监视流程自动生成，只保留标题、小节名和少量短句。
- 关键结论在人工复核前保持 `draft`。

## 原文结构

{heading_lines}

## 摘录

{bullet_lines}

## 待核实

- 自动摘录，未对照全文复核。

## 相关

- [MOC](../MOC.md)
"""
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(body, encoding="utf-8")
    ensure_moc_link(folder, title, dest.relative_to(ROOT / "wiki").as_posix())
    return dest


def catalog_path(folder: str) -> Path:
    return ROOT / "wiki" / folder / "incoming-sources.md"


def write_catalog_entry(path: Path, folder: str, heading: str, tag: str) -> Path:
    rel = rel_posix(path)
    dest = catalog_path(folder)
    today = date.today().isoformat()
    row = f"| `{rel}` | {path.suffix.lower().lstrip('.') or 'file'} | {today} |"
    if dest.exists():
        text = dest.read_text(encoding="utf-8")
        if f"`{rel}`" in text:
            return dest
        if "## 相关" in text:
            text = text.replace("## 相关", f"{row}\n\n## 相关", 1)
        else:
            text = text.rstrip() + "\n" + row + "\n"
        if f"path: {rel}" not in text:
            text = text.replace(
                "sources:\n",
                f"sources:\n  - path: {rel}\n    note: 自动收录，仅登记路径\n",
                1,
            )
        dest.write_text(text, encoding="utf-8")
        return dest
    title = f"自动收录资料（{heading}）"
    body = f"""---
title: {title}
summary: 监视 raw 时自动登记、尚未提炼正文的新文件
tags: [{tag}, ingest]
status: draft
ingest: auto
updated: {today}
sources:
  - path: {rel}
    note: 自动收录，仅登记路径
---

# {title}

## 结论摘要

- 本页只登记新落入 raw 的非文本文件，不转写正文。
- Markdown 会另建自动摘录页。

## 文件

| 路径 | 类型 | 收录时间 |
|------|------|----------|
{row}

## 待核实

- 自动登记，未阅读正文。

## 相关

- [MOC](../MOC.md)
"""
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(body, encoding="utf-8")
    ensure_moc_link(folder, title, dest.relative_to(ROOT / "wiki").as_posix())
    return dest


def pid_alive(pid: int) -> bool:
    if pid <= 0:
        return False
    if os.name == "nt":
        import ctypes

        handle = ctypes.windll.kernel32.OpenProcess(0x1000, False, pid)
        if handle:
            ctypes.windll.kernel32.CloseHandle(handle)
            return True
        return False
    try:
        os.kill(pid, 0)
    except OSError:
        return False
    return True


def acquire_lock() -> None:
    LOCK_PATH.parent.mkdir(parents=True, exist_ok=True)
    if LOCK_PATH.exists():
        try:
            pid = int(LOCK_PATH.read_text(encoding="utf-8").strip() or "0")
        except ValueError:
            pid = 0
        if pid_alive(pid):
            print(f"另一轮收录仍在进行（pid {pid}），本次跳过。")
            raise SystemExit(0)
        LOCK_PATH.unlink(missing_ok=True)
    LOCK_PATH.write_text(str(os.getpid()), encoding="utf-8")


def release_lock() -> None:
    try:
        if LOCK_PATH.exists() and LOCK_PATH.read_text(encoding="utf-8").strip() == str(os.getpid()):
            LOCK_PATH.unlink(missing_ok=True)
    except OSError:
        pass


def commit_paths(paths: list[Path], message: str) -> bool:
    existing = [rel_posix(path) for path in paths if path.exists()]
    if not existing:
        return False
    run_git(["add", "--", *existing])
    staged = run_git(["diff", "--cached", "--quiet"], check=False)
    if staged.returncode == 0:
        return False
    msg_file = ROOT / ".git" / "INGEST_COMMIT_MSG"
    msg_file.write_text(message.strip() + "\n", encoding="utf-8")
    result = run_git(["commit", "-F", str(msg_file)], check=False)
    if result.returncode != 0 and "trailer" in (result.stderr + result.stdout):
        git_exe = Path(run_git(["--exec-path"]).stdout.strip())
        tree = run_git(["write-tree"]).stdout.strip()
        parent = run_git(["rev-parse", "HEAD"]).stdout.strip()
        commit = subprocess.run(
            [str(git_exe / "git-commit-tree.exe"), tree, "-p", parent, "-F", str(msg_file)],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
        ).stdout.strip()
        subprocess.run(
            [str(git_exe / "git-update-ref.exe"), "HEAD", commit],
            cwd=ROOT,
            check=True,
        )
    elif result.returncode != 0:
        print(result.stderr or result.stdout, file=sys.stderr)
        raise SystemExit(result.returncode)
    msg_file.unlink(missing_ok=True)
    return True


def new_files(ledger: dict[str, object]) -> list[Path]:
    known: dict[str, object] = ledger["files"]  # type: ignore[assignment]
    fresh: list[Path] = []
    for path in iter_raw_files():
        rel = rel_posix(path)
        record = known.get(rel)
        stat = path.stat()
        if (
            isinstance(record, dict)
            and record.get("bytes") == stat.st_size
            and record.get("mtime_ns") == stat.st_mtime_ns
        ):
            continue
        current = file_record(path)
        if isinstance(record, dict) and record.get("sha256") == current["sha256"]:
            record["mtime_ns"] = current["mtime_ns"]
            record["bytes"] = current["bytes"]
            continue
        fresh.append(path)
    return fresh


def init_ledger() -> int:
    files = iter_raw_files()
    ledger = {
        "version": 1,
        "files": {rel_posix(path): file_record(path) for path in files},
    }
    save_ledger(ledger)
    print(f"已记录基线 {len(files)} 个文件，没有改写 wiki。")
    return 0


def process(dry_run: bool, do_commit: bool, do_push: bool) -> int:
    if not LEDGER_PATH.exists():
        print("还没有收录基线，先记录当前 raw，不处理为新资料。")
        return init_ledger()
    ledger = load_ledger()
    fresh = new_files(ledger)
    if not fresh:
        print("没有新的 raw 文件。")
        return 0
    secret = [path for path in fresh if looks_secret(path)]
    if secret:
        print("发现疑似口令或密钥，已停止。这些文件不会写入 wiki，也不会提交：", file=sys.stderr)
        for path in secret:
            print(f"  {rel_posix(path)}", file=sys.stderr)
        return 2
    written: list[Path] = []
    for path in fresh:
        topic = topic_for(rel_posix(path)) or ("tech", "技术杂项", "tech")
        folder, heading, tag = topic
        if dry_run:
            kind = "摘录" if path.suffix.lower() in TEXT_EXT else "登记"
            print(f"{kind} {rel_posix(path)} -> wiki/{folder}/")
            continue
        if path.suffix.lower() in TEXT_EXT:
            page = write_text_page(path, folder, tag)
        else:
            page = write_catalog_entry(path, folder, heading, tag)
        if page is not None:
            written.append(page)
        files = ledger["files"]
        assert isinstance(files, dict)
        files[rel_posix(path)] = file_record(path)
    if dry_run:
        print(f"将处理 {len(fresh)} 个文件。")
        return 0
    save_ledger(ledger)
    written.extend([LEDGER_PATH, MOC_PATH])
    subprocess.run([sys.executable, str(ROOT / "scripts" / "build_llm_index.py")], cwd=ROOT, check=True)
    written.append(ROOT / "wiki" / "INDEX.llm.md")
    if not do_commit:
        print(f"已更新 wiki，未提交。新文件 {len(fresh)} 个。")
        return 0
    message = f"收录 raw 新增资料并更新 wiki。\n\n自动处理 {len(fresh)} 个新文件。"
    raw_paths = [path for path in fresh if topic_for(rel_posix(path)) is not None]
    if not commit_paths([*raw_paths, *written], message):
        print("没有需要提交的变更。")
        return 0
    print("已提交。")
    if do_push:
        run_git(["push", "origin", "master:main"])
        print("已推送到 origin/main。")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Ingest new raw files into the wiki")
    parser.add_argument("--init-ledger", action="store_true", help="Record the current raw tree and stop")
    parser.add_argument("--dry-run", action="store_true", help="Print actions without writing")
    parser.add_argument("--commit", action="store_true", help="Commit wiki, ledger, and new raw files")
    parser.add_argument("--push", action="store_true", help="Push master to origin/main after commit")
    args = parser.parse_args()
    acquire_lock()
    try:
        if args.init_ledger:
            return init_ledger()
        return process(args.dry_run, args.commit, args.push)
    finally:
        release_lock()


if __name__ == "__main__":
    sys.exit(main())
