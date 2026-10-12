# Argument_State — tese de mestrado (Lente 2, APODICTIC)

> **Bloco:** Nonfiction Argument Engine · **Pergunta:** o argumento se sustenta, e onde ele cede? · **Execução:** 2026-10-10, single-agent, register=asserted, gate de alto risco ativo.

**Cabeçalho.** Lente 2 (APODICTIC, motor de argumento não ficcional). Protocolos: Dialectical Clarity v2.1 (passos 1 a 9), Argument Red Team v1.0, Argument Evidence Deep-Dive v1.0; a Persuasion está em `persuasao.md`. Leitura: Caps. 1 a 6, Resumo, Abstract, todas as tabelas e figuras em imagem. Limites: sem Field Reconnaissance (contraevidência na literatura não pesquisada), sem verificação de citações (outra lente), sem leitura das normas originais (ICH, ISO, MDR): onde cito cláusulas, é a leitura que a tese faz delas. Os IDs A-xxx remetem a `registro.md`.

---

## §1. Contexto e classificação

```
Argument type: AT3 (proposta de desenho: "um centro pode operar este framework")
  com um subargumento AT2 (avaliativo: "os instrumentos deixam uma lacuna no nível do centro").
  Promessa: derivar, de forma rastreável, um framework de qualidade do centro que complementa o do patrocinador.
  Burden level: HIGH (dissertação; afirmações regulatórias; júri de especialistas).
  Audience:
    Expertise: EXPERT, mas MIXED entre si (regulação/GCP vs cirurgia ortopédica).
    Receptivity: MIXED (orientadores simpáticos; examinadores céticos por função).
    Consequence context: HIGH (atribuição de grau).
  Consistent throughout: N (o tipo é estável; o C0 varia, ver §2 e §8).
  Codes: AC1 (cada examinador precisa de garantias que o outro dá por sabidas: CtQ/QbD/DSRM para o cirurgião; clustering e curva de aprendizagem para o regulador).
Register: asserted (DEFAULT-ASSERTED; o contrato marca alto risco).
Cash-out inventory: não se aplica (não é registro gerativo).
```

**Comparativo (AT3).** A tese cumpre parte do ônus comparativo: 5.1 examina três rotas (patrocinador, CRO, software) e declara a anti-ideia ("does not establish that a site-owned architecture is the only workable answer"); 4.2.1 compara três modelos de supervisão. Não há derrota FM-A10 (proposta sem comparação). O ponto fraco é outro: a quarta rota (patrocinador constrói, centro opera) aparece em 5.5, depois de 5.1 dizer que não foi examinada (A-053).

---

## §2. Arquitetura das afirmações

**C0 (contrato, aprovado pelo autor).** ICH E6(R3) e ISO 14155:2026 dão ao centro uma parte maior da responsabilidade pela qualidade, mas a maioria dos instrumentos revisados foi feita para o patrocinador. A tese deriva um framework de qualidade do centro que complementa o sistema do patrocinador, para que o centro possa agir sobre riscos que o patrocinador não vê a tempo e possa mostrar como controlou a própria condução.

**C0 como aparece no texto (o C0 nunca está numa frase única; A-058):**
- Abstract: "The architecture provides a traceable method for converting regulatory principles and identified site-level gaps into operational controls across the clinical investigation lifecycle." (método rastreável; sem "a tempo")
- 1.5: "This thesis defines what a site should operate for itself." (normativo, mais forte; A-015)
- 5.1: "the framework as one defensible way of evidencing site-level processes" (conta probatória; modesto)
- Conclusão: "It derives a site-level quality architecture … without inventing an obligation" e "one traceable structure for closing it" (rastreabilidade + "sem inventar", contra a exceção do parágrafo anterior; A-008)

**C0 type:** ASSERTION.

