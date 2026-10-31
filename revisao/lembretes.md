# Lembretes da revisão da tese

Registro de tudo o que ficou para depois ("depois eu corrijo", "lá na frente a gente vê", "me lembra", "deixa pro final") e das decisões em que o autor mudou de ideia. Serve para duas coisas: conferência periódica durante a revisão e conferência final na revisão geral da tese.

Montado em 25/10/2026 a partir de toda a conversa desde 09/10. O estado de cada item foi conferido contra o arquivo `Revisao_manual_tese_alteracoes_19-10.docx` da entrega de 25/10.

Estados: **ABERTO** (falta fazer), **DECIDIR** (falta uma decisão do autor), **MUDOU** (o autor mudou de ideia; não reabrir), **FEITO** (atendido; só conferir na revisão geral).

Os flags dos instrumentos (modelos em PDF x texto) ficam em `revisao/flags-instrumentos.md`.

---

## 1. Coisas que o autor disse que faria ou veria depois

| # | Data | O que foi dito | Estado em 25/10 |
|---|---|---|---|
| L1 | 24/10 | Edição das imagens: "ignora isso, eu já corrijo isso mais tarde" | **ABERTO**. Ver lista na seção 5 |
| L2 | 22/10 | 3.4.4 com referências autor-ano; "depois, mais tarde, eu vou pedir para você pegar essas referências, colocar na bibliografia, transformar isso em número" | **FECHADO 30/10** (Tese_completa_30-10.docx: 13 referências convertidas para números 73–85; Karlberg 2009 com periódico a confirmar). Antes: o texto ainda tinha [Drain 2018], [Karlberg 2009], [Glass 2020], [Getz 2017], [Ebrahimi 2024], [Wang 2022], [Rossier 2026], [Ciupek 2024], [Bastek 2025] e outros. Converter para Vancouver e incluir na bibliografia (Karlberg 2009 é literatura cinzenta) |
| L3 | 22/10 | "Me recorde se eu falei na metodologia sobre a dificuldade que foi para conseguir dados europeus… e que não foram analisadas outras bases (asiática, americana, africana) para limitar o escopo" | **ABERTO**. A 3.4.4 diz que o Eudamed devolveu poucos dados, mas nem o cap. 2 nem o 3 dizem que as outras bases regionais ficaram fora do escopo de propósito |
| L4 | 10/10 | P7: dizer que o desenho seguiu o contexto regulatório europeu onde a tese foi feita, e que os dados dos EUA dominaram por estarem mais disponíveis | **ABERTO**. A frase não está no texto (3.4.5 ou 5.7). Redigir de forma neutra, sem apresentar os orientadores como origem do problema. Junta com L3 |
| L5 | 10/10 | P13: o autor tem uma ideia própria sobre por que a ICH E6 importa para o centro de dispositivos; "deixar e perguntar depois" | **DECIDIR**. A ideia nunca foi enviada. Perguntar ao autor |
| L6 | 24/10 | Parágrafo histórico da 3.2 ("The instruments have also moved…"), apagado em revisão: "vamos deixar isso pro final" | **DECIDIR**. Manter a exclusão, rejeitá-la ou usar a versão corrigida proposta em 24/10 (sem o trecho truncado e sem dizer que a responsabilidade passou ao site) |
| L7 | 25/10 | Ao terminar o cap. 4: "gerar um report com todas essas flags" dos instrumentos | **ABERTO**. Gerar a partir de `revisao/flags-instrumentos.md` |
| L8 | 24/10 | Apêndices na 4.2.4: "eu mesmo adiciono" | **FEITO** por Claude no arquivo, com as letras pela ordem de primeira citação |

- 4.5.3: texto final pronto (scratchpad t453.json), mas o autor pediu em 25/10 para não aplicar nada ainda ("aplica nada no texto do git hub ainda"). Aplicar só quando ele mandar; o mesmo vale para as subseções seguintes até nova ordem

- **Ciclo de revisão, decisão do autor em 28/10.** O framework não deve impor revisão mensal a tudo. Cada instrumento ou categoria tem o seu ritmo (mensal, trimestral, semestral, anual, ou por número de casos, como o SLCT depois dos primeiros 5 e 10 casos). Fixamos o ritmo só onde é necessário (a curva de aprendizagem, por exemplo) e deixamos o resto aberto para o site definir conforme a sua capacidade. Também é preciso falar das revisões por gatilho (triggered review), além das periódicas. Pontos a rever no cap. 4: 4.3.3 ("at least once a month", revisão de eventos); 4.5.2 ("monthly oversight meeting"); 4.5.4 ("at least once a month"); 4.5.6 ("calculated monthly", "three monthly measures", "two consecutive months"); 4.6.1 ("reviews safety cases at least once a month"); 4.7 ("including the monthly review of safety cases"). Ver também o cap. 3 e a Figura 4.1 ("at least monthly"), e alinhar com o cap. 5 (5.3.2 passa a "The review cycle").

