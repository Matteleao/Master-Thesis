# Lente 4 — Ghost-writer consistency-check (Onda 1)

## 1. Cabeçalho

**Lente.** Auditoria de consistência entre capítulos, no protocolo `ghost-writer:consistency-check` (SKILL.md do plugin). O protocolo pede seis verificações: deriva de termos, afirmações contraditórias, promessas quebradas, exemplos repetidos, deriva de tom e coerência do arco. A tarefa acrescentou três inventários: abreviaturas, números ditos mais de uma vez e referências cruzadas.

**Adaptação do protocolo.** Ainda não existem `book-memory.md` nem `demolition-history.md`. Por isso li o texto inteiro, e não os resumos, e montei o inventário antes de começar as verificações (seção 4 deste arquivo). Como o protocolo manda, as seis categorias saem consolidadas no livro-razão (seção 3). Não incluí a pergunta final do protocolo ("Which of these do you want to address first?"), porque nesta onda a lente só produz análise.

**Hierarquia aplicada.** (1) `.claude/skills/thesis-writing/SKILL.md`; (2) `revisao/projeto/contrato-apodictic.md`; (3) `revisao/projeto/style-rules.md` (R1 a R26); (4) `revisao/guia-de-estilo.md`, só as seções 1, 2, 3 e 5. A terminologia fixa da seção 3 do guia foi a régua da deriva de termos. Nada cobrado da tese ultrapassa as cinco anti-ideias do contrato. O que sinalizo além delas é desproporção (afirmação que excede o que a própria tese mostra).

**O que li.**
- `tese/00-elementos-pre-textuais.md` (Resumo, Abstract, Lista de Abreviaturas, Listas de Tabelas e Figuras) e `tese/01` a `tese/06`, inteiros.
- Imagens: Tabelas 3.1, 3.2, 3.3, 3.4, 4.1, 4.3 e 4.4 (partes 1 e 2); Figuras 4.1 a 4.5; todas com as legendas do texto.
- `tese/07-references.md`, consultado só para ver a que obra corresponde cada número em quatro conflitos de numeração ([9], [37], [39], [41], [59], [61], [70], [71]). Não verifiquei o conteúdo das obras.
- `tese/08-appendices.md`, consultado só por busca, para confirmar que o Apêndice Y citado em 4.6.2 existe. Não revisei o conteúdo, porque os apêndices estão fora do escopo.

**O que não li, por independência.** `revisao/diagnostico.md`, a seção 4 do guia, `revisao/fase-0/` e os outros arquivos de `revisao/analise-v2/`. Não usei git.

**Limites desta execução.**
- Nada foi conferido nas fontes primárias (ISO 14155:2026, MDR, artigos). Quando duas passagens da tese se contradizem sobre uma fonte, digo que é contradição e não decido qual lado está certo. Esses casos vão marcados como *não verificável* e ficam para a lente 1.
- As contagens (regressões a forma por extenso, ocorrências de *architecture* etc.) saíram de busca no texto. Alguns usos são legítimos, então os números são aproximados.
- As estimativas de palavras redundantes vêm da contagem dos parágrafos envolvidos, menos as frases que trazem conteúdo novo. São ordem de grandeza, não medição.
- As imagens foram lidas visualmente e estavam legíveis. Trechos citados de imagem vêm marcados "(imagem)" e não puderam ser conferidos por busca.
- Os trechos citados de arquivos de texto foram conferidos por script contra o texto da tese, com normalização de espaços, asteriscos e barras de escape do markdown.

**Severidade.** *Must* = erro factual, ou contradição que um membro do júri pode usar contra o método, a cadeia rastreável ou um número não negociável, ou texto inacabado à vista. *Should* = enfraquece claramente. *Could* = melhoria.

## 2. Resumo da lente

- **A cadeia rastreável se contradiz em quatro juntas.** O contrato exige que essa cadeia fique cristalina. (a) O critério de seleção dos requisitos: 2.5 diz que obrigação já existente "adds nothing", enquanto 3.5, 4.3.3, 4.7.1 e 5.1 dizem que o framework organiza obrigações existentes (C-009). (b) A origem dos requisitos: 3.5 diz que "all three came from the clause comparison" (C-006). (c) A fonte dos quatro pilares, com cinco versões diferentes em 2.5.1, 3.2.1, 4.1, 5.1 e 6 (C-008). (d) A atividade DSRM a que os requisitos pertencem (C-003).
- **O centro-alvo não está fixado.** 3.4.5 descreve um centro não hospitalar no nível mínimo de implementação. 4.7.1 diz que o alvo é o Tipo B, com implementação completa. 5.7 quer testar em centros Tipo B (C-007). A variável "permanent infrastructure", que sustenta 38/65 e 187/235, remete a uma definição que não existe em 2.4.2 (C-005) e muda de sentido entre capítulos (C-031). A Conclusão diz "one in four", quando o dado é 38/235, cerca de um em seis (C-001).
- **Números e citações.** O mesmo Delphi aparece com 21 participantes (1.4.1) e com 71 (5.2) (C-002). A lacuna 3 da Tabela 3.1, a mais importante da tese, cita [59, 61], dois estudos de concordância de imagem, em vez de [70, 71] (C-010). Fora isso, os números do registro conferem nas dez reapresentações (inventário 4.4).
- **Texto inacabado à vista.** Há um marcador de pendência ética em 2.4.1 (C-013), uma frase "Section 3.4.4 has to state…" em 5.7 que 5.3 dá como já feita (C-012) e resíduos de versões anteriores: "our earlier set of five indicators", "earlier instrument", "original set", e uma descrição do SLCT que já não existe no texto (C-044, C-045, C-087).
- **Deriva de termos contra a seção 3 do guia.** O artefato aparece como framework, architecture e model (C-017). O pilar 2 aparece como RBQM (C-016). As cinco condições têm três nomes cada (C-015). Há PRO e PROM (C-018), e os nomes dos instrumentos fogem da Tabela 4.4 (C-019). A prosa do Capítulo 4 não nomeia nenhum dos 24 instrumentos (C-020), e o DR3, requisito da única lacuna sem obrigação correspondente, nunca aparece na prosa (C-056).
- **Abreviaturas.** Há cerca de 60 regressões à forma por extenso depois da definição, cerca de 55 delas no Capítulo 5, que parece ter sido escrito para ser lido isolado (C-041). RACI e CAPA têm dois significados cada (C-040). SAE e CRF são usados sem definição no texto (C-079).
- **Referências cruzadas.** Conferi cerca de 125 remissões, agrupadas em 70 linhas no inventário 4.5. Treze linhas estão quebradas, entre elas a definição prometida em 2.4.2, o termo "proactive" atribuído a 2.2.2, os três temas de 2.3.2, a coluna prometida da Tabela 3.2, a "Section 1.2" da Conclusão e a Tabela 4.2, que não existe. Outras quinze são imprecisas.
- **Afirmações proporcionais contraditas.** 3.2 diz que a comparação ICH × ISO "has not been done in the published literature", contra o limite que 2.3.2, 2.6, 5.2 e 5.7 fixam (C-014). 5.2 afirma maior dependência do operador que 1.4.2 tinha recusado afirmar (C-028). 5.4 diz que a instância local "acts first", contra 4.3.3 (C-029). 5.3 transforma suposições de projeto em fatos (C-030). 4.7 fala em prevalência que 3.4.4 diz não poder estabelecer (C-032).
- **Redundância de cerca de 1.500 a 1.700 palavras.** Ela se concentra no Capítulo 5: 5.2 reconta 1.4 (cerca de 500 palavras) e 5.3 reconta 3.4 (cerca de 390). É o corte mais barato rumo à R25 e o que mais ajuda o Capítulo 5 a cumprir a regra da Discussão.
- **Deriva de tom.** O Capítulo 2 está mais solto e menos revisado (C-042). O Capítulo 4 tem uma camada ensaística em molde fixo, com "X is harder than Y" cinco vezes e "the difficulty" quatro (C-043). 5.1 e 5.5 sobem para um registro aforístico e retórico (C-066). O "we" da Introdução aparece em 1.3 (C-065).

## 3. Livro-razão

Contagem: **92 achados**, sendo **13 Must, 43 Should e 36 Could**. A ordem é por severidade. Nas colunas Trecho e Problema, o texto entre aspas retas é citação literal da tese; propostas em inglês vão em itálico.