| ID | Subafirmação (necessária para C0) | Onde |
|---|---|---|
| C1 | As diretrizes recentes aumentaram a responsabilidade do centro pela qualidade (modelo de governança). | 1.1, 1.2, 5.1 |
| C2 | Os três instrumentos comparados põem a gestão estruturada da qualidade no patrocinador; há cinco lacunas no nível do centro. | 3.2, 3.2.1, Tabela 3.1 |
| C3 | A infraestrutura existente foi escrita para o patrocinador ou avalia o centro de fora; poucos instrumentos são operados pelo próprio centro. | 1.4, 5.2 |
| C4 | Uma classe de dados críticos nasce no ponto de cuidado e só o centro está presente para capturá-la; riscos de execução local não chegam ao patrocinador a tempo. | 3.4.3, 4.3, 4.3.1, 4.3.3, 5.3, 5.4 |
| C5 | O contexto cirúrgico com implante (dependência do operador, curva de aprendizagem, clustering, confiabilidade de medida, peso do seguimento) exige controles locais; a aprendizagem do cirurgião não é observada durante a condução. | 1.3, 3.4.1, 3.4.2, 4.3.2, 5.1 |
| C6 | Uma parte relevante dos centros é não hospitalar e sem infraestrutura de pesquisa permanente, por isso o framework tem de funcionar em papel, com os papéis existentes e profundidade escalável. | 1.3, 3.4.4, 3.4.5, 4.7, 5.3 |
| C7 | Cada componente responde a um requisito, e cada requisito vem de uma lacuna, de um domínio CtQ ou de uma condição operacional (rastreabilidade). | 2.5, 3.5, Tabelas 3.4 e 4.1, Figuras 4.4 e 4.5, 5.1 |
| C8 | O framework complementa o patrocinador (interfaces definidas) e é exequível sem investimento de capital. | 4.4.3, 4.4.4, 4.7, 4.8, 5.4 |

**Teste de necessidade.** Se C2 cai, C0 perde a lacuna. Se C4 cai, C0 perde "a tempo" e a razão para o centro ser o dono. Se C7 cai, C0 perde "deriva". C5 sustenta a especificidade cirúrgica e o único componente sem obrigação correspondente. C6 sustenta a forma (papel, escalabilidade). C1 e C3 são motivação e posicionamento; C8 é viabilidade.

**STAKES.** Práticos e epistêmicos: segurança do participante e confiabilidade dos dados em investigações de dispositivos implantáveis; capacidade de o centro mostrar o próprio controle. Tipo: PRACTICAL + EPISTEMIC.

**KEY TERMS (onde a pressão definicional importa):**

| Termo | Sentido operacional | Deriva |
|---|---|---|
| T1 gap | 2.2.3: obrigação substantiva que existe mas recai sobre o patrocinador. | 5.1: "silence"; lacuna 3: ausência de obrigação para qualquer parte; 1.4.2: assimetria na literatura. **CL4** (A-042, A-025). |
| T2 instrument | Normas (ICH, ISO, MDR). | Também os 24 modelos do framework e, em 1.4, instrumentos de medida. **RT5** (A-063). |
| T3 site-owned / belong to the site | Registro mantido e controlado pelo centro. | 5.3: "operate at that moment" passa a "belong to the site"; 5.5: patrocinador constrói, centro opera e é dono dos registros. **WR0** (A-049). |
| T4 cannot see / in time | DR4: "cannot reach in time". | 4.3.1: "does not see any of these"; 4.3: "neither function is positioned to see"; 4.3.3: não estabelecido. **DI4** (A-003, A-033). |
| T5 governance review | Revisão que procura uma conta do processo do centro (1.1, 5.1). | Quem revê nunca é dito; 5.5: "the same regulatory surface". **DI3** (A-044). |
| T6 target center | 3.4.5: não hospitalar, infraestrutura incerta, nível mínimo. | 4.7.1: Tipo B, implementação completa. **CL1** (A-004). |
| T7 permanent infrastructure | Variável do registro que seleciona o alvo. | Sem definição em 2.4.2; cinco nomes diferentes. **AE1** (A-012). |

**Códigos CL:** CL1 (C0 em três variantes; alvo em duas identidades), CL3 (encaixe dos requisitos nos pilares feitos a partir deles; A-021), CL4 (gap; A-042).

---

## §3. Mapa de suporte

