#!/usr/bin/env python3
"""Self-test: verifies example receipt + schemas exist and are parseable."""
from __future__ import annotations
import json
from pathlib import Path
import subprocess
import sys

def main() -> int:
    root = Path(__file__).resolve().parents[1]
    json.loads((root / "paihi/schemas/impact_record.schema.json").read_text(encoding="utf-8"))
    json.loads((root / "paihi/schemas/receipt.schema.json").read_text(encoding="utf-8"))
    receipt_path = root / "paihi/examples/receipt.example.json"
    p = subprocess.run([sys.executable, str(root / "tools/verify_receipt.py"), str(receipt_path)], capture_output=True, text=True)
    if p.returncode != 0:
        print(p.stdout)
        print(p.stderr)
        return p.returncode
    print("Self-test OK.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