| ID | Seção | Trecho literal | Problema | Tipo | Severidade | Critério | Proposta (opcional, em inglês) |
|---|---|---|---|---|---|---|---|
| C-001 | 6 | "roughly one in four in the sample examined, present no publicly documented permanent research structure" | 38 de 235 é 16,2% (3.4.4), ou seja, cerca de um em seis. "One in four" corresponde aos 65 não hospitalares (27,7%), não aos que não têm estrutura. A seção 3 do guia já decidiu que o texto se ajusta a 38/235. | F | Must | thesis-writing: numbers traceable; guia §3 (outras decisões) | *roughly one in six organizations in the sample examined (38 of 235) had no permanent research structure that public sources could establish* |
| C-002 | 1.4.1; 5.2 | "A Delphi process with 21 stakeholders produced 59 strategies" / "A Delphi process with 71 stakeholders produced 59 strategies" | O mesmo estudo [37] aparece com dois tamanhos de painel. Não verificável aqui; a lente 1 deve conferir na fonte e corrigir um dos lados. | F | Must | consistency-check: contradicted claim; thesis-writing: never invent a number | — |
| C-003 | 2.1.1; 2.5; 3.5; 4.1 | "With the creation of those requirements, we complete the first part of the third DSRM activity" / "Section 3.5 states the objectives for a solution, as design requirements DR1 to DR12." | 2.1.1 e 2.5 situam os DR na 2ª atividade (objetivos da solução). 3.5 os põe na 3ª. 4.1 diz as duas coisas na mesma frase: "Chapter 3 closed the second activity of the DSRM… and started the third by designing the requirements DR1 to DR12". O método DSRM é não negociável, e o júri vai perguntar. | C | Must | consistency-check: contradicted claim; contrato (DSRM) | *With these requirements, we complete the second DSRM activity, the definition of the objectives for a solution.* (4.1: *Chapter 3 completed the second DSRM activity… This chapter carries out the third, design and development.*) |
| C-004 | 2.1.1 | "Since this thesis originates from an observed problem of practice, it enters at the first activity." | Viola um não negociável do contrato e a R26: o problema nasce das lacunas encontradas na leitura das diretrizes. Também contradiz 2.1.2, que diz "The regulatory analysis came first and produced the grid of domains that founded the design". | C | Must | contrato (non-negotiables); R26 | *Since this thesis originates from gaps identified by reading the governing guidelines, it enters at the first activity.* |
| C-005 | 3.4.4 | "Permanent clinical trial infrastructure was assessed separately under the definition in Section 2.4.2" | 2.4.2 só define os quatro ambientes, e o Capítulo 2 não define em lugar nenhum "permanent clinical trial infrastructure". Ficam sem definição operacional a variável de 38/65, 27/65 e 187/235 e a própria escolha do centro-alvo (3.4.5). Referência quebrada. | C | Must | consistency-check: broken promise; thesis-writing item 23 | Acrescentar a definição em 2.4.2. O critério tem de vir do autor e não pode ser inventado. |
| C-006 | 3.5 | "each requirement comes from a gap, a domain, or an operating condition, and all three came from the clause comparison in Section 2.2. The chain ends in the instruments, so nothing in the framework is invented." | As condições operacionais vêm da literatura (1.3, 3.4.1) e do registro (2.4, 3.4.4). 2.1.2 descreve três fontes de evidência. Os pilares são "the synthesis adopted in this thesis" (3.2.1), e as condições do centro são "conservative design assumptions" (3.4.5). O próprio 5.1 corrige: "That correspondence shows internal coherence and nothing more". | C | Must | consistency-check: contradicted claim; thesis-writing: proportionality; contrato (cadeia rastreável) | *Each component answers a requirement, and each requirement comes from a gap, a domain, or an operating condition that this chapter derived from the clause comparison, the literature, or the registry.* |
| C-007 | 3.4.5; 4.7.1; 5.7; Tab. 4.3 | "We defined it as a nonhospital organization with limited or uncertain permanent clinical trial infrastructure." / "This is the context the framework was designed for" | 3.4.5 diz que essas condições "define the minimum implementation level", isto é, o núcleo reduzido do Tipo C. 4.7.1 diz que o alvo é o Tipo B (implementação completa, incluindo hospitais). 5.7 propõe testar "in a small number of Type B centers", e 4.2.1 fala em "small or mid-sized centers this framework targets". São quatro descrições do público-alvo. | C | Must | consistency-check: contradicted claim; contrato (3 site types) | Decidir se o centro de 3.4.5 é Tipo B ou C e alinhar 3.4.5, 4.7.1, 5.7 e a legenda da Tabela 4.3. |
| C-008 | 5.1; 2.5.1; 3.2.1; 4.1; 6 | "ISO 13485, ISO 14971, and ISO 15189 each require the same four functions of the organization they govern, and Section 3.2.1 took the taxonomy of pillars from them." | 2.5.1: a ISO 15189 "remained a structural analogy… we did not map its clauses" e "These standards do not state a common four-part taxonomy". 3.2.1 sintetiza a partir de ISO 13485, ISO 14971 e ISO 14155, sem a 15189. 4.1 acrescenta "ICH guidance". 6 lista "the risk function holds ISO 14971". São cinco conjuntos de fontes para os mesmos pilares. | C | Must | consistency-check: contradicted claim; contrato (cadeia rastreável) | *Section 3.2.1 synthesized the four pillars from recurring functions in ISO 13485, ISO 14971, and ISO 14155:2026, which do not state them as a shared taxonomy.* |
| C-009 | 2.5 | "If the ISO 14155, the MDR, or ICH E6(R3) already obliges the site to do something, the framework adds nothing, because the obligation exists." | A regra de seleção (só obrigações novas) é contradita em vários pontos. 3.5: "It takes duties that already exist and makes them workable at the site". 4.3.3: "This component adds timing to an obligation the MDR and ISO 14155 already impose". 4.7.1: "Some of these elements operationalize requirements that ISO 14155:2026 or the MDR already establish". 5.1: "the framework supplies organization where the obligation already exists". | C | Must | consistency-check: contradicted claim; contrato (cadeia rastreável) | *A finding became a design requirement when no instrument requires the site to run it as a structured, documented process, even where the underlying duty already exists.* |
| C-010 | Tab. 3.1, lacuna 3 (imagem) | "published evidence indicates that observation of learning during conduct is rare [59, 61]." | [59] é Patra et al. (core lab × médico assistente, aneurisma) e [61] é Lippe et al. (concordância interavaliador, manguito rotador). O texto (3.4.2) sustenta a mesma afirmação com [70, 71] (Conroy et al.). A numeração está desatualizada justamente na lacuna central. | F | Must | thesis-writing: honesty rules; contrato (learning curve crystal clear) | *…observation of learning during conduct is rare [70, 71].* |
| C-011 | 4.2.4; 4.2.3 | "The sponsor therefore has to document what training exists, and no clause requires the site to verify that the resulting competence is maintained" / "Clause 10.6 further requires the PI to maintain and document an adequate investigation site team" | Duas leituras incompatíveis da ISO 14155:2026 em subseções vizinhas. 4.2.3 também cita "Clauses 10.1 and 10.3 require the PI to ensure team qualification, training, documentation, and oversight". Não verificável aqui; a lente 1 deve conferir as cláusulas. | F | Must | consistency-check: contradicted claim | Se a norma confirmar: *…and no clause specifies how the site verifies that device-specific competence is maintained after release.* |
| C-012 | 5.7; 5.3 | "Section 3.4.4 has to state which of the two governs the argument." / "Section 3.4.4 states which of the two governs the argument" | Nota de trabalho à vista em 5.7 ("has to state"). 5.3 dá a tarefa como feita, mas 3.4.4 não decide se governa o ambiente regulatório europeu ou o fenótipo dos EUA. A promessa está quebrada justamente no limite UE × EUA. | C | Must | consistency-check: broken promise; R19 | Escrever a decisão em 3.4.4 ou 3.4.5 e só então referenciá-la. O conteúdo é decisão do autor. |
| C-013 | 2.4.1 | "[institutional ethics determination or policy citation required]" | Marcador de pendência no texto, precedido de "must be cited here before the thesis states that approval was not required". | C | Must | consistency-check: broken promise | O autor fornece a determinação institucional; não há texto a propor. |
| C-014 | 3.2 | "The work of reconciling the pharmaceutical GCP framework with the device-specific standard has not been done in the published literature" | Afirmação absoluta contra o limite que a própria tese fixa. 2.3.2: "any reported absence of published work is an outcome of this review". 2.6 diz o mesmo. 5.2 usa a forma proporcional: "has not reached the indexed literature". 5.7: "is a result of our search". | C | Should | consistency-check: contradicted claim; R10 | *Within the literature this review examined, no reconciliation of the two frameworks was found, so a site that draws on both does it informally.* |
| C-015 | 1.3; 3.4.1; Tab. 3.4 | "The third condition is traceability." / "Persistent traceability." / "The operational weight of follow-up." / "Limited classification reliability." | As cinco condições mudam de nome entre 1.3, 3.4.1, Tab. 3.4 e 5.3 (onde aparece "unit-level traceability"). A seção 3 do guia fixa *irreversibility, operator dependence, unit-level traceability, follow-up burden, measurement reliability*. "Follow-up burden" não aparece em lugar nenhum. | C | Should | guia §3; R12 | *3. Unit-level traceability. 4. Follow-up burden. 5. Measurement reliability.* |
| C-016 | Abstract; Resumo; 2.5.1 | "The resulting architecture comprises four pillars: governance, risk-based quality management (RBQM), operational controls, and performance oversight." / "Governance, RBQM, Operational Controls, and Performance Oversight" | O pilar 2 se chama Risk Management em 4.1, 4.3, Fig. 4.2, Tab. 4.3 e 6. O Resumo usa "gestão da qualidade baseada no risco". | C | Should | guia §3; R12 | *Governance, Risk Management, Operational Controls, and Performance Oversight* (Resumo: *gestão do risco*) |
| C-017 | 1.5; 2.1.1; 4.1; Abstract; Resumo; Tab. 3.4; Cap. 5–6 | "This thesis aims to develop an operational quality architecture" / "The model is called the Site-Centered Operational Quality Management Framework." | O artefato tem três nomes. *Framework* é o do título. *Architecture* aparece cerca de 40 vezes nos Caps. 1 a 6 (algumas legítimas, como *role architecture*), 14 delas no Cap. 5, e também no Abstract, no Resumo ("arquitetura") e nos DR1, DR2, DR4, DR7, DR10, DR11 e DR12. *Model* aparece em 2.1.1, 4.1 e 4.6.2. No último parágrafo do Abstract, *architecture* e *framework* se alternam. | C | Should | guia §3; R12 | *This thesis aims to develop an operational quality framework…*; *the development of the framework that meets those requirements* |
| C-018 | 3.4.1; 4.2.2; 4.3.2; 4.5.3; Tab. 3.2; Fig. 4.1 | "while PROs require consistent collection at the specified time points" | PROM foi definido em 1.3 ("patient-reported outcome measures (PROMs)") e é usado em 4.2.4 e na Tab. 4.4 (PFVR). Mas PRO/PROs aparecem em 3.4.1, 4.2.2, 4.3.2, 4.5.3 (duas vezes), na Tab. 3.2 (que define "patient-reported outcome (PRO)") e na Fig. 4.1. A Lista de Abreviaturas só tem PRO. | C | Should | guia §3 (PROM); R12; R13 | *PROMs* em todo o texto; trocar a entrada da Lista por *PROM — Patient-Reported Outcome Measure*. |
| C-019 | 4.4.4; 5.1; 6; Tab. 4.1; Fig. 4.1; Fig. 4.2 | "a risk register, a learning curve log, a complication log, a surveillance template, and several review records" / "Surgical Learning Curve Tracking therefore rests on a weaker derivation" | Os instrumentos fogem do nome fixo da Tab. 4.4. SLCT: "Surgical Learning Curve Tracking" (Tab. 4.1, 5.1, 6) e "learning curve log" (11 vezes). POT: "PI Oversight Plan" (Tab. 4.1), "PI oversight plan" (Fig. 4.1), "oversight plan" (4.4.4, 5.4, 5.5). TRE: "…and Training Release" (Fig. 4.2). CSST: "complication signal template", "signal surveillance template". SCML: "complication log". CAPA Log: "corrective action log/record/process". ICDL: "the intraoperative checklist and the device log" (5.3). CCDM: "criticality-coded delegation log" (Tab. 4.1). | C | Should | R12; guia §3 | Nomes da Tab. 4.4: *Surgeon Learning Curve Tracking Log*, *PI Oversight Template*, *Training Record Evaluation and Release*… |
| C-020 | 4.2 a 4.7; 4.8 | "several instruments are referred to at more than one point in the preceding sections" | Nenhum dos 24 instrumentos aparece pelo nome ou pela sigla na prosa do Cap. 4. A busca deu zero ocorrências de CCDM…PIDLR e dos nomes completos. Os nomes formais só aparecem no Cap. 5 (5.3, 5.4, 5.5). O leitor do Cap. 4 não consegue ligar cada componente ao instrumento que o opera, e a frase de 4.8 não se cumpre. | C | Should | consistency-check: broken promise; R12 | *The oversight model is recorded in the PI Oversight Template (POT) and reviewed at milestones in the Milestone Review Log (MRL).* (nomear o instrumento onde o componente é descrito) |
| C-021 | 3.4.1; 3.2.1; 3.2; 3.1; Abstract; Resumo | "none of the four governing instruments requires the same assessor at every visit" / "A documentary search of the three governing instruments" | Os "governing instruments" ora são três (1.5, 3.1, 3.2.1, Tab. 3.1, 5.1), ora quatro (3.2 "the four instruments", 3.4.1, Abstract "four regulatory and guidance instruments", Resumo "quatro instrumentos oficiais"). Além disso, 3.1 diz que o ICH E6(R3) "govern[s] shoulder device investigations", enquanto 1.1 e 2.2.1 tratam o ICH como referência conceitual de escopo medicamentoso. | C | Should | consistency-check: term drift | *the three instruments compared clause by clause (ICH E6(R3), ISO 14155:2026, and MDR Annex XV), read against ICH E8(R1)* |
| C-022 | 4.6.2; Fig. 4.1 | "which is why it is initialized in phase 2, one phase before the first surgery" | Na Fig. 4.1, a Phase 2 é Start-up, a 3 é Enrollment e a 4 é Surgery. A Phase 2 fica, portanto, duas fases antes da cirurgia. A lista de ações da Phase 2 na figura também não inclui abrir o SLCT. | C | Should | consistency-check: contradicted claim; thesis-writing item 23 | *…which is why it is initialized in Phase 2, before the first surgery in Phase 4.* (e acrescentar a ação na Fig. 4.1) |
| C-023 | 4.6.1; legenda Fig. 4.1 | "Figure 4.1 sets out the seven phases and the transversal safety stream, with the entry actions, the exit condition, and the predominant quality objective assigned to each." | A figura mostra só o objetivo e as ações (marcadas – e ✓). Não há condição de entrada nem de saída, embora 4.6.1 diga "We state the entry and exit conditions explicitly". A legenda também promete "entry conditions". | C | Should | consistency-check: broken promise | Acrescentar entrada e saída em cada fase, ou: *with the actions and the predominant quality objective of each phase.* |
| C-024 | 3.3; Tab. 3.2 | "and by the place in the framework where it is addressed" | A Tab. 3.2 só tem "What it covers" e "Principal threat to quality". Não há coluna de localização no framework, e a legenda não a promete. | C | Should | consistency-check: broken promise | *Each domain is described by what it covers and by the principal threat that arises when control is inadequate, and Figure 4.4 shows where the framework addresses it.* |
| C-025 | 2.3.2 | "Three themes shaped the rest of the work, and Section 3.2 reports them alongside the regulatory gap they help to define." | Nenhum dos três temas é nomeado, nem em 2.3.2 nem em 3.2. | C | Should | consistency-check: broken promise | Nomear os três temas em 2.3.2 (o autor fornece) ou apagar a frase. |
| C-026 | 2.6 | "Three limitations apply to the work as a whole." | Vêm só duas: a revisão narrativa e a ausência de implementação. A terceira candidata, o avaliador único que "also applies to the other qualitative classifications" (2.4.3), não é retomada. | C | Should | consistency-check: broken promise | *Two limitations apply to the work as a whole, in addition to the single-assessor limitation stated in Section 2.4.3.* |
| C-027 | Lista de Tabelas; Cap. 4 | "Table 4.1 Design requirements and framework components" / "Table 4.3 The scalability model" | Não existe Tabela 4.2. A numeração salta de 4.1 para 4.3, tanto na lista quanto no texto. | C | Should | thesis-writing item 23 | Renumerar 4.3 para 4.2 e 4.4 para 4.3, com todas as remissões. |
| C-028 | 5.2; 1.4.2 | "since outcomes depend far more on operator technique" / "not to claim that one specialty is more operator dependent than another" | 5.2 afirma, sem citação, exatamente o que 1.4.2 declarou que não afirmaria. | C | Should | consistency-check: contradicted claim; R10 | *…since outcomes depend on operator technique and learning-curve effects [18, 19], and functional and radiographic assessment adds standardization problems with no equivalent in the automated data streams of cardiac rhythm devices.* |
| C-029 | 5.4; 4.3.3 | "A cluster confined to one center reaches the threshold for a local response long before it reaches a trial-level signal, so the local instrument acts first" / "The available sources do not establish that either level will detect a signal first." | Contradição direta com a ressalva de 4.3.3. | C | Should | consistency-check: contradicted claim; R17 | *A cluster confined to one center can reach the local threshold before it forms a trial-level signal, although the sources examined do not establish which level detects it first.* |
| C-030 | 5.3; 1.3; 3.4.5 | "Investigation is not the primary business of the target center." / "research is neither the main nor the largest source of income" | 1.3 ("design assumptions that the registry did not test") e 3.4.5 ("We therefore treated these conditions as conservative design assumptions") tratam isso como suposição. 5.3 afirma como fato. | C | Should | consistency-check: contradicted claim; R18 | *We assumed that research is a secondary activity at the target center, run alongside an elective surgical practice; the registry did not measure income or staffing.* |
| C-031 | 5.3; 5.7; Tab. 3.3; 1.3; 6 | "since 38 of those 65 organizations declare no permanent structure for clinical research" / "That variable records a declared organizational function" | A variável muda de sentido. Na nota da Tab. 3.3 ela significa "the public sources consulted did not establish the defined permanent structure". Em 5.3, "declare no". Em 5.7, "self-declared institutional identity". Na Tab. 3.3, "Confirmed research infra.". Em 1.3, "no documented permanent research structure". Em 6, "no publicly documented". "Não estabelecido por fontes públicas" não é o mesmo que "declara não ter". | C | Should | consistency-check: term drift | *…38 of those 65 organizations had no permanent research structure that the public sources consulted could establish* |
| C-032 | 4.7; 3.4.4 | "since those environments are the most prevalent in shoulder device investigations" | 3.4.4 diz que os dados "cannot establish the prevalence of comparable organizations in Europe or across the global population", e a anti-ideia 4 do contrato vai no mesmo sentido. O dado sustenta apenas "maioria na amostra" (162/235). | C | Should | contrato (anti-ideia 4); R10 | *…since those environments made up 162 of the 235 organizations in the registry sample.* |
| C-033 | 6; 3.2.1; 5.1; 1.4; 5.2 | "The site is the only party in the device conformity chain without a documented quality system, while the manufacturer holds ISO 13485, the risk function holds ISO 14971" | A tese cita ISO 9001 implementada em centros de ensaio [31] e o CTAIM [30] como precedentes operados pelo centro (1.4, 5.2). Além disso, a lista de partes muda. Em 3.2.1 são o fabricante (ISO 13485) e o laboratório (ISO 15189). Em 6 são o fabricante, uma "risk function" (que não é uma parte) e o promotor. | C | Should | consistency-check: contradicted claim; R10 | *Among the standards examined here, none describes a quality system for the investigational site in the way ISO 13485 does for the manufacturer and ISO 15189 for the laboratory.* |
| C-034 | 3.5; Tab. 3.4 | "Some domains already carry an obligation from one of the instruments. These produce no requirement" | Na Tab. 3.4, o DR2 deriva de "CtQ domains All twelve", e todo domínio aparece em ao menos um DR (o domínio 3 só pelo DR2). Nenhum domínio fica sem requisito. | C | Should | consistency-check: contradicted claim | Decidir se o DR2 deriva mesmo dos doze domínios e reescrever uma das duas passagens. |
| C-035 | 3.2.1; 5.1; 4.2.3 | "Clauses 10.2 and 10.3 therefore establish entry qualifications. They do not describe an ongoing local quality-management system." / "so what the clause describes is a process without calling it one" | A leitura da Clause 10 oscila entre "entrada" (3.2.1; 5.1, "qualified at baseline and stop there") e "processo contínuo" (5.1, "run for the whole investigation"; 4.2.3, Clause 10.6, "throughout the investigation"). | C | Should | consistency-check: contradicted claim | *Clause 10 sets duties that run through the investigation (Clauses 10.1 and 10.6) but describes no process for meeting them, and its qualification clauses (10.2, 10.3) act at entry.* |
| C-036 | 3.4.1; 3.3; 5.3 | "and ISO 14155:2026 adds an implant card [8, 10]" / "while the MDR requires traceability for implantable devices and an implant card for the patient" | O cartão de implante é atribuído à ISO 14155:2026 em 3.3 e 3.4.1 e ao MDR em 5.3. Não verificável aqui (lente 1). | F | Should | consistency-check: contradicted claim | — |
| C-037 | 5.3; 3.4.1 | "with the same assessors and the same acquisition conditions at every time point" | 5.3 apresenta como exigência o que 3.4.1 diz que nenhum instrumento exige: "none of the four governing instruments requires the same assessor at every visit". | C | Should | consistency-check: contradicted claim | *…preferably with the same assessors and acquisition conditions at every time point, which no governing instrument requires.* |
| C-038 | 5.5; Fig. 4.1; Tab. 4.4 | "The seven Governance instruments come first, because all seven can be completed before the first participant exists" / "The Site Risk Register follows, since it has to open during feasibility" | O POT ("Records the PI's active oversight of the investigation as it runs") e o MRL (que recebe entradas do PIR e do SRR) não podem estar concluídos antes do primeiro participante. Feasibility é a Phase 1, antes do Start-up (Phase 2), onde a Fig. 4.1 constrói a Governança. Se o SRR abre na Phase 1, ele não pode vir depois. | C | Should | consistency-check: contradicted claim | *The Site Risk Register opens first, during feasibility, and the Governance instruments are set up during start-up, before the first participant exists.* |
| C-039 | 4.3.2 | "the validated Clinical Trial Site Performance Measure contains no counterpart for surgeon procedural consistency once a trial is under way [37, 39]" | O CTSPM é a referência [41] (1.4.2, 5.2). [37] e [39] são, respectivamente, o SQA-Onc e a revisão sobre enxertos arteriovenosos. | F | Should | thesis-writing: honesty rules | *SQA frameworks address the learning curve mainly at selection [37, 39], and the validated Clinical Trial Site Performance Measure contains no counterpart… [41].* |
| C-040 | Tab. 4.3; Tab. 4.4; Tab. 3.1; 4.5.7 (imagens e texto) | "starts a corrective and preventive action (CAPA) cycle" | Duas siglas têm dois sentidos cada. RACI é método na Tab. 4.3 ("Responsible, Accountable, Consulted, and Informed (RACI)") e instrumento na Tab. 4.4 ("Responsibility Assignment Matrix (RACI)"). CAPA é processo na Tab. 3.1, em 4.5.7 e na Lista, e instrumento na Tab. 4.4 ("Corrective and Preventive Action Log (CAPA)"). CAPA ainda é definida duas vezes: na Tab. 3.1 e em 4.5.7. | C | Should | R13; R12 | Dar sigla própria ao log (ex.: *CAPA Log*) e definir CAPA uma vez só. |
| C-041 | Cap. 5 inteiro; 2.2.2; 3.3; 6 | "the Clinical Trials Transformation Initiative issued quality by design recommendations" | Há cerca de 60 regressões à forma por extenso depois da definição, cerca de 55 delas no Cap. 5. Exemplos: Critical-to-Quality 9 vezes (incluindo os títulos de 2.2.2 e 3.3), PI 5, RBM 5, CIP 4, QMS 4, AE 4, CRO 3, PD 3, CAPA 4. Ver o inventário 4.1. | E | Should | R13; thesis-writing: terminology and abbreviations | Usar a sigla depois da primeira definição (lista completa no inventário 4.1). |
| C-042 | 2.1.1; 2.2.1; 2.2.2; 2.3.1; 2.5; 2.5.1 | "As already stated, the objective of this thesis is to build a framework of quality that supports the guidelines required principles." / "so we needed to go after the device-specific obligations" | O Cap. 2 tem um registro visivelmente mais solto e menos revisado que os Caps. 3 a 5. Outros exemplos: "As a disclaimer, these labels are our own"; "We can see that those considerations are more related to guide CtQs"; "Before we can build the framework, we must decide what we are looking for"; "But it does not prove that another better taxonomy can exist"; a frase emendada em "prevent divergence, this is important". | T | Should | consistency-check: tone drift; R11; R24 | *The objective of this thesis is to build a site-level quality framework that puts the principles of the guidelines into practice.* |
| C-043 | 4.2.1; 4.2.3; 4.3.1; 4.3.3; 4.4.1; 4.4.2 | "Turning that principle into a workable schedule is harder than it sounds." / "Executing that review well is harder than scheduling it." | Uma camada ensaística em molde fixo atravessa o Cap. 4: "X is harder than Y" 5 vezes, "The harder question/task" 2, "The difficulty"/"The real difficulty" 4, mais "the third/fourth difficulty". Vem com ponto e vírgula e idiomatismos ("judgment call", "Set the threshold too low…; set it too high…"). Destoa do registro de especificação do capítulo e da promessa de 4.1 ("in enough detail for a site to operate it"). | T | Should | consistency-check: tone drift; thesis-writing: vary the development path; R24 | *A site has to decide in advance, for each type of activity, which decisions need the investigator's own judgment and which can be reviewed afterward.* |
| C-044 | 4.5; 4.8; Fig. 4.5 | "and our earlier set of five indicators left it without a measure" / "from one inherited through a combined or earlier instrument, from an extension added to the original set" | Histórico de redação exposto: uma versão anterior com cinco indicadores, e instrumentos "anteriores" e um "conjunto original" que não existem no texto atual. A R19 cita o primeiro trecho como exemplo proibido. | T | Should | R19 | *Domain 11 needed its own measure, so the set includes critical data completeness.*; legenda: *derived from another instrument* / *complementary contribution* |
| C-045 | 5.5 | "Describing the learning curve log as an instrument that does not assess professional performance is therefore inaccurate" | A frase corrige uma descrição que não existe na versão atual. Nenhuma passagem diz que o SLCT não avalia desempenho profissional. É resíduo de versão anterior. | C | Should | R19 | *The Surgeon Learning Curve Tracking Log therefore assesses professional performance in substance, and its use has to be governed as a quality instrument with possible professional consequences.* |
| C-046 | 5.2; 1.4.1–1.4.2 | "The field has proposed a great deal and validated very little." / "The field has therefore proposed a great deal and validated very little." | Os parágrafos 2 a 7 de 5.2 recontam 1.4 quase literalmente: TransCelerate/CTTI/MDIC, a revisão SQA, ROMIO, os dois Delphi, os enxertos AV, os 109 estudos, o CTSPM (126→18), [42–47] e Diani [48]. São cerca de 500 palavras repetidas, e a regra da Discussão manda confrontar, não reapresentar. | R | Should | consistency-check: repeated examples; thesis-writing: Discussion; R20; R25 | Manter o relato em 1.4 e reduzir 5.2 ao confronto: *Against the bodies of work set out in Section 1.4, the framework differs in who operates it…* |
| C-047 | 5.3; 3.4.1–3.4.3 | "These records are created in the operating room, under time pressure, by staff whose attention is on the procedure" / "It is executed in the operating room, under time pressure, by staff whose attention is on the surgical procedure." | 5.3 repete 3.4.2 (44 CTUs, 89%, "cannot standardize the many small decisions", o operador como unidade de análise), 3.4.3 (a lista de registros da ISO e os exemplos de dado no ponto de cuidado) e o item 5 de 3.4.1 (kappa, TC, core outcome sets). São cerca de 270 palavras. | R | Should | consistency-check: repeated examples; R25 | *Section 3.4.3 showed that these records exist only if they are captured at implantation, and DR6 turns that condition into a design demand.* |
| C-048 | 5.1; 3.5; 6 | "That silence is the gap this work reports, so we cannot justify the framework by naming an obligation it satisfies." / "We therefore cannot justify its existence by pointing to a rule." | A mesma justificativa "backward" aparece três vezes (3.5, 5.1, 6 §2), cerca de 80 palavras em 5.1. A versão proporcional está em 5.1; a de 3.5 é a que exagera (C-006). | R | Should | consistency-check: repeated examples; R25 | Manter o argumento só em 5.1 e cortá-lo de 3.5. |
| C-049 | 5.5; 4.3; 4.4.2 | "The second and third fall outside ISO 14971 and are assessed descriptively." / "and these are assessed descriptively" | 5.5 repete 4.3 (os três fluxos de risco da Clause 6.2) e 4.4.2 (Clause 9.2.4.5 p) e Annex A.6.4), cerca de 150 palavras, e diverge num detalhe. Em 4.3, só a 6.2.3 é "assessed descriptively". Em 5.5, a segunda e a terceira. | R | Should | consistency-check: repeated examples; contradicted detail | Remeter a 4.3 e deixar em 5.5 só a observação dirigida a uma revisão futura da norma. |
| C-050 | 4.3.3 | "This is proactive risk management in the sense Section 2.2.2 already gave the term" | 2.2.2 não define "proactive", e a palavra não ocorre no Cap. 2. Referência quebrada. | C | Should | thesis-writing item 23 | *This is proactive risk management, with prevention and detection built into routine conduct before any report falls due.* |
| C-051 | 6 | "Section 1.2 opened this thesis by describing a shift" | A mudança de modelo prescritivo para governança está em 1.1 (5.1 cita corretamente "Section 1.1"). Além disso, 1.2 não abre a tese. | C | Should | thesis-writing item 23 | *Section 1.1 opened this thesis by describing a shift…* |
| C-052 | legenda Fig. 4.3 | "so Operational Controls appears as four groups, safety, surgery and device, enrollment, and follow-up" | Na figura, a linha "Safety stream" contém só o SART, que é Risk Management (cor vermelha, Fig. 4.2). Operational Controls aparece em três grupos. | C | Should | consistency-check: contradicted claim | *…so Operational Controls appears as three groups, surgery and device, enrollment, and follow-up, and the safety stream row holds the SART.* |
| C-053 | 5.3; 5.6; Tab. 4.4 | "the imaging charter and assessor qualification do that work" / "The complication categories and the imaging charter do carry anatomical content" | Na Tab. 4.4 (SIRR, IQL), o imaging charter é documento do promotor ("the sponsor's imaging charter"). Em 5.3 e 5.6 vira componente do framework. Em 4.6.2 ("a better imaging charter") fica ambíguo. | C | Should | R12 (one object, one name) | *the Site Imaging Readiness Record and the Imaging Quality Log, which apply the sponsor's imaging charter at the site* |
| C-054 | Resumo; Abstract | "Esta tese teve como objetivo desenvolver uma arquitetura de gestão da qualidade operacional para centros que conduzem investigações clínicas de dispositivos médicos." | O Resumo omite o escopo do ombro, que é não negociável. O Abstract diz "for shoulder medical device clinical investigations". A lista de funções dos instrumentos também difere: o Abstract inclui "deviation control", o Resumo não. | C | Should | contrato (non-negotiables: shoulder scope) | Resumo: *…centros que conduzem investigações clínicas de dispositivos médicos do ombro.* |
| C-055 | 2.3.3; 5.2 | "For each pairing we recorded one of three outcomes" / "Section 5.2 reports that comparison and states what the framework adds." | 5.2 não apresenta a classificação em três desfechos nem os quatro atributos registrados por instrumento (nível, quem opera, a quem se aplica, campo). Só compara item a item com o CTSPM. | C | Should | consistency-check: broken promise | Pôr em 5.2 uma tabela curta com os quatro atributos e o desfecho de cada instrumento, ou reduzir 2.3.3 ao que 5.2 de fato faz. |
| C-056 | 4.3.2; Cap. 4–5 (prosa) | "Section 3.4.2 established why this matters and why no instrument examined in this thesis assigns the site a role in watching it once the investigation is under way." | O DR3, requisito da única lacuna sem obrigação correspondente (que o contrato exige cristalina), nunca é citado na prosa dos Caps. 4 e 5. Todos os outros DR são citados. 4.3.2 também não nomeia o instrumento (SLCT). | A | Should | consistency-check: arc coherence; contrato (learning curve crystal clear) | *This component answers DR3, and the site operates it through the Surgeon Learning Curve Tracking Log (SLCT).* |
| C-057 | 4.4.1; 4.5.6 | "Delay is a defensible trigger, since the MDIC risk-indicator model weights queries older than sixty days" / "Delay is already used as a risk trigger in the MDIC indicator model and the EMA reflection paper." | Mesmo argumento duas vezes (MDIC + EMA; backlog como hipótese), cerca de 55 palavras. O nome do modelo varia. | R | Could | consistency-check: repeated examples | Manter em 4.5.6 e remeter a partir de 4.4.1. |
| C-058 | 4.4.1 | "The nine checks below define what it has to cover." / "Nine checks define the scope of internal review." | Duas frases seguidas dizem a mesma coisa. | R | Could | R7 | Apagar a primeira. |
| C-059 | 5.4; 4.6; 4.6.2 | "whose claim is that a quality activity performed at the wrong moment does not perform its function" | A frase aparece em 4.6 e de novo em 5.4, que também retoma a premissa de fases de 4.6.2. Cerca de 60 palavras. | R | Could | consistency-check: repeated examples | *The lifecycle (Section 4.6) applies the same logic in time.* |
| C-060 | 5.7; 2.6; 5.2 | "A narrative review supports a map of the problem space. It does not support a claim that a body of work is absent from the field" | Repete 2.6 quase literalmente. A ausência de comparação ICH × ISO é tratada três vezes (3.2, 5.2, 5.7). Cerca de 100 palavras. | R | Could | consistency-check: repeated examples; R25 | Remeter a 2.6. |
| C-061 | 5.6; 5.7; 4.8 | "makes structural adaptability plausible; it does not establish it" / "That derivation makes structural adaptability plausible without establishing it" | A mesma ideia duas vezes dentro de 5.6. O teste hip/knee aparece em 5.6 e 5.7, e a divisão estrutura/conteúdo em 4.8 e 5.6. Cerca de 110 palavras. | R | Could | consistency-check: repeated examples | Deixar uma formulação em 5.6 e só a referência em 5.7. |
| C-062 | 5.3; 4.7.2 | "Reduced implementation depth at a smaller center raises an objection about regulatory exposure" / "Reduced depth raises an obvious objection" | A objeção de 4.7.2 é retomada como se fosse nova. Cerca de 60 palavras sobrepostas. | R | Could | consistency-check: repeated examples | *Section 4.7.2 answered the inspection objection conditionally; the premise behind that answer is unsourced.* |
| C-063 | 1.3; 3.4.1; 3.3; 5.3 | "the framework extends the operational record to the surgical decisions that produced the device configuration in a given patient" / "Traceability here also extends to reconstructing the surgical decisions that produced that configuration in that participant" | A ideia se repete entre 1.3 e 3.4.1. O cartão de implante aparece em 3.3 e 3.4.1, e a exclusão do Art. 27 em 1.3 e 5.3. Cerca de 60 palavras. | R | Could | consistency-check: repeated examples | — |
| C-064 | 3.2; 3.2.1 | "Even the site-qualification clause makes the principal investigator (PI) responsible for demonstrating that the site has enough eligible participants and a qualified team" / "Even Clause 10.3 places the duty on the PI" | A mesma frase em seções contíguas, cerca de 30 palavras. | R | Could | consistency-check: repeated examples | Manter só em 3.2.1. |
| C-065 | 1.3 | "Within this context, we narrowed the work to orthopaedic investigations" | É a única primeira pessoa da Introdução (R14), e usa grafia britânica. | T | Could | R14; consistency-check: tone drift | *Within this context, the work was narrowed to orthopedic investigations…* |
| C-066 | 5.5; 5.1 | "the quality of conduct at the site measures how seriously that consent is honored" / "none of the three judgments reaches the person whose shoulder is opened" | Registro elevado, retórico e aforístico que não aparece nos outros capítulos. 5.1 também abre com aforismo ("Conducting an investigation well and showing that one operates a system are separate accomplishments"). | T | Could | consistency-check: tone drift; R7; R24 | *A delayed safety report, an incomplete traceability record, or an eligibility error reaches participants who see none of the quality system.* |
| C-067 | legenda Tab. 3.2; 4.8 | "The twelve site-level CtQ domains derived in Section 2.2.2" / "against the twelve CtQ domains from Section 2.2.2" | Os domínios são produzidos em 2.2.3 ("the result was twelve domains") e relatados em 3.3. | C | Could | thesis-writing item 23 | *…derived in Section 2.2.3 and reported in Section 3.3* |
| C-068 | 1.3 | "Those are design assumptions that the registry did not test, and Section 3.4.4 states them explicitly." | As suposições estão em 3.4.5 ("We therefore treated these conditions as conservative design assumptions"). | C | Could | thesis-writing item 23 | *…and Section 3.4.5 states them explicitly.* |
| C-069 | 5.1 | "The center described in Section 3.4.4 can conduct an investigation properly" | O centro-alvo é descrito em 3.4.5. | C | Could | thesis-writing item 23 | *The center described in Section 3.4.5…* |
| C-070 | Tab. 4.1, DR6 (imagem) | "4.4.1, 4.6.2 phase 4, 4.3.2, 4.3.3" | A ligação entre a Phase 4 e o DR6 está em 4.6.1. Além disso, nenhuma linha da Tab. 4.1 cita 4.2.4 (device training documentation), embora a Fig. 4.5 ligue o DTRM e o TRE a DR3 e DR10. Fica um componente sem linha na tabela que 2.1.1 promete completa. | C | Could | thesis-writing item 23; consistency-check: broken promise | *4.4.1, 4.6.1 (Phase 4), 4.3.2, 4.3.3*; acrescentar 4.2.4 nas linhas de DR3 e DR10. |
| C-071 | 4.5.7 | "against the domains listed in Section 4.4.1" | 4.4.1 lista nove *checks*, não domínios. | C | Could | thesis-writing item 23 | *against the nine checks listed in Section 4.4.1* |
| C-072 | 5.7; 6 | "The absence of any implementation weakens the claims in Section 5.3 about protected margin" | 5.3 não fala em "protected margin"; o termo só aparece em 5.7 e 6. O argumento de 5.3 é "an avoidable error becomes a direct loss". | C | Could | thesis-writing item 23 | *…the claims in Section 5.3 about avoidable losses at a resource-limited center* |
| C-073 | 1.3; 2.4.1 | "This retrieval count indicates a substantial registry base; it is not the final analytic sample described in Section 2.4." | 2.4.1 não menciona os 996 registros nem o caminho até 46 (critérios e excluídos em cada etapa). A busca de 2.4.1 usa critérios diferentes (patrocinador industrial, início entre 2000 e 2026). O leitor não consegue reconciliar os dois números. | C | Could | consistency-check: broken promise | Acrescentar a 2.4.1 o fluxo 996 → 46 (os números de cada etapa vêm do autor). |
| C-074 | 3.2.1; 2.2.2 | "did not occur in ISO 14155:2026, ICH E6(R3), or the MDR" | Esta busca documental (proficiency, credential, proctor, learning curve, training) não está descrita no Cap. 2, que só descreve a busca por "CtQ"/"QbD" de 20/09/2026. Faltam data e método. | C | Could | R20 (Methodology answers what was done) | Acrescentar uma frase em 2.2.2 com os termos buscados e a data. |
| C-075 | 5.7; 2.4.3; 2.4.2 | "All classifications were verified case by case and reviewed in a second internal pass" / "Eight of the 235 organizations remain unresolved on the trials structure variable" | 5.7 diz retomar as limitações de 2.4.3, mas traz fatos novos (uma segunda revisão interna; registro obrigatório nos EUA), omite a limitação da unidade de análise e muda a variável dos oito não resolvidos, que em 2.4.2 eram entradas não vinculáveis a uma organização. | C | Could | consistency-check: contradicted claim | Alinhar 5.7 com 2.4.3, ou levar os fatos novos para 2.4.3. |
| C-076 | 6; 5.1 | "Section 5.1 treats that exception as the framework's most exposed claim and its clearest addition to what the field already requires." | 5.1 diz só que o componente "rests on a weaker derivation than the other four components". "Clearest addition" não está lá. Além disso, 6 diz que 5.1 defende a rastreabilidade "over the alternative of asking the sponsor or a commercial vendor", mas 5.1 rejeita essas rotas por propriedade e ponto de cuidado, e 5.5 propõe uma arquitetura construída pelo promotor. | C | Could | thesis-writing item 23 | *Section 5.1 identifies that exception as the component with the weakest derivation.* |
| C-077 | 5.6; 6 | "The five complexity strata used in the learning curve log" | O número cinco só aparece na Discussão e na Conclusão ("five-stratum learning-curve model"). O Cap. 4 e a Tab. 4.4 falam em "complexity stratification" sem número. É dado de projeto introduzido fora dos Resultados. | C | Could | consistency-check: arc coherence | Declarar os cinco estratos em 4.3.2 ou 4.5.5. |
| C-078 | 4.3.1; 1.4.2; 3.2 | "A 2023 study of Portuguese clinical trial sites found that" | Introduzido duas vezes como novo (4.3.1 e 5.1). É a evidência empírica mais direta da lacuna 2, mas não aparece em 1.4.2 nem em 3.2, onde a lacuna é definida. Aparece pela primeira vez nos Resultados. | A | Could | consistency-check: arc coherence; repeated examples | Levar o estudo [76] para 1.4.2 e remeter a ele em 4.3.1 e 5.1. |
| C-079 | 4.3.3; 4.4.1; 5.3; 2.2.1; 1.5 | "any SAE with a causal relationship to the investigational device" / "so UDI-DI and UDI-PI are not themselves mandatory" / "also known as medical device regulations (MDR)" | SAE (4.3.3, 4.4.1, 4.5.4), CRF (4.4.1, 4.4.4, 4.5.6) e UDI-DI/UDI-PI (5.3) são usados sem definição no texto. MDR é redefinida em 2.2.1 com outro nome, e ISO em 1.5. SQA-Onc está na Lista e não ocorre no texto. Seis siglas são usadas uma única vez (CT, ICC, PRISMA, ISO/TR, DSR, IVDR), contra a skill: "do not abbreviate a term used only once". | E | Could | R13; thesis-writing: terminology and abbreviations | Definir SAE e CRF na primeira ocorrência; apagar a redefinição de 2.2.1 e de 1.5. |
| C-080 | 3.4.4; 3.4.5; Tab. 3.3; diversos | "Within the non hospital environment, 27 organizations met the definition" | Quatro grafias do mesmo termo: non-hospital (1.3, 2.4.2, 2.4.3, 5.3, 5.7, 6), nonhospital (3.4.4, 3.4.5), non hospital (3.4.4, 3.4.5), Non hospital (Tab. 3.3). O mesmo ocorre com non-academic/nonacademic/Non Academic, orthopaedic (1.3, 1.4.2, 3.4.1, 3.4.2)/orthopedic, inter-observer/interobserver/inter-rater, pre-specified/prespecified e timepoint/time point. As imagens têm grafia britânica (enrolment, centre, standardised, specialised, programme, authorisation, recognise, theatre, afterwards). | E | Could | guia §3 (prefixos, ortografia) | *nonhospital*, *nonacademic*, *orthopedic*, *interobserver*, *prespecified*, *time point* |
| C-081 | 4.4.2; 4.7.2; 4.5.7; 4.6.1; 4.2.4; 4.5.4; 3.4.1; Tab. 3.4 | "Clause 9.2.4.5 p) requires routine monitoring visits" / "ISO 14155 Section 9.2.4.5(p)" / "Annex XV, Clause 3.8" | A notação das normas varia, contra a R23. A ISO aparece como "Section" (4.5.7, 4.6.1, 4.7.2). Há "p)" e "h)" sem parênteses de abertura (4.2.4, 4.4.2, 5.5), "§ 3.3.2" (3.4.1), "§3.2" (Tab. 3.4) e o MDR como "Annex XV, Clause 3.8" (4.5.4). | E | Could | R23; R22 | *Clause 9.2.4.5(p)*; *ISO 13485:2016 Clauses 8.5.2 and 8.5.3*; *MDR Annex XV, Chapter II, Section 3.8* (conferir a seção) |
| C-082 | 4.8; 4.3.2; 4.4.1; 4.4.2; Listas | "Table 4.4 lists all twenty-four instruments" / "an average of approximately twenty-five cases" | Números do desenho aparecem por extenso: "twenty-four" 14 vezes, "twelve" 17 vezes. O mesmo vale para dados ("twenty-five cases", "twelve and eighty-six cases", "sixty days", "five degrees", "nine degrees"). A seção 3 do guia manda usar algarismos para dados. | E | Could | guia §3 (números) | *24 instruments*, *12 domains*, *25 cases*, *60 days*, *5 degrees* |
| C-083 | Abstract; Resumo; 4.7.1; Tab. 4.3; 5.7 | "A seven-phase lifecycle and three implementation depths adapt these components" / "Field research across the three site types" | Os três tipos têm nomes diferentes: "implementation depths" (Abstract), "níveis de implementação" (Resumo), "site contexts" (4.7.1 e Tab. 4.3), "site types" (4.7.2, 5.7). Os rótulos também mudam. Tipo A: "large academic hospitals and established research institutions" (4.7.1) × "Large or complex research hospital" (Tab. 4.3). Tipo C: "Smaller centers and ambulatory surgical units" × "Small surgical centre". | C | Could | consistency-check: term drift; R12 | Escolher *site types* e alinhar os rótulos A, B e C com a Tab. 4.3. |
| C-084 | nota da Fig. 4.3 (imagem); Tab. 4.4 | "An evidence record never depends on a synthesis or decision document existing first." | Na Tab. 4.4, o TRE (camada de evidência na Fig. 4.3) "Compares the evidence held for that person against what the DTRM requires" e usa o CCDM, que são documentos de decisão e precisam existir antes. | C | Could | consistency-check: contradicted claim | *An evidence record is filled from the event it documents; decision documents only set the criteria it is checked against.* |
| C-085 | 4.4.4 | "The first records data that has no other home, which is the case for the learning curve log" / "The learning curve log records that a component substitution occurred and points to the operative note." | Duas frases depois, o mesmo dado aparece com outra "casa": a nota operatória. | C | Could | consistency-check: contradicted claim | *The first category holds data that are aggregated nowhere else…* |
| C-086 | 5.5; 1.1; 4.2.4; 4.3; 1.2; 5.2; 5.4 | "listed under Regulation (EU) 2017/745 in OJ L 2026/193" / "as listed in Commission Implementing Decision (EU) 2026/193 [9]" / "an Investigator Brochure" | O mesmo ato aparece com duas designações, e 5.5 o cita sem número de referência. Outras variações de nome: "Investigator Brochure" (5.5) × "Investigator's Brochure" (4.2.4); "EMA Reflection Paper" (4.3) × "EMA reflection paper" (4.2.1, 4.4.1, 4.5.6); "Failure Modes and Effects Analysis" (1.2) × "failure mode and effects analysis" (4.3); "Diani and colleagues" e "Adams and colleagues" (5.2, 5.4) × "et al." (guia §3). | E | Could | guia §3; R12 | *Commission Implementing Decision (EU) 2026/193 [9]*; *Investigator's Brochure*; *Diani et al.* |
| C-087 | 5.7 | "We have not recalculated the median number of sites or the median target enrollment for the 46 investigations in the current sample" | "Recalculated" e "current sample" supõem uma versão anterior, e o leitor não sabe de que cálculo se trata. A seção 2 do guia já registra a decisão pendente: calcular a mediana ou reescrever sem tom de nota de trabalho. | T | Could | R19; guia §2 | Se o autor não calcular: *The median number of sites and the median target enrollment of the 46 investigations were not calculated, so no figure is given.* |
| C-088 | 3.1 | "The fourth step brings the three analyses together into an explicit set of design requirements," | Frase truncada (termina em vírgula) no parágrafo que anuncia a estrutura do capítulo. | G | Could | consistency-check: broken promise | *…into an explicit set of design requirements (Section 3.5).* |
| C-089 | 4.5; Fig. 4.4; Tab. 3.4 | "The two remaining indicators, the PD rate and surgeon procedural consistency, answer domains 12, 5, and 6." | Na Fig. 4.4, o PIR não tem marcador no CtQ6. Além disso, o DR8 deriva só dos domínios 2, 7, 10 e 11 (Tab. 3.4), então 5, 6 e 12 extrapolam a origem declarada do requisito que o indicador responde. | C | Could | consistency-check: contradicted claim | Acrescentar o marcador PIR × CtQ6 e os domínios 5, 6 e 12 à origem do DR8, ou reformular 4.5. |
| C-090 | Tab. 3.4 (imagem) | "The CAPA cycle (§3.2.1)" / "Team size and the personification of quality (§3.4.5)" | 3.2.1 não discute ciclo CAPA. 3.4.5 não fala em "team size" nem em "personification". | C | Could | thesis-writing item 23 | *A loop that measures performance and corrects it (Section 3.2.1)*; *Records that survive changes in individual responsibilities (Section 3.4.5)* |
| C-091 | 6; 3.2 | "derived clause by clause from the texts that created the gap in the first place" / "These five gaps are not defects in the regulatory framework." | "Created the gap" atribui a lacuna aos textos, perto da anti-ideia 2 do contrato. 3.2 diz que as lacunas decorrem da divisão de responsabilidades. | C | Could | contrato (anti-ideia 2) | *…derived clause by clause from the division of responsibility those texts express.* |
| C-092 | Tab. 3.4, DR10 (imagem); 4.2.2; 4.7.1; 5.7 | "In a small or mid-sized center, one individual may hold more than one of them." | O DR10 exige que "no CtQ function may depend on a single individual" (imagem). O framework, porém, aceita que uma pessoa acumule funções (4.2.2, Tipos B e C em 4.7.1) e considera equipes de "one investigator and one coordinator" (5.7). A tese não diz como o DR10 se cumpre nesse caso. | C | Could | consistency-check: contradicted claim | Uma frase em 4.2.2 sobre a cobertura de substituto (o RACI já tem "a backup"). |