| Sub | Suporte | Tipo | Esquema | Código |
|---|---|---|---|---|
| C1 | ICH E6(R3), E8(R1), ISO 14155:2026; comentário [7]; pesquisa de maturidade RBQM [13] | AUTHORITY | AUTHORITY | PASS no núcleo; premissa do "modelo de governança" com um só comentário (P3; A-064) |
| C2 | Leitura cláusula a cláusula do autor; busca documental de termos (3.2.1); Tabela 3.1 | REASON + AUTHORITY | SIGN (ausência de cláusula indica lacuna) | **SM4/AE1**: matriz não mostrada, contagens ausentes, um só leitor (A-023, A-017); lacuna 3 não cabe na categoria (A-025) |
| C3 | Revisão narrativa: TransCelerate, CTTI, MDIC [32–34]; SQA [35–40]; CTSPM [41]; estudos de centros [42–47]; Diani [48] | EXAMPLE + DATA | EXAMPLE | PASS em 1.4 ("relatively few"); **BP3/R10** quando passa a "has not been done" (A-024) ou "none of the four" |
| C4 | Raciocínio de mecanismo; cláusulas de rastreabilidade (ISO 14155, MDR); estudo português 19,6% [76] | REASON | CAUSAL / PRACTICAL REASONING | **SM3** (só razão para a vantagem temporal; nenhum dado sobre quem detecta primeiro); a tese o admite em 4.3.3 |
| C5 | Literatura metodológica com números: clustering (>20% erro tipo I [67]; 21,5% [68]); 44 CTUs, 89% [70]; 247 ensaios, 39% [71]; curvas 25 casos, 12–86 [20, 77]; perda de seguimento 14,8% vs 9,8% [23], 34,3% [24]; kappa, ICC 0,91 [61, 62, 83] | DATA + AUTHORITY | CAUSAL + SIGN | PASS (melhor portfólio da tese) |
| C6 | Registro próprio: 46 investigações, 235 organizações, 65 não hospitalares, 38 sem infraestrutura, 60/65 nos EUA | DATA | EXAMPLE (amostra) | **AE1** (variável sem definição; A-012); **BP2** quando generaliza (A-039); **SM0** nas afirmações econômicas de 5.3 (A-050) |
| C7 | Tabelas 3.4 e 4.1; Figuras 4.4 e 4.5 | REASON (artefato) | SIGN (correspondência) | **CL3** (circularidade dos pilares); rótulos partidos (A-029, A-030); DR9 sem mapa (A-041) |
| C8 | Raciocínio de desenho; regra contra registros paralelos; modelo de escalabilidade; premissa de inspeção declarada como não fundamentada | REASON | PRACTICAL REASONING | Regra classifica 8 de 24 instrumentos (A-035); "minimum" não demonstrado (A-052) |

---

## §4. Mapa de garantias (warrants)

| Sub | Garantia | Status | Backing | Qualificador | Defeater refs | Código |
|---|---|---|---|---|---|---|
| C1 | Quem é corresponsável pela qualidade precisa poder mostrar como a exerce (5.1, "Our reading"). | EXPLICIT | THIN (um comentário [7]) | MATCHED em 5.1 ("one defensible way"); OVERCONFIDENT em 1.5 | O6 | WR1 leve |
| C2 | Se nenhuma cláusula atribui ao centro um sistema de qualidade operável, há uma lacuna que o centro pode preencher. | RECOVERABLE | PRESENT para lacunas 1, 2, 4, 5; THIN para a 3 | OVERCONFIDENT em 3.2 ("has not been done"), 3.5 ("nothing invented") | O2 | WR3 (A-002, A-024) |
| C3 | Um instrumento aplicado de fora não serve para o centro perceber a própria deriva a tempo (1.4.2). | EXPLICIT | PRESENT (estudos de centros [42–47]) | MATCHED em 1.4 | NO-MATERIAL-TEXT-INTERNAL-DEFEATER-IDENTIFIED — critério: nenhuma exceção que um leitor misto trataria como viva | PASS |
| C4 | Quem está presente quando o dado nasce tem de ser dono do instrumento que o captura (5.3). | MISSING no salto "operar → pertencer"; RECOVERABLE pela continuidade do registro (5.1, 5.4) | THIN | OVERCONFIDENT em 4.3.1 e 5.4; MATCHED em 4.3.3 e no parágrafo de qualificação de 5.3 | O1, O3 | **WR0** (A-049), **DI4** (A-003, A-033) |
| C5 | Se a execução muda com a experiência, a qualificação inicial não controla uma ameaça que é trajetória (5.1). | EXPLICIT | PRESENT (literatura metodológica) | OVERCONFIDENT em "stop there" (A-032) | O2 | WR3 local |
| C5' | O centro (e não o ensaio, o roll-in ou o patrocinador) é o lugar certo para observar a aprendizagem (3.4.2). | RECOVERABLE (o centro detém a decisão de autorização; 4.2.3) | THIN | — | O1 | **WR0** (A-028) |
| C6 | As condições operacionais de um subgrupo concentrado nos EUA valem para um centro sob o MDR. | MISSING | ABSENT | — | O5 | **WR0** (A-013), premissa P5 |
| C7 | Rastrear cada componente até um requisito mostra que o framework é derivado (não que é necessário nem completo). | EXPLICIT em 5.1 | PRESENT | MATCHED em 5.1; OVERCONFIDENT em 3.5 e na Conclusão | O4 | WR1 em 3.5 (A-002, A-008) |
| C8 | Documentar com instrumentos específicos reduz a probabilidade de uma falha passar despercebida (5.4). | EXPLICIT | THIN (mecanismo, sem evidência) | MATCHED (a tese declara que é expectativa) | — | PASS (honesto) |

---

## §5. Ônus, escopo e comparativo

