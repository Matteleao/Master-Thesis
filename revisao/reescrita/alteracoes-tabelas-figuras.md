# Alterações nas tabelas e figuras (imagens)

As tabelas e figuras estão em imagem, por isso eu não consigo editar o conteúdo delas. As legendas e as remissões já estão corrigidas no texto. Esta lista é o que **você** precisa mudar nos arquivos de origem das imagens. Está em ordem de gravidade dentro de cada tabela: primeiro o que é erro de fato, depois a coerência com o texto novo, por último a grafia.

Convenções que valem para todas:
- **Grafia americana:** *centre* → *center*, *standardised* → *standardized*, *specialised* → *specialized*, *authorisation* → *authorization*, *programme* → *program*, *enrolment* → *enrollment*, *recognise* → *recognize*, *afterwards* → *afterward*.
- **Sem hífen depois de *non*, *re*, *under*:** *non-compliance* → *noncompliance*, *non-conformity* → *nonconformity*, *non-comparable* → *noncomparable*, *re-consent* → *reconsent*, *Under-reporting* → *Underreporting*, *Non-hospital* → *Nonhospital*, *Non-academic* → *Nonacademic*.
- ***architecture* → *framework*** em todas.
- **Construções "X, not Y" / "instead" / "rather than"** saem (a sua regra R3). Abaixo vai a sugestão de cada uma.

## Tabela 3.1 (lacunas)

| Onde | Hoje | Trocar por | Por quê |
|---|---|---|---|
| Cabeçalho da 2ª coluna | What the instruments require instead | What the instruments require | R3 (*instead*) |
| Lacuna 3, título | No monitoring of the surgical learning curve during conduct | No site-level observation of the surgical learning curve during conduct | P2 (lacuna estreita) |
| Lacuna 3, texto | All three governing instruments treat investigator competence… [59, 61]. | None of the three instruments assigns the site the case-by-case observation of each operator's proficiency during conduct. Investigator competence is established before the investigation, and keeping an adequate team (ISO 14155:2026, Clause 10.6) is a staffing duty. Published surveys indicate that learning effects are rarely analyzed or reported [70, 71]. | **F3: as referências [59, 61] estão erradas** (aneurisma e manguito rotador); P2; F10 |
| Lacuna 5, 1ª frase | The MDR states a reactive corrective and preventive action (CAPA) duty, and only for significant non-compliance. | ICH E6(R3) (Section 3.12.2) asks the sponsor for root cause analysis and corrective and preventive action (CAPA) when significant noncompliance is found. | **F6: o MDR não contém esse dever**; a formulação é da ICH E6(R3) |

## Tabela 3.2 (domínios CtQ)

| Onde | Hoje | Trocar por | Por quê |
|---|---|---|---|
| Domínio 4, ameaça | Broken patient and device link, UDI and MDR non-compliance | Broken patient and device link, loss of unit-level traceability, and MDR noncompliance | **F13: o Art. 27(1) do MDR exclui os dispositivos em investigação do sistema UDI** |
| Domínio 8 | patient-reported outcome (PRO) | patient-reported outcome measure (PROM) | Terminologia fixa (PROM) |
| Domínio 2 | Ineligible enrolment | Ineligible enrollment | Grafia |
| Domínios 3, 8, 10, 12 | re-consent; non-comparable; Under-reporting; non-compliance | reconsent; noncomparable; Underreporting; noncompliance | Hífen |

## Tabela 3.3 (ambiente organizacional)

- Conferir os rótulos *Non-hospital* / *Non-academic* → *Nonhospital* / *Nonacademic*, iguais ao texto.

## Tabela 3.4 (requisitos de conceção)

| Onde | Hoje | Trocar por | Por quê |
|---|---|---|---|
| DR10, requisito | …and no CtQ function may depend on a single individual. The architecture must hold… | …and every CtQ function must have a named substitute. The framework must hold… | **P9** (a sua decisão) |
| DR10, *Derived from* | Team size and the personification of quality (§3.4.5) | Small team; quality knowledge held by few people (§3.4.5) | C8 (agora a 3.4.5 diz isso com essas palavras) |
| DR2 | separate from and not duplicating the sponsor's trial-level risk assessment | separate from the sponsor's trial-level risk assessment, without duplicating it | R3 |
| DR3 | as a trajectory monitored during conduct and not as a state established at baseline | as a trajectory monitored during conduct, specific to surgeon, procedure, and device | R3 |
| DR4 | positioned as complementary to sponsor monitoring and not as a duplicate of it | complementary to sponsor monitoring, without duplicating it | R3 |
| DR5 | and not reactively once significant non-compliance has occurred | before significant noncompliance occurs | R3 + hífen |
| DR11 | instead of replacing it; centre's | and must reuse the center's existing documentary system | R3 + grafia |
| DR6, DR7, DR12 | afterwards; standardised; centre | afterward; standardized; center | Grafia |
| DR1, DR2, DR4, DR7, DR10 | architecture | framework | Terminologia |