## 4. Artefatos da lente

### 4.1 Inventário de abreviaturas

"Forma por extenso depois" conta regressões no texto dos Caps. 1 a 6. O Resumo e o Abstract têm definições próprias e não entram na conta.

| Sigla | Primeira definição no texto | Forma por extenso depois da definição | Observações |
|---|---|---|---|
| ICH | 1.1 | — | ok |
| RBM | 1.1 | 5.2 (3×), 5.4, 5.5 = 5 | |
| QbD | 1.1 | 5.2, 5.4 = 2 | |
| CtQ | 1.1 | títulos de 2.2.2 e 3.3; 5.1 (3×); 5.2 (2×); 5.4; 6 = 9 | Abstract em minúsculas, "critical-to-quality (CtQ)"; plural "CtQs" em 2.2.2 e 3.5 |
| GCP | 1.1 | 5.7 = 1 | |
| ISO | 1.1 | redefinida em 1.5 | |
| EU, EN | 1.1 | — | ok |
| MDR | 1.1, "Regulation (EU) 2017/745 on medical devices (MDR)" | redefinida em 2.2.1 como "medical device regulations (MDR)" | "Regulation (EU) 2017/745" como citação legal é aceito pela skill |
| RBQM | 1.1 | — | usada como nome do pilar 2 no Abstract e em 2.5.1 (C-016) |
| AE/AEs | 1.2 | 5.2 (2×), 5.7 (2×) = 4 | |
| ROM | 1.3 | 5.3, 5.6 = 2 | |
| PROM(s) | 1.3 | 5.3, "patient-reported outcomes" = 1 | concorre com PRO/PROs (Tab. 3.2 define PRO); a Lista só tem PRO (C-018) |
| API | 1.3 | — | 2 usos |
| UDI | 1.3 | 5.3, 5.4 = 2 | UDI-DI e UDI-PI usados em 5.3 sem definição |
| QMS | 1.4.1 | 5.1, 5.2, 5.5 (2×) = 4 | a sigla só reaparece na Tab. 3.1 |
| CTTI | 1.4.1 | 5.2 = 1 | |
| MDIC | 1.4.1 | 5.2 = 1 | |
| SQA | 1.4.1 | 5.2 = 1 | SQA-Onc está na Lista sem uso no texto |
| ROMIO | 1.4.1 | — | ok |
| QA | 1.4.1 | 5.2 (2×) = 2 | |
| CRO | 1.4.2 | 5.1 (2×), 5.2 = 3 | a sigla aparece uma única vez na prosa |
| DSR / DSRM | 2.1.1 | 5.7, 6 = 2 | DSR usada uma só vez |
| PRISMA | 2.3.1 | — | uso único |
| MDCG | 2.3.2 | — | |
| IVDR | não definida (só dentro do título do MDCG 2020-1) | — | está na Lista |
| CTIS | 2.4.1 | — | |
| ISO/TR | não definida no texto | — | uso único (2.2.1) |
| DR | rótulo "DR1 to DR12" (2.1.1), sem definição formal | — | aceitável como rótulo |
| PD | 3.2 | título de 4.5.2; 5.2; 5.4 (2×) = 3 | |
| CIP | 3.2 | 5.5 (3×), 5.6 = 4 | |
| PI | 3.2 | 5.1, 5.4 (2×), 5.5 (2×) = 5 | |
| SADEs, DDs | 3.2 | — | |
| CEC | 3.2 | 5.4, 5.5 = 2 | |
| CER | 3.2.1 | 5.5 = 1 | |
| EMA | 3.4.1 | — | o nome do documento varia (C-086) |
| QC | 3.4.1 | — | |
| CT | 3.4.1 | 5.3 = 1 | uso único |
| CAPA | Tab. 3.1 (imagem), redefinida em 4.5.7 | 4.5.2; 5.1; 5.4 (2×) = 4 | também sigla de instrumento (C-040) |
| FDA | 4.2.1 | — | |
| IFU | 4.2.4 | — | |
| ADEs | 4.3.3 | — | |
| SAE(s) | nunca definida no texto | — | 4.3.3, 4.4.1, 4.5.4 |
| CRF | nunca definida no texto | — | 4.4.1, 4.4.4, 4.5.6 |
| CFR | 4.4.1 | — | 1.1 usou a forma longa sem sigla; ok |
| ICC | 4.4.2 | — | uso único |
| RACI | Tab. 4.3 (método); Tab. 4.4 (instrumento) | — | dois significados (C-040) |
| 22 siglas de instrumentos (CCDM…PIDLR) | só na Tab. 4.4 e na Fig. 4.2 | — | nunca aparecem na prosa (C-020) |

