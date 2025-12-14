#!/usr/bin/env python3
"""Generate a human-readable report of impact records.

Usage:
  python3 tools/impact_report.py
"""
from __future__ import annotations
import json
from pathlib import Path

def main() -> int:
    root = Path(__file__).resolve().parents[1]
    records_dir = root / "impact" / "records"
    if not records_dir.exists():
        print("No impact records directory found.")
        return 2

    records = []
    for p in sorted(records_dir.glob("*.json")):
        records.append(json.loads(p.read_text(encoding="utf-8")))

    print(f"Impact records: {len(records)}\n")
    for r in records:
        print(f"- {r.get('id')} :: {r.get('title')}")
        print(f"  ts: {r.get('timestamp_utc')}")
        print(f"  tags: {', '.join(r.get('tags', []))}")
        summary = (r.get('summary') or '').strip().replace('\n', ' ')
        if len(summary) > 160:
            summary = summary[:157] + "..."
        print(f"  summary: {summary}\n")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
