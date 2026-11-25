"""合并各卡 log.md 的文件表，生成 docs/plan/file-map.md。

修 bug 的顺序：先在 file-map.md 查文件 -> 拿到卡号 -> 读那张卡的 spec.md。
本表是生成的，不要手改；要改就去改对应卡的 log.md 再重跑本脚本。

用法：python scripts/map.py
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SPECS_DIR = ROOT / "specs"
OUT_FILE = ROOT / "docs" / "plan" / "file-map.md"
SKIP_DIRS = {"_template"}

FILE_HEADER = "文件"


def use_utf8_stdout() -> None:
    """Windows 控制台默认 cp936，直接 print 中文会抛 UnicodeEncodeError。"""
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        if callable(reconfigure):
            reconfigure(encoding="utf-8", errors="replace")


def split_row(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def parse_rows(text: str) -> list[tuple[str, str, str]]:
    """只解析表头第一格是「文件」的那张表，避免把「本卡消耗」也算进来。"""
    rows: list[tuple[str, str, str]] = []
    in_table = False
    for raw in text.splitlines():
        line = raw.strip()
        if not line.startswith("|"):
            in_table = False
            continue
        cells = split_row(line)
        if not in_table:
            in_table = bool(cells) and cells[0] == FILE_HEADER
            continue
        if all(set(cell) <= set("-: ") for cell in cells):
            continue
        if len(cells) < 3 or not cells[0]:
            continue
        rows.append((cells[0], cells[1], cells[2]))
    return rows


def card_id(dirname: str) -> str:
    return dirname.split("-", 1)[0]


def collect() -> tuple[list[tuple[str, str, str, str]], list[str]]:
    """返回 (文件, 卡, 动作, 作用) 列表与读到的卡目录名。"""
    entries: list[tuple[str, str, str, str]] = []
    cards: list[str] = []
    if not SPECS_DIR.is_dir():
        return entries, cards
    for card_dir in sorted(p for p in SPECS_DIR.iterdir() if p.is_dir()):
        if card_dir.name in SKIP_DIRS:
            continue
        log_file = card_dir / "log.md"
        if not log_file.is_file():
            continue
        cards.append(card_dir.name)
        card = card_id(card_dir.name)
        for path, action, purpose in parse_rows(log_file.read_text(encoding="utf-8-sig")):
            entries.append((path.replace("\\", "/"), card, action, purpose))
    entries.sort(key=lambda item: (item[0], item[1]))
    return entries, cards


def render(entries: list[tuple[str, str, str, str]], cards: list[str]) -> str:
    lines = [
        "# 文件地图（自动生成，勿手改）",
        "",
        "> 由 `uv run python scripts/map.py` 从各卡的 `specs/<卡>/log.md` 合并生成。",
        "> 修 bug 的顺序：本表查文件 -> 拿到卡号 -> 读 `specs/<卡>/spec.md`。",
        f"> 覆盖 {len(cards)} 张卡、{len(entries)} 行。",
        "",
        "| 文件 | 卡 | 动作 | 作用 |",
        "|---|---|---|---|",
    ]
    for path, card, action, purpose in entries:
        lines.append(f"| {path} | {card} | {action} | {purpose} |")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    use_utf8_stdout()
    entries, cards = collect()
    if not entries:
        print("[skip] no file tables found under specs/*/log.md", flush=True)
        return 0
    OUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUT_FILE.write_text(render(entries, cards), encoding="utf-8", newline="\n")
    rel = OUT_FILE.relative_to(ROOT).as_posix()
    print(f"[ok] {rel}: {len(entries)} row(s) from {len(cards)} card(s)", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
