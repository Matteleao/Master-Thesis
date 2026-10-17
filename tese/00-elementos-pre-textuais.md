Universidade de Lisboa

Faculdade de Farmácia / Instituto Superior Técnico

![logo-ulisboa](figuras/logo-ulisboa.png)

**Translating ICH E6(R3) into Practice: A Site-Centered Operational Quality Management Framework for Shoulder Medical Device Clinical Investigations**

Felipe Gregorio Lima

> Dissertation Report supervised by Professor Gracinda Maria Martins Sanches Fernandes and co-supervised by Dr. Nuno Jorge da Silva Moura

Master’s of Pharmaceutical Engineering

2025/2026

![logo-ulisboa](figuras/logo-ulisboa.png)

Código de Conduta e de Boas Práticas da Universidade de Lisboa:

Declaro ter desenvolvido e elaborado o presente trabalho em consonância com o Código de Conduta e de Boas Práticas da Universidade de Lisboa. Mais concretamente, afirmo não ter incorrido em qualquer das variedades de fraude académica, que aqui declaro conhecer, e que atendi à exigida referenciação de frases, extratos, imagens e outras formas de trabalho intelectual, assumindo na íntegra as responsabilidades da autoria.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

# Resumo

A conceção orientada para a qualidade e a gestão da qualidade proporcional ao risco são princípios centrais das Boas Práticas Clínicas. A diretriz do International Council for Harmonisation (ICH) E6(R3), baseada na ICH E8(R1), incorpora a qualidade na conceção e na condução do ensaio. A norma da International Organization for Standardization (ISO) 14155:2026 e o Regulamento (UE) 2017/745 aplicam esses princípios às investigações de dispositivos médicos. Contudo, a sua tradução para as atividades operadas pelos centros permanece insuficientemente definida. Esta tese teve como objetivo desenvolver uma arquitetura de gestão da qualidade operacional para centros que conduzem investigações clínicas de dispositivos médicos.

Aplicámos a Design Science Research Methodology (DSRM) e através de uma revisão narrativa e a análise cruzada dos quatro instrumentos oficiais e análise de registos de 46 investigações e 235 organizações. Foram identificadas 5 lacunas regulamentares, 12 domínios críticos para a qualidade e 12 requisitos de conceção.

A arquitetura resultante assenta em quatro pilares: governação, gestão da qualidade baseada no risco, controlos operacionais e supervisão do desempenho. Um conjunto integrado de 24 instrumentos compatíveis com suporte em papel apoia a supervisão do investigador, a identificação de riscos, a atribuição de responsabilidades, a monitorização interna, a vigilância da curva de aprendizagem cirúrgica, a deteção de complicações, a rastreabilidade do dispositivo e a avaliação do desempenho. Um ciclo de vida de sete fases e três níveis de implementação adaptam esses componentes à capacidade do centro e ao risco da investigação.

A arquitetura fornece um método rastreável para converter princípios regulamentares e lacunas locais em controlos operacionais. Foi concebida para complementar o sistema de qualidade do promotor, preservando a responsabilidade do centro pelos seus processos e registos. Como ainda não foi implementada ou avaliada, a sua viabilidade e os seus efeitos requerem avaliação prospetiva.

**Palavras-chave:** investigação clínica; dispositivos médicos; gestão da qualidade baseada no risco; ICH E6(R3); cirurgia ortopédica

# Abstract

Quality by Design (QbD) and risk-proportionate quality management are central principles of Good Clinical Practice (GCP). International Council for Harmonisation (ICH) E6(R3), grounded in ICH E8(R1), treats quality as a property built into trial design and conduct. International Organization for Standardization (ISO) 14155:2026 and Regulation (EU) 2017/745 apply related principles to medical device investigations. However, their practical translation into the day to day operations at the investigational site remains insufficiently defined. This thesis aimed to develop a site-centered operational quality management architecture for shoulder medical device clinical investigations.

We used problem-centered Design Science Research Methodology (DSRM). The study combined a narrative review, a cross-framework analysis of four regulatory and guidance instruments, and a registry analysis of 46 investigations involving 235 organizations. The analysis identified 5 regulatory gaps, 12 critical-to-quality (CtQ) domains, and directed the creation of 12 design requirements.

The resulting architecture comprises four pillars: governance, risk-based quality management (RBQM), operational controls, and performance oversight. An integrated set of 24 paper-compatible instruments supports investigator oversight, risk identification, responsibility allocation, internal monitoring, surgical learning-curve surveillance, complication signal detection, device traceability, deviation control, and performance review. A seven-phase lifecycle and three implementation depths adapt these components to site capacity and investigation risk.

The architecture provides a traceable method for converting regulatory principles and identified site-level gaps into operational controls across the clinical investigation lifecycle. It is designed to complement the sponsor's quality system while preserving site ownership of local quality processes and records. The framework has not been implemented or evaluated at a site. Its feasibility and effects on conduct, early signal detection, record completeness, and staff workload therefore require prospective evaluation.

**Keywords:** clinical investigation; medical devices; risk-based quality management; ICH E6(R3); orthopedic surgery

#  Acknowledgments

# List of Abbreviations

- ADE — Adverse Device Effect

- AE — Adverse Event

- API — Application Programming Interface

- CAPA — Corrective and Preventive Action

- CCDM — Criticality-Coded Delegation Matrix

- CEC — Clinical Events Committee

- CER — Clinical Evaluation Report

- CFR — Code of Federal Regulations

- CIP — Clinical Investigation Plan

- CRF — Case Report Form

- CRO — Contract Research Organization

- CSST — Complication Signal Surveillance Template

- CT — Computed Tomography