```
CLAIM SCOPE: NORMATIVE (um centro pode operar este framework) + LOCAL (ombro, centro-alvo)
EVIDENCE SCOPE: LOCAL (leitura de três textos; amostra de registro; literatura metodológica)
COMPARATIVE BURDEN:
  Alternatives considered: Y (5.1: patrocinador, CRO, software; 4.2.1: três modelos de supervisão)
  Precision justified: Y em geral (números com fonte); N em "one in four" (A-006) e 21/71 (A-010)
  Testimony overextended: N/A (não há testemunho)
MATCH: N em pontos localizados
  - Escopo cresce na Conclusão: "the only party … without a documented quality system" (A-007).
  - Escopo cresce em 4.7: "the most prevalent in shoulder device investigations" (A-039).
  - A rota híbrida (patrocinador constrói, centro opera) é declarada não examinada em 5.1 e proposta em 5.5 (A-053).
Codes: BP2 (A-007, A-039), BP3 (A-024), BP4 (A-006, A-052), BP5 parcial (A-053; não é derrota, há alternativas nomeadas).
```

---

## §6. Objeções e integridade dialética

**STRONGEST OBJECTION (derivada pelo Test B, interna ao texto).**

> O próprio texto diz que o centro-alvo não vai construir um sistema de qualidade voluntariamente (5.5: "expecting a center to build one voluntarily is probably unrealistic"), que o patrocinador é a parte que pode absorver o custo e já fornece protocolo, brochura e treinamento (5.5), que formulários de nível de ensaio já capturam desvios intraoperatórios (3.4.1, Blencowe et al.), e que não se sabe quem detecta um sinal primeiro (4.3.3). Então o remédio que sobrevive às premissas da tese é uma arquitetura construída pelo patrocinador e operada pelo centro, que é a rota que 5.1 afasta e que a Conclusão rejeita ("A framework built on that alternative would reach the site without making the site the party that holds it").

- Target: C0 (o lugar do framework: "site-level", "derives") e C4.
- Relation: ALTERNATIVE. Basis: TEXT-INTERNAL.
- Derivation anchors: 5.5 (parágrafo sobre o tamanho das observações), 3.4.1 item 2, 4.3.3, 5.1 (rotas), Conclusão §4.
- Engaged: Y, parcialmente (5.5 propõe a rota; 5.7 propõe pilotá-la). Quality: SUBSTANTIVE em 5.5, mas a concessão não muda 5.1 nem a Conclusão.
- Dialectical integrity: PSEUDO-RESOLUTION na Conclusão (DI2) e concessão sem custo (OB4).
- O que sobrevive: a tese não precisa que o centro construa; precisa que o centro opere e detenha o registro (continuidade quando monitores e patrocinadores mudam; conta própria na qualificação). Essa defesa existe no texto (5.1 parágrafo sobre o Pilar 2; 5.4 último parágrafo), mas não está ligada à objeção.
- Code: **OB4** + **DI2** na Conclusão; FM-A20 (remédio que depende do que a tese afasta). Severidade: Must na Conclusão (A-008), Should em 5.1/5.5 (A-053).

**Inventário (2 a 4 objeções principais + varredura por garantia).**