Os rótulos *"Research as a secondary activity (§3.4.5)"*, *"All three features of the target center (§3.4.5)"* e *"The CAPA cycle (§3.2.1)"* agora estão certos, porque o texto novo da 3.4.5 e da 3.2.1 diz exatamente isso. Não precisam mudar.

## Tabela 4.1 (requisitos × componentes)

| Onde | Hoje | Trocar por | Por quê |
|---|---|---|---|
| DR1 | The four pillars as one architecture, with the PI Oversight Plan and the criticality-coded delegation log | The four pillars, with the PI Oversight Template (POT) and the Criticality-Coded Delegation Matrix (CCDM) | C9: nomes iguais aos da Tabela 4.3 |
| DR3 | Surgical Learning Curve Tracking | Surgeon Learning Curve Tracking Log (SLCT), supported by the Surgical Credentialing Record (SCR) | C9 |
| DR4 | Internal Monitoring Plan and its nine review checks | Internal Monitoring Plan (IMP) and Internal Monitoring Checklist (IMC), with nine review checks | C9 |
| DR5 | CAPA cycle and self-inspection schedule | CAPA Log and periodic self-inspection | C20 |
| DR6, coluna *Section* | 4.4.1, 4.6.2 phase 4, 4.3.2, 4.3.3 | 4.4.1, 4.6.1 (Phase 4), 4.3.2, 4.3.3 | C9 (a Fase 4 está na 4.6.1 e na Figura 4.1) |
| DR6 | Intraoperative traceability and deviation capture | Intraoperative Checklist and Device Log (ICDL) | C9 |
| DR7 | Imaging standardization in four elements | SIRR and IQL (imaging standardization), and the PSEAR (structured eligibility verification) | C9 |
| DR9 | where it carries leverage | where it has most effect | Vocabulário |
| DR10, requisito | Quality functions explicitly assigned, with authority distinct from task-level responsibility | Copiar o DR10 inteiro da Tabela 3.4, já com o substituto nomeado | **P9** |
| DR10, componente | Minimum functional delegation architecture and the responsibility matrix, with institutional memory as a by-product | Six named functions with named substitutes (CCDM and RACI matrix), and site records that survive staff changes | P9 + terminologia |

## Tabela 4.2 (antiga 4.3: escalabilidade)

- **Renumerar** para Tabela 4.2 (não existe Tabela 4.2 hoje; C6).
- Cabeçalho do Tipo B: acrescentar *(target center)*.
- Grafia: *specialised*, *centre*, *authorisation*, *programme*, *non-conformity*.

## Tabela 4.3 (antiga 4.4: os 24 instrumentos)

| Onde | Hoje | Trocar por | Por quê |
|---|---|---|---|
| Número | Table 4.4 | Table 4.3 | C6 |
| SCML, *How it works* | referencing those records **rather than** repeating their content | referencing those records without repeating their content | O único *rather than* literal da tese |
| SLCT, *How it works* | against the complexity of each case, not against a fixed count | against the complexity of each case, with no fixed count | R3 |
| ICDL, *How it works* | Records times, components, UDI and lot | Records times, components, device identifiers (UDI where the device carries one) and lot | F13 |
| CAPA, *Purpose* | needs correction and prevention, not a one-off fix | needs correction and prevention beyond the single case | R3 |
| FUCR, *Purpose* | across a cohort and a period, not one visit at a time | across a cohort and a period | R3 |
| PIDLR, *Purpose* | into a controlled lesson, not an informal memory | into a controlled lesson | R3 |
| CAPA, nome | Corrective and Preventive Action Log (CAPA) | sem mudança no nome; no texto agora é sempre "CAPA Log" (instrumento) e "CAPA" (método) | C20 |

## Figura 4.1 (ciclo de vida)

- **Fase 1:** acrescentar "Site Risk Register (SRR) opened". (C5: o texto diz que o SRR abre na Fase 1.)
- **Fase 2:** acrescentar "SLCT prepared for each delegated surgeon". (C5)
- **Fase 4:** acrescentar "SLCT entry for each case"; trocar "UDI, lot, model" por "device identifiers, lot, model". (C5; F13)
- **Fase 5:** "Patient-reported outcomes" → "PROMs".
- **Fluxo de segurança:** "recognise" → "recognize".

## Figura 4.3 (granularidade)

- A figura em si está certa. A legenda dizia que os Operational Controls aparecem em quatro grupos, incluindo a segurança, mas a linha *Safety stream* só tem o SART, que é de Risk Management. **A legenda já foi corrigida no texto** (C18).

## Figura 4.5 (instrumentos × requisitos)

- A legenda fala em *"an extension added to the original set"*. Isso descreve a história do rascunho (R19). **Precisa da sua confirmação:** o que o marcador tracejado quer dizer? Se for "o instrumento estende um requisito além da resposta principal", eu reescrevo a legenda com isso.