- CTIS — Clinical Trials Information System

- CtQ — Critical-to-Quality

- CTTI — Clinical Trials Transformation Initiative

- DD — Device Deficiency

- DR — Design Requirement

- DSR — Design Science Research

- DSRM — Design Science Research Methodology

- DTRM — Device and Study Training Requirements Matrix

- EMA — European Medicines Agency

- EN — European Standard (European Norm)

- EU — European Union

- FDA — Food and Drug Administration

- FUCR — Follow-up Compliance Review

- GCP — Good Clinical Practice

- ICC — Intraclass Correlation Coefficient

- ICDL — Intraoperative Checklist and Device Log

- ICH — International Council for Harmonisation of Technical Requirements for Pharmaceuticals for Human Use

- IFU — Instructions for Use

- IMC — Internal Monitoring Checklist

- IMP — Internal Monitoring Plan

- IQL — Imaging Quality Log

- ISO — International Organization for Standardization

- ISO/TR — ISO Technical Report

- IVDR — In Vitro Diagnostic Medical Devices Regulation

- MDCG — Medical Device Coordination Group

- MDIC — Medical Device Innovation Consortium

- MDR — Medical Device Regulation — Regulation (EU) 2017/745

- MRL — Milestone Review Log

- PD — Protocol Deviation

- PFVR — Participant Follow-up Visit Record

- PI — Principal Investigator

- PIDLR — Post-Investigation Debrief and Lessons Record

- PIR — Performance Indicator Record

- POT — PI Oversight Template

- PRISMA — Preferred Reporting Items for Systematic Reviews and Meta-Analyses

- PRO — Patient-Reported Outcome

- PSEAR — Participant Screening and Eligibility Assessment Record

- QA — Quality Assurance

- QbD — Quality by Design

- QC — Quality Control

- QMS — Quality Management System

- RACI — Responsible, Accountable, Consulted, Informed

- RBM — Risk-Based Monitoring

- RBQM — Risk-Based Quality Management

- ROM — Range of Motion

- ROMIO — Randomised Oesophagectomy: Minimally Invasive or Open

- SADE — Serious Adverse Device Effect

- SAE — Serious Adverse Event

- SART — Safety and Adverse Effect Reporting Template

- SCML — Site Complication Monitoring Log

- SCR — Surgical Credentialing Record

- SIFSL — Subject Identification and Failure Screening Log

- SIRR — Site Imaging Readiness Record

- SLCT — Surgeon Learning Curve Tracking Log

- SQA — Surgical Quality Assurance

- SRR — Site Risk Register

- TRE — Training Record Evaluation and Release

- UDI — Unique Device Identification

- UDI-DI — Device Identifier

- UDI-PI — Production Identifier

# List of Tables

**Table 3.1** Site-level regulatory gaps [**Erro! Indicador não definido.**](#bm_tbl_31)

**Table 3.2** Site-level CtQ domains [35](#bm_tbl_32)

**Table 3.3** Organizational environment [39](#bm_tbl_33)

**Table 3.4** Design requirements (origin) [43](#section-11)

**Table 4.1** Design requirements and framework components [45](#table-4.1.-the-twelve-design-requirements-from-section-3.5-the-framework-component-that-answers-each-one-and-the-section-of-chapter-4-where-that-component-is-developed.)

**Table 4.3** The scalability model [73](#table-4.3.-the-scalability-model-with-the-implementation-depth-of-six-framework-elements-across-type-a-large-or-complex-research-hospital-type-b-medium-private-clinic-or-hospital-and-type-c-small-surgical-center-site-contexts.)

**Table 4.4** The twenty-four instruments [75](#bm_tbl_44)

# List of Figures

**Figure 4.1** The quality lifecycle [70](#figure-4.1.-the-seven-phase-quality-lifecycle-and-the-transversal-safety-stream-with-the-actions-entry-conditions-and-objective-of-each-phase-arranged-to-show-that-the-cycle-closes-and-feeds-the-next-investigation.)

**Figure 4.2** The twenty-four instruments grouped by pillar [76](#figure-4.2.-the-twenty-four-instruments-grouped-by-the-pillar-that-owns-each-one-seven-in-governance-five-in-risk-management-nine-in-operational-controls-and-three-in-performance-oversight-each-shown-by-acronym-with-its-full-name.)

**Figure 4.3** Instrument granularity and the information chain [77](#figure-4.3.-the-granularity-of-each-instrument-from-individual-evidence-to-the-site-level-decision-it-supports-with-the-arrows-marking-the-chain-through-which-information-rises-and-a-verification-requirement-returns-to-the-evidence-layer.-rows-group-instruments-by-operational-area-so-operational-controls-appears-as-four-groups-safety-surgery-and-device-enrollment-and-follow-up.)

**Figure 4.4** Instruments mapped against CtQ domains [78](#figure-4.4.-the-twenty-four-instruments-mapped-against-the-twelve-ctq-domains-with-a-filled-marker-for-a-primary-or-emphasis-relationship-and-an-open-marker-where-the-instrument-only-supports-limits-or-scopes-another-instruments-control.)

**Figure 4.5** Instruments mapped against design requirements [78](#figure-4.5.-the-twenty-four-instruments-mapped-against-the-twelve-design-requirements-with-a-filled-marker-for-a-direct-answer-an-open-marker-for-a-relationship-inherited-from-a-combined-or-earlier-instrument-a-dashed-marker-for-an-extension-added-to-the-original-set-and-a-small-marker-for-a-supporting-contribution.-dr11-and-dr12-apply-to-all-instruments-as-a-set-and-are-marked-once-for-the-whole-set.)
