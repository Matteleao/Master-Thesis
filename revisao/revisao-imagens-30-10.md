# Revisão das tabelas e figuras (30/10)

Base: `Tese_completa_30-10.docx`. Os números de citação abaixo já seguem a numeração nova (110 referências).

## Regras que valem para todas as imagens

1. **Alinhamento.** A sua regra para as tabelas é: primeira coluna e cabeçalho centralizados, demais colunas à esquerda e todas centralizadas na vertical. Hoje as Tabelas 3.1, 3.2 e 3.4 têm a primeira coluna à esquerda, enquanto 4.1, 4.3 e 5.2 a têm centralizada. Uniformizar.
2. **Cor.** Proponho uma regra só: a cor identifica o pilar e aparece num único lugar de cada figura (a barra ou faixa do pilar). Siglas, marcadores e texto ficam em preto ou cinza-escuro. Assim as figuras 4.2, 4.3 e 4.4 conversam com as tabelas (cabeçalho preto, linhas creme).
3. **Ortografia americana.** Nas imagens aparecem "enrolment", "recognise" e "theatre"; o texto usa a grafia americana.
4. **Resolução.** Exportar tudo em PNG com pelo menos 2000 px de largura. A Tabela 3.4 hoje é um EMF com um bitmap de 940 px. Fica borrada e some quando o arquivo é convertido fora do Word (no PDF gerado pelo LibreOffice ela sai em branco).
5. **PRO e PROM.** A Tabela 3.2 usa "PRO", a Tabela 4.1 e o capítulo 4 usam "PROM", e a 3.4.1 usa "PROs". Escolher um termo para as imagens. Sugiro PROM quando se fala do instrumento de medida e PRO quando se fala do desfecho.

---

## Tabela 3.1 (lacunas regulatórias)

Concordo que tem texto demais. A explicação de cada lacuna já está na 3.2, logo abaixo da tabela, então a tabela pode dizer o essencial em uma linha.

**Problemas atuais**
- A Lacuna 3 cita ^59,61^. A 61 (PROVIDENT) trata de imagem e não sustenta a frase. O texto da 3.2 sustenta a mesma afirmação com 35, 36, 37 e 39. Sugiro tirar a citação da tabela, já que o texto ao lado a carrega.
- O cabeçalho "What the instruments require instead" soa estranho. Sugiro "What the instruments provide".

**Versão proposta**

| Regulatory gap | What the instruments provide |
|---|---|
| 1. No structured site-level QMS | Quality duties spread across the PI and the site team; clinical quality management assigned to the sponsor |
| 2. No site-level risk register or risk-management cycle | Ongoing risk management of the investigation, led by the sponsor |
| 3. No monitoring of the surgical learning curve during conduct | Surgeon competence confirmed as a qualification before the investigation starts |
| 4. No internal, site-initiated monitoring function | Monitoring planned and run by the sponsor; the site supports it and applies the corrective actions it receives |
| 5. No proactive site-level continuous-improvement cycle | Corrective action after significant noncompliance (MDR) and ongoing risk review (ISO 14155:2026), with no improvement cycle owned by the site |

---

## Tabela 3.2 (domínios CtQ)

Nada de estrutura a mudar; só acabamento.
- Domínio 12: "Regulatory compliance, deviation management" deve ser "Regulatory compliance and deviation management", que é o nome na planilha (aba Domínios).
- Vírgula serial: o domínio 1 a tem ("capability, readiness, and capacity"), mas os domínios 4, 6, 7, 9 e 11 não. Exemplos: "Device management, accountability, and traceability"; "Training, credentialing, and learning-curve control".
- "rehab staffing" → "rehabilitation staffing"; "enrolment" → "enrollment".
- "re-consent", "non-compliance", "non-comparable" → "reconsent", "noncompliance", "noncomparable" (regra da skill: sem hífen depois de re/non).

---

## Tabela 3.3 (ambientes organizacionais)

