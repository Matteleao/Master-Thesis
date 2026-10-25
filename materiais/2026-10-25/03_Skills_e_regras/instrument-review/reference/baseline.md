# Baseline of the 24 instruments (source: thesis)

Source of truth: `/Users/felipegregorio/Desktop/auditor_tese_corrigido/Revisao manual tese.docx`
- Table 4.4 (purpose, inputs, how it works, output): images in `.../auditor_tese_corrigido/Tabelas/Table · The 24 instruments, part 1 of 2 ...png` and `part 2 of 2 ...png`
- Figure 4.3 (information layer): `.../Imagens/Fig. Instrument map by information layer@2x.png`
- Figures 4.4 and 4.5 (CtQ and DR coverage): read with `scripts/read_matrix_marks.py <ACR>`, never from memory
- Figure 4.1 (lifecycle phases): `.../Imagens/Fig. Quality lifecycle@2x.png`

If the thesis changes, update this file before the next review. Transcribed 2026-10-04.

## Information layers (Figure 4.3)

| Row group | Evidence (one person, event, image) | Synthesis (aggregates records) | Decision (site-level) |
|---|---|---|---|
| Governance | SCR, TRE | MRL | DTRM, CCDM, RACI, POT |
| Risk management | none | SLCT, SCML, CSST | SRR |
| Safety stream | SART | (SCML, CSST span this row) | none |
| Surgery and device | ICDL, IQL | IMC | IMP, SIRR |
| Enrollment | PSEAR | SIFSL | none |
| Follow-up | PFVR | FUCR | none |
| Performance oversight | none | CAPA | PIDLR |
| Indicators (side panel) | | | PIR (six indicators) |

Rule shown in the figure: an evidence record never depends on a synthesis or decision document existing first. Information rises; decisions come back down as a requirement to verify.

## Per instrument (Table 4.4, verbatim) and declared links

Declared links come only from the Inputs/Output columns of Table 4.4. "Feeds" lists the instruments whose Inputs name this one.