**Total aproximado:** cerca de 60 regressões, cerca de 55 delas no Capítulo 5.

### 4.2 Termos definidos e nomes fixos (régua: guia §3)

| Conceito | Forma fixa | Variantes encontradas (seção) |
|---|---|---|
| Artefato | framework | architecture (≈40 nos Caps. 1–6, algumas legítimas; Abstract; Resumo "arquitetura"; DR1, DR2, DR4, DR7, DR10, DR11, DR12); model (2.1.1, 4.1, 4.6.2); "Site-Centered Operational Quality Management Framework" (4.1) |
| Pilar 2 | Risk Management | RBQM (Abstract, 2.5.1); "gestão da qualidade baseada no risco" (Resumo); "Risk management" (Fig. 4.3) |
| Condição 3 | unit-level traceability | traceability (1.3); Persistent traceability (3.4.1); Traceability as obligation (Tab. 3.4) |
| Condição 4 | follow-up burden | "Follow-up carries substantial operational weight" (1.3); "The operational weight of follow-up" (3.4.1) |
| Condição 5 | measurement reliability | Limited classification reliability (3.4.1, Tab. 3.4) |
| PROM | PROM | PRO, PROs (3.4.1, 4.2.2, 4.3.2, 4.5.3, Tab. 3.2, Fig. 4.1) |
| Instrumentos | nome da Tab. 4.4 | ver C-019 e o quadro abaixo |
| Variável do registro | (sem definição no Cap. 2; C-005) | permanent clinical trial infrastructure (3.4.4); permanent research structure (1.3); Confirmed research infra. (Tab. 3.3); declared permanent structure (5.3); publicly documented (6) |
| Tipos de centro | (não fixado) | implementation depths; níveis de implementação; site contexts; site types |
| Instrumentos regulatórios | (não fixado) | "three governing instruments" × "four governing instruments" (C-021) |