## 2. Decisões que o autor ainda precisa tomar (Claude perguntou, sem resposta)

| # | Origem | Decisão |
|---|---|---|
| D1 | 4.2.2 | Coluna de domínios na Tabela 4.1. Proposta: coordenador 2, 3 e 7; centro cirúrgico 4 e 5; radiologia 9; avaliador funcional 8; dados 11; PI todos |
| D2 | 4.2.1 | O texto diz que o PI revisa em quatro marcos; o MRL tem 13 (M0 a M12). Decidir qual versão vale (o texto manda, salvo se o modelo estiver mais certo) |
| D3 | 1.2, 3.4.1, Tabela 3.4 | Nomes únicos das cinco condições estruturais. Na 3.4.1 hoje: Irreversibility, Operator dependence, Device traceability, The operational weight of follow-up, Limited classification reliability |
| D4 | 4.7.1 | Tipos A, B e C de centro definidos por porte, com o Tipo B como "o contexto para o qual o framework foi desenhado", em conflito com a 3.4.5 (organização não hospitalar, que define o nível mínimo). Resolver ao chegar na 4.7. Afeta também a 5.x ("a small number of Type B centers" no estudo piloto), a Tabela 4.2 e o RACI |
| D5 | 4.7.2 | "Clauses 10.2 and 10.3" x Clause 7.6, para registro de delegação e treinamento |
| D6 | Registro | Duplicatas Utah e Johns Hopkins, Levy Shoulder Center, referência do FDAAA |
| D8 | 4.2.1 | Cadência das oversight meetings: o POT diz revisão mensal e a 4.5.2 diz "monthly oversight meeting"; decidir se a 4.2.1 diz "monthly" ou deixa a cadência para o site |
| D7 | 4.2.3 | Números dos domínios por área de treinamento (dispositivo e documentação 4 e 5; avaliação 8 e 9; protocolo e segurança a confirmar) e DR10 no fecho (Claude usou o DR10 com base na Figura 4.5) |

## 3. Decisões em que o autor mudou de ideia ou desistiu (não reabrir)

| # | Data | Antes | Decisão final |
|---|---|---|---|
| M1 | 10/10 → 22/10 | Centro-alvo = Tipo B (clínicas privadas com atividade recorrente) | A 3.4.5 fixou a organização não hospitalar como alvo. É lei. O que ainda fala em Tipo B como alvo tem de se ajustar (D4) |
| M2 | 17/10 | Permanent clinical trial infrastructure na metodologia e nos resultados | Retirada da tese ("vamos fingir que nunca fizemos"). Conferido em 25/10: não aparece mais no texto aceito |
| M3 | 22/10 | Reclassificar os 5 hospitais ortopédicos de cirurgiões para nonacademic hospital | Não mexer. Ficam as 68 organizações não hospitalares e os números antigos (108 de 347 registros) |
| M4 | 22/10 → 24/10 | Tirar o filtro de relevância da 2.4.2 | Mantido. Não remove nada, mas continua válido |
| M5 | 10/10 | "Five complexity strata": ignorar e tirar as menções, porque o instrumento não existia | O SLCT agora existe e define estratos de complexidade definidos pelo site (inferior, padrão, superior). A 4.8 ainda diz "five complexity strata used in the learning curve log". Ajustar na 4.3.2 e na 4.8 |
| M6 | 25/10 | Ajustar o texto aos modelos dos instrumentos | O texto é a referência e os modelos se ajustam, salvo quando o modelo estiver mais certo (aceito: SCR antes da liberação no TRE) |
| M7 | 10/10 | Fluxo de registro (recomendação), P12 e P14 | Descartados ("esquece") |
| M8 | 17/10 | Annex ZA da ISO e a frase de busca de termos | Saíram do texto. Conferido em 25/10 |
| M9 | 24/10 | Alterações controladas palavra a palavra | Cap. 1 a 3: alterações em bloco. Cap. 4 em diante: editar direto, sem marcas |
| M10 | 24/10 | Remissões a seções e números de cláusula em toda frase | Só o essencial: o que está atrás e é crítico, o que vem e o leitor estranharia, tabelas, figuras e apêndices. Cada cláusula uma vez no capítulo |
| M12 | 25/10 | FUCR em Operational Controls (9 instrumentos no pilar) | FUCR passa para Performance Oversight (mede o agregado do seguimento). Operational Controls fica com 8 e Performance Oversight com 4: corrigir Figuras 4.2 e 4.3, Tabela 4.3 e legendas. PSEAR, SIFSL e PFVR ganham a nova 4.4.3; o controle de elegibilidade e de visita sai da 4.5.1 e da 4.5.3; as atuais 4.4.3 e 4.4.4 se fundem (com o ICDL). SIFSL e SIRR em Operational Controls aguardam confirmação |
| M11 | 24/10 | Ordem dos apêndices pela tabela de instrumentos | Ordem da primeira citação no cap. 4. A tabela de instrumentos segue a mesma ordem dentro de cada pilar (o autor corrige a tabela) |

