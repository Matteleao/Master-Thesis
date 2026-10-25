# POT: what the thesis text requires (extracted 2026-10-11)

Sources: OLD = `Escrita da tese/04_Results_The_Quality_Framework.md` (28/09); CUR = current thesis `Revisao manual tese.docx`.

| # | Requirement | Source |
|---|---|---|
| R1 | Records the PI's active oversight as the investigation runs. Inputs: signals from SRR, PIR, FUCR, IMC, SART and SCML, read on a defined cycle. Process: the PI reviews those sources each cycle and documents a decision, an action and any escalation. Output: an oversight decision and the response it triggers. Feeds the MRL. | Table 4.4 row F |
| R2 | The plan states which activities require direct investigator review, which may be delegated, how often formal review takes place, what triggers investigator involvement outside the schedule, and what evidence shows oversight happened. | OLD 4.2.1 |
| R3 | Purpose: oversight must not stay implicit, informal or dependent on local custom. | OLD 4.2.1 |
| R4 | The PI is accountable for every activity (ISO 14155:2026 Clause 10.1). | OLD 4.2.1, 4.2 intro |
| R5 | Tiered, risk-adjusted: involvement stratified by task criticality (CCDM codes C1-C3, supervision S0-S3). | OLD/CUR 4.2.1; CCDM feeds POT ("what requires the PI") |
| R6 | PI attention reserved for irreplaceable judgments: surgical appropriateness, interpretation of intraoperative deviations, device-relatedness of complications, early signs of executional drift. | OLD/CUR 4.2.1 |
| R7 | Explicit statement of what requires direct investigator involvement: borderline eligibility, unplanned intraoperative changes, component substitutions, revision-related interpretation, inconsistencies not apparent from the documentation. | OLD/CUR 4.2.1 |
| R8 | Difficulty: decide in advance, for each type of activity, what needs the PI's own judgment and what can be reviewed after the fact; the line moves with device, procedure and team experience; too low a threshold reverts to the investigator-centered model, too high makes oversight a formality. | CUR 4.2.1 |
| R9 | Difficulty: criticality is not intrinsic; routine activities can carry latent significance; a scheme copied from another site misses what is specific to this investigation. | CUR 4.2.1 |
| R10 | Formal review points (site initiation, first case, post-operative window, monthly, before endpoint data review, before close-out and device reconciliation) belong to the milestone review structure (MRL); the POT cycle feeds the MRL. | OLD/CUR 4.2.1; Table 4.4 |
| R11 | Event-triggered escalation pathway, independent of the routine cadence: surgery by a surgeon not released; missing lot or UDI; unplanned component substitution; substantial eligibility uncertainty; delayed SAE reporting; missed critical imaging window; major PD affecting endpoints; revision, explant, reoperation or readmission. Must reach the PI before the next scheduled point. | OLD 4.2.1; CUR 4.2.1 |
| R12 | Oversight meeting architecture: weekly operational huddle (coordinator and OR or research staff), monthly governance review (investigator, coordinator, data lead, imaging function), case-triggered review after a critical event. Hard to sustain in small centers. | OLD/CUR 4.2.1 |
| R13 | DR1 at the level of authority; DR10: written, scheduled and evidenced, so the record survives staff departure. | CUR 4.2.1; Figure 4.5 |
| R14 | Phase 2: oversight plan written, escalation pathway agreed, meeting architecture scheduled, before the first participant. | OLD 4.6.2 |
| R15 | At site qualification the oversight plan is evidence for the sponsor under ISO 14155:2026 Clause 6.8. | CUR 5.4 |
| R16 | The POT and the MRL overlap at several points and the burden is unmeasured; the design should keep the overlap small. | CUR 5.6 |
| R17 | Type B: tiered PI oversight with combined functions, concise milestone reviews, explicit event triggers, coordinator as operational integrator. Type C: essential governance map with named combined functions, direct PI escalation for CtQ-critical events, external or sponsor support. | Table 4.3 |
| R18 | Receives escalations from other instruments: CCDM escalation triggers, SCR (case outside the credentialing decision), RACI (coverage gaps). | CCDM, SCR, RACI reviews |
| R19 | No parallel record: actions are routed to the owning record (CAPA for systemic correction); the POT records the PI decision. | 4.4.4; 4.5.7 |

Figure 4.4: CtQ1, CtQ6, CtQ10, CtQ12 FILLED; CtQ2, 3, 4, 5, 7, 8, 9, 11 OPEN. Figure 4.5: DR1 DIRECT, DR10 DIRECT.

## Review history
- 2026-10-11: v0.8 (edited export 04/10, blank with example rows) reviewed. NEEDS REVISION (B 0, I 8, M 4): six cycle sources not explicit; no escalation trigger list; no meeting architecture; PI-retained decisions not derived from the CCDM; F/G/H duplicate the CAPA; MRL absent (overlap and feed); decision not a closed set; no simulated shoulder example.
- 2026-10-11: author asked to see the proposals applied: v0.9 blank built (`scratchpad/build_pot_v09.py`, file `POT/POT_PI_Oversight_Template_v0.9_blank_editable.html`, 5 pages; v0.8 preserved). Part 1 plan: A Purpose and use; B PI-retained decisions (4 framework judgments printed + CCDM C1/S1 rows; when the PI acts: Before / At decision / After); C escalation pathway (8 framework triggers printed + 3 blank; who notifies, PI notified within, immediate action, record); D review cycle and meetings (huddle, monthly review = POT cycle, case-triggered; Type C rule); E plan approval (reason checkboxes; Prepared by + PI / accountable approver). Part 2 review record (repeatable): F identification; G six cycle sources + escalations received + other (signal Yes/No, PI interpretation, decision No signal / Monitor / Action routed / Escalated, destination); H conclusion (No action needed / Actions routed / Escalated to the sponsor / Hold), rationale, items for the next MRL milestone, open items, next review, PI + supporting reviewer signatures. Old F/G/H (actions, effectiveness, controlled updates) removed (CAPA). Simulated version not yet built.

- 2026-10-11: simulated v0.9 built (GLENOS-01, POT-014 v0.2 revised after PD-014-07 / CAPA-014-2026-003; monthly review POT-014-R-2026-10 on 6 Oct 2026 reading the six sources; SART-014-002 and the RACI interim cover as escalations received; decision Actions routed; items to MRL-014-M2). Generator now builds both versions.