| Instrumento (Tab. 4.4) | Outros nomes no texto e nas figuras |
|---|---|
| Surgeon Learning Curve Tracking Log (SLCT) | Surgical Learning Curve Tracking (Tab. 4.1, 5.1, 6); learning curve log (4.4.4, 4.6, 4.6.2, 4.8, 5.4, 5.5, 5.6, 5.7) |
| PI Oversight Template (POT) | PI Oversight Plan (Tab. 4.1); PI oversight plan (Fig. 4.1); oversight plan (4.4.4, 5.4, 5.5) |
| Training Record Evaluation and Release (TRE) | Training Record Evaluation and Training Release (Fig. 4.2) |
| Criticality-Coded Delegation Matrix (CCDM) | criticality-coded delegation log (Tab. 4.1); delegation log (4.2.2, 4.2.3, 4.4.4, 5.4, Fig. 4.1) |
| Complication Signal Surveillance Template (CSST) | complication signal template (4.4.4); signal surveillance template (5.4); surveillance template (4.4.4) |
| Site Complication Monitoring Log (SCML) | complication log (4.4.4) |
| Corrective and Preventive Action Log (CAPA) | corrective action log (4.4.4); corrective and preventive action log (5.4); corrective action record (5.5) |
| Intraoperative Checklist and Device Log (ICDL) | "the intraoperative checklist and the device log" (5.3); "Intraoperative traceability and deviation capture" (Tab. 4.1) |
| Site Imaging Readiness Record / Imaging Quality Log | "imaging charter" usado como componente (5.3, 5.6), mas na Tab. 4.4 o charter é do promotor |