- M (26/10): 4.5.5 fica sem frase sobre quem vê o painel. Os códigos de cirurgião podem ser usados, mas são atribuíveis (pseudonimizados, não anônimos), e o desempenho observado alimenta a reautorização da 4.2.4. Intenção do autor: a revisão de consistência serve para achar problemas cedo e apoiar o cirurgião, não para punir. Não reabrir; texto da 4.5.5 aceito como entregue (t455.json), ainda não aplicado

- M (26/10): 4.5.7 fica separada, com o mesmo título; tirar o acessório e o repetido (autoinspeção = 4.4.1; lista de gatilhos; frase de efeito) e manter: o que torna o ciclo proativo, a mecânica da CAPA com verificação de eficácia, a volta para o risk register, e o CAPA log (Appendix W). Não jogar para a introdução nem dividir a 4.5 em blocos. O PIDLR sai da 4.5.7 e vai para a 4.6.1 (fase 6). O autor acha a 4.6.1 fraca hoje ("meio merda"): revisar com cuidado quando chegar lá

- M (26/10): D10 decidido. A 4.4.1 ganha uma décima verificação, "Endpoint data agreement", entre "Follow-up execution" e "Timeliness and closure", e o 2º parágrafo passa de "nine checks" para "ten checks". O autor colou isso na versão LOCAL dele; o docx de trabalho do Claude ainda não tem. Ao voltar a aplicar, incluir essa mudança e conferir com o autor se a versão local dele tem outras edições que o docx de trabalho não tem. Na 4.5.6, a quarta medida passa a ler "the share of sampled records" (t456.json atualizado)

- M (26/10): varredura de split brain do cap. 4 (4.1 a 4.5.6) em revisao/split-brain-cap4.md, com 13 trocas. A troca 7 substitui o texto da verificação nova da 4.4.1 passado antes; inclui também "across all nine checks" → "ten" no 5º parágrafo da 4.4.1. O autor aplica na versão local; o docx de trabalho do Claude ainda não tem nada disso. Sincronizar antes de voltar a aplicar

- M (26/10): reanálise da varredura de split brain. Ficam só as trocas 7 e 13 (obrigatórias), 1 em versão curta e 2 (recomendadas). As trocas 3 a 6 e 8 a 12 foram descartadas; não reabrir. Ver o topo de revisao/split-brain-cap4.md

- M (26/10): o autor mandou o docx dele de 26/10, que passa a ser a base (scratchpad v26). Sete pontos de sincronização na seção 0 de revisao/diagnostico-4.6-4.8.md (EMA "multidisciplinary" voltou; páginas da [77]; pontos duplos; trocas 7 e 13 incompletas; "nine checks" no 5º parágrafo da 4.4.1; lista de tabelas com erro de indicador; CCDM × RACI; contagem por pilar na 4.8)

- M (26/10): D11 decidida. (1) [SUBSTITUÍDO em 26/10, ver abaixo] Escalabilidade por capacidade. (2) O MRL vira o registro do lifecycle (passagens de fase + os quatro marcos da 4.2.1), o que resolve a D2; a 4.2.1 ganha meia frase. (3) O Apêndice Y sai (e a frase da 4.6.2); refazer só se sobrar tempo. (4) Saem as Figuras 4.2 e 4.5; a Tabela 4.4 ganha colunas de instrumento e de fase. Ainda pendente: CCDM ou RACI na 4.2.4

- M (26/10): mapa instrumento × fase aprovado. O SRR abre "before the first participant" (fase 2), sem rascunho na viabilidade; não reabrir. Sincronização da seção 0 aplicada no docx (v27) e entregue; o RACI leva a autorização ao delegation record na 4.2.4 (o CCDM foi erro da versão do autor). Ainda não escrever a 4.6: o autor vai mandar outra análise para comparar

