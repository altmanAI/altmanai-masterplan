#!/usr/bin/env python3
"""Compute SHA-256 for a file.

Usage:
  python3 tools/hash_file.py path/to/file
"""
from __future__ import annotations
import hashlib
import sys
from pathlib import Path

def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python3 tools/hash_file.py <path>")
        return 2
    p = Path(sys.argv[1])
    if not p.exists() or not p.is_file():
        print(f"File not found: {p}")
        return 2
    print(sha256_file(p))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
