# Imagens e tabelas: o que muda e o que é novo (26/10)

Vale para o capítulo 4 a partir da 4.6, e inclui as pendências antigas de imagem do capítulo 3 e da 4.2. O texto das legendas sai junto com o texto de cada seção.

## 1. Numeração depois das mudanças

Saem a Fig. 4.2 (instrumentos por pilar) e a Fig. 4.5 (instrumentos × DRs). Entra uma figura nova na 4.6. A tabela de registros invariantes da 4.7 foi descartada em 27/10 (os registros ficam citados em prosa). A tabela de portas da 4.6.1 foi descartada em 27/10: as condições de cada fase entram na própria Fig. 4.1.

| Hoje | Depois | Onde |
|---|---|---|
| Fig. 4.1 lifecycle | Fig. 4.1 | 4.6.1 |
| (nova) matriz instrumento × fase | Fig. 4.2 | 4.6.2 |
| Fig. 4.3 granularidade | Fig. 4.3 (o número não muda) | 4.8 |
| Fig. 4.4 instrumentos × domínios | Fig. 4.4 combinada (domínios em cima, DRs embaixo; imagem do autor de 27/10) | 4.8 |
| Fig. 4.2 por pilar | sai | — |
| Fig. 4.5 instrumentos × DRs | sai | — |
| Tabela 4.1 funções | Tabela 4.1 | 4.2.2 |
| Tabela 4.2 escalabilidade | Tabela 4.2 | 4.7.1 |
| Tabela 4.3 instrumentos | Tabela 4.3 (o número não muda) | 4.8 |
| Tabela 4.4 DR × componente | sai (27/10): entra na Fig. 4.4 combinada; a seção de cada instrumento vai para a Tabela 4.3 | — |

As remissões no texto e as listas de figuras e de tabelas mudam junto (Ctrl+A, F9 no fim).

## 2. Novas

### Fig. 4.2: matriz instrumento × fase (DR9). Eu gero.
- **Linhas:** os 24 instrumentos agrupados por pilar, na ordem da Tabela 4.4:
  - Governance: CCDM, MRL, POT, RACI, DTRM, TRE, SCR;
  - Risk Management: SRR, SLCT, SCML, SART, CSST;
  - Operational Controls: IMP, IMC, SIRR, IQL, PSEAR, SIFSL, PFVR, ICDL;
  - Performance Oversight: PIR, FUCR, CAPA, PIDLR.
- **Colunas:** fases 1 Feasibility, 2 Start-up, 3 Enrollment, 4 Surgery, 5 Follow-up, 6 Close-out e 7 Continuous improvement, mais uma coluna para a corrente de segurança (fases 3 a 5).
- **Marcadores:** vazio = montado (preparado, regras fixadas); cheio = em uso.
- **Conteúdo:** o mapa aprovado (`mapa-instrumento-fase.md`) no formato montado / em uso. A coluna da fase 2 mostra que quase tudo é montado ali.
- **Estilo:** a mesma família visual da Fig. 4.4.

### Tabela 4.3: registros invariantes (Word, sem imagem)
- **Colunas:** registro | onde fica no framework | fonte.
- **Linhas:** consentimento, delegação e treino, contabilidade do dispositivo, desvios, eventos adversos, calibração, essential records, documentos fonte.
- Cada cláusula é conferida na ISO 14155:2026 e no MDR antes de entrar. O conteúdo sai com o texto da 4.7.2.

## 3. Existentes que mudam

### Fig. 4.1 lifecycle (sua imagem)
- **Fase 2:**
  - entram o SRR (aberto antes do primeiro participante), o SLCT (base de comparação), o IMP, as regras do PIR, e o SCML, o SART e o CSST preparados (critérios e limiares);
  - a ordem passa a ser treino e liberação (DTRM, TRE) e depois credenciamento (SCR);
  - "Delegation log created, criticality codes assigned" → CCDM e RACI;
  - "PI oversight plan" → PI Oversight Template (POT).
- **Fase 1:** a análise de lacunas da imagem passa a ter o nome do instrumento (SIRR).
- **Fase 4:** entra a revisão da imagem pós-operatória imediata (IQL, DR6).
- **Fase 6:**
  - sai "Final safety report for the whole study period", que é do sponsor;
  - entra "Site safety records reconciled with the sponsor's".
- **Fase 7:** entra o PIDLR (debrief e lições).
- **Corrente de segurança:**
  - "Structured causality assessment separating device, procedure and patient factors" → "Event categorization: related to device use, to a CIP-required procedure, or to neither";
  - "recognise" → "recognize";
  - "at least monthly" fica.
