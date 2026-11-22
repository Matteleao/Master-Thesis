# Guião da defesa — sequência de slides (versão 2)

**Base:** `revisao/Tese_Final_2026-11-16` (branch `claude/claudinho-status-check-8tzmxz`).
**Duração:** 30 min. O guião soma cerca de 29 min, com 32 slides principais e slides de reserva.
**Status:** só a ordem e o conteúdo dos slides. Ainda não há estilo visual.

---

## Abertura

**Slide 1 — Título** (0:20)
- Título da tese, autor, orientadora, coorientador, mestrado e ano letivo.

**Slide 2 — Estrutura da apresentação** (0:20)
- Introdução, objetivos, metodologia, resultados (lacunas e requisitos; framework), discussão e conclusão.

## Introdução (3:30)

**Slide 3 — Enquadramento regulatório: qualidade planeada e proporcional ao risco** (1:15)
- ICH E8(R1) (2021): QbD e fatores CtQ.
- ICH E6(R3) (adotada a 6/1/2025):
  - QbD e proporcionalidade passam a ser princípios;
  - a supervisão do que é delegado é proporcional ao risco.
- Dispositivos médicos:
  - a ISO 14155:2026 (março de 2026) é a norma de BPC;
  - o MDR é o quadro legal na UE;
  - a EN ISO 14155:2020+A11:2024 ainda é a versão harmonizada.
- Repartição de responsabilidades:
  - a gestão da qualidade ao nível do ensaio cabe ao promotor;
  - ao investigador cabem a condução e a supervisão, sem uma estrutura definida para o centro.

**Slide 4 — Investigações cirúrgicas com dispositivos implantáveis: cinco condições** (1:00)
- **Irreversibilidade:** o implante não pode ser suspenso como um fármaco.
- **Dependência do operador:** curva de aprendizagem de cerca de 12 a 86 casos na artroplastia do ombro.
- **Rastreabilidade unitária:** componente ↔ participante durante todo o seguimento.
- **Peso do seguimento:** 34,3% de perda de seguimento ao 7.º ano numa coorte de artroplastia do ombro.
- **Fiabilidade limitada das classificações:** concordância interobservador de fraca a moderada.

**Slide 5 — Instrumentos de qualidade existentes e os seus utilizadores** (1:15)
- Três grupos, por quem aplica e a quem se aplica:
  1. **Aplicados pelo promotor ou pela equipa do ensaio:** TransCelerate, CTTI QbD, MDIC; frameworks de SQA cirúrgica.
  2. **Medem o centro a partir de fora:** framework de prontidão, Clinical Trial Site Performance Measure, monitorização central.
  3. **Aplicados pelo centro a si próprio:** CTAIM, ISO 9001, unidades de ensaios clínicos.
- Lacuna: nenhum liga os CtQ de uma investigação específica aos riscos da conduta do centro, aos seus controlos e aos seus indicadores.
- Duas necessidades não atribuídas ao centro:
  - curva de aprendizagem durante a condução;
  - captura intraoperatória de dados não reconstruíveis.
- Dado: 9 de 46 centros portugueses (19,6%) tinham uma ferramenta de análise de risco ao nível do centro.

## Objetivos (1:00)

**Slide 6 — Objetivo e objetivos específicos** (1:00)
- Objetivo geral: um framework de gestão da qualidade operacional para centros que conduzem investigações de dispositivos médicos do ombro.
- Objetivos específicos:
  1. comparar cláusula a cláusula a ICH E6(R3), a ISO 14155:2026 e o Anexo XV do MDR;
  2. identificar os domínios CtQ ao nível do centro;
  3. derivar requisitos de desenho explícitos e rastreáveis;
  4. desenvolver o framework e os instrumentos operacionais.
- Âmbito:
  - quadro regulatório europeu;
  - ortopedia, e o ombro em particular;
  - estudo de desenho: o framework não foi implementado.

## Metodologia (3:00)

**Slide 7 — Design Science Research Methodology** (0:45)
- Peffers et al., com início centrado no problema.
- As 6 atividades:
  - realizadas: identificação do problema, definição de objetivos, desenho e desenvolvimento, e comunicação (esta tese);
  - deixadas para trabalho futuro: demonstração e avaliação.

**Slide 8 — Fontes de evidência** (1:15)
- **Comparação normativa:**
  - E6(R3), ISO 14155:2026 e Anexo XV do MDR, comparados cláusula a cláusula;
  - a E8(R1) entra como referência (18 considerações);
  - 3 categorias: fortemente harmonizado, parcialmente harmonizado, sem obrigação para o centro.