- Cap. 5 depois da 4.6 a 4.8 (26/10, da segunda análise): "has to open during feasibility" (SRR) → before the first participant; "A Type C center reviews less often than a Type B center", "three site types", "a small number of Type B centers" (→ centers operating at the minimum level); "a current delegation log with criticality coding" (→ CCDM e RACI); a premissa "inspection assesses compliance through the completeness … sophistication … secondary" tem de bater com a nova 4.7.2; o checklist macro + MRL pode virar linha de trabalho futuro junto ao "versioned master index"; Tabela 4.4 DR12 "three site contexts"
- Figuras e tabelas da 4.6 a 4.8 (26/10): Figura 4.1 (condições de entrada e saída, IQL pós-operatório imediato na fase 4, SRR/SLCT/IMP/regras do PIR/SIRR, ordem treino → credenciamento, "recognise", CCDM no lugar de "delegation log", fase 6 sem "final safety report", PIDLR na fase 7); Figura 4.3 (legenda volta para três grupos de Operational Controls e a linha de segurança à parte; linha "Surgery and device" tem IMP, IMC, SIRR e IQL; rodapé "never depends" falso para o TRE); Figura 4.4 (regra de primário = onde o controle do domínio é executado; CtQ 11 com marcador cheio em MRL, PIR e PIDLR e vazio em ICDL, PFVR, PSEAR); Tabela 4.3 (cabeçalhos por pilar e coluna Appendix; TRE com o mesmo nome em todo lugar); Tabela 4.4 (refazer com colunas de instrumento e fase; "nine" → ten; "carries leverage" → "has most effect"; DR6 sem "4.6.2 phase 4" e com IQL/4.4.2; DR7 4.4.3 no lugar de 4.5.1; DR11 sem 4.4.3; DR3 SCR como apoio; DR10 com DTRM e TRE; DR12 sem "three site contexts")

- M (26/10, muda a D11-1): a escalabilidade NÃO usa critérios de pessoal dedicado, função de qualidade ou unidade de pesquisa (o autor não quer; não existem no cap. 2 e 3). Os três níveis são as categorias da Tabela 3.3: nonhospital (centro-alvo, nível mínimo), nonacademic hospital e academic. O argumento usa só o que a 3.4.4 e a 3.4.5 já dizem: o nível diz o que o framework pode supor que existe atrás do site ("no hospital system or university stands behind the site"); como a categoria não informa o preparo de um site em particular (3.4.4), um site sem esse apoio opera na profundidade do nível mínimo; o risco da investigação ajusta a profundidade dentro de cada nível (4.7.3). Os 24 instrumentos ficam em uso nos três níveis; sai o núcleo reduzido. Nada é acrescentado aos cap. 2 e 3 nem à 4.1 a 4.5. No abstract só se tira o que falar de pessoal dedicado ou estrutura de pesquisa, sem acrescentar nada. Não reabrir
- M (26/10): a matriz instrumento × fase da 4.6 entra como figura, na família visual da Fig. 4.4, com marcadores "montado" e "em uso". A Fig. 4.2 sai (confirmado)

- M (26/10): da 4.6 em diante, um pedaço por vez: primeiro só o texto introdutório da 4.6, depois a 4.6.1, depois a 4.6.2, e assim por diante. Nunca entregar a seção inteira de uma vez. Os rascunhos da 4.6.1 e da 4.6.2 (t46.json) e a Fig. 4.2 ficam guardados para quando chegar a vez de cada um

- M (27/10): sem tabela de portas na 4.6.1. A condição que fecha cada fase vai para a Fig. 4.1 (lista em imagens-4.6-4.8.md). O MRL fica em segundo plano no texto: uma menção leve às revisões de marco, nada de tabela nem de parágrafo destacando o MRL. A numeração das tabelas volta a: 4.2 escalabilidade, 4.3 registros invariantes, 4.4 instrumentos, 4.5 DR × componente

- Cap. 5 (27/10, da análise da 4.6.2): a hipótese de fases aparece como "predictable phases… predictable forms" no cap. 5 e como "identifiable phases" na 4.6; usar um nome só. Se a universidade exigir declaração de uso de IA, ela vai para a declaração geral ou para os métodos, não para o cap. 4 (o parágrafo do Apêndice Y saiu)

