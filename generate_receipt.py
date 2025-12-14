#!/usr/bin/env python3
"""Generate a public-safe receipt for a single artifact.

Receipt format v0.1:
receipt_sha256 = sha256(receipt_version|impact_record_id|timestamp_utc|artifact.path|artifact.sha256)

Usage:
  python3 tools/generate_receipt.py path/to/artifact --impact-id AFG-PAIHI-YYYY-MM-DD-XXXX --out receipts/
"""
from __future__ import annotations
import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def sha256_text(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("artifact", help="Path to the artifact file")
    ap.add_argument("--impact-id", required=True, help="Impact record id")
    ap.add_argument("--out", default="receipts", help="Output directory")
    args = ap.parse_args()

    artifact_path = Path(args.artifact)
    if not artifact_path.exists() or not artifact_path.is_file():
        raise SystemExit(f"Artifact not found: {artifact_path}")

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    ts = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    artifact_hash = sha256_file(artifact_path)

    canonical = f"0.1|{args.impact_id}|{ts}|{artifact_path.as_posix()}|{artifact_hash}"
    receipt_hash = sha256_text(canonical)

    receipt = {
        "receipt_version": "0.1",
        "impact_record_id": args.impact_id,
        "timestamp_utc": ts,
        "artifact": {"path": artifact_path.as_posix(), "sha256": artifact_hash},
        "receipt_sha256": receipt_hash,
        "notes": "receipt_sha256 = sha256(receipt_version|impact_record_id|timestamp_utc|artifact.path|artifact.sha256)"
    }

    out_path = out_dir / f"{args.impact_id}.receipt.json"
    out_path.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    print(out_path.as_posix())
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