Está certa. Um detalhe: o cabeçalho "Site records" mostra números com porcentagem; trocar para "Site records, n (%)".

---

## Tabela 3.4 (requisitos de projeto)

Concordo: título curto e, se precisar, uma frase depois. Os títulos abaixo são os mesmos da Figura 4.4, para as duas peças usarem o mesmo nome; troquei só o DR9, cujo nome atual ("Activation at peak leverage") é jargão.

| # | Design requirement | Derived from |
|---|---|---|
| DR1 | **Site quality system.** One documented system that brings together the investigator duties the instruments distribute across separate clauses | Normative gap: Gap 1 (Section 3.2). Supporting analysis: position of the site in the conformity assessment chain (Section 3.2.1) |
| DR2 | **Prospective local risk.** Identification, rating, ownership and review of the risks created by the site's own processes, separate from the sponsor's trial-level assessment | Normative gap: Gap 2 (Section 3.2). CtQ domains: all twelve (Section 3.3). Supporting analysis: documented risk cycle of the other actors in the chain (Section 3.2.1) |
| DR3 | **Operator proficiency.** Proficiency followed as a trajectory during conduct, by surgeon, procedure and device | Normative gap: Gap 3 (Section 3.2). CtQ domains: 5, 6 (Section 3.3). Structural conditions: operator dependence (Section 3.4.1); clustering and learning during conduct (Section 3.4.2) |
| DR4 | **Site-initiated verification.** Internal verification of the point-of-care domains that external monitoring cannot reach in time, complementary to sponsor monitoring | Normative gap: Gap 4 (Section 3.2). CtQ domains: 4, 5, 9, 10 (Section 3.3). Structural condition: traceability as a point-of-care obligation (Section 3.4.3) |
| DR5 | **Closed-loop correction.** Correction triggered by defined thresholds and periodic self-inspection, before significant noncompliance occurs | Normative gap: Gap 5 (Section 3.2). CtQ domain: 12 (Section 3.3). Supporting analysis: the CAPA cycle (Section 3.2.1) |
| DR6 | **Capture at generation.** Data that cannot be reconstructed later (device and production identifiers, intraoperative deviations and substitutions, immediate postoperative imaging) are recorded when they arise | CtQ domains: 4, 5, 9 (Section 3.3). Structural conditions: irreversibility and unit-level traceability (Section 3.4.1); point-of-care capture (Section 3.4.3) |
| DR7 | **Measurement variance control.** The site controls its own sources of measurement variance: acquisition, assessor qualification, local review, and timing and mode of assessment | CtQ domains: 8, 9 (Section 3.3). Structural conditions: operational weight of follow-up; limited classification reliability (Section 3.4.1) |
| DR8 | **Indicators that expose drift.** Indicators show process drift while correction is still possible and support analysis of cause, recurrence and concentration | CtQ domains: 2, 7, 10, 11 (Section 3.3). Structural conditions: irreversibility; operational weight of follow-up (Section 3.4.1); concentration of cases under one operator (Section 3.4.2) |
| DR9 | **Timing by phase.** Each instrument is assigned to the phase in which it acts | Structural conditions: irreversibility (Section 3.4.1); learning during conduct (Section 3.4.2); data that cannot be recovered once lost (Section 3.4.3) |
| DR10 | **Functions and accountability.** Quality functions assigned, with authority kept apart from task-level responsibility, no function resting on one person, and a dated site record of decisions that survives changes of staff and monitor | CtQ domains: 1, 6 (Section 3.3). Operating conditions: investigator turnover (Section 3.4.4); research duties shared among clinical staff (Section 3.4.5) |
| DR11 | **No capital investment.** Runs on the site's existing documentary system, without new software, staff or infrastructure | CtQ domain: 11 (Section 3.3). Operating conditions: no dedicated research or quality function (Section 3.4.5); organizational environment of the sites (Section 3.4.4) |
| DR12 | **Scalable depth.** Depth matched to the center's resources and the investigation's risk, with the same complete and consistent documentation trail at every level | Normative gap: Gap 1 (Section 3.2). Operating conditions: design assumptions of the target center (Section 3.4.5); distribution across organizational environments (Section 3.4.4) |