- Para a 4.7.1 e a 4.7.3 (27/10, da análise da abertura da 4.7): (a) a ressalva da 3.4.4 (categoria não informa preparo) vira regra: um site sem o apoio que a categoria supõe opera na profundidade do nível mínimo; (b) o nível é decidido na revisão de saída do start-up e revisto quando a capacidade muda durante a condução (por exemplo, saída do coordenador), além do risco; (c) DR10 x nível mínimo: acumular funções numa pessoa não fere o DR10 porque cada função tem substituto nomeado (4.2.2), e o conflito restante segue a regra da 3.5 (a restrição operacional prevalece); (d) a unidade que escala: cadência, independência da revisão, registros combinados, acúmulo de funções
- Nomenclatura (27/10): um nome só para os níveis, "implementation level" (termo do cap. 3). Trocar "site contexts" (título da 4.7.1), "site types" (cap. 5), "Type A/B/C" (4.7.1, Tabela 4.2, cap. 5) e conferir "three implementation depths" no abstract

- M (27/10): a 4.7 perde as subseções 4.7.1 a 4.7.3 (pedido do autor: tudo num bloco só, para dar volume ao argumento da escalabilidade). Proposta de Claude: a 4.7 fica com a abertura e o corpo, sem subtítulos (uma subseção única 4.7.1 não se justifica). Confirmar com o autor. Atualizar o sumário e o cap. 5 se citar 4.7.1 a 4.7.3. As referências [88], [89], [90] e [30] foram mantidas no texto novo

- M (27/10, muda a escalabilidade): NÃO existe "forma enxuta" de instrumento nem combinação de registros. Os instrumentos são um só, na versão mais completa; os modelos ficam em formato aberto e editável para o site adaptar ao padrão visual e acrescentar ou tirar campos (dizer isso na 4.8). O que escala é QUANTOS instrumentos o site usa: no nível mínimo (nonhospital), só um subconjunto; os outros ficam opcionais, com um instrumento do subconjunto servindo de proxy. O POT sempre fica; o MRL sai no mínimo e o POT registra as revisões de marco. Critério do autor: deixar de fora o que não é obrigação do site. Pendente: decidir o conjunto mínimo (proposta de Claude em 27/10) e onde mostrar: DECIDIDO em 27/10, só na Tabela 4.2 (linha "Role structure and instruments" lista os que ficam e os proxies; sem coluna nem figura extra). O SLCT no mínimo: o autor vai escrever a resposta. Refazer o texto da 4.7 (tirar "leanest form", "compatible records kept together", "Every site uses all twenty-four instruments", "never in which functions exist") e a Tabela 4.2 enviada em 27/10 (ela ainda diz "kept together in one file", "compatible records may be combined" e "All 24 instruments are in use" nos três níveis)

- M (27/10): conjunto mínimo (nonhospital) decidido pelo autor = 11 instrumentos: POT, RACI, TRE, SCR, SART, IMC, PSEAR, ICDL, IQL, FUCR, PIDLR. Saem do mínimo, com proxy: CCDM (RACI), MRL (POT), DTRM (requisitos de treino do sponsor), SRR (riscos levantados na reunião do POT; avaliação de risco do sponsor), SLCT (reavaliação do SCR + substituições no ICDL), SCML e CSST (casos do SART revistos juntos na reunião do POT), IMP (escopo e cadência no IMC), SIRR (charter do sponsor), SIFSL (log de identificação do sponsor, ISO 7.5.2), PFVR (páginas de visita do CRF), PIR (FUCR + reunião), CAPA (processo de CAPA que o site ou o sponsor já tem). Critério do autor: gaps não são obrigação; no mínimo fica o essencial e o que é fácil de operar. Consequência para o texto da 4.7: no nível mínimo, os gaps 2, 3 e 5 ficam cobertos só por proxies, e as respostas completas vêm nos níveis acima; dizer isso sem rodeio. Prompt da Tabela 4.2 em revisao/prompt-tabela-4.2.md
- Nomes dos instrumentos (27/10): o autor acha os nomes difíceis de lembrar (ex.: PIDLR) e cogita novos nomes. Decidir antes da passada final; se mudar, muda em todo o cap. 4, nas figuras, tabelas e apêndices

- M (27/10, muda o conjunto mínimo): o SRR sobe; o mínimo tem 12 instrumentos (POT, RACI, TRE, SCR, SRR, SART, IMC, PSEAR, ICDL, IQL, FUCR, PIDLR). Proxy da CAPA no mínimo: ações decididas na reunião ou pedidas pelo sponsor ficam registradas e acompanhadas no POT (não supor que o centro-alvo tem processo de CAPA próprio, o que contradiria o Gap 1). Argumento para a 4.7: no mínimo, cada gap tem ao menos um instrumento leve (Gap 1 POT e RACI, Gap 2 SRR, Gap 3 reavaliação do SCR, Gap 4 IMC, Gap 5 PIDLR), e as obrigações já existentes vêm primeiro porque o site responde por elas de qualquer jeito (3.5: o framework organiza deveres existentes e responde aos gaps)

