# Diagnóstico da tese (versão recebida: `Revisao_manual_tese.docx`)

Li a tese inteira, incluindo tabelas e figuras (que estão como imagem), referências e apêndices, e comparei tudo com o guia de estilo (`revisao/guia-de-estilo.md`). Os itens abaixo indicam a **seção** onde está cada problema, porque é assim que você acha no Word. Os códigos [F], [C], [R], [T], [G] e [E] estão explicados na seção 5 do guia.

## Atualização: depois da skill do autor (`thesis-writing`)

Este diagnóstico (v1) foi escrito antes de eu receber a sua skill. Com ela, três pontos daqui mudam e aparecem achados novos. A análise v2 (`revisao/workflow.md`) já parte das regras da skill.

**O que muda neste diagnóstico:**
- **Tamanho das frases.** Ignore as metas de média ou de teto que apareciam no guia v1. A skill não tem teto nem média: o que importa é a **dispersão** e se uma frase longa obriga a reler. As médias da tabela abaixo ficam só como informação.
- **"therefore".** Não é defeito por si (ver a linha "Palavras-muleta" da seção 6). É o conector de consequência que a skill pede. Só é defeito quando abre dois parágrafos da mesma seção ou não marca consequência nenhuma.
- **P4, a mediana não recalculada.** A frase segue a sua regra de honestidade (é o *worked case* da skill). A melhor saída é **calcular** a mediana com os seus dados do registro. Se não der, a frase fica, reescrita sem tom de nota de trabalho.

**Achados novos com a skill:**
- **Versão do arquivo.** Sete formulações que a sua skill lista como *já substituídas* ("Written → Replaced with") continuam no Cap. 1 deste `.docx`: *formalized Quality by Design*, *gave this idea an operational form*, *has to be operational to be real*, *noted the absence of standardized instruments*, *translates … into practices*, *designed to complement the obligations*, *an artifact derived from documented evidence*. Das versões aceitas, só *pointed out that there are no standardized instruments* aparece (5.2). **Decisão do autor:** este `.docx` passa a ser a versão definitiva, e as substituições já aceitas na skill entram na reescrita.
- **"we" na Introdução:** *"Within this context, we narrowed the work…"* (1.3). Pela skill, a Introdução é impessoal.
- **Disfarces de oposição:** 18 casos de *", not X"* (11 no Cap. 4) e 5 de *"not X. It is Y"*. *rather than*, *instead of* e *and not* já estão em zero.
- **Caudas autocomentadas:** 55 candidatos *", and this/that/it"* e 14 *", which is the"*. São candidatos, não veredito.
- **Ponto e vírgula fora de citação:** 21.
- **Trios:** muito frequentes, sobretudo no Cap. 4.
- Já estão em zero: travessões, contrações, *Taken together*.

## Visão geral

O argumento é bom e a tese é honesta sobre os próprios limites. A ideia central (o centro de investigação é o único elo da cadeia sem um sistema de qualidade descrito) está bem sustentada, e a rastreabilidade requisito → componente é um ponto forte. Os problemas são de **acabamento**:

1. **Incoerências internas**: números que mudam entre capítulos, remissões para seções que não dizem o que se afirma, as etapas da DSRM contadas de formas diferentes, a origem dos quatro pilares contada de quatro jeitos.
2. **Redundância**: a Discussão (5.2) repete quase toda a Introdução (1.4), e os números do registro aparecem em sete lugares.
3. **Tom desigual**: o Cap. 2 tem frases informais e algumas quebradas. Os Caps. 4 e 5 são lisos e longos demais, com marcas de texto de IA (seção 4 do guia).
4. **Convenções**: siglas alternando com a forma por extenso, ortografia britânica nas tabelas, hífens, números, maiúsculas nos títulos.
5. **Pendências** que impedem a entrega (seção 1 abaixo).

Números do texto, sem referências nem apêndices:

| Capítulo | Palavras | Média de palavras por frase | Frases com mais de 35 palavras |
|---|---|---|---|
| 1 Introduction | 3.064 | 18,5 | 5 |
| 2 Methodology | 3.749 | 17,0 | 3 |
| 3 Gaps and requirements | 4.578 | 18,4 | 6 |
| 4 Results | 11.201 | 21,6 | 48 |
| 5 Discussion | 8.720 | 23,6 | 51 |
| 6 Conclusion | 765 | 24,7 | 4 |

---

## 1. Pendências (antes de qualquer polimento)

| # | Onde | O que falta |
|---|---|---|
| P1 | 2.4.1 | Ainda está no texto o marcador **"[institutional ethics determination or policy citation required]"**. Falta citar a decisão ou norma da faculdade sobre ética e dispensa de aprovação. |
| P2 | Apêndices A–X | Os 24 templates estão como *"[Template pending]"*, e o Apêndice Y como *"[Content pending]"*. |
| P3 | Acknowledgments | A página está vazia. |
| P4 | 5.7 | *"We have not recalculated the median number of sites or the median target enrollment for the 46 investigations…, so no figure is given here."* É nota de trabalho: ou se calcula o número (você tem os dados do registro), ou a frase sai. |
| P5 | 5.7 (e 5.3) | *"…Section 3.4.4 has to state which of the two governs the argument."* Outra nota de trabalho. Além disso, a 5.3 diz que a 3.4.4 **já** afirma isso, e ela não afirma. Falta escrever essa frase na 3.4.4 ou na 3.4.5. |
| P6 | Listas de tabelas e figuras | Todas as entradas mostram a página "1" (o campo não foi atualizado), e **não existe Tabela 4.2** (a numeração pula de 4.1 para 4.3). |
| P7 | Figura 4.1 | A imagem está inserida **duas vezes** no mesmo parágrafo, uma por cima da outra. É preciso apagar uma no Word. |

## 2. Fatos, números e referências [F]: preciso da sua confirmação