- **Grupos:** os três blocos que a figura já tem (PREPARATION, CONDUCT, CLOSURE) passam a ser citados no texto: preparação e fechamento são do site e sequenciais; condução é por participante.
- **Objetivo da fase 2:** "Build the Governance pillar before any participant data exist" → "Set up the four pillars before any participant data exist".
- **Fase 2, dispositivo:** entra "Device receipt, storage and access control ready" (domínio 4).
- **Fase 2, imagem:** "imaging charter agreed with radiology" → "Imaging readiness (SIRR) submitted to the sponsor" (a charter é do sponsor).
- **Fase 3:** entra "Consent documented before any study assessment" (domínio 3).
- **Condução (fases 3 a 5):** entram "Deviations recorded when found" (domínio 12) e "Critical data completeness reviewed monthly" (domínio 11).
- **Fase 5:** "Late adverse events … captured" sai (pertence à corrente de segurança).
- **Corrente de segurança:** acrescentar "Implant records kept current while the participant is followed".
- **Fase 7:** "Corrective actions closed and their effectiveness assessed" → "No corrective action left open"; as ações fecham durante a condução, quando a revisão mostra eficácia.
- **Linha nova em cada fase: a condição que fecha a fase** (substitui a tabela de portas):
  - 1 Feasibility: "Closes when capability and imaging readiness are documented and the sponsor decides on selection"
  - 2 Start-up: "Closes when the site is ready to enroll: tasks released, surgeons credentialed, SRR in place, rules of each instrument in use fixed, implementation level recorded"
  - 3 Enrollment: "From the first screened candidate to the last enrolled participant"
  - 4 Surgery: "From the first to the last study procedure"
  - 5 Follow-up: "From the first follow-up to the last required visit"
  - Corrente de segurança: "From the first enrolled participant to the last follow-up assessment"
  - 6 Close-out: "Closes when devices and safety records are reconciled with the sponsor, data are verified and records archived"
  - 7 Continuous improvement: "Closes when lessons are turned into standing procedures and no corrective action is left open"
- **Legenda nova:** "Figure 4.1. The seven phases of the quality lifecycle in three groups, with the transversal safety stream and, for each phase, its objective, its actions and checks, and the condition that closes it."

### Tabela 4.2 escalabilidade (sua imagem)
- **Colunas:** nonhospital (nível mínimo, centro-alvo) | nonacademic hospital | academic. Saem "Type A/B/C" e as descrições por porte ("Large or complex research hospital", "Medium private clinic/hospital", "Small surgical centre").
- **Sai** qualquer menção a pessoal dedicado, função de qualidade, "imaging liaison" e "formal multidisciplinary reviews".
- **Os 24 instrumentos em uso nos três níveis.** O que muda por coluna é a cadência, a independência da revisão e a separação ou combinação de registros.
- **"Role architecture and controlled instruments"** → "Role structure and instruments".
- **Grafia:** specialised, programme, authorisation, centre → americano.
- O SCML não pode aparecer só numa coluna.
- O conteúdo final das células sai junto com o texto da 4.7.
#### Proposta de células da Tabela 4.2 (27/10; para validar com o texto da 4.7)

| Elemento | Nonhospital (nível mínimo, centro-alvo) | Nonacademic hospital | Academic |
|---|---|---|---|
| Governance | Supervisão do PI em camadas, funções acumuladas com substituto nomeado; revisões de marco e gatilhos curtos | Funções em pessoas diferentes quando a equipe permite; reuniões de supervisão incluem os serviços do hospital de que o site depende | Supervisão dentro da governança de pesquisa da instituição, sem substituí-la |
| Risk register and complication surveillance | Registro completo em forma enxuta, revisto pelo PI; complication log e revisão mensal de sinais podem ficar num registro só | Mesmo registro e mesma revisão, em registros separados | Registro ligado aos sistemas de risco da instituição |
| Procedural competence and stability | Credenciamento, liberação e learning curve log para todo cirurgião; proctoring combinado com o sponsor quando necessário | Igual, com o credenciamento alinhado ao do hospital | Igual, dentro do credenciamento institucional |
| Internal verification and imaging | Revisão por um par treinado ou pelo PI, nunca por quem fez o trabalho; prontidão de imagem combinada com o prestador externo | Revisão por alguém fora da execução diária quando possível; revisão local de imagem no serviço de radiologia do hospital | Revisão por uma unidade separada da investigação; revisão de imagem integrada à imagem institucional |
| Performance Oversight | Os seis indicadores, lidos como contagens sobre denominadores; CAPA log como registro próprio | Os seis indicadores, também comparados entre as investigações do site | Indicadores podem entrar nos painéis institucionais; CAPA ligada ao sistema institucional, quando existir |
| Role structure and instruments | Seis funções em poucas pessoas; instrumentos em papel ou no sistema que o site já usa | Funções distribuídas em cargos; instrumentos dentro dos registros do hospital | Instrumentos dentro das plataformas de pesquisa ou de qualidade da instituição |