**Verificação da coluna "Derived from"**

Conferi contra a seção 3.5, o capítulo 4, a Figura 4.4 e a planilha `derivacao-ctq-site-v5.xlsx` (abas Domínios e Lacunas). Está correta nos pontos que importam:
- Lacunas 1 a 5 → DR1 a DR5, na mesma ordem da aba Lacunas.
- Domínios 5, 6, 8 e 9 → DR3, DR6 e DR7.
- DR8 ← domínios 2, 7, 10 e 11; DR5 ← domínio 12; DR10 ← domínios 1 e 6. Bate com o capítulo 4.
- O consentimento (domínio 3) só aparece em DR2, como diz a 3.5.

Dois ajustes já estão na versão proposta acima:
1. **Rótulo.** A tabela chama tudo de "Operating condition(s)", mas o texto separa as condições estruturais (3.4.1 a 3.4.3) das condições de operação do centro-alvo (3.4.4 e 3.4.5). Na proposta: "Structural condition" para DR3, DR4 e DR6 a DR9, e "Operating condition" para DR10 a DR12.
2. **Condição sem destino.** A condição 4 da 3.4.1 (o peso operacional do seguimento) não aparecia em nenhum DR. Ela sustenta o DR7 (mesma avaliação em todas as visitas) e o DR8 (indicador de adesão ao seguimento, domínio 7), e entrou nos dois.

A planilha não tem uma aba que ligue os DRs às origens; essa ligação existe só na tese. Se o repositório for servir para verificação, vale acrescentar uma aba "Requisitos" com esta tabela.

---

## Tabela 4.1 (funções)

Concordo, não há muito o que cortar. Acabamento:
- "Operating room staff" usa imperativo ("Prepare… Record…"), enquanto as outras linhas usam a terceira pessoa ("Supports…", "Conducts…"). Passar para "Prepares… Records…".
- "Clinical." no início da célula do coordenador fica solto. Sugiro "No clinical authority. Does not decide eligibility, interpret safety information, or classify a PD."
- "Data QA": QA não está na lista de abreviaturas. Escrever "Data quality assurance" ou acrescentar a sigla.

---

## Figura 4.1 (ciclo de vida)

- **Paleta.** Não consegui abrir o Claude Design: a ferramenta que tenho só sincroniza projetos de design system e não acessa as suas figuras. A versão em tons pastel também não está em nenhum arquivo que eu tenha. Me mande o PNG ou o link compartilhado que eu coloco no lugar.
- **Conteúdo, o mais importante.** Duas frases contradizem a decisão do ciclo de revisão (frequência definida pelo site, mais revisões por gatilho):
  - em "Follow-up": "completion monitored monthly";
  - em "Transversal safety stream": "Safety trend analysis at least monthly".

  Sugestões: "completion monitored at the frequency the site sets" e "Safety trend analysis at the frequency the site sets, feeding the signal surveillance of Section 4.3.3".
- "recognise" → "recognize"; "theatre" → "operating room".
- "Transversal safety stream" → "Cross-phase safety stream" ("transversal" é um decalque do português).

## Figura 4.2 (instrumentos por fase)

Concordo com você e iria até o fim: siglas e marcadores em preto ou grafite, a cor só na barra do pilar e numa faixa de grupo bem clara (ou branca). A coluna "S" pode manter o fundo rosado, porque ali a cor carrega significado (o fluxo de segurança). O conteúdo bate com o texto: 15 instrumentos atuam no start-up, como diz a 5.4.2.

## Tabela 4.2 (escalabilidade)