| App. | Acr. | Pillar | Purpose and use | Inputs | How it works | Output | Named upstream | Feeds |
|---|---|---|---|---|---|---|---|---|
| A | CCDM | Governance | Defines which tasks may be delegated and how much supervision each one requires. | The set of study tasks and the criteria used to grade their clinical and operational significance. | Classifies each task by criticality, states the authorized function, any prerequisite, the supervision level, and the escalation trigger. | The delegation and supervision limits the rest of the framework works from. | none | TRE |
| B | RACI | Governance | States who is Responsible, Accountable, Consulted, and Informed for each activity. | The activity list and the site's role structure. | Maps each activity against the current role holder, a backup, the limit of authority, and acceptance of responsibility. | An ownership map that shows where coverage is complete and where it is not. | none | none named |
| C | DTRM | Governance | Sets what training a role or task requires before it can be assigned. | The site's functional roles, the study's activities, and the device and protocol requirements behind them. | Links role, activity, required training, prerequisite, assessment method, evidence, and renewal interval. | The training rule the TRE checks individual evidence against. | none | TRE |
| D | TRE | Governance | Decides whether a specific person is ready to perform a role or task independently. | Individual training and competence evidence, checked against the DTRM, the CCDM, and, where relevant, the SCR. | Compares the evidence held for that person against what the DTRM requires for the role. | A release decision: released, conditional release, or not released. | DTRM, CCDM, SCR | none named |
| E | SCR | Governance | Decides whether a surgeon has the competence and scope for the study procedure. | Formation, experience, privileges, training, technical competence, and any condition or trigger for recredentialing. | Reviews that evidence against the credentialing criteria the framework sets for the procedure. | A credentialing decision: credentialed, conditional, restricted, or not credentialed. | none | TRE |
| F | POT | Governance | Records the PI's active oversight of the investigation as it runs. | Signals and sources from the other instruments, read on a defined cycle: the SRR, the PIR, FUCR, IMC, SART, and SCML. | The PI reviews those sources each cycle and documents a decision, an action, and any escalation. | An oversight decision and the response it triggers. | SRR, PIR, FUCR, IMC, SART, SCML | MRL |
| G | MRL | Governance | Decides whether the investigation passes, passes conditionally, or is blocked at a defined milestone. | The milestone's criteria, the evidence gathered against them, and any gap already logged in the POT, PIR, or SRR. | Compares the criteria to the evidence and states which CtQ domains, if any, remain affected. | A milestone decision: pass, pass with conditions, or not pass. | POT, PIR, SRR | none named |
| H | SRR | Risk Management | Holds the site's own prospective risks and the controls in place for each one. | A risk, its CtQ domain, its cause and consequence, and the controls already in place. | Rates the risk, assigns an owner, and sets a residual risk level and a review trigger. | An updated risk and control plan. | none | POT, MRL |
| I | SLCT | Risk Management | Assesses whether a surgeon's technical performance is stabilizing or still varying case to case. | The sequence of cases for that surgeon, their complexity, and the technical metrics, deviations, and complications recorded for each. | Aggregates that sequence and reads it against the complexity of each case, not against a fixed count. | A call on whether supervision, retraining, restriction, or continued release is warranted. | none | CAPA (learning-curve review as trigger) |
| J | SCML | Risk Management | Gives the site a single index of every complication, without duplicating the individual case record. | The SART case, the ICDL record of the procedure, the action taken, and the outcome. | One entry per complication, referencing those records rather than repeating their content. | A complication log the CSST reads to detect a pattern. | SART, ICDL | CSST, POT |
| K | SART | Risk Management | Tracks one safety occurrence, device deficiency, or new finding from the moment it opens to the moment it closes. | The facts of the event, its relationship to the device and the procedure, and any protection, communication, or follow-up already taken. | Keeps the classification, the causality determination, and the reporting status current as the case develops. | A traceable safety case and the notification route it falls under. | none | SCML, POT |
| L | CSST | Risk Management | Decides whether a pattern of complications, not a single case, requires a response. | The SCML and any relevant contextual source (implant component, model, lot, timing, surgeon, indication). | Aggregates events against a numerator, a denominator, and a stratification, and reads the trend. | A disposition: maintain surveillance, investigate, escalate, or close the signal. | SCML | CAPA (confirmed signal) |
| M | IMP | Operational Controls | Defines how the site will monitor itself internally. | The domains, CtQs, and sources the site decides are worth watching. | Sets the frequency, sample, criteria, responsible party, trigger, and escalation route for each domain. | A review plan for the IMC to execute. | none | IMC |
| N | IMC | Operational Controls | Executes the periodic review the IMP defines, including the site's own scheduled self-inspection. | The IMP, and the execution evidence for each domain it names. | Evaluates execution, evidence, and effectiveness domain by domain. | Findings, actions, an owner, a deadline, and verification for each. | IMP | POT |
| O | SIRR | Operational Controls | A site self-assessment of whether its local imaging arrangements can meet the sponsor's imaging charter. | The applicable sponsor imaging charter or manual, the current protocol, and local acquisition, equipment, and radiology evidence. | Maps each charter requirement against local capability and records the gap, if any. | A readiness decision before imaging arrangements are submitted for sponsor or CRO review. | none | none named |
| P | IQL | Operational Controls | Decides whether each required image or exam is acquired, complete, and usable. | The applicable imaging charter and the image set acquired for a given participant and time point. | Checks the image against window, technical acceptability, completeness, and traceability. | A quality decision and, where needed, a route to correction, repeat acquisition, or escalation. | none | FUCR |
| Q | ICDL | Operational Controls | Preserves the record of the procedure and the device at the point it happens. | Operating room readiness, the critical steps of the technique, and the device components used. | Records times, components, UDI and lot, any substitution, and the final configuration as the case proceeds. | The procedure and device evidence, and the exception route where one is needed. | none | SCML |
| R | PSEAR | Operational Controls | Decides the eligibility of one candidate. | The CIP's eligibility criteria and the clinical, imaging, and assessment evidence available for that candidate. | Checks the evidence against each criterion and routes unresolved uncertainty for clarification. | An eligibility decision, with its supporting sources and any handoff it requires. | none | SIFSL |
| S | SIFSL | Operational Controls | Keeps the administrative reconciliation of every candidate screened, whatever the outcome. | Coded candidate identification and the PSEAR decision for each. | Logs the screening outcome and the reason, and aggregates the pattern across candidates. | Reconciled counts and a view of where and why screening fails. | PSEAR | none named |
| T | PFVR | Operational Controls | Records one participant's one follow-up visit. | The visit window and the components the protocol requires at that time point. | Compares what was obtained, imaging, tests, PROMs, assessment, against what was required. | The visit's status, its completeness, and any exception. | none | FUCR |
| U | FUCR | Operational Controls | Measures follow-up performance across a cohort and a period, not one visit at a time. | The PFVR and IQL records for the relevant participants and period. | Aggregates visits expected, completed, missed, delayed, and incomplete, with the reason for each gap. | Follow-up metrics and the action they point to. | PFVR, IQL | POT |
| V | PIR | Performance Oversight | Decides whether the six performance indicators show control, a trend, or a need for action. | The sources, denominators, and numerators the six indicators are built from. | Reconciles those sources against the period and the rule defined for each indicator. | An indicator interpretation and, where warranted, an escalation. | none | POT, MRL, CAPA |
| W | CAPA | Performance Oversight | Handles a systemic problem, a recurrence, or a trend that needs correction and prevention, not a one-off fix. | A trigger from an indicator, a confirmed signal, a recurrent deviation, or a learning-curve review. | Records the extent of the problem, its root cause, the corrective and preventive action, and the owner and deadline. | A controlled response and evidence of whether it worked. | PIR, CSST, SLCT (as triggers) | SRR (Section 4.5.7: the cycle returns to the site's risk assessment) |
| X | PIDLR | Performance Oversight | Converts what the site learned running the investigation into a controlled lesson, not an informal memory. | The milestones, problems, and records accumulated across the other instruments during the study. | Reconstructs what worked and what did not, and states the lesson and who owns any resulting change. | Lessons routed to process, risk, training, or the design of the next investigation. | MRL and all others (close-out) | next investigation |

## Thesis anchors per pillar (where to read the concept the instrument must serve)

- Governance: Section 4.2 (4.2.1 oversight model, 4.2.2 delegation, 4.2.3 surgeon qualification, 4.2.4 device training). Section 4.2.2 requires the delegation structure to be task-based, competency-gated, version-controlled, and linked to the review intensity of the oversight model.
- Risk Management: Section 4.3 (4.3.1 site risk layer, 4.3.2 operator learning curve, 4.3.3 complication monitoring).
- Operational Controls: Section 4.4 (4.4.1 internal verification and its nine checks, 4.4.2 imaging, 4.4.3 source documentation, 4.4.4 no parallel records).
- Performance Oversight: Section 4.5 (4.5.1 to 4.5.6 the six indicators, 4.5.7 CAPA cycle).
- Lifecycle: Section 4.6 and Figure 4.1. Scalability (Type A/B/C): Section 4.7 and Table 4.3. DR list: Table 3.4. CtQ list: Table 3.2.