- **Revisão da literatura:**
  - 5 áreas: gestão da qualidade em investigação clínica, SQA, metodologia de ensaios cirúrgicos, literatura clínica do ombro e organização de centros;
  - pesquisa iterativa ao longo de todo o trabalho.
- **Análise de registos:**
  - ClinicalTrials.gov, API v2, com acesso a 2/5/2026 (o Eudamed não forneceu dados suficientes de centros);
  - estudos de intervenção no ombro, com dispositivo e promotor da indústria, de 2000 a 2026, restritos a dispositivos implantáveis;
  - unidade de análise: o registo de centro;
  - 3 categorias organizacionais.

**Slide 9 — Da evidência ao framework** (1:00)
- A cadeia:
  - matriz de cláusulas;
  - → filtros (responsabilidade, âmbito, relevância);
  - → domínios, testados com 4 critérios (proporcionalidade, parcimónia, responsabilidade atribuída, conhecimento existente);
  - → requisitos (lacunas + domínios + condições operacionais);
  - → pilares (ISO 13485:2016, ISO 14971:2019, ISO 15189:2022);
  - → instrumentos.
- Justificação: nenhuma norma exige um sistema de qualidade no centro. Por isso, cada componente é rastreado até um requisito, e cada requisito até à sua origem.

## Resultados I — Lacunas, domínios e requisitos (cap. 3) (6:15)

**Slide 10 — Comparação normativa** (1:15)
- 251 entradas: 100 da E6(R3), 90 da ISO 14155:2026 e 61 do MDR, agrupadas em 43 temas.
- Entradas com um dever para o investigador ou o centro: 55% (E6(R3)), 59% (ISO) e 25% (MDR).
- Temas: 8 fortemente harmonizados, 21 parcialmente harmonizados e 14 sem obrigação para o centro.
- Exemplo de tema parcialmente harmonizado: a notificação de segurança.
  - Os prazos do investigador diferem entre as normas.
  - A ISO 14155:2026 separa os eventos do dispositivo dos eventos dos procedimentos do CIP.

**Slide 11 — Cinco lacunas** (1:15)
- Tabela 3.1 redesenhada, com o que as normas preveem e o que falta:
  1. sistema de gestão da qualidade do centro;
  2. registo e ciclo de risco do centro;
  3. curva de aprendizagem durante a condução;
  4. monitorização interna iniciada pelo centro;
  5. ciclo proativo de melhoria.
- Assimetria na cadeia de evidência do CER:
  - fabricante: ISO 13485 e ISO 14971;
  - laboratório: ISO 15189;
  - centro: nenhuma exigência de sistema próprio.

**Slide 12 — Derivação dos domínios CtQ do centro** (1:00)
- O funil de temas:
  - 43 temas, menos 9 (responsabilidade), menos 5 (âmbito), menos 1 (relevância: randomização e ocultação);
  - restam 28: 22 requisitos e 6 controlos.
- Os 22 requisitos formam 12 domínios. Os 6 controlos alimentam as lacunas.
- Fator CtQ × domínio: o fator é do estudo e é definido pelo promotor; o domínio é a área de operação do centro onde os fatores se situam.

**Slide 13 — Os doze domínios CtQ** (1:00)
- Os 12 domínios, agrupados por fase (Tabela 3.2 redesenhada).
- Em destaque, os domínios 5, 6, 8 e 9: assentam em requisitos que nenhuma norma atribui ao centro. Os restantes 8 organizam deveres já existentes.
- Verificação externa: o suplemento do MDIC para dispositivos corresponde aos domínios 1, 4, 6 e 9.

**Slide 14 — Ambientes organizacionais dos centros** (1:00)
- Seleção: 46 investigações com 355 registos, que resultam em 45 investigações, 347 registos de centro e 238 organizações.
- Registos por ambiente:
  - académicos: 137 (39,5%);
  - hospitais não académicos: 102 (29,4%);
  - fora de hospital: 108 (31,1%).
- Peso dos EUA:
  - 70,0% dos registos;
  - 63 das 68 organizações fora de hospital.
- Decisão de desenho: a pequena clínica independente como caso mais restritivo.

**Slide 15 — Doze requisitos de desenho** (0:45)
- Origem em 3 blocos:
  - DR1–DR5: lacunas;
  - DR6–DR9: domínios e condições estruturais;
  - DR10–DR12: condições operacionais.
- Regra de prioridade: o DR11 prevalece em caso de conflito (papel ou sistema existente; sem software nem pessoal novos).

## Resultados II — O framework (cap. 4) (9:10)

**Slide 16 — Arquitetura: quatro pilares** (1:00)
- Pilares e número de instrumentos:
  - Governação: 7;
  - Gestão do Risco: 5;
  - Controlos Operacionais: 8;
  - Supervisão do Desempenho: 4.