- **Proxy.** A definição está no texto, na 4.7: "Where the site does not use a separate instrument, an existing record takes on its control function. Table 4.2 identifies this proxy for each instrument omitted from a minimum set." Está definido; se quiser deixar mais explícito, dá para trocar a primeira frase por "…an existing record, its proxy, takes on its control function".
- **Linhas.** As linhas misturam pilares (Governance, Performance Oversight) com temas (Risk register and complication surveillance, Procedural competence and stability, Operational quality review and imaging). Por isso SCR e TRE aparecem duas vezes (em Governance e em Procedural competence). O DTRM está em Governance na Figura 4.2, mas na linha "Procedural competence" do nível acadêmico. Proponho usar os quatro pilares como linhas, na mesma ordem da Figura 4.2 e da Tabela 4.3, com o SLCT em Risk Management. As contagens (12, 18, 24) continuam iguais; conferi.

## Tabela 4.3 (os 24 instrumentos)

- SCR, coluna Inputs: "Formation" é decalque de "formação"; trocar por "Education".
- IMP, coluna Inputs: "The domains, CtQs, and sources" → "The CtQ domains and sources".
- PFVR:
  - "Records one participant's one follow-up visit" → "Records one follow-up visit of one participant";
  - "Compares what was obtained, imaging, tests, PROMs, assessment, against what was required" → "Compares the assessments obtained (imaging, tests, PROMs) with those the protocol requires".

## Figura 4.3 (níveis da informação)

Concordo que está carnavalesca, e há três problemas além da cor:
- Na coluna do PIR, "protocol deviation rate" e "surgeon procedural consistency" estão na mesma célula, sem divisória. Parece um indicador só; são seis indicadores e a figura mostra cinco caixas.
- O painel de baixo ("The information chain") repete o cabeçalho de cima. É informação desnecessária: dá para tirar e levar a seta tracejada de retorno para o cabeçalho.
- "INFORMATION RISES" com seta para a direita: a informação anda na horizontal. Trocar por "Information flows" ou girar a figura. A legenda da figura no texto diz "Arrows show information moving up"; eu ajusto para "moving across" quando você fechar a imagem.

Para ficar sóbria: as caixas das siglas em branco com contorno cinza, e só o marcador do pilar colorido em cada linha.

## Figura 4.4 (cobertura)

- **Cor.** Concordo que está carregada: o fundo colorido em todas as colunas, mais os marcadores coloridos, dobram a informação. Proposta: marcadores em preto, colunas sem fundo, cor só na faixa do cabeçalho de cada pilar (como na Tabela 4.3). Cheio e vazio já carregam o significado.
- **DR6.** O SLCT e o SCML aparecem como resposta direta ao DR6 ("Capture at generation"), mas a Figura 4.3 os coloca em "Synthesis": eles leem registros feitos por outros. Sugiro passar os dois para marcador vazio e manter cheios o ICDL e o IQL.
- O DR9 passa a "Timing by phase", como na Tabela 3.4 proposta.

O resto confere com o texto da 4.8: todo domínio tem um instrumento com marcador cheio e toda coluna tem pelo menos um marcador cheio.

## Tabela 5.1 (literatura)

Está boa. Só trocar os números de citação (lista na mensagem anterior):

| Antigo | Novo |
|---|---|
| 74 | 87 |
| 77 | 90 |
| 79 | 92 |
| 86 | 99 |
| 89 | 101 |
| 90 | 102 |
| 91 | 105 |

## Tabela 5.2 (falhas)

Entendi o "essa tabela tem que ser revista na totalidade" como sendo a 5.2, já que você disse que a 5.1 está ótima. Se era outra, me diga.

**O que não funciona hoje**
- A coluna "Phase" mistura fases ("Feasibility", "Enrollment") com grupos ("Start-up and conduct", "Conduct"), que não são fases do ciclo de vida.
- Faltam Follow-up e Continuous improvement.
- A linha "Lessons recorded without a change in procedures" pertence à fase 7, não ao close-out.

**Proposta.** Fazer dela, de fato, a avaliação de risco do próprio framework, como diz a 5.3.3, usando a lógica do SRR. As linhas seguem as sete fases e os três grupos da Figura 4.1. A nova coluna "How the site would notice" mostra a detecção, que hoje falta.

