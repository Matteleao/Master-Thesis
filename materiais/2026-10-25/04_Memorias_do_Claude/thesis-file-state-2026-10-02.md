---
name: thesis-file-state-2026-10-02
description: State and pitfalls of the canonical thesis docx after the 2026-10-02 cleanup (Word overwrite incident, numbering, appendices)
metadata:
  type: project
---

Canonical file: `/Users/felipegregorio/Desktop/auditor_tese_corrigido/Revisao manual tese.docx`. On 2026-10-02 the user's own manual save (from Word) silently overwrote my 2026-10-01 edits (Appendices chapter, native reference numbering) and brought in a rewritten Discussion (5.1-5.7, 4.2.5 removed). I redid everything on top of that version; backup at `Revisao manual tese.BACKUP_2026-10-02_antes_da_limpeza.docx`.

**Why:** the user edits the same file in Word while I edit via python-docx, so whichever saves last wins.
**How to apply:** before editing, check mtime and whether Word has the file open; always make a backup first; after editing, tell the user to close the doc in Word without saving and reopen.

State after cleanup: 90 refs, Vancouver by first citation, native Word list numbering (numId 2), citations merged as `[a, b]` sorted ascending; Appendices A-X (24 instruments in Table 4.4 order) + Appendix Y (lifecycle model), PDFs still pending from user; List of Tables/Figures use PAGEREF bookmarks bm_*; TOC field added; updateFields set. Table 3.1 and 4.1 images were pixel-patched (corrected copies in Tabelas/corrigidas). Images still carry British spellings (standardised, specialised, centre, authorisation) that need regeneration at source.