| # | Objeção | Target | Relation | Basis | Condition / âncoras | Engaged | Qualidade | Código |
|---|---|---|---|---|---|---|---|---|
| O1 | A objeção mais forte (acima). | C0, C4 | ALTERNATIVE | TEXT-INTERNAL | 5.5, 3.4.1, 4.3.3 | Parcial | SUBSTANTIVE em 5.5, sem custo em 5.1/Conclusão | OB4, DI2 |
| O2 | "A curva de aprendizagem não é lacuna: a Cláusula 10.6 já exige manter uma equipe adequada durante toda a investigação, e a E8(R1) exige retreinamento e revisão periódica durante a condução." | C5.warrant ("no counterpart obligation") | WARRANT-DEFEATER | TEXT-INTERNAL | Condição: "unless 'maintain an adequate team throughout' covers ongoing proficiency". Âncoras: 4.2.3, 4.2.4, 4.3.2 | Parcial (5.1: "it measures a state at one moment and the threat is a trajectory") | SUBSTANTIVE, mas depois do absoluto "stop there" | OB2 leve (A-032) |
| O3 | "O patrocinador vê boa parte desses riscos: SDV confere identificadores, prazos e backlog são gatilhos de monitoramento central, e o CEC agrega sinais." | C4.warrant | WARRANT-DEFEATER | TEXT-INTERNAL | Condição: "unless the risk leaves a record the monitor reads". Âncoras: 4.4.1 (gatilhos EMA), 4.3.3 (CEC), 5.1 ("Deadlines … allow a sponsor to tighten a site") | Parcial (5.3 parágrafo de qualificação; 4.3.3) | SUBSTANTIVE em 5.3; contradito em 4.3.1 e 5.4 | DI4 (A-003, A-033) |
| O4 | "A rastreabilidade não prova nada: os pilares foram tirados dos requisitos e depois os requisitos 'cabem' nos pilares." | C7 | EVIDENCE-CHALLENGE | TEXT-INTERNAL | Âncoras: 2.5.1, 3.2.1 | Y (5.1: "That correspondence shows internal coherence and nothing more") | SUBSTANTIVE (força da tese) | PASS em 5.1; CL3 em 2.5.1 (A-021) |
| O5 | "O fenótipo-alvo está nos EUA (60/65) e as lacunas vêm do MDR." | C6.warrant | WARRANT-DEFEATER | TEXT-INTERNAL | Condição: "unless operating conditions are jurisdiction-independent". Âncoras: 1.3, 3.4.4, 5.3 | Nomeada, não respondida (5.7: "has to state") | EVASION involuntária | OB2 (A-013) |
| O6 | "Documentar não melhora a conduta." | C8 | CLAIM-CHALLENGE | IMPORTED | — | Y (5.4) | SUBSTANTIVE (força da tese) | PASS |
| O7 | "Monitorar cirurgiões é avaliação profissional; num consultório de propriedade do cirurgião, quem decide e quem é restringido podem ser a mesma pessoa." | C5 (SLCT) | VALUE-CONFLICT | TEXT-INTERNAL | Âncora: 5.5 | Y (5.5) | SUBSTANTIVE, mas a salvaguarda falha no caso descrito | OB2 leve (A-054) |
| O8 | "Vinte e quatro instrumentos para uma equipe de duas pessoas." | C8 | CLAIM-CHALLENGE | IMPORTED | — | Y (5.3, 5.7) | SUBSTANTIVE (incerteza declarada) | PASS |

Varredura por garantia (6a-sweep): C1 → O6 não se aplica; registro `Defeater refs: NO-MATERIAL-TEXT-INTERNAL-DEFEATER-IDENTIFIED` para C3. C2 → O2 (lacuna 3). C4 → O1, O3. C5 → O2, O7. C6 → O5. C7 → O4. C8 → O6, O8.

**Integridade dialética:** DI0 leve (C1: "governance model" tratado como aceito; A-064); DI2 na Conclusão (A-008); DI3 ("governance review"; A-044); DI4 (C4 "a tempo"; A-003, A-033; contribuição "nada inventado" vs "uma exceção"; A-002).

---

## §7. Narrativa como evidência

A tese não usa vinhetas. Os "casos" são estudos citados (ROMIO, Blencowe, Diani, estudo português). Todos funcionam como EVIDENCE de nível agregado ou como precedente; nenhum carrega sozinho uma subafirmação, exceto [76], que é a única medida direta da lacuna 2 e merece aparecer onde a lacuna é definida (A-034). NE: PASS.

---

## §8. Rastreamento entre seções

| Seção | Afirmação como aparece | Qualificação | Termos-chave | Deriva em relação ao C0 |
|---|---|---|---|---|
| Abstract | método rastreável que converte princípios e lacunas em controles | moderada | architecture | sem "a tempo" (A-058) |
| 1.4 / 1.5 | poucos instrumentos operados pelo centro; "defines what a site should operate" | hedged em 1.4; confiante em 1.5 | gap = assimetria na literatura | normativo (A-015) |
| 2.1.1 / 2.5 | problema "observado na prática"; requisito só se novo | confiante | — | origem trocada (A-001); critério ≠ aplicação (A-020) |
| 3.2 / 3.5 | cinco lacunas; "has not been done"; "nothing … invented" | confiante | gap = obrigação do patrocinador | escopo cresce (A-024, A-002) |
| 4.3 / 4.3.1 | "neither function is positioned to see"; "does not see any of these" | confiante | cannot see | absoluto (A-033) |
| 4.3.3 | "do not establish that either level will detect a signal first" | hedged | in time | coerente com o contrato |
| 5.1 | "one defensible way"; "internal coherence and nothing more"; "one exception" | hedged, honesto | gap = silêncio | melhor versão do C0 |
| 5.4 | "the local instrument acts first" | confiante | in time | volta a crescer (A-003) |
| 5.5 | patrocinador constrói, centro opera | hedged | site-owned = operar e deter | nova rota (A-053) |
| 6 | "the only party … without a documented quality system"; traceability "over the alternative"; "without inventing an obligation"; "one in four" | confiante | — | escopo cresce na conclusão (A-006, A-007, A-008) |

