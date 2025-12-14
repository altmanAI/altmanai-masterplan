# MANIFEST

Updated: 2025-12-13T00:00:00-05:00

This file is the single source of truth for "what exists / what's next / what's blocked" in the MasterPlan repo.

## Exists (in this repo now)

### Foundation
- Repo structure + governance docs
- PAIHI public spec skeleton + schemas + examples
- Tools: hash/receipt generation + receipt verification
- Sample impact registry records

### Placeholders for product tracks
- `projects/dailypilot/`
- `projects/impact-explorer/`
- `projects/civic-knowledge-engine/`

## Next (7 days)

### Ship v0.1: Impact Explorer (lite)
- A minimal registry format for impact records (JSON)
- A command-line verifier for receipts + hashes
- A simple static viewer (optional) to browse impact entries

### Publish Build Log cadence
- Weekly build log in `logs/`
- One public-safe impact entry per week in `impact/records/`

## Blockers / Dependencies
- None required for v0.1; everything here runs locally with Python 3.10+.

## Owner / Maintainers
- AltmanAI by Altman Family Group, LLC
