---
name: "instrument-review"
description: "Use when reviewing one of the 24 thesis instruments (CCDM, RACI, DTRM, TRE, SCR, POT, MRL, SRR, SLCT, SCML, SART, CSST, IMP, IMC, SIRR, IQL, ICDL, PSEAR, SIFSL, PFVR, FUCR, PIR, CAPA, PIDLR). Main question: does the instrument actually do what the thesis body text says this part of the framework must do."
---

# Instrument review

The author sends one HTML. Review that file and nothing else. Same steps, same criteria, every time. Reply to the author in Portuguese.

**The main question:** does this instrument, together with the instruments it works with, actually do what the thesis body text says must be done? The text describes each concept in depth (for example device-specific complication monitoring, operator-dependent risk and the learning curve, internal verification of site conduct). The review checks the instrument against that description point by point. Figures and tables are a secondary check.

Files of this skill:
- `reference/sources.md`: where in the thesis, current and older versions, each instrument's concept is described.
- `reference/requirements/<ACR>.md`: the requirement list extracted from the text in an earlier review (reuse it, extend it if the text says more).
- `reference/baseline.md`: Table 4.4 row, Figure 4.3 layer and declared links for each instrument.
- `reference/standards.md`: rules that every instrument must follow equally (header, Section A, signature block...).
- `scripts/check_instrument.py <file.html>`: a helper that flags possible formal problems for me to check.
- `scripts/read_matrix_marks.py <ACR>`: the instrument's marks in Figures 4.4 (CtQ) and 4.5 (DR), read from the figure images.

Reviews are saved in `/Users/felipegregorio/Documents/Tese - Clinical trials/Forms, templates and tools/Revisoes/`.

## Steps

**1. Read what the text asks for (main step).** Using `reference/sources.md`, read every passage about this instrument's concept, starting with the older detailed Chapter 4, then the current Chapters 3 to 5 and the older Discussion. Extract a numbered list of requirements, each with its source (file and section):
- what the function has to do, decide or record;
- the difficulties the text names (for example, in complication monitoring, recognizing that several events share a cause), since an instrument that records fields but does not handle the difficulty does not answer the text;
- triggers, thresholds, timing and who acts;
- regulatory obligations cited (clause numbers);
- claims the Discussion makes about what the instrument enables;
- limits the text sets (what the instrument must not do, for example duplicate source records).
Save or update the list in `reference/requirements/<ACR>.md`.

**2. Read the secondary references from the image files, not from inside the thesis document.** Figures and tables are in `/Users/felipegregorio/Desktop/auditor_tese_corrigido/Imagens/` and `/Users/felipegregorio/Desktop/auditor_tese_corrigido/Tabelas/` (Table 4.4 parts 1 and 2, Table 4.1, Table 4.3, Table 3.2, Table 3.4, Figures 4.1 to 4.5). Open the ones that matter for the instrument with the Read tool. Use `baseline.md` for the Table 4.4 row and `read_matrix_marks.py` for the Figure 4.4 and 4.5 marks.

**3. Read the HTML in full and look at every page.** Open it in the browser pane, view each page, and run this to find clipped content:
`[...document.querySelectorAll('main.page')].map((p,i)=>({page:i+1,overflow:p.scrollHeight>p.clientHeight+1}))`
Run `check_instrument.py` as a helper: it lists possible formal problems (skipped section letter, page without header, version mismatch, unknown acronyms). Check each one on the page; only the real ones go into the review, as evidence under the criteria below.

**4. Check coverage of the text.** For each requirement from step 1: COVERED, PARTIAL or MISSING, with where in the instrument (section, table, row, field), and what to add or change. When the requirement is covered by another instrument, name it and say whether the hand-off between the two is explicit.

**5. Judge the criteria** below: PASS, PARTIAL, FAIL or N/A, with evidence and the concrete change.

**6. Check the links with other instruments, in both directions.** What this instrument says it receives must match what the other instrument says it delivers, and the reverse. A mismatch is reported against the instrument that has to change.

**7. Check the common rules (`standards.md`).** These are rules every document must follow in the same way, so the 24 read as one set. Rules the author has approved count as criteria. When this review shows that something should be the same in all documents and no rule exists yet, propose it; it becomes a rule only when the author approves it.

**8. Write, save and deliver the report.** Write it in Portuguese (quotes from the instrument and the thesis stay in English), as a self-contained HTML page with simple styling, following the format below. Save it to `Revisoes/<ACR>_revisao_v<x.y>_<YYYY-MM-DD>.html`, add one line to `Revisoes/STATUS.md`, and send it with SendUserFile (`display: "render"`) so it opens in the side panel. In the chat, give only the verdict, the blocking issues and the decisions the author needs to take.

