---
name: pir-instrument-scope-feedback
description: "User rejected over-built PIR redesigns (v0.9, v0.10); confirm the instrument's intended role before rebuilding"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 1180205c-fb3a-417d-9f7b-53b0177e4525
  modified: 2026-09-29T11:17:06.364Z
---

For the thesis site-quality instruments (PIR and siblings in `Documents/Tese - Clinical trials/Forms, templates and tools/`), the user rejected two rebuilds of the Performance Indicator Record: v0.9 (9 pages, ~15 tables, "MUITO complexo e grande demais") and v0.10 (4 pages, "tu realmente não entendeu a ideia"). They then dropped the PIR work ("deixa pra lá") without saying what the intended idea was.

**Why:** I answered a request for an opinion with a long critique, then implemented every point at once. I never asked what role the PIR plays in their design (dashboard pointing at sibling instruments vs. a form that stores figures), so both rebuilds rested on my own reading. The v0.8 (6 pages) is the last version the user built themselves; v0.9 and v0.10 are unaccepted drafts.

**How to apply:**
- Before redesigning any of these instruments, ask in one or two lines what the instrument is for and who fills what. Do not infer it from the thesis text alone.
- Keep changes small and close to the user's own last version; do not add fields, pages or sections that were not asked for.
- When the user rejects a direction, stop and ask instead of producing another full rebuild.
- Related: [[surgical-site-roles]] for the site-role vocabulary used in these instruments.