**Leitura dinâmica.** O padrão não é a erosão clássica (cauteloso no início, confiante no fim). É uma onda: confiante no Cap. 3, absoluto em 4.3, honesto em 5.1 e 4.3.3, confiante de novo em 5.4 e na Conclusão. A versão honesta está no meio da tese e não governa nem o começo nem o fim. FM-A16 (qualification erosion) na Conclusão; FM-A13 (motte-and-bailey) entre 5.1 e Conclusão.

---

## §9. Resumo diagnóstico

**Veredito de garantia: WARRANTED.** Um leitor cuidadoso que não concorda com a tese consegue identificar o que se afirma (embora distribuído), avaliar a evidência (com exceção da matriz de cláusulas e da variável de infraestrutura), recuperar as pontes (a do C4 pela continuidade do registro), julgar o escopo (a tese declara muitos limites) e ver que as objeções existem (5.1, 5.2, 5.4). Os códigos são a agenda de reparo, não uma derrota.

| Teste | Resultado | Nota |
|---|---|---|
| Claim-accessibility | pass (fraco) | C0 em três variantes; nenhuma frase única |
| Evidence-evaluability | pass (com falhas locais) | matriz não mostrada; variável de infraestrutura sem definição |
| Bridge-recoverability | pass | C4 recuperável; C6 (EUA → UE) ausente |
| Scope-honesty | pass no meio, falha nas pontas | Cap. 3 e Conclusão excedem o que 5.1 estabelece |
| Objection-awareness | pass | objeções reais engajadas com custo (5.2, 5.3, 5.4) |
| Form-fit | pass | DSRM bem declarado; numeração de atividades inconsistente |

**Flags de plausibilidade de premissa (não são juízo de verdade).**

| ID | Premissa como usada | Papel | Flag | Por que | Limite do firewall | Reparo |
|---|---|---|---|---|---|---|
| P1 | O centro detecta sinais locais antes do nível do ensaio (5.4; 4.3.1) | garantia de C4 | UNEARNED + CONTESTABLE | 4.3.3 diz que as fontes não estabelecem isso | não julgo quem detecta primeiro | qualificar (hipótese de desenho) |
| P2 | A inspeção avalia o registro, não a sofisticação do sistema (5.3) | garantia de C8 (escalabilidade) | UNEARNED (declarada pela tese) | a própria tese diz que não encontrou fonte | não julgo práticas de inspeção | manter a declaração; é honesta |
| P3 | Houve uma mudança para um "modelo de governança" que pede uma conta do centro (1.1, 5.1) | motivação de C1 | EXTERNAL-VERIFY | um comentário [7] | não julgo a literatura | apoiar ou apresentar como leitura |
| P4 | Remuneração por FMV não financia qualidade interna; pesquisa não é a renda principal do centro-alvo (5.3) | garantia de C6 | UNEARNED + EXTERNAL-VERIFY | sem fonte; 3.4.5 diz que orçamentos não foram medidos | não julgo contratos | citar ou declarar como suposição |
| P5 | As condições operacionais do subgrupo norte-americano valem para centros sob o MDR | garantia de C6 | UNEARNED | ponte não argumentada; 5.7 remete a 3.4.4, que não a contém | não julgo os centros europeus | declarar e delimitar |
| P6 | Documentar com instrumentos específicos reduz a probabilidade de uma falha passar despercebida (5.4) | garantia de C8 | CONTESTABLE | mecanismo sem medida | não julgo o efeito | já qualificado; manter |

**Diagnóstico de prioridade.**
- Quebra estrutural: o C0 tem uma versão honesta (5.1) e duas infladas (Cap. 3 e Conclusão); a garantia de C4 ("a tempo", "ser dono") oscila.
- Cluster de falha: Relational (FM-A13, FM-A6) + Dynamic (FM-A16 na Conclusão).
- Por que importa: o examinador de regulação vai ler 3.5 e a Conclusão contra 5.1 e 4.3.3; a contradição é dele de graça.
- Primeiro alvo de reparo (diagnóstico, sem reescrita): fazer a versão de 5.1 governar 2.5, 3.5, 4.3.1, 5.4 e a Conclusão.

---

## §10. Anotações dos módulos companheiros

### 10.1 Evidence Analysis
_Argument Evidence Deep-Dive v1.0, 2026-10-10._

Corredor examinado: suporte de C2 (lacunas), C4 (vantagem temporal), C5 (curva de aprendizagem) e C6 (registro).