- M (27/10): mínimos RECOMENDADOS por nível: nonhospital 12 (POT, RACI, TRE, SCR, SRR, SART, IMC, PSEAR, ICDL, IQL, FUCR, PIDLR); nonacademic hospital 18 (+ SLCT, SCML, CSST, IMP, PIR, CAPA, o que completa a resposta a todos os gaps); academic 24 (+ CCDM, MRL, DTRM, SIRR, SIFSL, PFVR, instrumentos de estrutura formal). É o mínimo recomendado, não o literal: todo site pode e deve usar mais, e os 24 sempre que possível. O texto da 4.7 tem de dizer isso com clareza
- Correção (27/10): o proxy da CAPA no mínimo NÃO contradiz o Gap 1. O Gap 1 é a falta de um requisito de sistema de qualidade estruturado no site, e não a falta de qualquer procedimento; um centro que conduz investigações já tem SOPs e registros básicos, e a ISO 14155:2026 (10.6(o)) já pede ao PI causa e CAPA para não conformidade significativa. Proxy: o processo que o site já usa ou que o sponsor pede, acompanhado no POT. O Gap 1 não precisa ser reescrito

- M (27/10): a tabela de registros invariantes da 4.7 saiu (o autor achou que não acrescenta). Os registros ficam citados em prosa no último parágrafo da 4.7, sem números de cláusula, com [8, 10]. Numeração das tabelas: 4.1 funções, 4.2 escalabilidade, 4.3 instrumentos, 4.4 DR × componente (as duas últimas mantêm o número)

- M (27/10, final): fica "proxy", definido no primeiro uso na 4.7 ("a proxy, another record that the site keeps and that takes on its function"). Não reabrir

- Coerência com a escalabilidade 12/18/24 (27/10), fora da 4.8, para a passada final: (a) 4.1: "The depth at which a site uses each instrument follows the risk…" → quais instrumentos o site usa e com que frequência revisa seguem o risco e o nível; (b) cap. 2: "Figure 4.5 does the same for the 24 instruments" (a Fig. 4.5 saiu; trocar por Table 4.4); (c) cap. 5: "a center that adopts all twenty-four at once will operate none of them well", "can sustain the full set", "a small number of Type B centers"; (d) Fig. 4.1, saída do start-up: "SRR in place, rules of each instrument in use fixed" (IMP e PIR não estão no mínimo). Na 4.6.2 já ajustei: "in its plan or on its checklist" e "each indicator in use"

## 4. Passadas finais já combinadas

- **Regra (27/10, do autor):** o texto nunca descreve figura ou tabela (marcadores, linhas, colunas, cores, forma). Descrição fica na legenda; no texto, só a afirmação sobre o framework com a remissão entre parênteses. Na passada final, varrer os caps. 3 e 4 inteiros com essa regra.

- **Tabela 4.4 saiu (27/10).** Trocar as remissões: 2.5.1 ("Table 4.4 lists each requirement with the components that answer it") → Figure 4.4; 4.1 ("Table 4.4, at the end of the chapter, lists each design requirement…") → Figure 4.4 para os DRs e Table 4.3 para a seção de cada instrumento; lista de tabelas e de figuras.
- **4.8 reescrita do zero (27/10, t48b).** O argumento: a 3.5 diz que o framework só se justifica pela origem de cada parte; a 4.8 entrega essa justificativa para o conjunto, em duas frentes (os registros se ligam; as partes são completas e necessárias). A versão t48 fica arquivada.

- 4.7.1: o "PD record" do núcleo do Type C é o registro de desvios exigido pelo CIP, não um instrumento do framework (não há registro de desvios entre os 24); ajustar a frase ao revisar a 4.7

- 4.5.1 e 4.5.3: ao revisar, tirar o texto de controle que foi para a nova 4.4.3 (confirmação estruturada de critérios de imagem ou de várias fontes, erro de inclusão irreversível, definição de visita utilizável); a 4.5.1 e a 4.5.3 ficam só com o indicador; nomear o FUCR na 4.5.3 (decidido em 25/10)
- Apêndices: reordenar os títulos de Q em diante quando a 4.4 e a 4.5 fecharem (Q PSEAR, R SIFSL, S PFVR, T ICDL, U PIR, V FUCR, W CAPA, X PIDLR, Y modelo interativo) e passar a ordem final para a Tabela 4.3 e as Figuras 4.2 e 4.3

- 4.5.5 (Surgeon procedural consistency): ao revisar, tirar a lógica de leitura da curva (comparação com o próprio cirurgião, case mix, clustering) e a lista de consequências, que agora estão na 4.3.2; e remeter à 4.3.3 para o padrão de complicações (decidido em 25/10 na revisão da 4.3.2 e da 4.3.3)

