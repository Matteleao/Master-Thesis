# TRE (with DTRM): requirements carried over from other reviews

From the CCDM review (2026-10-06).

| # | Requirement | Source |
|---|---|---|
| C-R3 | Delegated persons qualified (ICH E6(R3) 2.3.2), training documented before assignments begin (ISO 14155:2026 Clause 7.6). | OLD 4.2.1, 4.2.2 |
| C-R5 | Each delegation linked to evidence of competence. | OLD 4.2.1 |
| C-R7 | No delegation before release: the release decision is what the RACI assignment relies on. | OLD/CUR 4.2.2 |
| C-X2 | Release decision states which CCDM task IDs it covers, so the RACI can cite it. | Author's design, 2026-10-06 |
| C-R4 | Shares the ISO 14155:2026 Clause 7.6 record with RACI and DTRM: holds the identified person, the release and the signature; cites the RACI assignment and the DTRM requirement it checks. | OLD/CUR 4.2.2; author 2026-10-06 |
| C-R16 | With SCR and DTRM: who was authorized to do what, on what basis, and from when. | OLD 4.2.5; DR10; author 2026-10-06 |

## Own requirements from the thesis text (extracted 2026-10-08)

| # | Requirement | Source |
|---|---|---|
| R1 | Individual record of who was trained, on what, when, by whom, under which controlled document version, and when authorized to work independently. | 4.2.4 |
| R2 | Completion is not release; explicit release decision for higher-risk or higher-variability activities (device, imaging, outcome assessment). In the framework this is driven by the DTRM codes (TR completion, AS assessment + release, AW acknowledgment, CD conditional). | 4.2.4; DTRM codes |
| R3 | Connects to the delegation structure (CCDM tasks) and, for surgeons, to qualification (SCR), without collapsing into either. | 4.2.4 |
| R4 | Living record: release maintained and re-opened by triggers; shows training at start-up and that it stayed current. | 4.2.4 |
| R5 | Table 4.4: individual evidence checked against the DTRM, the CCDM and, where relevant, the SCR; compares evidence with what the DTRM requires for the role; output released / conditional release / not released. | Table 4.4 |
| R6 | Who was authorized for what, on what basis, from when (with RACI for the assignment). | OLD 4.2.5; DR10 |
| R7 | Feeds the RACI: release stated per CCDM task ID; RACI assigns C2/C3 tasks only to released persons. | Author order CCDM -> DTRM -> TRE -> RACI |
| R8 | ISO 14155:2026 Clause 7.6: documented training before assignment; TRE holds the identified person and signature/initials. | 4.2.2; C-R4 |
| R9 | Qualified by education, training and experience (ICH E6(R3)). | 4.2.4 |
| R10 | References source evidence (certificates, records) and does not copy it. | 4.4.4 |

## Author decisions on the TRE review (2026-10-08)
- R1: DTRM version (and profile ID) go in the page-1 header only; no new section. D column now reads "DTRM module ID / training activity".
- R2: TRE does not use the DTRM codes, accepted. Open question: who defines the assessment method (sponsor or site); depending on the answer, change DTRM or remove the method choice from TRE.
- R3: SCR cited in Section B as a qualification row for surgical tasks (SCR checks qualification, not training).
- R5, T2, C-R4: linked to DTRM (A, header, D, M). R7, D4, C-X2: Section H has CCDM task ID; A and H state the release feeds the RACI.
- R8: keep 4 signature boxes, larger.
- 2026-10-08 (second pass): v0.3 preserved; v0.4 built as a new file (blank + simulated, editor included). Applied: D6 (DTRM module ID column in C and D; CCDM task ID in E), I1/4 (summaries C, E, G and overall decision L removed; outcome meanings as a note above the release register), V6/8 (CCDM-style header: title + subtitle + version), 6 (thesis name "Training Record Evaluation and Release"), 7 (simulated shoulder example, functional assessor P-05, CCDM T06), 9 (Review status / Next review removed from header; TRE record ID and revision added), 10 (trigger choice list in maintenance log), 11 (sentence case, American spelling). Kept: 4 signature boxes, larger. Not done (author: evaluate later): change 3 beyond the SCR note in B. P1 accepted as is. Method column reads "Method (per DTRM)" pending the author's answer on where the assessment is described.