| # | Onde | Problema | Proposta |
|---|---|---|---|
| F1 | 1.4.1 vs 5.2 | O Delphi da ref. [37] aparece com **21** participantes na 1.4.1 e com **71** na 5.2. No PubMed, o resumo de Butterworth et al. (2025) diz *"Seventy-one peer-nominated, international, expert trial stakeholders"* ([DOI](https://doi.org/10.1016/j.ejso.2025.109593)). | Corrigir a 1.4.1 para 71. |
| F2 | Tabela 3.1, lacuna 3 | Cita **[59, 61]** para *"observation of learning during conduct is rare"*. Na lista de referências, [59] é Patra (imagem de aneurisma) e [61] é Lippe (RM do manguito rotador). O que sustenta a frase são **[70, 71]** (Conroy et al.), como na 3.4.2. A numeração da tabela-imagem é de uma versão antiga da bibliografia. | Trocar por [70, 71] e conferir as citações de **todas** as tabelas em imagem. |
| F3 | 4.3.2 | *"…the validated Clinical Trial Site Performance Measure contains no counterpart… [37, 39]"*. A *Clinical Trial Site Performance Measure* é a ref. **[41]**; [37] e [39] cobrem só a parte de SQA. | Usar [37, 39, 41]. |
| F4 | 2.3.2 e 2.5.2 vs ref. [34] | O texto fala do suplemento do MDIC **de 2017**; a referência [34] diz **2016**. | Conferir o ano e alinhar. |
| F5 | Cap. 6, 3º parágrafo | *"roughly **one in four** … present no publicly documented permanent research structure"*. Os números dizem outra coisa: 38/235 = 16,2% (≈ um em seis). "Um em quatro" (65/235 = 27,7%) é a fatia de organizações **não hospitalares**. | Corrigir para "about one in six" ou reescrever. |
| F6 | Cap. 6, último bloco | *"Section 1.2 opened this thesis by describing a shift…"*. Essa mudança é descrita na **1.1** (a 5.1 cita a 1.1 corretamente). | Trocar por 1.1. |
| F7 | 3.4.4 | *"Permanent clinical trial infrastructure was assessed … under the definition in Section 2.4.2"*. A 2.4.2 **não define** infraestrutura permanente: a palavra *permanent* não aparece no Cap. 2. | Acrescentar à 2.4.2 a definição usada e as fontes consultadas. |
| F8 | 5.7 | *"Eight of the 235 organizations remain unresolved on the trials structure variable"*. Na 2.4.2 e na Tabela 3.3, essas oito ficaram sem classificação de **ambiente**, e a infraestrutura delas é "N/A". | Alinhar a formulação. |
| F9 | 5.7 | *"All classifications were verified case by case and reviewed in a second internal pass"*. Essa segunda revisão interna não está descrita nos Métodos (2.4.2–2.4.3). | Descrever na 2.4.3 ou tirar da 5.7. |
| F10 | 4.3.3 | *"…proactive risk management in the sense Section 2.2.2 already gave the term"*. A 2.2.2 não define *proactive* (a palavra não aparece no Cap. 2). | Definir no ponto certo ou tirar a remissão. |
| F11 | 5.3 | Fair Market Value e regras antissuborno dos EUA, e *"Research compensation … is calculated per procedure and per participant…"*: nada disso tem citação. | Citar ou reduzir a afirmação. |
| F12 | 5.7 | *"registration on ClinicalTrials.gov is mandatory for a large share of studies conducted there and voluntary elsewhere"*: sem citação (FDAAA 801 ou 42 CFR Part 11). | Citar. |

## 3. Incoerências internas [C]

| # | Onde | Problema | Proposta |
|---|---|---|---|
| C1 | 2.1.1, 2.5, 3.5, 4.1 | **As etapas da DSRM são contadas de formas diferentes.** A 2.1.1 e a 2.5 dizem que os requisitos (DR1–DR12) são a **2ª** atividade (*objectives for a solution*). A 3.5 diz que eles completam *"the first part of the **third** DSRM activity"*. A 4.1 diz que o Cap. 3 *"closed the second activity … and started the third by designing the requirements"*. | Seguir Peffers: os requisitos são a 2ª atividade e o Cap. 4 é a 3ª. Corrigir a 3.5 e a 4.1. |
| C2 | 2.5.1, 3.2.1, 4.1, 5.1 | **De onde vêm os quatro pilares**: cada seção conta de um jeito. 2.5.1: ISO 13485 + ISO 14971, com a ISO 15189 só como analogia e *"these standards do not state a common four-part taxonomy; we synthesized"*. 3.2.1: ISO 13485 + 14971 + **14155**. 4.1: 13485 + 14971 + 14155 + **ICH**, com mapeamento cláusula a cláusula. 5.1: *"ISO 13485, ISO 14971, and **ISO 15189 each require the same four functions** … Section 3.2.1 took the taxonomy of pillars from them"*. A 5.1 contradiz a 2.5.1 de frente. | Uma versão só (a da 4.1 é a mais completa), dita na 2.5.1 e retomada sem variação. |
| C3 | Abstract, Resumo, 1.5, 3.1, 3.2, 3.2.1, 3.4.1 | **Quantos instrumentos foram analisados?** O Abstract diz *"four regulatory and guidance instruments"*. A 1.5, a 3.1 e a 3.2.1 dizem três. A 3.2 começa com *"the four instruments place…"*. A 3.4.1(4) fala em *"none of the four governing instruments"*. | Definir uma vez: "três na comparação cláusula a cláusula (ICH E6(R3), ISO 14155:2026, MDR Anexo XV), com a ICH E8(R1) como referência conceitual". |
| C4 | Abstract, Resumo, 2.5.1 vs Cap. 4 | O **pilar 2** se chama *RBQM* ou *gestão da qualidade baseada no risco* nos três primeiros e *Risk Management* no Cap. 4 e nas figuras. | *Risk Management* ⚠️ |
| C5 | Título, Abstract, Resumo, 1.5, Cap. 4 | **Framework, architecture ou model?** O título diz *Framework*; o Abstract e o Resumo, *architecture/arquitetura*; o Cap. 4, *Site-Centered Operational Quality Management Framework*. | *framework* para o artefato ⚠️ |
| C6 | 1.3, 3.4.1, 5.3 | As **cinco condições** mudam de nome (*traceability*, *persistent traceability*, *unit-level traceability*; *follow-up*, *the operational weight of follow-up*; *measurement reliability*, *limited classification reliability*). A 5.3 transforma as cinco em *"the four demands"* sem avisar que irreversibilidade e rastreabilidade viraram uma só. | Nomes fixos e uma frase explicando a fusão. |
| C7 | 3.4.3, 5.3, Tabela 3.4 (DR6) | **Os "quatro dados" do ponto de cuidado** mudam de lista. A 3.4.3 lista substituição, desvio técnico, imagem pós-op. imediata e complicação precoce. A 5.3 lista registro de rastreabilidade, substituição, desvio e imagem. O DR6 lista identificadores, desvios e substituições, e imagem. | Uma lista só. |
| C8 | 3.4.1(4) vs 5.3 | A 3.4.1 diz que nenhum instrumento exige *"the same assessor at every visit"*. A 5.3 diz que ROM e PROs *"require … the same assessors and the same acquisition conditions at every time point"*. | Na 5.3, trocar por "consistent assessment procedures". |
| C9 | 4.6.2 vs Figura 4.1 | *"…initialized in phase 2, **one phase before the first surgery**"*. Na Figura 4.1 a cirurgia é a Fase 4 (a 3 é Enrollment), então são duas fases. | "before the first surgery" |
| C10 | 4.6, 5.5, Figura 4.1 | **Quando abre o Site Risk Register?** A 4.6 diz "antes da inclusão". A 5.5 diz que ele *"has to open during feasibility"* (Fase 1), mas o põe **depois** dos sete instrumentos de Governance (Fase 2). A Figura 4.1 não mostra o SRR em nenhuma fase. A 5.5 também põe o *learning curve log* depois do SRR *"since both depend on cases having started"*, enquanto a 4.6.2 diz que ele é iniciado na Fase 2. | Alinhar a ordem de implantação (5.5) com o ciclo de vida (4.6 e Figura 4.1). |
| C11 | 3.3 vs Tabela 3.2 | O texto diz que cada domínio é descrito *"by the place in the framework where it is addressed"*, mas a tabela não tem essa coluna. | Acrescentar a coluna ou tirar a frase. |
| C12 | 2.6 | Anuncia *"Three limitations apply to the work as a whole"* e apresenta só duas. | Incluir a terceira (avaliador único) ou dizer "two". |
| C13 | 4.5.7 | *"…against the **domains** listed in Section 4.4.1"*, mas a 4.4.1 lista nove **checks**. | "checks". |
| C14 | 4.2.1 | Anuncia *"five mechanisms"*. Os três primeiros parágrafos descrevem a **dificuldade** de cada mecanismo sem dizer qual é o mecanismo (agenda de revisão por níveis? graduação da criticidade? pontos de revisão predefinidos?). O 4º e o 5º estão claros. | Abrir cada parágrafo dizendo o mecanismo e só depois a dificuldade. |
| C15 | 4.4.2 | Aparecem a *"third difficulty"* e a *"fourth difficulty"*, mas a primeira e a segunda nunca são chamadas assim. | Numerar todas ou nenhuma. |
| C16 | Tabelas 3.4 e 4.1 | O DR10 cita *"personification of quality (§3.4.5)"*, e o DR11, *"Research as a secondary activity (§3.4.5)"*. Nenhum dos dois termos aparece na 3.4.5 (o segundo só aparece na 5.3). O DR6 da Tabela 4.1 aponta para *"4.6.2 phase 4"*, mas as fases estão na 4.6.1 e na Figura 4.1. | Atualizar as remissões. |
| C17 | Legendas da Tabela 3.2 e da Figura 4.4 | Dizem que os domínios vêm *"from Section 2.2.2"*. A 2.2.2 descreve o **método**; os domínios estão na **3.3**. | "Section 3.3". |
| C18 | 3.5 | *"…each requirement comes from a gap, a domain, or an operating condition, and **all three came from the clause comparison in Section 2.2**… so nothing in the framework is invented."* As condições operacionais vêm do registro e da literatura, não da comparação de cláusulas. E o Cap. 6 admite uma exceção (curva de aprendizagem). | Ajustar a frase. |
| C19 | 5.1, 5.5, Cap. 6 | A 5.1 descarta as vias "patrocinador" e "software". A 5.5 propõe que o patrocinador **construa** a arquitetura e o centro a opere e seja dono dos registros. O Cap. 6 volta a descartar o patrocinador, sem mencionar essa via híbrida. | Fazer o Cap. 6 refletir a nuance da 5.5. |
| C20 | Resumo vs Abstract | O Resumo não diz **ombro** (o Abstract e o título dizem *shoulder*). Na lista de funções, falta *deviation control*. "Quatro instrumentos oficiais" também não bate com o Abstract. | Alinhar o Resumo ao Abstract final. |
| C21 | 3.4 | *"Six main conditions apply in total. Five are structural…, and two of those are restrictive enough… The sixth…"*: difícil de seguir. | Reescrever com a estrutura explícita. |
| C22 | 5.5 (ética) | *"Describing the learning curve log as an instrument that does not assess professional performance is therefore inaccurate"* responde a algo que a tese nunca diz. Parece resposta a um comentário de orientador. | Afirmar diretamente: "The log assesses professional performance, so its use has to be governed…". |

## 4. Redundâncias [R]

O maior ganho de clareza da revisão está aqui. Só cortando repetições, a Discussão deve encolher uns 25–30%.

| # | O que se repete | Onde | Proposta |
|---|---|---|---|
| R1 | **Revisão de literatura inteira**: TransCelerate, CTTI e MDIC (parágrafo quase idêntico), revisão SQA em oncologia, ROMIO, os dois Delphi, enxertos arteriovenosos, os 109 estudos de QI ("2 de 12" e "86 de 97"), CTSPM ("126 → 18"), "reactive and ad hoc" [42–44], [45], [46, 47] e Diani [48]. | 1.4 e 5.2 | A 1.4 apresenta (o que existe). A 5.2 só **posiciona** o framework (o que ele acrescenta e a comparação item a item com a CTSPM), remetendo à 1.4 sem descrever de novo. |
| R2 | **Números do registro** (235, 65, 27,7%, 38, 58,5%, 60, 92,3%, 149, 63,4%) | 1.3, 2.4.2, 2.4.3, 3.4.4, 3.4.5, 5.3, 5.7, 6 | Números completos só na 3.4.4 (resultados). Introdução e Conclusão com uma frase cada. A 5.3 remete. |
| R3 | "O centro é o único elo sem norma de sistema de qualidade" | 3.2.1, 3.5, 5.1 (2×), 6 | Uma afirmação na 3.2.1; depois, remissão. |
| R4 | "A justificativa corre para trás" (*traces back*) | 3.5 e 5.1 (quase o mesmo parágrafo) | Manter na 3.5; a 5.1 discute os limites dessa justificativa sem repeti-la. |
| R5 | Curva de aprendizagem: survey de 44 CTUs no Reino Unido (89%) e *"a protocol … cannot standardize the many small decisions…"* | 3.4.2 e 5.3 (frases quase iguais); o assunto volta na 3.2.1, 4.3.2, 5.1 e 6 | Dados na 3.4.2; a 5.3 discute a implicação para o desenho. |
| R6 | Rastreabilidade no ponto de cuidado: *"in the operating room, under time pressure, by staff whose attention is on the procedure"* | 3.4.3 e 5.3 | Uma vez. |
| R7 | Confiabilidade das classificações (kappa, fraturas do úmero proximal, *core outcome sets*) | 1.3, 3.4.1(5), 5.3 | Dados na 3.4.1; a 1.3 só cita; a 5.3 remete. |
| R8 | Exposição a inspeção nos centros menores | 4.7.2 e 5.3 | Argumento na 4.7.2; a 5.3 só registra que a premissa não tem fonte. |
| R9 | Três fluxos de risco da ISO 14155 Cl. 6.2; calibração Cl. 9.2.4.5(p); CEC Cl. 6.12 | 3.2.1, 4.3, 4.3.3, 4.4.2, 5.4, 5.5 | Detalhe técnico uma vez; depois, remissão. |
| R10 | Estudo português, 19,6% [76] | 4.3.1 e 5.1 | Uma vez, com remissão. |
| R11 | "Adaptabilidade estrutural é plausível, mas não demonstrada" | 4.8, 5.6 (2× em parágrafos seguidos), 6 | Uma vez na 5.6. |
| R12 | *"The nine checks below define what it has to cover. Nine checks define the scope of internal review."* | 4.4.1, frases seguidas | Cortar uma. |
| R13 | Conclusão que repete a Discussão (limitações, transferibilidade) | Cap. 6 | Cap. 6 com 4 parágrafos: pergunta → resposta → contribuição e limite principal → o que fica aberto. |

## 5. Tom e registro [T], capítulo por capítulo

**Resumo e Abstract.** O Resumo tem uma frase quebrada: *"Aplicámos a DSRM e através de uma revisão narrativa e a análise cruzada dos quatro instrumentos oficiais e análise de registos de 46 investigações e 235 organizações."* Não tem verbo principal para "através de". O Abstract está bem, com três ajustes: *"day to day"* → *"day-to-day"*; *"directed the creation of 12 design requirements"* → *"led to 12 design requirements"*; e confirmar se *"problem-centered DSRM"* é o termo de Peffers (*problem-centered initiation*). Os dois devem ser revisados **por último**.

**Cap. 1.** É o capítulo mais limpo. Pontos a ajustar:
- 1.1: *"sites and sponsors would find problems … and then corrected them"* mistura tempos.
- 1.2: a lista "1- Identify…" tem formato fora do padrão.
- 1.3: as cinco condições são apresentadas com cinco construções diferentes. Em especial, *"Follow-up carries substantial operational weight, the fourth condition"* soa estranho.
- A ISO é redefinida na 1.5.

**Cap. 2.** É o capítulo que mais precisa de trabalho. É o mais coloquial e tem frases gramaticalmente quebradas, o que destoa do resto. Exemplos:
- 2.1.1: *"As already stated, the objective of this thesis is to build a framework of quality that supports the guidelines required principles."*
- 2.1.1: *"Four of those activities are reported here Chapter 1 and Sections 3.2 and 3.3 carry…"* (faltam dois-pontos e falta concordância).
- 2.1.2: *"…and the site registry helps define where the work is done and direct construction."*
- 2.2.1: *"Although very important their main focus is still mainly drug investigational products, so we needed to go after the device-specific obligations…"*
- 2.2.1: *"…also known as medical device regulations (MDR)"* (a sigla MDR já foi definida na 1.1, e de outra forma).
- 2.2.2: *"We can see that those considerations are more related to guide CtQs based on the perspective of the sponsor."*
- 2.2.2: *"…we recorded every attribute that introduced a concept CtQ…"*
- 2.2.2: *"…in the ICH guidelines [5, 6].)"* (pontuação).
- 2.3.1: *"A narrative review may lose exhaustiveness, but it improves the focus on the right scope and prevent divergence, this is important since…"*
- 2.5.1: *"But it does not prove that another better taxonomy can exist."* O sentido está invertido; o certo seria "that no better taxonomy exists".

**Cap. 3.** Está bom no geral. Pontos a ajustar:
- 3.1: a última frase termina em vírgula (*"…an explicit set of design requirements,"*).
- 3.2: *"These attributes cluster into five gaps as we can see at Table 3.1"* (falta o ponto final; o certo é *in* Table 3.1).
- 3.2: *"A set of attributes that despite being heavily influenced by day-to-day operations is unaddressed at site level…"* (sintaxe quebrada).
- 3.2: *"…the instruments would be glad the site has…"* (personificação).
- 3.3: *"described at section 2.2"*.
- 3.5: *"culminated on"* (o certo é *in*) e *"But the requirements and the domains are therefore not…"*.
- Aforismos que fecham parágrafos: *"Verification comes too late."*, *"What the protocol cannot standardize, the site has to govern."*

**Cap. 4.** Tecnicamente rico, mas é aqui que se concentram as marcas de IA. O molde *"X is harder than…"* aparece 5 vezes (4.2.1, 4.2.3, 4.3.1, 4.3.3, 4.4.1), e há 48 frases com mais de 35 palavras. Frases quebradas ou informais:
- 4.2: *"…which is why the surgical learning curve is treated in Section 4.3 while the qualification decision **it is treated here**."*
- 4.7: *"A framework that completely ignored the academic centers … would fail to achieve any significance…"*
- 4.7: *"We aim that every site that chooses to operate this framework is able to use it to the full extent…"*
- 4.5: *"…our earlier set of five indicators left it without a measure"* (história do rascunho, sai).

**Cap. 5.** Tem as frases mais longas da tese (média de 23,6 palavras; 51 frases com mais de 35), muitas ressalvas e muitos *Nobody* e *itself*. A honestidade sobre limites é uma qualidade e deve ficar, mas concentrada na 5.7 e não espalhada em todo parágrafo. A seção ética (5.5) é boa; só precisa do ajuste C22.

**Cap. 6.** O fecho é bom, mas repete a Discussão (R13). Na primeira frase, *"…what structure does it use to discharge that responsibility."* precisa de ponto de interrogação.

## 6. Convenções [G] e [E]

O detalhe está na skill `thesis-writing` e nas seções 2–3 do guia. Contagens no texto corrido (Caps. 1–6):

| Item | Situação |
|---|---|
| Siglas alternando com a forma por extenso | *Critical-to-Quality* por extenso 8× (sigla CtQ 43×); *principal investigator* 6× (PI 17×); *corrective and preventive action* 5× (CAPA 2×); *Clinical Investigation Plan* 5× (CIP 12×); *contract research organization* 4× (CRO 2×); *risk-based monitoring* 5× (RBM 5×); *adverse event* 5× (AE 12×). A maior parte das formas por extenso está no Cap. 5. |
| Siglas redefinidas | ISO (Abstract, 1.1, 1.5), MDR (1.1, 2.2.1, com formas diferentes), CAPA (Tabela 3.1, 4.5.7). |
| PRO e PROM | PROMs definido na 1.3; PRO na lista de siglas e na Tabela 3.2; *PROs* e *PROMs* se alternam. |
| Ortografia | *orthopaedic* 2× no texto (1.3, 3.4.1); grafia britânica em todas as tabelas e figuras. |
| Hífens | *non-hospital* / *nonhospital* / *non hospital* (as três formas); *non-academic* / *nonacademic*; *inter-observer* / *interobserver*; *learning curve log* / *learning-curve*. |
| Números | *twenty-four* / *24*, *twelve* / *12* alternando (Abstract com algarismos, corpo por extenso). |
| Títulos de seção | *Title Case* em 1.1–1.5 (*"Historical Overview and Recent Updates"*) e *sentence case* no resto (*"Design research"*). |
| *phase 2* / *Phase 2* | As duas formas (4.6.1 e 4.6.2). |
| Normas | *ISO 14155:2026 Section 6.2*, *Section 9.1(b)*, *ISO 13485 Sections 8.5.2* misturados com *Clause*; *9.2.4.5 p)* e *9.2.4.5(p)*. |
| Citações | Caps. 1–4 com citações em **subscrito** (o normal no estilo Vancouver é [n] na linha ou sobrescrito). O Cap. 5 inteiro (19 citações) e 5 citações do Cap. 4 (4.2.1, 4.3.1, 4.3.2, 4.4.1) estão em texto normal. |
| Autores | *Peffers et al.*, *Avendano et al.*, *Blencowe et al.* ao lado de *Diani and colleagues*, *Adams and colleagues*. |
| Palavras-muleta | *", which is"* 27×. *itself* (36×) é traço da voz do autor (aparece 15× nos ditados, calque de "próprio"): corta-se só quando é ênfase vazia. *therefore* (60×) só conta onde abre dois parágrafos da mesma seção ou não marca consequência (ver Atualização). |
| Referências | Títulos ora em *Title Case*, ora em *sentence case* (ex.: refs. 61–65 e 70 em minúsculas); algumas com PMID e outras sem. |

## 7. Tabelas e figuras

| # | Problema | Proposta |
|---|---|---|
| T1 | **Todas as tabelas são imagens.** Não dá para editá-las, buscar texto nelas nem passar o corretor, e é por isso que ficaram com ortografia britânica e referências antigas (F2). | Recriar como tabelas do Word. Posso gerar as tabelas prontas. |
| T2 | Grafia britânica nas imagens: *centre*, *standardised*, *specialised*, *programme*, *authorisation*, *enrolment*, *recognise*, *theatre*, *afterwards*. | Uniformizar (vem junto com T1). |
| T3 | Tabela 3.3: *"Non Academic hospital"*, *"Non hospital"*, *"Confirmed research infra."*, enquanto o texto diz *"permanent clinical trial infrastructure"*. | Alinhar com o texto e com a definição pedida em F7. |
| T4 | A Tabela 4.4 está dividida em duas imagens, e a segunda está ancorada no parágrafo da Figura 4.2. | Uma tabela só, contínua. |
| T5 | A Figura 4.2 usa *"Training Record Evaluation and **Training** Release"* e uma ordem dos instrumentos diferente da Tabela 4.4 e dos apêndices. | Mesmo nome e mesma ordem. |
| T6 | A legenda da Figura 4.5 fala em *"inherited from a combined or earlier instrument"* e *"extension, added to the original set"* (história do rascunho). | Reescrever a legenda sem a história do rascunho. |
| T7 | Legendas com formatação diferente: Tabela 3.2 e Tabela 4.4 em itálico; um "l." em negrito no fim da legenda da 3.2. | Um formato só. |

## 8. Ordem de revisão proposta

1. **Decisões suas**: os itens ⚠️ da seção 3 do guia e os itens [F] acima.
2. **Cap. 2**: reescrever para o registro do resto da tese (maior ganho por palavra).
3. **Caps. 3 e 1**: coerência (C1–C21) e convenções.
4. **Cap. 4**: tirar as marcas de IA, dividir frases longas, ajustar C14–C16.
5. **Cap. 5**: cortar redundâncias (R1–R11) e concentrar ressalvas na 5.7.
6. **Cap. 6, Abstract e Resumo por último**, porque resumem o corpo já revisado.
7. **Tabelas** (T1–T7) e **referências** (formato Vancouver uniforme).

A cada capítulo revisado, o texto em `tese/` é atualizado num commit próprio (o histórico mostra o antes e o depois) e você recebe o arquivo para conferir.