- "architecture" ainda aparece 16 vezes, inclusive no Abstract e no Resumo e no cap. 5. Trocar por framework. O Abstract também chama o pilar de "risk-based quality management (RBQM)", e o nome do pilar é Risk Management
- Números novos (68, 108, 347) na 5.3, na 5.7, no cap. 6, no Resumo e no Abstract
- Cap. 5 repete o estudo português [77] e as três correntes de risco da ISO 6.2, que agora estão na 4.3 e na 4.3.1. Remeter em vez de repetir
- Vírgula serial nos cap. 1 a 3
- FDA definida no primeiro uso (1.4.1)
- Frase que distingue CTAIM e ISO 9001 [30, 31] (o autor confere)
- E8(R1) "Section 7 lists 18 considerations" e a tríade de risco do E8 na 2.5.2
- String de busca do ClinicalTrials.gov
- "25% of the MDR entries" (Claude conta cerca de 30%)
- Citações em subscrito, que devem ficar na linha
- Apêndices ainda "[Template pending]"
- IMP (Internal Monitoring Plan) é o único modelo que não está no repositório (25/10)
- Atualizar sumário e índices (Ctrl+A, F9)
- A frase "attendance alone does not show that a visit was complete" aparece na 4.4.1 (verificação Follow-up execution) e na 4.4.3. Deixar em uma só (a 4.5.3 não repete; 25/10)

## 5. Edições de imagem que ficaram com o autor (L1)

- Tabela 3.1: referências do Gap 3 → [71, 72]; Gap 5 → ISO 14155:2026 Clause 10.6(o) no lugar do MDR
- Tabela 3.2: termo "UDI" no domínio 4 (avaliar "batch, serial or unique device code"); itens antigos a confirmar: menção a delegação no domínio 6 e mascaramento do avaliador no domínio 8
- Tabela 3.4: "architecture" → framework; rótulos das condições (depois de D3); grafia americana
- Tabela 4.1 (funções): "PROM workflows" → "PROM administration"; "Data QA" → "Data QA function"
- Tabela 4.3 (instrumentos): ordem pela primeira citação. Governance: CCDM, MRL, POT, RACI, DTRM, TRE, SCR. Os outros pilares quando a revisão do cap. 4 fechar
- Figura 4.2: conferir o nome do TRE
- Figura 4.4: o PIR não tem marcador no domínio CtQ 6, mas o texto da 4.5 diz que a consistência do cirurgião responde aos domínios 5 e 6 (e o PIR v0.10 diz SP-01 CtQ 5, 6)
- Tabela 4.2 (escalabilidade): grafia britânica (programme, centre, authorisation, specialised); linha "Role architecture and controlled instruments" → role structure; tipos definidos por porte ("Large or complex research hospital", "Medium private clinic/hospital", "Small surgical centre") dependem de D4 (4.7.1 x 3.4.5)
- Figura 4.1: "PI oversight plan" → PI Oversight Template (POT); "Delegation log" → delegation record (CCDM e RACI); "recognise" → "recognize"; manter "at least monthly" (a 4.3.3 adotou)
- Antiga tabela de DRs: **FEITO** (refeita como Tabela 4.4 em 24/10)

- **Referências (30/10, v4):** cortadas 21 referências redundantes (auditoria de utilidade + decisões anteriores): 2, 4, 15, 16, 25, 28, 38, 47, 50, 58, 65, 70, 74, 82, 88, 89, 93, 95, 98, 99, 103 (numeração da v3). Mantidas apesar da auditoria: Getz (única fonte da rotatividade de investigadores, origem do DR10 na Tabela 3.4), Wang (único exemplo de hospital comunitário) e Adams (citado na Tabela 5.1). A FDA RBM guidance ficou só na Tabela 5.1. Lista com 89 referências. A imagem da Tabela 5.1 precisa ser refeita com a nova numeração (ver mensagem de 30/10).

- **Referências, revisão de 30/10 (v5):** depois de ler os artigos cortados, voltaram: van der Aa (SQA checklist; frase nova na 1.4.1 e nuance na 5.2), Stergiopoulos (único sobre as informações de site no ClinicalTrials.gov), Conroy 2022 (única fonte da curva de aprendizagem na frase da 3.4.2), Jalbert (único que sustenta "metodologia feita para fármacos"), Deger (mostra que a padronização funciona: ICC 0,91) e Vulcano (existe, white paper ACRP/SCRS; fica só na Tabela 5.1, como trabalho mais próximo). Ficam cortadas 15: Bhatt, Bharati, Buccheri, Sidor, Bakobaki, Jaguste, Ergina, Gagnier, Karlberg (agora verificada: Clin Trial Magnifier 2009;2(7):348–60; pode voltar se o autor quiser), Ciupek, Anderson, Feehan, Gottlieb, Bouaicha, Li. Lista com 95 referências.

