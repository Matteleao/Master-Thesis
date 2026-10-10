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

A diretriz E6(R3) do International Council for Harmonisation (ICH), baseada na ICH E8(R1), incorpora a qualidade na conceção e na condução do ensaio, proporcionalmente ao risco, e a norma ISO 14155:2026 e o Regulamento (UE) 2017/745 aplicam princípios semelhantes às investigações clínicas de dispositivos médicos. Estes textos atribuem ao centro de investigação uma parte maior da responsabilidade pela qualidade, mas a maioria dos instrumentos analisados foi construída para o promotor. Esta tese deriva um *framework* de qualidade ao nível do centro para investigações clínicas de dispositivos médicos do ombro, complementar ao sistema do promotor, que permita ao centro agir sobre os riscos que o promotor não consegue ver a tempo e demonstrar como controlou a sua própria condução.

Aplicámos a Design Science Research Methodology, combinando uma revisão narrativa, uma comparação cláusula a cláusula da ICH E6(R3), da ISO 14155:2026 e do Anexo XV do Regulamento, e uma análise de registos de 46 investigações e 235 organizações. Identificaram-se 5 lacunas regulamentares e 12 domínios críticos para a qualidade, que originaram 12 requisitos de conceção.

O *framework* assenta em quatro pilares: governação, gestão do risco, controlos operacionais e supervisão do desempenho. Vinte e quatro instrumentos compatíveis com papel apoiam a supervisão do investigador, a gestão do risco no centro, a monitorização interna, a vigilância de complicações e a rastreabilidade do dispositivo. Um deles acompanha a curva de aprendizagem cirúrgica durante a condução, função que os instrumentos comparados não atribuem ao centro. Um ciclo de vida de sete fases e três níveis de implementação adaptam o *framework* à capacidade do centro e ao risco da investigação, dirigido a centros privados com investigação recorrente.

Cada componente é rastreável até um requisito de conceção. Como o *framework* ainda não foi implementado nem avaliado, a sua viabilidade e os seus efeitos requerem avaliação prospetiva.

**Palavras-chave:** investigação clínica; dispositivos médicos; gestão da qualidade baseada no risco; ICH E6(R3); cirurgia ortopédica

# Abstract

International Council for Harmonisation (ICH) E6(R3), grounded in ICH E8(R1), builds quality into trial design and conduct in proportion to risk, and International Organization for Standardization (ISO) 14155:2026 and Regulation (EU) 2017/745 apply related principles to medical device investigations. These texts give the investigational site a larger share of the responsibility for quality, but most of the instruments reviewed here were built for the sponsor. This thesis aimed to derive a site-level quality framework for shoulder medical device clinical investigations that complements the sponsor's system, so that a site can act on the risks the sponsor cannot see in time and can show how it controlled its own conduct.

We used a problem-centered Design Science Research Methodology. The study combined a narrative literature review, a clause-level comparison of ICH E6(R3), ISO 14155:2026, and Annex XV of Regulation (EU) 2017/745, and a registry analysis of 46 investigations involving 235 organizations. The analysis identified 5 regulatory gaps and 12 Critical-to-Quality domains, from which 12 design requirements were derived.

The resulting framework has four pillars: Governance, Risk Management, Operational Controls, and Performance Oversight. Twenty-four paper-compatible instruments support investigator oversight and delegation, site risk assessment, internal monitoring, complication surveillance, and device traceability. One of them follows the surgical learning curve during conduct, a function for which the instruments compared assign the site no obligation. A seven-phase lifecycle and three implementation depths adapt the framework to site capacity and investigation risk, with private centers that run investigations recurrently alongside surgical care as the target.

Every component traces back to a design requirement and its regulatory or operational origin. The framework has not been implemented or evaluated at a site, so its feasibility and effects require prospective evaluation.

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

- CTIS — Clinical Trials Information System

- CtQ — Critical-to-Quality

- CTTI — Clinical Trials Transformation Initiative

- DD — Device Deficiency

- DR — Design Requirement

- DSRM — Design Science Research Methodology

- DTRM — Device and Study Training Requirements Matrix

- EMA — European Medicines Agency

- EN — European Standard (European Norm)

- EU — European Union

- FDA — Food and Drug Administration

- FUCR — Follow-up Compliance Review

- GCP — Good Clinical Practice

- ICDL — Intraoperative Checklist and Device Log

- ICH — International Council for Harmonisation of Technical Requirements for Pharmaceuticals for Human Use

- IFU — Instructions for Use

- IMC — Internal Monitoring Checklist

- IMP — Internal Monitoring Plan

- IQL — Imaging Quality Log

- ISO — International Organization for Standardization

- ISO/TR — ISO Technical Report

- MDIC — Medical Device Innovation Consortium

- MDR — Regulation (EU) 2017/745 on medical devices

- MRL — Milestone Review Log

- PD — Protocol Deviation

- PFVR — Participant Follow-up Visit Record

- PI — Principal Investigator

- PIDLR — Post-Investigation Debrief and Lessons Record

- PIR — Performance Indicator Record

- POT — PI Oversight Template

- PRISMA — Preferred Reporting Items for Systematic Reviews and Meta-Analyses

- PROM — Patient-Reported Outcome Measure

- PSEAR — Participant Screening and Eligibility Assessment Record

- QA — Quality Assurance

- QbD — Quality by Design

- QC — Quality Control

- RACI — Responsibility Assignment Matrix (Responsible, Accountable, Consulted, Informed)

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



# List of Tables

**Table 3.1** Site-level regulatory gaps

**Table 3.2** Site-level CtQ domains

**Table 3.3** Organizational environment

**Table 3.4** Design requirements (origin)

**Table 4.1** Design requirements and framework components

**Table 4.2** The scalability model

**Table 4.3** The twenty-four instruments

# List of Figures

**Figure 4.1** The quality lifecycle

**Figure 4.2** The twenty-four instruments grouped by pillar

**Figure 4.3** Instrument granularity and the information chain

**Figure 4.4** Instruments mapped against CtQ domains

**Figure 4.5** Instruments mapped against design requirements
