# SCR: what the thesis text requires (extracted 2026-10-10)

Sources: OLD = `Escrita da tese/04_Results_The_Quality_Framework.md` (28/09); CUR = current thesis `Revisao manual tese.docx`. Requirements carried over from other reviews keep their IDs (C-...).

| # | Requirement | Source |
|---|---|---|
| R1 | Decides whether a surgeon has the competence and scope for the study procedure. | Table 4.4 row E |
| R2 | Inputs: formation, experience, privileges, training, technical competence, and any condition or trigger for recredentialing. | Table 4.4 |
| R3 | Reviews that evidence against the credentialing criteria set for the procedure (sponsor threshold: CIP, training requirements, study risk assessment). | Table 4.4; OLD/CUR 4.2.3 |
| R4 | Output: credentialed, conditional, restricted, or not credentialed. | Table 4.4 |
| R5 | Three layers of entry evidence: professional eligibility (specialty status, institutional privileges, experience in the anatomical field); procedure-specific competency (comparable procedures, recent volume, cases of similar complexity); device-specific release (training in the system, instrumentation and workflow, initial proctoring where applicable). | OLD 4.2.3 |
| R6 | The difficulty: standing, procedure-specific competency and readiness on this device are three different questions; the site decides how much uncertainty the sponsor criteria resolve and how much its own judgment must close before the first case. | CUR 4.2.3 (para "Building that evidence...") |
| R7 | Sponsor sets the threshold; the site applies it and documents a decision for each surgeon (ISO 14155:2026 Clauses 6.8, 9.2.1, 10.1, 10.3, 10.6). | OLD/CUR 4.2.3 |
| R8 | Temporary controls when risk or the expected learning curve supports them: proctoring, co-surgery, initial lower-complexity cases; proportionate. | OLD/CUR 4.2.3 |
| R9 | Status kept current: re-evaluation annually and after protocol amendments, safety signals, complication clusters or evidence of performance drift; confirm, restrict, suspend or restore. | OLD/CUR 4.2.3 |
| R10 | SLCT supplies post-release performance information and supports reassessment (SLCT outputs: continue, intensified review, renewed device training, temporary proctoring, restriction to lower-complexity cases, escalation). | OLD 4.2.3, 4.3.2 |
| R11 (= C-R18) | Decision linked to the delegation so assigned surgical tasks match current authorization (via TRE Section B and the RACI). | CUR 4.2.3 |
| R12 (= C-R16) | Who was authorized to do what, on what basis, from when. | OLD 4.2.5; DR10 |
| R13 | Created in phase 2 (surgeons qualified and released) before enrollment; checked before each case in phase 4 (start-up release does not close it). | OLD 4.6.2, 4.6.3 |
| R14 | Surgery by a surgeon not released is an escalation trigger to the PI. | OLD 4.2.1 |
| R15 | Table 4.3: Type B credentialing and device release retained; Type C documented authorization and training retained, enhanced review or proctoring activated when risk or limited local experience requires it. | Table 4.3 |
| R16 | A record the site can maintain and present at monitoring or audit. | OLD 4.2.3 |
| R17 | Author: SCR is a qualification check, not training; it is recorded as a qualification row in TRE Section B; TRE uses the SCR, not the reverse. | Author, TRE review 2026-10-08; Table 4.4 (SCR feeds TRE) |
| R18 | Evidence record for one person (Figure 4.3); cites sources (CV, privileges, case logs) without copying them. | Figure 4.3; 4.4.4 |
| R19 | Credentialing gates entry (Discussion). | CUR 5.3 |

Figure 4.4: CtQ1 OPEN, CtQ5 FILLED, CtQ6 FILLED. Figure 4.5: DR3 DIRECT, DR10 DIRECT.

## Review history
- 2026-10-10: v0.4 simulated (30/09) reviewed. BLOCKED (B 1, I 7, M 4): circular dependency with the TRE (SCR F reads the TRE device release while the TRE reads the SCR); outcomes not those of Table 4.4; sponsor-vs-site residual uncertainty not handled; triggers not explicit; Section A title; duplicated header/B; signature format; example from another study with non-framework codes.
- 2026-10-10: author approved all changes, decisions and S20. v0.5 built as new files (blank + simulated; v0.4 preserved) with `scratchpad/build_scr_v05.py`: A Purpose and use (feeds TRE B; RACI; pre-case check; POT); B Professional eligibility and C Procedure-specific competence (sponsor criterion column; uniform options with N/A); D Credentialed scope and temporary controls (procedure/CCDM task, complexity limit, proctoring/co-surgery/lower-complexity cases with closing criterion; device-specific release = TRE, pointer only); E decision Credentialed/Conditional/Restricted/Not credentialed (green/amber/orange/red), dates with next review at most 12 months, residual uncertainty, rationale, Type C rule; F three signature boxes (assessor, PI / accountable approver, surgeon); G reassessment log landscape with trigger checkboxes and effect Confirmed/Restricted/Suspended/Restored. Simulated: Dr Paulo Teixeira SCR-014-03, conditional, assessor Dr Lina Costa, PI Dr Alex Morgan.
- 2026-10-11 (author comments on D and E): Section D split into D1 Credentialed scope (study procedure with CCDM task ID; cases the surgeon may operate; standing exclusions beyond the CIP) and D2 Temporary controls (one row per control, same options Proctoring / Co-surgery / Lower-complexity cases / Other; what it requires; ends when); device-specific-release row turned into a footnote; cross-references written "Section D2"; closing criterion no longer depends on the TRE. Decision definitions: Credentialed = full D1 scope, no control; Conditional = D1 with D2 controls until their end criterion; Restricted = narrower standing scope with no end date, changed only by reassessment; rule: mark one; if both apply mark Restricted and list controls in D2.