- Origem de cada pilar nas cláusulas das ISO 13485, 14971 e 15189.
- Requisitos a que cada pilar responde.

**Slide 17 — Os 24 instrumentos** (1:00)
- Tabela 4.3 redesenhada: sigla, nome e função numa linha, agrupados por pilar.

**Slide 18 — Organização funcional: evidência, síntese, decisão** (1:00)
- Figura 4.3 redesenhada. A decisão define a regra para os registos seguintes.
- Registos no momento clínico:
  - 5 instrumentos são preenchidos no momento clínico: PSEAR, ICDL, IQL, PFVR e SART;
  - os outros 19 reutilizam esses registos ou os registos clínicos existentes.

**Slides 19 a 24 — O ICDL (Intraoperative Checklist and Device Log), página a página**

São as 6 páginas do Apêndice T (versão 0.15, dados simulados), uma por slide, com a página inteira visível e realce nos campos indicados.

| Slide | Pág. | Secções | Campos a realçar | Tempo |
|---|---|---|---|---|
| 19 | 1 | A–B | Finalidade: preenchido durante o procedimento, porque os dados intraoperatórios não são reconstruíveis. Não substitui a nota operatória, o registo de contabilidade do dispositivo nem a notificação; remete para eles. Unidade de análise: um participante, um procedimento. Liberação para início (B). | 0:40 |
| 20 | 2 | C–D | Passos críticos do CIP, cada um com execução, evidência e resultado. Tempos e dados do caso (complexidade, apoio sénior) que alimentam o SLCT. Ligação à lacuna 3 e ao DR3. | 0:50 |
| 21 | 3 | E | Componentes com catálogo, UDI-DI, lote ou série, tamanho e destino (implantado, prova, devolvido, descartado, explantado). Regra: copiar os identificadores do rótulo no momento. Reconciliação com a nota operatória e o registo de contabilidade antes do fecho. | 0:50 |
| 22 | 4 | F–G | Alterações ao plano: o que aconteceu, motivo, efeito possível, resposta e registo ligado. O exemplo do apêndice é a ausência de liners de prova no kit, que deu origem a um desvio. Complicações e desempenho do dispositivo, encaminhados para o SART e o SCML. | 0:50 |
| 23 | 5 | H–I | Revisão pós-operatória imediata: configuração, reconciliação, estado pós-operatório e imagem registada no IQL. Critérios para encerrar o caso. | 0:30 |
| 24 | 6 | J–K | Ações em aberto: destino, responsável, prazo e prova de eficácia. Assinaturas e arquivo. | 0:30 |

**Slide 25 — Ciclo de vida da qualidade** (1:00)
- Figura 4.1 redesenhada:
  - 7 fases: viabilidade, arranque, inclusão, cirurgia, seguimento, encerramento e melhoria contínua;
  - uma faixa de segurança atravessa as fases de condução.
- 15 dos 24 instrumentos são preparados ou usados no arranque.
- 4 regras temporais que as normas não impõem:
  - registo de risco antes do 1.º participante;
  - base de comparação da curva de aprendizagem antes do 1.º caso;
  - âmbito da verificação interna definido antes da condução;
  - regras dos indicadores fixadas antes do 1.º participante.

**Slide 26 — Modelo de escalabilidade** (1:00)
- 12, 18 ou 24 instrumentos (fora de hospital, hospital não académico, académico).
- Cada instrumento omitido tem um registo substituto (Tabela 4.2).
- A categoria não define a capacidade:
  - o PI regista o nível no fim do arranque;
  - o centro acrescenta instrumentos para os domínios de risco elevado.

## Discussão (4:00)

**Slide 27 — Contribuição** (1:15)
- Classificação de Gregor e Hevner:
  - 7 instrumentos de desenho de rotina;
  - 14 exaptações;
  - 3 melhorias (CCDM, SCR e ICDL);
  - nenhuma invenção.
- A ligação entre instrumentos e o modelo de escalabilidade também contam como melhorias.
- Conhecimento reutilizável, independente do ombro: os domínios, os requisitos e a ligação registo → revisão → decisão.

**Slide 28 — Implicações** (1:00)
- **Centro:** controlo documentado da própria conduta, independente da rotação de pessoas; o trabalho de qualidade pode entrar no orçamento.
- **Promotor e monitor:**
  - o centro chega com o seu próprio registo de risco;
  - o ICDL pode servir como fonte dos identificadores de implante;
  - o SLCT pode servir à análise da aprendizagem, que só 1 de 247 ensaios cirúrgicos fez.