- **Referências "cortar depois" e "condicionais" (30/10, v5):** reavaliadas FD&C Act (9), Roemer (51), Drain (65), Getz (67), Deger (83), FDA RBM guidance (88), Vulcano (90) e Skivington (95). Todas ficam: cada uma é a única fonte de uma afirmação que continua no texto (Drain conferida no PubMed: 540 contra 202 trial site-years por milhão). Nenhum corte, numeração da v5 inalterada. Planilha com a função de cada uma das 95 referências: `revisao/referencias-funcao-30-10.xlsx`.

- **v6 (30/10):** nova imagem da Tabela 5.1 (numeração da v5, linha "Operator learning is controlled by the trial team") inserida na largura do texto; ordem das citações conferida por script, incluindo a sequência da Tabela 5.1: 1 a 95 em ordem de primeira aparição. Títulos: seções e subseções (Heading 2 e 3) voltam a herdar o recuo de primeira linha de 1,27 cm, como no arquivo de 29/10; títulos de capítulo, References e Appendices ficam rentes à margem (na 29/10 só o capítulo 4 estava rente; padronizado). Criada a List of Tables (11 tabelas, com marcadores e PAGEREF, como a List of Figures); números de página das listas e do sumário preenchidos, e o Word atualiza os campos ao abrir.

- **Regra dos instrumentos (autor, 30/10):** cada instrumento funciona sozinho e de um só jeito, independente do nível de implementação. Nada de "implementation level", "site type", modos proxy ou campos que mudam conforme o nível; nada de cláusulas de norma nem seções da tese dentro dos formulários (eles não são extensão da tese; servem a qualquer centro que queira implementar). O conjunto será entregue também em .docx editável. As propostas de "modo proxy" da auditoria de 30/10 (B1) ficam descartadas. A Section A deve explicar com clareza como o documento funciona (partes, quando, quem preenche, o que lê e para onde manda).

- **POT v1.1 concluído (autor, 30/10):** em branco e preenchido (GLENOS-01), HTML e PDF, em `revisao/instrumentos/POT/` e em `codex/thesis-work:instrumentos-concluidos/` (README, manifesto, VERIFICACAO e checklist atualizados; 8 de 24 concluídos). PDFs com Liberation Sans, Comic Neue e Dancing Script no lugar de Arial, Comic Sans e Z003, que não existem neste ambiente.

- **SART v1.0 (autor, 30/10):** reconstruído a partir da análise do Codex. Decisões do autor: nome novo "Safety Assessment, Reporting and Tracking Template" (a tese terá de ser ajustada depois: abreviaturas, Tabela 4.3, 4.3.3, 4.5.4, Apêndice K); contexto contribuinte em C3 mantido; rótulos Pending / Preliminary / Final (PI); seção F com PIR e rota de DD do patrocinador; três caixas de assinatura; sem "Editor v2 canônico" (usa o editor dos concluídos).
- **SART v1.0 concluído (autor, 30/10):** em branco e preenchido, HTML e PDF, em `revisao/instrumentos/SART/` e em `codex/thesis-work:instrumentos-concluidos/` (9 de 24). O autor não se importa com exemplos fictícios diferentes entre instrumentos (Northbridge no SCML, GLENOS-01 nos demais).

## IMP v1.0 (31-10)
- Páginas 2–7 sem faixa de cabeçalho repetida (documento grampeado). Vale para os próximos instrumentos.
- Tabela H: resposta mínima em branco, o centro escreve; sem "checked again".
- Assinatura do responsável: "Plan owner" (padrão "Matrix owner", "SCML owner"), não "Prepared by".
- Sem "covered by proxy" nem níveis. Linhas em branco extras só se todas as tabelas equivalentes tiverem.
- Em aberto: incluir checks de consentimento/elegibilidade e de delegação/treinamento (mudaria 4.4.1 e IMC).
- IMP 2ª rodada: status só Draft/Approved (o "Supersedes" da versão nova já registra a substituição); sem caixa de independência do revisor (regra fica no guia da D); checks 11 consentimento/elegibilidade e 12 delegação/treinamento + linhas 13–14 livres; C, D (agenda+revisor+amostra fundidos) e E em duas páginas cada (7 + 7 linhas); 9 páginas.
- Pendente na tese: 4.4.1 passa de dez para doze checks; IMC precisa dos dois novos domínios.
