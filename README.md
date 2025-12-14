# AltmanAI MasterPlan

**AltmanAI MasterPlan** is the public execution OS for the **$1T AltmanAI x Humanity mandate**: build human-first AI products, prove real-world impact, and scale with integrity.

This repo is the **root hub**: strategy, roadmap, governance, and the public-proof layer (**PAIHI**) that keeps us honest.

## What we're building

### Flagship tracks
- **DailyPilot**: a human-first daily prioritization companion (stress down, clarity up).
- **Impact Explorer**: a public ledger + viewer for verifiable impact records.
- **Civic Knowledge Engine**: transparent civic data -> explainable, traceable public knowledge.

### Proof layer
- **PAIHI (Proof-of-AI-Human-Impact)**: a public, verifiable way to show *who did what, when*, and *what changed*.

## How to navigate

- **`ROADMAP.md`**: 90-day execution plan (weekly milestones).
- **`MANIFEST.md`**: what exists, what's next, what's blocked.
- **`docs/`**: architecture, principles, operating model.
- **`paihi/`**: public PAIHI spec + schemas + examples.
- **`impact/`**: sample impact records + registry format.
- **`tools/`**: small scripts to generate/verify hashes and receipts.

## Quickstart: verify a file's SHA-256

```bash
python3 tools/hash_file.py path/to/file
```

Generate a public-safe receipt:

```bash
python3 tools/generate_receipt.py path/to/file --impact-id AFG-PAIHI-YYYY-MM-DD-XXXX --out receipts/
```

Verify a receipt:

```bash
python3 tools/verify_receipt.py receipts/<receipt>.json
```

## Our baseline
We prioritize **human dignity and well-being** in every AI interaction. AI exists to amplify human potential while safeguarding ethical values.

See: `CODE_OF_CONDUCT.md` and `docs/PRINCIPLES.md`.

## Community
- Start with `CONTRIBUTING.md`
- Security issues: `SECURITY.md`

---

© Altman Family Group, LLC. All rights reserved. ™
