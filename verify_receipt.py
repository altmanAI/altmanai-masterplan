#!/usr/bin/env python3
"""Verify a public-safe receipt.

Usage:
  python3 tools/verify_receipt.py path/to/receipt.json
"""
from __future__ import annotations
import hashlib
import json
import sys
from pathlib import Path

def sha256_text(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()

def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python3 tools/verify_receipt.py <receipt.json>")
        return 2
    receipt_path = Path(sys.argv[1])
    if not receipt_path.exists():
        print(f"Not found: {receipt_path}")
        return 2

    receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
    v = receipt.get("receipt_version")
    impact_id = receipt.get("impact_record_id")
    ts = receipt.get("timestamp_utc")
    art = receipt.get("artifact") or {}
    art_path = art.get("path")
    art_sha = art.get("sha256")
    claimed = receipt.get("receipt_sha256")

    canonical = f"{v}|{impact_id}|{ts}|{art_path}|{art_sha}"
    computed = sha256_text(canonical)

    if computed == claimed:
        print("OK: receipt_sha256 matches canonical fields")
        return 0
    print("FAIL: receipt_sha256 mismatch")
    print(f"claimed:  {claimed}")
    print(f"computed: {computed}")
    return 1

if __name__ == "__main__":
    raise SystemExit(main())
