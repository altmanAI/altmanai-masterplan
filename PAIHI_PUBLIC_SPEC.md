# PAIHI Public Spec (v0.1)

PAIHI = **Proof-of-AI-Human-Impact**.

This repo publishes a **public-safe** version of the spec: enough for anyone to verify integrity and provenance *without* exposing private workflows.

## Goals
1) Make impact claims verifiable (hashes, timestamps, provenance).
2) Make authorship and responsibility clear (who/what/when).
3) Make changes auditable over time (append-only logs where possible).

## What PAIHI is (here)
PAIHI is a bundle of:
- An **Impact Record** (what changed and why)
- One or more **Artifacts** (docs, code, datasets) referenced by hash
- A **Receipt** that binds the record to artifact hashes

## What PAIHI is NOT (here)
- Not a private identity or authorization system
- Not a substitute for legal compliance
- Not a guarantee of correctness (it guarantees integrity + traceability)

## Minimal fields
See `paihi/schemas/impact_record.schema.json` and `paihi/schemas/receipt.schema.json`.

## Verification (public)
Anyone can:
- Hash an artifact (SHA-256)
- Verify the artifact hash matches what a receipt claims
- Verify the receipt matches the impact record id and timestamps

## Example
See:
- `paihi/examples/impact_record.example.json`
- `paihi/examples/receipt.example.json`

© Altman Family Group, LLC. All rights reserved. ™