Em inglês na imagem. Nada de "quality function", "imaging liaison", "dedicated staff". Os 24 instrumentos aparecem nos três níveis.


### Tabela 4.4 instrumentos (antiga 4.3; sua imagem)
- Cabeçalhos por pilar.
- Coluna nova "Appendix" (A a X).
- **Ordem pela primeira citação:**
  - Governance: CCDM, MRL, POT, RACI, DTRM, TRE, SCR;
  - Risk Management: SRR, SLCT, SCML, SART, CSST;
  - Operational Controls: IMP, IMC, SIRR, IQL, PSEAR, SIFSL, PFVR, ICDL;
  - Performance Oversight: PIR, FUCR, CAPA, PIDLR.
- O FUCR fica em Performance Oversight.
- O TRE tem um nome só em toda a tese: Training Record Evaluation and Release.

### Fig. 4.3 granularidade (sua imagem)
- **27/10: vale a versão por linhas de pilar com o quadro "The information chain"** (a lista de siglas por nível foi descartada, porque repete a Tabela 4.3). Ajustes que faltam: tirar a nota do MRL ("consolidates the governance evidence at each milestone"), porque o MRL fica em segundo plano; deixar só uma das duas frases sobre o retorno da decisão (fica a do rodapé).
- **Legenda:** volta para "Operational Controls appears as three groups (surgery and device, enrollment, follow-up), and the safety stream appears as a row of its own". SART, SCML e CSST são de Risk Management.
- **Linha "Surgery and device":** hoje tem IMP, IMC, SIRR e IQL, que são verificação e imagem. Reagrupar ou renomear a linha.
- O FUCR passa para Performance Oversight.
- **Rodapé:** "An evidence record never depends on a synthesis or decision document existing first" é falso para o TRE. Trocar por "The evidence record is created at the event; decisions return as the requirement it is checked against".

### Fig. 4.4 instrumentos × domínios (sua imagem)
- **Regra:** marcador cheio só onde o controle do domínio é executado.
- **Domínio 11:** tirar os marcadores cheios do MRL, do PIR e do PIDLR. Pôr cheio no ICDL, no PFVR e no PSEAR.
- Rever os marcadores cheios do MRL e do PIDLR nos outros domínios.
- **PIR:** marcador no domínio 6, porque o SP-01 responde aos domínios 5 e 6.
- O FUCR fica no grupo Performance Oversight.

### Tabela 4.5 DR × componente (antiga 4.4). Eu refaço, como em 24/10.
- **Colunas novas:** instrumento(s) e fase(s).
- **DR4:** "nine review checks" → ten, com o IMP e o IMC.
- **DR6:**
  - sai "4.6.2 phase 4";
  - entram o IQL e a 4.4.2;
  - instrumentos: ICDL, SLCT, SCML, IQL.
- **DR7:** "4.5.1" → 4.4.3. Entra a qualificação de avaliadores (DTRM, TRE) junto com o SIRR, o IQL e o PSEAR.
- **DR3:** o SCR passa a apoio. O SLCT é o instrumento direto.
- **DR9:** "carries leverage" → "has most effect". Vira propriedade do conjunto ("all instruments, each assigned to its phase"), com o MRL como registro.
- **DR10:** CCDM e RACI, mais DTRM e TRE.
- **DR11:** sai "4.4.3". Fica 4.4.4 e 4.8.
- **DR12:** "three site contexts" → os três níveis da Tabela 3.3.

### Fig. 4.4 combinada (27/10, imagem do autor)
Substitui a antiga Fig. 4.4 (domínios) e a Tabela 4.4 (DRs). O autor ainda vai fechar a posição dos marcadores. O texto novo da 4.8 depende só de dois pontos:
- **Legenda da parte de DRs:** só cheio e vazado, como na parte de domínios. "Inherited from a combined or earlier instrument" e "extension, added to the original set" contam uma história de versões que os caps. 2 a 4 não apresentam, e "combined" bate com a decisão de não haver registros combinados.
- **DR9:** vira barra, como DR11 e DR12 ("all instruments · each assigned to the phase where it has most effect, Figure 4.2"). O marcador cheio no MRL contradiz o MRL em segundo plano.
- Quando a figura fechar, conferir no texto da 4.8 (t48b): toda linha de domínio e de DR1 a DR10 com um cheio; toda coluna com um cheio em uma das partes; DTRM, TRE, PFVR e FUCR sem cheio na parte de DRs.

