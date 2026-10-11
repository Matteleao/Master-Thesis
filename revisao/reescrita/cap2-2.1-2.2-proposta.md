# Cap. 2, Seções 2.1 e 2.2: proposta em revisão (11/10/2026)

Esta é a versão em discussão com o autor. Ela parte do texto que o autor colou na conversa, com as correções do relatório `mudancas-cap2-2.1-2.2.html`, e já inclui a versão refeita do último parágrafo (candidatos e mecanismos). **Ainda não foi aplicada em `tese/02-methodology.md`**, que continua com a reescrita anterior.

Trechos entre colchetes e em negrito são pendências que dependem de uma resposta do autor.

---

## 2.1 Design research

### 2.1.1 Design science research methodology

The objective of this thesis, stated in Section 1.5, is to build a site-level quality management framework for surgical device investigations. To achieve it, we followed the Design Science Research Methodology (DSRM) set out by Peffers et al. [49]. Design science research creates and evaluates artifacts that solve identified organizational problems. DSRM organizes that work into six activities: problem identification and motivation, definition of the objectives for a solution, design and development, demonstration, evaluation, and communication.

Four of those activities are reported here. Chapter 1 and Sections 3.2 and 3.3 carry the problem identification and motivation. Section 3.5 states the objectives for a solution as design requirements DR1 to DR12. Chapter 4 reports the design and development, and this thesis is the communication. The remaining two activities, demonstration and evaluation, were not undertaken.

Peffers et al. also note that a DSRM study can enter the sequence at different activities, depending on what triggers the research, and that a study triggered by a problem, which they call problem-centered initiation, starts at the first activity. This thesis is problem-centered. The difficulty of managing quality at the site is already recognized in the literature, which describes data-quality management at sites as often reactive and standardized site practices as uncommon [42, 45], and **[finds]** that measures for surgical trials are rarely carried through conduct [39]. As Sections 1.1 and 1.3 describe, the recent guidelines place more of the responsibility for quality on the investigator and the site team, but they do not describe how a site should organize itself to carry it. Section 3.2 examines this clause by clause.

Since the problem is the absence of a structured, site-level quality management framework for surgical device investigations, the artifact is a model together with the methods that put it to work.

DSRM also asks that the link between problem and solution stay visible. We kept it visible by tracing each major component of the framework to the design requirement it answers, and each requirement to the regulatory gap, CtQ domain, or operating condition that motivated it. Section 3.5 states the requirements and Table 3.4 traces each one to its origin, while Table 4.1 maps the requirements onto the components that answer them and Figure 4.5 does the same for the 24 instruments.

### 2.1.2 Overview of the research process

Three sources of evidence fed the first two DSRM activities. The first is an analysis of the normative instruments that govern device investigations. The second is a review of the literature. The third is a characterization, from registry data, of the setting where these investigations are conducted.

The regulatory analysis came first and provided the domains on which the design was built. The instruments showed what is required, the literature showed what the field has observed and proposed, and the registry analysis showed where the work is done and under what conditions. A requirement supported by more than one source rests on more than one kind of evidence, which makes it harder to dismiss as an artifact of a single source.

## 2.2 Analysis of the normative instruments

### 2.2.1 Instruments and their status

We used ICH E8(R1) and ICH E6(R3) as conceptual and design references, because they define QbD and CtQ factors, which the device texts do not, and set out the principle of risk-proportionate quality. Their scope is medicinal products, so we took the device-specific obligations from two other instruments. ISO 14155:2026 is the GCP standard for device investigations and our main source of investigator-level requirements. The MDR supplies the European legal framework, including the traceability and safety reporting requirements specific to devices.

We consulted three further standards: ISO 13485, ISO 14971 with its guidance document ISO/TR 24971, and ISO 15189. None of them creates an obligation for the investigational site, and we used them as models of a documented quality system held by other organizations in the same regulatory and supply chain.

### 2.2.2 Derivation of the site-level CtQ domains