| Flag | Onde | Achado |
|---|---|---|
| AE1 Provenance Opacity | C2 (3.2, Tabela 3.1) | A matriz cláusula a cláusula e as contagens por categoria não aparecem; um só leitor. A lacuna é uma leitura não auditável pelo júri (A-023, A-017). |
| AE1 Provenance Opacity | C6 (3.4.4) | A variável "infraestrutura permanente" remete a uma definição inexistente em 2.4.2 (A-012). |
| AE3 Portfolio Narrowness | C4 | A vantagem temporal tem só suporte de razão; nenhum dado. A tese admite (4.3.3), mas 5.4 afirma como fato. |
| AE4 Representative Gap | C6 | 92,3% dos não hospitalares nos EUA; a anti-ideia 4 cobre a representatividade, mas não a ponte para o desenho sob o MDR (A-013). |
| AE7 Orphaned Statistic | 6 | "one in four" sem base no registro (A-006). |
| AE7 Orphaned Statistic | 5.2 vs 1.4.1 | 21 vs 71 participantes no Delphi (A-010). |
| AE9 Credential Substitution | 5.3 | Afirmações sobre FMV, anti-indução e economia do centro sem fonte (A-050). |
| AE10 Verification Hotspot Cluster | 1.4/5.2, 3.2, 4.3.2, Tabela 3.1 | Números e citações que precisam de conferência antes da defesa (ver 10.3). Dispara escalonamento para a carta. |

**Nota de portfólio.** O melhor suporte da tese é a literatura metodológica sobre cirurgia, imagem e seguimento (C5): números com fonte, delimitados ("These values are descriptive, not universal proficiency thresholds"). O suporte mais fraco é justamente o que sustenta a parte nova do C0 ("a tempo", "dono"): razão sem dado. O estudo português [76] é a única medida direta e europeia da lacuna e está enterrado nos Resultados (A-034).

**Testemunho:** não se aplica (AE5, AE6 não disparam).

### 10.2 Persuasion Assessment
Ver `persuasao.md`.

### 10.3 Verification and Research Handoff
_Para a lente de citações e verificação factual. Não verifiquei nenhum destes itens._

1. Delphi SQA-Onc [37]: 21 ou 71 participantes? (1.4.1 vs 5.2)
2. Tabela 3.1, lacuna 3: [59, 61] contra [70, 71] no texto para a mesma afirmação.
3. 4.3.2: CTSPM citado como [37, 39]; no restante é [41].
4. [44]: usado para gestão reativa (1.4.2) e para "83% of flagged sites" (4.5.6).
5. 4.4.1: o peso de queries com mais de sessenta dias atribuído ao MDIC só cita [1] (EMA).
6. Leitura das cláusulas que sustentam a lacuna 3 e o "stop there": ISO 14155:2026 Cláusulas 10.1, 10.3, 10.6, 7.6; ICH E8(R1) sobre retreinamento e revisão periódica.
7. MDR Artigo 27(1) e a ameaça "UDI and MDR non-compliance" da Tabela 3.2.
8. 5.3: afirmações sobre Fair Market Value e regras anti-indução nos EUA.

Por que importam: os itens 1 a 5 são números ou atribuições que um examinador pode conferir; os itens 6 e 7 sustentam a única lacuna sem obrigação correspondente e uma ameaça regulatória; o item 8 é afirmação factual sem fonte.

### 10.4 Red-Team Pressure
_Argument Red Team v1.0, 2026-10-10._
_Perfil do adversário: examinador de banca ("Reviewer 2"), competente no domínio, cético por função, lê a tese inteira e cruza seções._

**Contagem:** 12 vulnerabilidades — 0 Fatal, 9 Major, 3 Manageable, 0 Cosmetic.

