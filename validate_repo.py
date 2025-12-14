#!/usr/bin/env python3
"""Repo integrity checks.

Keeps the root hub from drifting and breaking the 'public execution OS' promise.
"""
from __future__ import annotations
from pathlib import Path

REQUIRED_FILES = [
    "README.md",
    "ROADMAP.md",
    "MANIFEST.md",
    "CODE_OF_CONDUCT.md",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "GOVERNANCE.md",
    "paihi/PAIHI_PUBLIC_SPEC.md",
    "paihi/schemas/impact_record.schema.json",
    "paihi/schemas/receipt.schema.json",
]

REQUIRED_DIRS = [
    "docs",
    "impact/records",
    "impact/receipts",
    "tools",
    "projects",
    "logs",
    ".github/workflows",
]

def main() -> int:
    root = Path(__file__).resolve().parents[1]
    missing = []

    for f in REQUIRED_FILES:
        if not (root / f).exists():
            missing.append(f"file:{f}")

    for d in REQUIRED_DIRS:
        if not (root / d).exists():
            missing.append(f"dir:{d}")

    if missing:
        print("Repo validation FAILED. Missing:")
        for m in missing:
            print(f"- {m}")
        return 1

    print("Repo validation OK.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