### 4.3 Promessas e afirmações estruturais

| Promessa ou afirmação | Onde | Status |
|---|---|---|
| "Section 2.6 states what that does and does not establish" | 1.5 | cumprida |
| Table 4.1 "maps each component onto the requirement it answers" | 2.1.1 | quase: falta o 4.2.4 (C-070) |
| Três temas relatados em 3.2 | 2.3.2 | quebrada (C-025) |
| Comparação em três desfechos relatada em 5.2 | 2.3.3 | imprecisa (C-055) |
| "Three limitations" | 2.6 | quebrada (C-026) |
| Quatro passos do Capítulo 3 | 3.1 | cumprida (frase truncada, C-088) |
| Coluna "place in the framework" na Tab. 3.2 | 3.3 | quebrada (C-024) |
| "Section 4.5.4 constructs the safety indicator accordingly" | 3.2 | cumprida |
| Definição de infraestrutura em 2.4.2 | 3.4.4 | quebrada (C-005) |
| "every section of this chapter returns to that mapping" | 4.1 | imprecisa: 4.2.2 a 4.2.4, 4.3.2, 4.3.3 e 4.5.1 a 4.5.5 não citam DR; DR3 nunca citado (C-056) |
| Instrumentos "referred to at more than one point in the preceding sections" | 4.8 | quebrada (C-020) |
| Condições de entrada e saída na Fig. 4.1 | 4.6.1 | quebrada (C-023) |
| "Section 5.4 presents this as an expected benefit" | 4.6.1 | cumprida (5.4) |
| "Section 3.4.4 states which of the two governs the argument" | 5.3 / 5.7 | quebrada; 5.7 ainda diz "has to state" (C-012) |
| "the disincentive described in Section 5.4" | 5.7 | cumprida |
| Determinação ética "must be cited here" | 2.4.1 | pendente (C-013) |