| # | Flag | Nome | Nível | Vetor de ataque | Classe | Referência |
|---|---|---|---|---|---|---|
| 1 | RT10 | Cross-Exam Trapdoor | Major | "Na 3.5 nada é inventado; na Conclusão há uma exceção. Qual é a verdadeira?" | Unexploited Defense (5.1 tem a resposta) | §2 C7; A-002 |
| 2 | RT12 | Clustered Weakness Corridor | Major | C4 junta três fraquezas: "não vê" absoluto (4.3.1), "age primeiro" (5.4), "operar → ser dono" (5.3). | Genuinely Vulnerable | §4 C4; A-003, A-033, A-049 |
| 3 | RT1 + RT7 | Easy Steelman Against + Alternative Suppression | Major | "A sua própria 5.5 diz que o patrocinador deve construir. Então o que é 'site-level'?" | Unexploited Defense (posse e continuidade do registro) | §6 O1; A-053, A-008 |
| 4 | RT4 | Exception Collapse | Major | "A Cláusula 10.6, como você mesmo a lê, exige equipe adequada durante toda a investigação." | Unexploited Defense (estado vs trajetória) | §6 O2; A-032 |
| 5 | RT9 | Evidence Chain Snap | Major | "Mostre a matriz. Quantos atributos? Quem mais leu?" | Genuinely Vulnerable | §3 C2; A-023, A-017 |
| 6 | RT11 | Standing and Scope Exposure | Major | "O seu alvo empírico está nos EUA; as suas lacunas estão no MDR; e o texto diz que a 3.4.4 'has to state' qual governa." | Genuinely Vulnerable | §6 O5; A-013 |
| 7 | RT10 | Cross-Exam Trapdoor | Major | "O seu alvo é o Tipo B ou o não hospitalar sem infraestrutura? E por que o log da curva de aprendizagem sai do Tipo C?" | Genuinely Vulnerable | §2 T6; A-004, A-040 |
| 8 | RT5 | Definition Front Open | Major | "Gap" e "instrument" mudam de sentido; "governance review" não tem revisor. | Genuinely Vulnerable | §2 T1, T2, T5; A-042, A-063, A-044 |
| 9 | RT9 | Evidence Chain Snap | Major | Números internos discordantes: "one in four", 21/71. | Genuinely Vulnerable | §10.1; A-006, A-010 |
| 10 | RT6 | Quote-Mine Exposure | Manageable | "A sponsor-level assessment does not see any of these." / "What is missing is not a rule. It is a layer." | Genuinely Vulnerable | A-033, A-069 |
| 11 | RT3 | Burden Inversion | Manageable | "Has not been done in the published literature" a partir de revisão narrativa. | Unexploited Defense (5.7 tem a versão certa) | A-024 |
| 12 | RT10 | Cross-Exam Trapdoor | Manageable | "Num consultório do próprio cirurgião, quem restringe o PI-cirurgião?" | Context-Dependent (pesa mais para o examinador B) | §6 O7; A-054 |

**Hard gates:** nenhum disparado. HG-RT4 (RT1 + RT7) foi considerado; não dispara porque o próprio texto engaja a rota alternativa em 5.5 (é uma defesa não explorada, não uma supressão).

**Distinguish:** Genuinely Vulnerable 7; Unexploited Defense 4; Context-Dependent 1; Intentional Risk 0.

**Prontidão para arguição:** PARTIALLY PREPARED. A tese tem as respostas para os ataques 1, 3, 4 e 11 dentro do próprio texto; precisa colocá-las antes das afirmações que elas corrigem.

**Perguntas de arguição (5 a 10), em ordem de escalada:**

| # | Pergunta | Alvo | Dificuldade esperada |
|---|---|---|---|
| Q1 | "Qual destas é a sua posição: 'nothing in the framework is invented' (3.5) ou 'with one exception' (Conclusão)?" | C7, A-002 | could answer but hasn't |
| Q2 | "Você escreve em 4.3.3 que não se sabe quem detecta primeiro e em 5.4 que o instrumento local age 'long before'. Qual vale?" | C4, A-003 | author would struggle |
| Q3 | "Se o centro não vai construir isto voluntariamente (5.5) e o patrocinador o constrói, o que resta da contribuição 'site-centered'?" | C0, O1 | could answer but hasn't |
| Q4 | "A Cláusula 10.6 exige manter uma equipe adequada durante toda a investigação. Por que isto não cobre a curva de aprendizagem?" | C5, O2 | could answer but hasn't |
| Q5 | "Quantos atributos a sua matriz tinha, quantos caíram em cada categoria, e quem conferiu a sua leitura?" | C2, A-023 | author would struggle |
| Q6 | "Como você definiu 'infraestrutura permanente de ensaios clínicos'? A 2.4.2 não diz." | C6, A-012 | author would struggle |
| Q7 | "O seu centro-alvo é o Tipo B ou o Tipo C? E por que o log da curva de aprendizagem não está no núcleo do Tipo C?" | C6, A-004, A-040 | author would struggle |
| Q8 | "Quando o log começa: na fase 2, como diz a 4.6.2, ou depois dos primeiros casos, como diz a 5.5? A Figura 4.1 não o mostra." | DR9, A-005 | author would struggle |
| Q9 | "A sua Conclusão diz 'roughly one in four'. Os seus dados dizem 38 de 235. Qual é o número?" | C6, A-006 | should answer easily |
| Q10 | "Num consultório de que o PI é dono e onde ele mesmo opera, quem decide restringir o PI?" | C5, A-054 | could answer but hasn't |

**Pontes recomendadas:**
- Argument Evidence: Y (rodado; ver 10.1).
- Citation Verifier: Y (itens 1 a 5 de 10.3).
- Reception Risk / Banister: N (não há conteúdo culturalmente contestado; a questão ética do 5.5 é estrutural e está no registro).
- Revision Coach: sequência sugerida pelos dados (não é prescrição): números e marcadores → limite da contribuição → C4 dividido → identidade do alvo → ciclo de vida → reestruturação da Discussão.