| Phase | Failure | What is lost | How the site would notice | Guard in the design |
|---|---|---|---|---|
| Feasibility | Implementation level set below the risk of the investigation | Controls where the risk is highest | Signals at the first milestone review | The level is recorded and justified at the end of start-up, where the sponsor can see it |
| Start-up | Risk register copied from the sponsor's risk list | The local risks | Entries without a local cause or owner | Each entry names a local cause and an owner from the RACI |
| Start-up | Training recorded as attendance only | Assurance that a person can perform a critical task | Delegation active without a release record | Release recorded separately from attendance; it activates the delegation |
| Start-up | Indicator rule changed after the data are known | The purpose of the indicator | Rule dated after the period it judges | Rules are dated, and a later change applies only to future periods |
| Enrollment | Eligibility evidence completed after the decision | The record of what was known at inclusion | Evidence dated after the decision in the PSEAR | The PSEAR records when each piece of evidence became available |
| Surgery | ICDL completed after surgery from the operative note | Capture when the data arise | Completion time later than the procedure | Internal verification checks the timeliness of operative records |
| Surgery | Learning curve log kept but not reviewed | Detection of drift | Review points passed without a recorded review | Review points fixed by case number |
| Follow-up | Visit window missed without warning | Endpoint data at that time point | Missed and delayed visits in the FUCR | Alerts before a window closes; follow-up compliance indicator |
| Follow-up | Image acquired outside the charter and found only at central reading | The chance to reacquire | IQL decision at acquisition | Image quality checked at acquisition, while reacquisition is still possible |
| Conduct (3–5) | Review by someone who depends on the person reviewed | Independence of review | Not detectable from the records | Only the rule that nobody reviews their own work |
| Conduct (3–5) | Departure of the person who runs the instruments | Continuity of every control that person held | Function without an active holder in the RACI | A named backup for each function in the RACI |
| Conduct (3–5) | Instruments run as parallel records | A single authoritative value for each datum | Discrepancies between instrument and source | The source rule and the source map made before enrollment |
| Close-out | Proxies held in sponsor systems lost after close-out | Part of the site's history | Records the site no longer has access to | A copy of the proxy records kept under site control at close-out |
| Continuous improvement | Lessons recorded without a change in procedures | Learning across investigations | PIDLR items with no owner or change | The PIDLR feeds the revision of standing procedures |

As linhas novas usam só elementos que o texto já descreve: os alertas de janela (Figura 4.1), a checagem de imagem na aquisição (IQL) e a cópia das proxies (5.4.1). Se a tabela mudar, a frase da 5.3.3 continua valendo.

## Tabela 5.3 (proposições)

Concordo em tirar o "Refuted if". Além disso, hoje a tabela contradiz o próprio texto: a 5.3.4 diz que as condições de refutação ficam "left open on purpose", porque cada site decide quantos períodos observar, e a tabela as fixa. Com três colunas (Proposition, Mechanism, Measure), texto e tabela passam a dizer a mesma coisa. A legenda ("testable propositions") continua correta, porque a coluna Measure é o que torna cada proposição testável.

Sobre a repetição com a Tabela 4.3: não vejo sobreposição. A 4.3 descreve cada instrumento (entrada, funcionamento, saída). A 5.3 descreve efeitos do conjunto e como medi-los. Algumas medidas nem vêm de instrumento algum, como o tempo de monitoria por visita e as horas de close-out.

## Tabela 5.4 (persistência)

Está correta e o texto em volta bate:
- 15 instrumentos atuam no start-up (conferi na Figura 4.2);
- uma estrutura de funções, um histórico de treino, um log de CAPA e uma reunião de supervisão para todas as investigações;
- registros de participantes separados por investigação.

O parágrafo amarelo "[Number to compute…]" foi apagado.

## Figura 5.1

Sem mudanças além das já apontadas: "Protocol" → "CIP" e "Trial" → "investigation", para seguir a terminologia de dispositivos da tese.