## Criteria

Severity: **B** blocking (contradicts the thesis or a regulation, or breaks the chain between instruments), **I** important (weakens use or coherence), **M** minor.

### T. Coherence with the thesis
- **T1** Purpose matches what the text and Table 4.4 give it, with no function the thesis does not give it.
- **T2** Inputs match what the text and Table 4.4 say it uses.
- **T3** The document produces the output the text expects, as a field or decision someone fills in.
- **T4** The information layer is respected: an evidence record holds one person, event or image; a synthesis aggregates; a decision document decides. No document holds data that belongs to another layer.
- **T5** Every CtQ marked FILLED in Figure 4.4 is controlled by a row, field or check; OPEN marks are at least referenced.
- **T6** Every DR marked DIRECT in Figure 4.5 traces to a concrete element. DR11: works on paper. DR12: states the minimum for a Type C center.
- **T7** Terminology identical to the thesis: instrument names, CtQ codes, DR codes, pillar names, American spelling.
- **T8** Regulatory references correct and current; the example is a shoulder device investigation.
- **T9** The moment it is created and the moments it is updated fit the lifecycle (Section 4.6).

### D. Dependencies and feeds
- **D1** Every instrument it names exists in the 24-instrument set; sponsor or site records outside the set are named generically.
- **D2** It can be created at its moment in the lifecycle with what exists then. If it has a fixed part and a running part, they are separate, and the fixed part does not depend on records created later.
- **D3** Update triggers are explicit: which finding in which instrument causes a revision.
- **D4** What it feeds is stated and matches what the receiving instrument expects.
- **D5** No circular dependency for creation.
- **D6** Rows that other instruments must reference carry an ID.

### P. Practicality
- **P1** A Type C center (one investigator, one coordinator) can fill it in during routine work.
- **P2** Each field has one meaning, a clear format, and a closed answer set where one exists.
- **P3** No dead field: every field is used by the output or by another instrument.
- **P4** The instructions on the form are enough to complete it.
- **P5** Paper logistics work: continuation sheets, sheet numbering, revisions.
- **P6** The decision is explicit, as a closed set of outcomes.

### I. Internal coherence
- **I1** No information appears twice.
- **I2** Codes, scales and colors run in one direction and mean one thing each.
- **I3** Sections lettered in sequence; internal cross-references correct.
- **I4** One version identity in header, footer and revision field.
- **I5** The simulated example is internally consistent: dates, IDs, counts and names agree.

### V. Visual
- **V1** Instrument header on every page.
- **V2** Section A "Purpose and use" first.
- **V3** Signature block in the common format, closing the controlled part of the document. Repeatable continuation sheets may come after it if their header links each sheet to the approved record (record ID, revision, effective date, sheet n of N).
- **V4** Footer "Page n of N" correct on every page.
- **V5** No clipped content; text legible; enough room to write by hand.
- **V6** Color only where it carries meaning; look matches the other instruments.
- **V7** Page orientation follows the common rule.

## Report format

```
# <ACR> v<x.y> review, <date>
File reviewed: <path>.

Verdict: READY / READY AFTER MINOR CHANGES / NEEDS REVISION / BLOCKED
Counts: B <n>, I <n>, M <n>

## Strengths
- ...

## Coverage of the thesis text
| # | What the text requires (source) | Status | Where in the instrument / which other instrument | Change |
|---|---|---|---|---|

## Criteria
| ID | Status | Evidence | Change |
|---|---|---|---|

## Changes to make (in order of severity)
1. [B] <what>, <where>. Add / Remove / Change: <exact change>.

## Implications for other instruments
- <ACR>: <what has to change there and why>

## Thesis changes this review suggests
- <section/figure/table>: <change> (only when the instrument is right and the thesis is wrong)

## Decisions for the author
1. ...

## Common rules proposed by this review
- ...
```

Verdict rule: any B gives BLOCKED; any I gives NEEDS REVISION; only M left gives READY AFTER MINOR CHANGES; none gives READY. Items waiting for an author decision are listed as open and do not change the verdict until decided.

## Rules for the reviewer

- The text comes first. A requirement found in the text outranks a mark in a figure.
- Evidence for every judgment: where in the instrument, and which file and section of the thesis.
- A preference that is not a criterion goes under "Decisions for the author", never as a FAIL.
- When the instrument is better than the thesis, say so and propose the thesis change.
- Do not edit the instrument unless the author asks.