We used CtQ factors as the organizing concept of the analysis because the task required a principled way to decide which of the many requirements in the instruments a site has to actively control. ICH E8(R1) and ICH E6(R3) offer the concept for that purpose. They ask that quality effort be concentrated on the factors whose failure would compromise participant protection or the reliability of results, and that controls be proportionate to the risks to those factors [5, 6]. Section 3.3 explains why these factors have to be identified again at the level of the site.

Deriving the domains required two inputs from the instruments: a set of candidate attributes, meaning what the instruments require of a clinical investigation, and a test for deciding which of those attributes are critical to quality. We took the candidates from all the instruments and the test from the ICH guidelines.

The test came from ICH because ICH E8(R1) and ICH E6(R3) are the only instruments examined that define CtQ factors and describe how to identify them [5, 6]. ISO 14155:2026 and the MDR use the same idea without naming it. ISO 14155:2026 bases the extent of monitoring on the “critical data points and endpoints” of the investigation (Clauses 6.7 and 9.2.3) [8], and both ISO 14155:2026 (Clause 7.4.2) and the MDR (Article 80(1)(a)) [10] refer to adverse events that the clinical investigation plan identifies as “critical to the evaluation of the results”. Neither text defines what makes a factor critical or gives criteria for identifying one.

ICH E8(R1), in Section 3.2, describes CtQ factors as “attributes of a study whose integrity is fundamental to the protection of study participants, the reliability and interpretability of the study results, and the decisions made based on the study results” [5]. Its Section 7 lists 18 considerations for identifying them:

1. Stakeholder engagement
2. Appropriate eligibility criteria
3. Adequacy of prior studies
4. Necessary data collection
5. Scientific study objectives
6. Well-defined endpoints
7. Meaningful control group
8. Bias minimization
9. Participant protection
10. Prespecified statistical analysis
11. Clear participant information
12. Critical data integrity
13. Staff competencies and training
14. Risk-proportionate monitoring
15. Study feasibility
16. Data monitoring committee
17. Adequate sample size, duration, and visit frequency
18. Transparent and timely reporting

These considerations are written from the position of the sponsor, as the party that designs the study. Our object was the site, so we drew from ICH E8(R1) four criteria that can be applied to any attribute, whatever party it binds, and ICH E6(R3) states each of them as well. The labels are ours, and neither guideline groups the principles in this way.

1. *Proportionality.* Study procedures and controls are scaled to the risks of the study and to the importance of the data they produce (ICH E8(R1), Section 3.2; ICH E6(R3), Principle 7) [5, 6].
2. *Parsimony.* The set of critical factors stays focused. Data and activities that serve neither participant protection nor the primary objectives are left out (ICH E8(R1), Sections 3.2 and 3.3.2) [5].
3. *Assigned responsibility.* The identification and protection of critical factors are allocated to defined parties, with qualified staff and sufficient resources. At the site, the investigator confirms that each person given a delegated activity is qualified for it (ICH E6(R3), Sections 2.3.2 and 3.2–3.4) [5, 6].
4. *Reliance on existing knowledge.* What is known about the product, the condition, and the population determines which factors are treated as critical and which controls apply, and both are revised as knowledge grows during the study (ICH E8(R1), Section 3.2; ICH E6(R3), Principle 4 and Section 3.10.1.5) [5, 6].

The candidate attributes came from a reading of three texts: ICH E6(R3), ISO 14155:2026, and **[the MDR / MDR Annex XV]**. In each text we recorded every requirement that concerns a feature of the investigation whose failure would affect participant protection or the reliability of the results, which is the ICH E8(R1) definition of a CtQ factor [5]. Each entry held three items: the attribute in our own words, the clause it comes from, and the excerpt of that clause. Informed consent, for example, was recorded once for each text that requires it, with the clause and its wording. The procedure was the same for the three texts, so their entries could be compared directly. **[We used the 18 considerations of ICH E8(R1) as a check on coverage, to confirm that no area they name had been missed.]**

Some requirements describe how quality is to be controlled, for example periodic risk review or quality tolerance limits in ICH E6(R3). These mechanisms are not attributes to be protected, so we kept them in a separate list, and Chapter 4 draws on them in the design of the instruments. The three sets of attributes were then merged into a single matrix, which Section 2.2.3 describes.