### 4.4 Números ditos mais de uma vez

| Número | Onde aparece | Status |
|---|---|---|
| 235 organizações | Resumo; Abstract; 1.3; 2.4.1; 2.4.2; 2.4.3; 3.4.4; Tab. 3.3; 5.3; 5.7 | consistente |
| 46 investigações | Resumo; Abstract; 2.4.1; 3.4.4; 5.7 | consistente |
| 65 não hospitalares / 27,7% | 1.3; 2.4.2; 2.4.3; 3.4.4; Tab. 3.3; 3.4.5; 5.3; 5.7 | consistente (65/235 = 27,66%) |
| 38 sem estrutura permanente / 58,5% / 16,2% | 1.3; 3.4.4; 3.4.5; 5.3 | consistente; 6 diz "one in four" (C-001); o sentido da variável muda (C-031) |
| 27 com infraestrutura / 42% | 3.4.4; 3.4.5; Tab. 3.3 | consistente (27/65 = 41,5%) |
| 60 nos EUA / 92,3% (não hospitalares) | 1.3; 2.4.3; 3.4.4; 5.3; 5.7 | consistente |
| 149 nos EUA / 63,4%; 86 fora | 2.4.3; 3.4.4; 5.7 | consistente |
| 86 acadêmicos; 76 hospitais não acadêmicos; 162 / 68,9% | 2.4.2; Tab. 3.3; 3.4.4 | consistente |
| 74 de 76 / 97%; 86 de 86 / 100% | Tab. 3.3; "almost all" (3.4.5) | consistente |
| 187 com infraestrutura / 79,6% | 3.4.4; Tab. 3.3 | consistente |
| 8 não resolvidos / 3,4% | 2.4.2; 3.4.4; nota da Tab. 3.3; 5.7 | número consistente; 5.7 muda a variável (C-075) |
| 996 registros | 1.3 | sem ligação com 2.4 (C-073) |
| 18 países; 335 vínculos | 2.4.1 | únicos |
| 20 de setembro de 2026 | 1.3; 2.2.2; 2.4.1 | consistente |
| 5 lacunas | Resumo; Abstract; 3.2; Tab. 3.1; 5.1 | consistente |
| 12 domínios CtQ | Resumo; Abstract; 2.2.3; 3.3; Tab. 3.2; Fig. 4.4; 4.8; 5.x | consistente (algarismo × "twelve", C-082) |
| 12 requisitos | Resumo; Abstract; 3.5; Tab. 3.4; Tab. 4.1; Fig. 4.5; 5.4; 6 | consistente |
| 4 pilares | Resumo; Abstract; 2.5.1; 3.2.1; 4.1; Fig. 4.2; 5.1; 6 | número consistente; nome (C-016) e fontes (C-008) não |
| 24 instrumentos (7/5/9/3) | Resumo; Abstract; 4.8; Tab. 4.4; Fig. 4.2 a 4.5; 5.5; 5.7; 6 | consistente: a Tab. 4.4 tem 12 + 12 e a Fig. 4.3 posiciona 24. 5.7 sugere que a contagem não é auditável. |
| 7 fases | Resumo; Abstract; 4.6; Fig. 4.1; 6 | consistente |
| 3 tipos de centro | Resumo; Abstract; 4.7.1; Tab. 4.3; 5.7 | número consistente; nomes não (C-083) |
| 6 indicadores | 4.5; Fig. 4.3; Tab. 4.1; 5.2; 5.4; 5.7 | consistente; 4.5 menciona "earlier set of five" (C-044) |
| 5 condições estruturais (+1) | 1.3; 3.4; 3.4.1; 5.3 | número consistente; nomes não (C-015) |
| 4 critérios do E8(R1) | 2.2.2; 2.2.3; 3.3 | consistente |
| 9 checks | 4.4.1 (2×); Tab. 4.1 | consistente, mas redundante (C-058) |
| 3 fluxos de risco (ISO 6.2) | 4.3; 4.6.1; 5.5 | número consistente; detalhe divergente (C-049) |
| Delphi: 21 × 71 participantes; 59 estratégias; 14 de consenso | 1.4.1; 5.2 | **inconsistente** (C-002) |
| Delphi: 40 especialistas, 15 países, 13 itens | 1.4.1; 5.2 | consistente |
| 109 estudos; 2 de 12; 86 de 97; 74 | 1.4.1; 5.2 | consistente |
| 126 → 18 indicadores; 4 domínios | 1.4.2; 5.2 | consistente |
| 44 CTUs; 89% | 3.4.2; 5.3 | consistente |
| 19,6% (Portugal) | 4.3.1; 5.1 | consistente |
| ISO 14155:2026 publicada em 23/03/2026 | 1.1; 5.5 | consistente |
| EN ISO 14155:2020+A11:2024; Decisão (UE) 2026/193 | 1.1; 5.5 | número consistente; designação varia (C-086) |
| 5 estratos de complexidade | 5.6; 6 | ausente nos Resultados (C-077) |
| Apêndices A a X (24) + Y | 2.5.2; 4.6.2; 4.8 | consistente (o Y existe na lista de apêndices; conteúdo não revisado) |

### 4.5 Referências cruzadas

Status: **ok** = aponta para o que diz; **quebrada** = o alvo não contém o que se promete, ou não existe; **imprecisa** = o alvo existe, mas o conteúdo está em outro lugar ou só em parte.