- **Normas:** uma revisão da ISO 14155 poderia descrever o papel do centro nos riscos da sua execução; possível acreditação de centros, por analogia com a ISO 15189.

**Slide 29 — Limitações** (1:00)
- O framework não foi implementado.
- A avaliação feita foi ex ante, formativa e artificial (rastreabilidade), realizada pelo autor.
- Os limiares dos indicadores são provisórios.
- O registo é dominado pelos EUA, com um único classificador.
- Não houve consulta formal a especialistas nem acesso a documentos internos de centros.

**Slide 30 — Trabalho futuro** (0:45)
1. Demonstração com uma série de casos simulada ou retrospetiva.
2. Revisão de conteúdo por centros, monitores e cirurgiões, e teste de usabilidade.
3. Estudo de viabilidade numa pequena clínica e num hospital, com o tempo da equipa por instrumento.
4. Avaliação de efeito com comparação concorrente, por exemplo uma introdução escalonada por um promotor.

## Conclusão

**Slide 31 — Conclusão** (1:00)
- Os 4 objetivos, cada um com o seu resultado:
  1. 251 entradas, 43 temas e 5 lacunas;
  2. 12 domínios CtQ do centro;
  3. 12 requisitos rastreáveis;
  4. 4 pilares, 24 instrumentos, ciclo de vida de 7 fases e níveis de 12, 18 e 24 instrumentos.
- Frase final sobre o papel do centro ao lado da supervisão do promotor.

**Slide 32 — Agradecimento e perguntas** (0:10)

---

## Resumo do tempo

| Secção | Slides | Tempo |
|---|---|---|
| Abertura | 1–2 | 0:40 |
| Introdução | 3–5 | 3:30 |
| Objetivos | 6 | 1:00 |
| Metodologia | 7–9 | 3:00 |
| Resultados I (cap. 3) | 10–15 | 6:15 |
| Resultados II (cap. 4) | 16–26 | 9:10 |
| Discussão | 27–30 | 4:00 |
| Conclusão | 31–32 | 1:10 |
| **Total** | **32** | **≈28:45** |

## Slides de reserva (perguntas prováveis)

Retiradas do plano de 19/11, `revisao/Plano_correcoes_avaliacoes_2026-11-19.md`, secção 6:

| R | Tema | Base na tese |
|---|---|---|
| R1 | Exclusão da randomização e da ocultação. Os riscos são condicionais: com avaliador ocultado, entram no SRR, e o domínio 8 cobre o caso. | 3.3 |
| R2 | Composição do conjunto mínimo de 12 instrumentos e o SLCT como acréscimo por risco | 4.7, Tabela 4.2 |
| R3 | Tempo de operação: não medido; primeira medida de um estudo de viabilidade | 5.3.1, 5.6.3 |
| R4 | A pequena clínica independente na Europa: limite do registo e decisão de desenho | 3.4.4–3.4.5 |
| R5 | Porquê as ISO 13485, 14971 e 15189, e não a ISO 9001 | 2.5.1, 3.2.1 |
| R6 | Deveres do investigador na E6(R3) versus sistema de qualidade (lacuna 1) | 3.2 |
| R7 | Reunião de supervisão não realizada (campos de revisão do POT). Atenção: o texto da 5.3.1 e da Tabela 5.2 diz o contrário. | 5.3.1 |
| R8 | Comparação com poucos casos: mesmo cirurgião, mesma complexidade, revisão clínica e não teste estatístico | 4.3.2, 4.5.5 |
| R9 | PI que é dono da clínica e cirurgião avaliado: substituto nomeado | 5.5.4 |
| R10 | Aumento inicial de desvios detetados | 5.3.3 |
| R11 | Os filtros retiraram 15 temas; os 12 candidatos cumpriram os 4 critérios | 3.3 |
| R12 | Figura 4.4: instrumentos × domínios × requisitos | 4.8 |
| R13 | Tabela 3.2 completa (domínios, âmbito, ameaças) | 3.3 |
| R14 | Figura 4.2: instrumentos por fase | 4.6.2 |

## Versão de 20 minutos

Cortes:
- tirar o slide 2;
- juntar os slides 10 e 11, os slides 12 e 13, os slides 16 e 17, os slides 25 e 26, e os slides 29 e 30;
- no ICDL, manter só as páginas 2, 3 e 4 (slides 20 a 22).

Com isso ficam cerca de 23 slides, em perto de 20 min.

## Decisões em aberto

1. Idioma dos slides e da apresentação (a tese está em inglês).
2. Confirmar 20 ou 30 minutos.
3. Confirmar que a versão entregue é a de 16/11, ou se entraram correções do plano de 19/11.
4. Slide 2 (estrutura): manter ou retirar?