### Tabela 4.3: coluna "Section"
Ao lado de "Appendix", para não perder a informação que a Tabela 4.4 dava.

## 4. Pendências antigas (capítulo 3 e 4.2; suas imagens)

- **Tabela 3.1:**
  - referências do Gap 3 → [71, 72];
  - Gap 5 → ISO 14155:2026 (a obrigação de CAPA do PI) no lugar do MDR.
- **Tabela 3.2:**
  - "UDI" no domínio 4 (avaliar "batch, serial or unique device code");
  - conferir a menção a delegação no domínio 6 e o mascaramento do avaliador no domínio 8.
- **Tabela 3.4:**
  - "architecture" → framework;
  - "carries leverage" → "has most effect" (DR9);
  - rótulos das condições (depois da D3);
  - grafia americana (centre, standardised, afterwards).
- **Tabela 4.1 (funções):** "PROM workflows" → "PROM administration"; "Data QA" → "Data QA function".

## 5. Padrão visual proposto (27/10)

- **Tabelas neutras, figuras com cor só onde a cor tem significado.** As tabelas são texto de referência: cabeçalho escuro (#1f1e1c) e linhas alternadas em creme (#f5f3ee), como já estão nos cap. 3 e 4. Nas figuras, a cor identifica só o pilar, com uma paleta única: Governance azul #2f5d9e, Risk Management ferrugem #b5492f, Operational Controls verde-azulado #1f6e60, Performance Oversight ocre #a8650f. Nenhuma outra cor carrega significado.
- **Única exceção nas tabelas:** a Tabela 4.3 (instrumentos) ganha linhas de cabeçalho por pilar com uma barra fina na cor do pilar, para ligar a tabela às figuras.
- **Fig. 4.1 (lifecycle):** hoje as fases usam marrom, ocre, azul-marinho e verde-azulado, as mesmas cores que nas outras figuras querem dizer pilar. Trocar por tons neutros, um para cada grupo (preparação, condução, fechamento), e a corrente de segurança em ferrugem, igual à coluna S da Fig. 4.2.
- **Marcadores:** uma convenção só nas figuras de matriz: círculo cheio = carrega o controle ou está em uso; círculo vazio = apoia ou está preparado. Mesmo tamanho e mesma espessura de traço na Fig. 4.2 e na Fig. 4.4. Sem quadrados (a Fig. 4.5, que os usava, saiu).
- **Impressão em preto e branco:** o significado tem de sobreviver sem cor. Cheio e vazio já fazem isso; conferir o contraste das faixas de pilar em cinza.
- **Tipografia:** uma família sem serifa em todas as figuras e tabelas, com monoespaçada só para as siglas dos instrumentos. Hoje as Figs. 4.1, 4.2 e 4.3 misturam títulos com serifa. Tamanho mínimo equivalente a 8 pt impresso (as notas em itálico da Fig. 4.3 estão menores que isso).
- **Largura e legendas:** todas na largura do texto; legenda acima nas tabelas e abaixo nas figuras; a legenda dos marcadores sempre embaixo à esquerda.
- **Fig. 4.3:** corrigir os grupos de linhas (o FUCR passou para Performance Oversight; a linha "Surgery and device" tem IMP, IMC, SIRR e IQL, que são verificação e imagem) e trocar a frase do rodapé por "The record of each event is made when the event happens; decisions return as the requirement that the next record is checked against".

### Acréscimos ao padrão visual (27/10, da segunda análise)
- **Tabelas como imagem (4.2, 4.3, 4.4 são PNG):** se der tempo, convertê-las em tabelas nativas do Word. Ficam pesquisáveis, editáveis e com a fonte da tese. Se converter, usar cabeçalho cinza-claro com filetes finos; se ficarem como imagem, manter o cabeçalho escuro de todas as outras.
- **Tabela 4.3 em paisagem,** com o cabeçalho repetido na página seguinte, para não cair abaixo de 8 pt; siglas em monoespaçada também na tabela, como nas figuras.
- **Família de matrizes:** a Fig. 4.2 (fases, sua versão final) tem os instrumentos nas linhas, e a Fig. 4.4 (domínios) nas colunas. Opcional: refazer a Fig. 4.4 com os instrumentos nas linhas, na mesma ordem, para as duas lerem igual.
- **Daltonismo:** ferrugem (Risk Management) e ocre (Performance Oversight) se confundem em daltonismo vermelho-verde; escurecer um e clarear o outro, e fazer um teste de impressão em preto e branco.