| Origem | Referência | O que de fato aponta | Status |
|---|---|---|---|
| 1.3 | Section 2.4 (amostra final) | 2.4 dá a amostra, sem ligação com os 996 registros | imprecisa (C-073) |
| 1.3 | Section 3.4.4 (suposições de projeto) | as suposições estão em 3.4.5 | imprecisa (C-068) |
| 1.5 | Section 1.4; Section 1.3; Section 2.6 | conteúdo correspondente | ok |
| 2.1.1 | Chapter 1, Sections 3.2 and 3.3 (problema) | ok; 3.4 (condições) fica de fora | ok |
| 2.1.1 | Section 3.5 (objetivos como DR) | ok, mas 3.5 se põe na 3ª atividade | ok (C-003) |
| 2.1.1 | Chapter 4; Table 4.1 | ok (falta o 4.2.4 na tabela) | ok |
| 2.2.2 | Chapter 4 (mecanismos do E6(R3)) | ok | ok |
| 2.2.3 | Section 3.3; Section 3.5 | ok | ok |
| 2.3.2 | Section 3.2 (três temas) | os temas não estão lá | quebrada (C-025) |
| 2.3.3 | Section 5.2 (três desfechos) | 5.2 só compara com o CTSPM | imprecisa (C-055) |
| 2.4 | Section 3.4.4 | ok | ok |
| 2.4.2 | Section 3.4.4 and Table 3.3 | ok | ok |
| 2.5 | Section 3.5 | ok | ok |
| 2.5.1 | Section 3.2.1; Table 4.1 | ok | ok |
| 2.5.2 | Section 3.4; Section 4.8; Appendices A through X | ok | ok |
| 2.6 | Section 2.4.3; Section 5.7 | ok | ok |
| 3.2 | Section 2.2; Table 3.1; Section 4.5.4 | ok | ok |
| 3.2.1 | Chapter 4 (quatro pilares) | ok | ok |
| 3.3 | "section 2.2" (critérios) | critérios em 2.2.2, teste em 2.2.3; minúscula (R22) | imprecisa |
| 3.3 | Table 3.2 (coluna "place in the framework") | a coluna não existe | quebrada (C-024) |
| legenda Tab. 3.2 | Section 2.2.2 | os domínios saem de 2.2.3 | imprecisa (C-067) |
| 3.4.1 | Section 1.3 | ok | ok |
| 3.4.2 | Section 3.2.1; Table 3.1 | ok | ok |
| 3.4.3 | Table 3.2 | ok | ok |
| 3.4.4 | Section 2.4; Section 2.4.2 (normalização) | ok | ok |
| 3.4.4 | Section 2.4.2 (definição de infraestrutura) | não existe | quebrada (C-005) |
| 3.4.5 | Table 3.3 | ok | ok |
| 3.4.5 | Section 4.7 ("minimum implementation level") | 4.7.1 põe o alvo no Tipo B, com implementação completa | imprecisa (C-007) |
| 3.5 | Table 3.4 | ok | ok |
| 3.5 | Section 2.2 ("all three came from the clause comparison") | só os gaps vêm de 2.2 | quebrada (C-006) |
| Tab. 3.4 | §3.2.1 ("The CAPA cycle"); §3.4.5 ("Team size…") | conteúdo ausente | imprecisa (C-090) |
| 4.1 | Chapter 3; Table 4.1; Section 3.4.4; Section 3.4.5 | ok | ok |
| legenda Tab. 4.1 | Section 3.5 | ok | ok |
| Tab. 4.1, DR6 | "4.6.2 phase 4" | está em 4.6.1 | imprecisa (C-070) |
| 4.2 | Section 4.3 (curva de aprendizagem) | ok | ok |
| 4.3.1 | Table 3.1 | ok | ok |
| 4.3.2 | Section 3.4.2 (2×) | ok | ok |
| 4.3.3 | Section 2.2.2 ("proactive") | o termo não está lá | quebrada (C-050) |
| 4.4.1 | Section 4.3.3 | ok | ok |
| 4.4.2 | Section 3.4.1 | ok | ok |
| 4.5 | Section 3.5 (DR8 ← domínios 2, 7, 10, 11) | ok (Tab. 3.4) | ok |
| 4.5.6 | Section 4.4.1 | ok | ok |
| 4.5.7 | Section 4.4.1 ("domains listed") | são *checks* | imprecisa (C-071) |
| 4.6 | Section 3.3 | ok | ok |
| 4.6.1 | Section 4.5.7; Section 5.4 | ok | ok |
| 4.6.1 / legenda | Figure 4.1 (condições de entrada e saída) | não estão na figura | quebrada (C-023) |
| 4.6.2 | "phase 2, one phase before the first surgery" | a cirurgia é a Phase 4 | quebrada (C-022) |
| 4.6.2 | Appendix Y | consta na lista de apêndices | ok |
| 4.7.1 | Section 3.4.5 (Tipo B = cenário de 3.4.5) | 3.4.5 descreve outro perfil | imprecisa (C-007) |
| 4.8 | Table 4.4; Figures 4.2 to 4.5; Section 3.5 | ok | ok |
| 4.8 | Section 2.2.2 (domínios) | 2.2.3 e 3.3 | imprecisa (C-067) |
| Lista de Tabelas | Table 4.2 | não existe | quebrada (C-027) |
| legenda Fig. 4.3 | "Operational Controls appears as four groups" | três grupos | quebrada (C-052) |
| 5.1 | Section 1.1 | ok | ok |
| 5.1 | Section 3.4.4 ("center described") | 3.4.5 | imprecisa (C-069) |
| 5.1 | Section 3.2; Chapter 3; Table 3.1; Section 3.4.2 | ok | ok |
| 5.1 | Section 3.2.1 (pilares tirados de ISO 13485, 14971 e 15189) | 3.2.1 usa 13485, 14971 e 14155 | quebrada (C-008) |
| 5.2 | Section 4.5; Section 3.3; Section 3.2; Section 2.3.2 | ok | ok |
| 5.3 | Section 1.3 and Section 3.4.1; Section 4.4.2; Section 3.5; Section 4.7.3; Section 5.7 | ok | ok |
| 5.3 | Section 3.4.4 ("states which of the two governs") | não decide | quebrada (C-012) |
| 5.4 | Section 3.3; Section 4.4.1; Section 5.3; Section 3.4.5 | ok | ok |
| 5.5 | Section 4.6; Section 5.3; Section 5.1; Section 3.4.1; Section 4.3.2 | ok | ok |
| 5.6 | Section 1.3; Section 4.8 | ok | ok |
| 5.7 | Section 2.1.1; Section 2.3.1; Section 5.2; Section 4.7; Section 5.6; Section 5.5; Section 5.4 | ok | ok |
| 5.7 | Section 5.3 ("protected margin") | o termo não está em 5.3 | imprecisa (C-072) |
| 5.7 | Section 3.4.4 ("has to state") | placeholder | quebrada (C-012) |
| 5.7 | Section 2.4.3 (limitações) | conteúdo diferente | imprecisa (C-075) |
| 6 | Chapter 3; Chapter 4; Section 3.5; Table 4.1; Section 2.4; Section 2.4.3; Chapter 2; Section 5.6; Section 5.7 | ok | ok |
| 6 | Section 5.1 ("most exposed claim and its clearest addition"; "traceability … over the alternative") | 5.1 diz outra coisa | imprecisa (C-076) |
| 6 | Section 1.2 ("opened this thesis… shift") | está em 1.1 | quebrada (C-051) |

**Totais:** 70 linhas, com cerca de 125 remissões individuais (as linhas "ok" agrupam várias remissões da mesma origem). Por linha: 42 ok, 15 imprecisas e 13 quebradas.

### 4.6 Redundância (estimativa)

| Bloco repetido | Onde | Palavras repetidas (estimativa) |
|---|---|---|
| Revisão da literatura recontada | 5.2 × 1.4.1–1.4.2 | ≈500 |
| Condições cirúrgicas recontadas | 5.3 × 3.4.1–3.4.3 | ≈270 |
| Objeção da escala e números do registro | 5.3 × 4.7.2, 3.4.4 | ≈120 |
| ISO 14155 (6.2, 9.2.4.5 p), CEC, edição harmonizada) | 5.5 × 4.3, 4.4.2, 1.1 | ≈190 |
| Justificativa "backward" | 5.1 × 3.5 × 6 | ≈80 |
| Limite da revisão narrativa e ausência de comparação ICH × ISO | 5.7 × 2.6 × 3.2 × 5.2 | ≈100 |
| Transferibilidade | 5.6 × 5.7 × 4.8 | ≈110 |
| Ciclo de vida | 5.4 × 4.6, 4.6.2 | ≈60 |
| Backlog MDIC/EMA; nove checks | 4.4.1 × 4.5.6 | ≈65 |
| Estudo português | 5.1 × 4.3.1 | ≈35 |
| UDI e decisões cirúrgicas; cartão de implante; Clause 10.3 | 1.3, 3.3, 3.4.1, 5.3; 3.2 × 3.2.1 | ≈100 |
| **Total** | | **≈1.600 (faixa 1.500 a 1.700)** |

### 4.7 Mapa de tom por capítulo (abertura e registro)

| Cap. | Abertura | Registro | Pessoa | Desvio |
|---|---|---|---|---|
| 1 | "Over the past decade, quality management in clinical research has changed [1, 2]." | expositivo, direto | 3ª impessoal, com um "we" em 1.3 | C-065 |
| 2 | "As already stated, the objective of this thesis is to build a framework of quality…" | mais solto, sinais de ditado pouco revisado | 1ª do plural | C-042 |
| 3 | "This chapter reports the analysis that precedes the framework…" | analítico, com frases curtas enfáticas ("What is missing is not a rule. It is a layer."; "Verification comes too late.") | 1ª do plural | (tratado por outras lentes) |
| 4 | "Chapter 3 closed the second activity of the DSRM…" | especificação, com uma camada ensaística em molde fixo | 1ª do plural | C-043 |
| 5 | "Conducting an investigation well and showing that one operates a system are separate accomplishments…" | abstrato e aforístico; 5.5 com registro ético-retórico | 1ª do plural | C-066 |
| 6 | "This thesis set out to answer a question that ICH E6(R3) and ICH E8(R1) raise without resolving: …" | fechamento; pergunta indireta sem ponto de interrogação; metacomentário ("still worth stating plainly") | impessoal | C-091 |

### 4.8 Coerência do arco (síntese)

- A cadeia lacuna/domínio/condição → requisito → componente está completa nas tabelas (3.4, 4.1, Fig. 4.5), mas a prosa se contradiz sobre o critério de entrada (C-009), a origem (C-006), a fonte dos pilares (C-008) e a atividade DSRM (C-003).
- A lacuna da curva de aprendizagem, ponto que o contrato manda deixar cristalino, tem citação errada na Tab. 3.1 (C-010), um DR3 que nunca aparece na prosa (C-056), um instrumento com três nomes (C-019) e uma tensão sobre a Clause 10 (C-035).
- A evidência empírica mais direta da lacuna 2 ([76]) só aparece nos Resultados (C-078). Os cinco estratos de complexidade só aparecem na Discussão (C-077).
- O Capítulo 5 gasta cerca de 900 palavras recontando 1.4 e 3.4 (C-046, C-047). Nessas passagens ele explica a obra de novo em vez de confrontá-la com algo de fora, como pede a skill.
