---
name: instrument-review-criteria
description: "How the user wants each of the 24 thesis instruments (Appendices A-X) critiqued one by one - coherence, dependencies, gap coverage, visual consistency"
metadata:
  node_type: memory
  type: project
  originSessionId: 49dd0209-6db7-4ec5-b0d8-cf31839c3a45
  modified: 2026-10-10T01:07:44.074Z
---

From 2026-10-04 the user sends the 24 instruments one at a time (built with other AIs) for critique: positives, negatives, and above all concrete improvements (add what is missing, remove what makes no sense).

Criteria the user set:
- Practical to use and easy to fill in; not visually cluttered.
- Coherent with the thesis text (pillar sections 4.2-4.5, Table 4.4 purpose/inputs/how/output, Figures 4.3-4.5, lifecycle Figure 4.1) and actually covers the gaps the text describes.
- Documentation logic: build order and feeds. SOME governance documents (not all, the user corrected this) precede logs and individual records and must be creatable without depending on them; they may reference them only when updated because of a problem found there. Other governance documents can legitimately depend on downstream records. Judge each instrument on its own place in the chain. Fine-grained individual records feed others (e.g. release decisions feed the delegation structure). Each instrument must state what it feeds and what feeds it.
- Internal coherence: no two tables saying the same thing.
- Cross-document visual uniformity: header with the instrument name on every page, Section 1 always "Purpose and use", the same final signature block in every document, same look overall.

**Why:** the instruments become Appendices A-X of the thesis and must read as one coherent set.
**How to apply:** use the same rubric for every instrument and keep a running list of cross-document standards fixed so far. See [[thesis-file-state-2026-10-02]].

The process is now the `instrument-review` skill at `~/.claude/skills/instrument-review/` (steps, criteria T/D/P/I/V, baseline, house standards register, two scripts). Reports go to `Forms, templates and tools/Revisoes/` (renamed from `_revisoes` by the author, Oct 2026).

Feedback 2026-10-04 on the skill: review only the single HTML sent (no file inventory, no blank-vs-simulated comparison). Main focus is the thesis body text, including older detailed versions in `/Users/felipegregorio/Documents/Escrita da tese/` (e.g. 04_Results_The_Quality_Framework.md, 28/09): check whether the instruments really deliver what the text describes (device-specific complication monitoring, operator-dependent risk and learning curve, internal verification of site conduct). User liked: link check in both directions, saved report, practicality criteria, B/I/M severity.

Working preferences (2026-10-06): after changing an instrument, show the files directly in the chat (SendUserFile, display render) so the author does not have to open the folder. Each instrument needs a blank HTML (appendix) and a simulated filled HTML (presentation). Deliver the HTML first; generate PDFs (saved in the instrument's own folder under `Forms, templates and tools/<ACR>/`) ONLY when the author asks for them (author, 2026-10-07). Chrome headless print works only from a /tmp copy of the HTML; kill the headless processes afterwards. Author's build order for governance (final, 2026-10-06): CCDM -> DTRM -> TRE -> RACI.

Form-design preferences (author, 2026-10-10, RACI v0.3 pass), apply to the remaining instruments:
- Blank (appendix) version leaves site-specific content empty, including pre-printed examples of functions or limits (only something universal like the PI row may stay printed); the simulated version carries the examples.
- Same answer options in every row of a table; no row with a different format (use N/A as an option where a case does not apply).
- Write N/A in a finding/notes cell that needs nothing, never restate the check.
- Rules shown as a compact table tied to the codes, not a numbered bullet list in a box; cut self-evident instructions.
- Distinct colors per code; separate columns for distinct data (e.g. code vs supervision); column headers spelled out (no bare "A").
- No "Combined" option, no compensating-review sub-table, no scheduled-review box in event-driven documents.
