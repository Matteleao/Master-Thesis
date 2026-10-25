# Passagem de contexto: tese do Felipe e revisão dos 24 instrumentos

Documento preparado pelo Claude (Claude Code) em 25/10/2026 para que outro assistente continue o trabalho com o mesmo raciocínio, as mesmas regras e o mesmo processo. Leia este arquivo inteiro antes de responder ao Felipe.

## 0. O que há neste pacote

| Arquivo / pasta | Para que serve |
|---|---|
| `01_LEIA_PRIMEIRO_Passagem_de_contexto.md` | Este resumo: projeto, método, regras, estado atual, próximos passos. |
| `02_Conversa_completa_Felipe_e_Claude.md` | A conversa inteira (23/09 a 25/10/2026), só mensagens e respostas, em ordem. Use para ver como as decisões foram tomadas e o tom da colaboração. |
| `03_Skills_e_regras/instrument-review/` | O processo de revisão dos instrumentos: `SKILL.md` (passos e critérios), `reference/standards.md` (regras comuns S1 a S21), `reference/baseline.md` (linha da Table 4.4 de cada instrumento), `reference/sources.md` (onde a tese descreve cada um), `reference/requirements/<SIGLA>.md` (requisitos extraídos e histórico de cada revisão), `scripts/` (verificações automáticas usadas localmente). |
| `03_Skills_e_regras/scientific-prose`, `argument-structure`, `evidence-and-delivery` | As regras de escrita acadêmica do Felipe. Valem para qualquer texto em inglês da tese. |
| `04_Memorias_do_Claude/` | Notas persistentes que o Claude guardou sobre preferências e decisões do Felipe. |
| `05_Status_e_revisoes/` | `STATUS.md` (estado de cada instrumento) e os relatórios de revisão em HTML (CCDM, DTRM, TRE, RACI, SCR, POT). |
| `06_Instrumentos_versoes_atuais/` | As versões vigentes em HTML (em branco e simulada) dos instrumentos já revisados. |

Os caminhos citados na conversa (por exemplo, `/Users/felipegregorio/...`) são do computador do Felipe e não estão acessíveis a você. Peça ao Felipe que envie o arquivo de que você precisar, como a tese em .docx ou um instrumento ainda não revisado.

## 1. O projeto

- **Autor:** Felipe, mestrando na Universidade de Lisboa (Faculdade de Farmácia). Citações no estilo Vancouver, numeradas por ordem de primeira aparição; citações juntas no formato "[a, b, c]", com vírgula e espaço, todos os números listados e sem intervalos.
- **Tese:** um framework de gestão da qualidade no nível do centro de pesquisa (site-level quality management) para investigações clínicas de dispositivos cirúrgicos, com exemplo em artroplastia de ombro. O método é Design Science Research Methodology (DSRM).
- **Estrutura do framework:**
  - Cinco lacunas regulatórias (Chapter 3, Table 3.1):
    1. ausência de sistema de qualidade estruturado no centro;
    2. ausência de risk register do centro;
    3. proficiência do operador não observada durante a condução (curva de aprendizado);
    4. ausência de função de verificação iniciada pelo centro;
    5. ausência de ciclo proativo de melhoria.
  - 12 domínios CtQ do nível do centro (Section 3.3, Table 3.2):
    1. Site capability, readiness and capacity maintenance;
    2. Participant selection and baseline characterization;
    3. Informed consent;
    4. Device management, accountability and traceability;
    5. Procedural delivery and surgical technique standardization;
    6. Training, credentialing and learning-curve control;
    7. Perioperative and postoperative care pathway and follow-up retention;
    8. Endpoint framework and outcome-assessment standardization;
    9. Imaging acquisition, interpretation and endpoint control;
    10. Safety surveillance and adverse device event management;
    11. Data capture, source documentation and data-flow integrity;
    12. Regulatory compliance and deviation management.
  - 12 requisitos de desenho, DR1 a DR12 (Table 3.4). Os mais citados nas revisões:
    - DR1: sistema de qualidade explícito;
    - DR3: proficiência do operador como trajetória;
    - DR10: funções atribuídas, autoridade distinta da execução, nenhuma função CtQ dependendo de uma pessoa só, registro datado que sobrevive à saída de pessoas;
    - DR11: operável sem investimento, em papel;
    - DR12: profundidade escalável (Type A, B e C).
  - Quatro pilares: Governance, Risk Management, Operational Controls e Performance Oversight.
  - 24 instrumentos e um ciclo de vida de sete fases, com um fluxo transversal de segurança (Section 4.6).
- **Tipos de centro (Section 4.7, Table 4.3):** Type A é o hospital grande; Type B é a clínica ou o hospital médio, alvo do desenho, com implementação completa; Type C é o centro pequeno, com núcleo essencial.
- **Regra dos pilares (importante):** as seções 4.2 a 4.5 da tese descrevem os conceitos e não podem citar instrumentos específicos (siglas, remissões à 4.8, à Table 4.4 ou aos apêndices). Conceitos genéricos como "risk register", "delegation log" ou "complication log" podem e devem ficar. Não exagere na limpeza: o Felipe reclamou quando termos genéricos foram tirados.

### Os 24 instrumentos (ordem da Table 4.4 e dos apêndices A a X)

| Ap. | Sigla | Nome | Pilar |
|---|---|---|---|
| A | CCDM | Criticality-Coded Delegation Matrix | Governance |
| B | RACI | Responsibility Assignment Matrix | Governance |
| C | DTRM | Device and Study Training Requirements Matrix | Governance |
| D | TRE | Training Record Evaluation and Release | Governance |
| E | SCR | Surgical Credentialing Record | Governance |
| F | POT | PI Oversight Template | Governance |
| G | MRL | Milestone Review Log | Governance |
| H | SRR | Site Risk Register | Risk Management |
| I | SLCT | Surgeon Learning Curve Tracking Log | Risk Management |
| J | SCML | Site Complication Monitoring Log | Risk Management |
| K | SART | Safety and Adverse Effect Reporting Template | Risk Management |
| L | CSST | Complication Signal Surveillance Template | Risk Management |
| M | IMP | Internal Monitoring Plan | Operational Controls |
| N | IMC | Internal Monitoring Checklist | Operational Controls |
| O | SIRR | Site Imaging Readiness Record | Operational Controls |
| P | IQL | Imaging Quality Log | Operational Controls |
| Q | ICDL | Intraoperative Checklist and Device Log | Operational Controls |
| R | PSEAR | Participant Screening and Eligibility Assessment Record | Operational Controls |
| S | SIFSL | Subject Identification and Failure Screening Log | Operational Controls |
| T | PFVR | Participant Follow-up Visit Record | Operational Controls |
| U | FUCR | Follow-up Compliance Review | Operational Controls |
| V | PIR | Performance Indicator Record | Performance Oversight |
| W | CAPA | Corrective and Preventive Action Log | Performance Oversight |
| X | PIDLR | Post-Investigation Debrief and Lessons Record | Performance Oversight |

Há ainda o Appendix Y, com o modelo interativo do ciclo de vida.

## 2. Como trabalhar com o Felipe

- **Idioma:** responder em português. Todo texto acadêmico e todo conteúdo dos instrumentos é em inglês, com grafia americana.
- **Tom:** direto e honesto. Discorde quando houver razão e explique. Dê recomendação, não um catálogo de opções. Termine com as decisões que cabem a ele, numeradas e com a sua recomendação.
- **Quando ele está cansado**, ele diz e aprova em bloco ("aprovo tudo, segue tuas recomendações"). Nesse caso aplique as recomendações e mostre o resultado. Quando ele comenta item por item, aplique exatamente o que ele disse.
- **Entregas de instrumentos:**
  - Sempre duas versões, uma em branco (vai para o apêndice da tese) e uma simulada, preenchida com o exemplo de ombro (vai para a apresentação).
  - Primeiro o HTML. **PDF só quando ele pedir.**
  - Versão nova é arquivo novo (v0.x+1); a anterior fica preservada.
  - Antes de entregar, conferir página por página: nada cortado, nada vazando para os lados, cabeçalho em todas as páginas.
- **Arquivo Word da tese:** ele edita o .docx em paralelo. Antes de mexer no arquivo, peça que ele feche o Word sem salvar e faça backup; já houve sobrescrita.
- **Regras de escrita** (detalhes nas skills da pasta 03):
  - prosa simples, de nível B2 a C1, sem floreio;
  - sem travessão (em dash) nem meia-risca (en dash), sem exclamação e sem contrações;
  - "rather than" e os disfarces dele são proibidos ("instead of", "not X but Y", "X, not Y");
  - nada de listas de três por ritmo, de frase de abertura que só anuncia o parágrafo, de cauda que comenta a própria frase ("and this is what...") ou de oposição repetida como forma de argumentar;
  - frases que formam cadeia de consequência devem ser ligadas com conectivo, sem picotar;
  - o verbo acompanha a força da evidência;
  - nunca inventar número, fonte ou precisão.

## 3. A cadeia de Governance (decidida pelo Felipe)

Ordem de construção: **CCDM → DTRM → TRE → RACI**, com o **SCR** antes do TRE, para cirurgiões. O **POT** lê os registros e alimenta o **MRL**.

| Instrumento | Papel | Códigos e saídas |
|---|---|---|
| CCDM | Tarefas do estudo (T01, T02...), criticidade e supervisão. Não diz quem faz. | Criticidade C1 (PI-retained, não delegável), C2 (delegável dentro de limite, após liberação), C3 (rotina). Supervisão S0 (PI-retained), S1 (revisão ativa do PI ou especialista), S2 (supervisão definida), S3 (rotina). C1 só aceita S0; C2, S1 ou S2; C3, S2 ou S3. Cores: C1 vermelho, C2 laranja, C3 verde. |
| DTRM | Que treinamento cada perfil (P-01...) e cada tarefa exigem. Nunca depende do TRE. | TR Trained, AS Assessed (método na Seção D do DTRM), CD Conditional, AW Awareness, NA Not applicable. As letras foram escolhidas para não colidir com R/A/C/I. |
| SCR | Checagem de qualificação do cirurgião, não treinamento. Vem antes do TRE e entra no TRE, Seção B, como linha de qualificação. A liberação no dispositivo fica no TRE. | Credentialed / Conditional (temporário, com controles que terminam por critério) / Restricted (escopo mais estreito permanente) / Not credentialed. Reavaliação: Confirmed / Restricted / Suspended / Restored. |
| TRE | Registro individual: qualificação, treinamento, avaliação e liberação por tarefa do CCDM. Alimenta o RACI. | Released / Conditional / Not released. |
| RACI | Quem assume cada tarefa do CCDM (lista de delegação, junto com o CCDM) e quem é dono de cada um dos 24 instrumentos (em teste). | R/A/C/I e A/R (obrigatório nas tarefas C1). IDs das funções = perfis do DTRM (P-01 a P-07). Uma tarefa C2 ou C3 só recebe R se titular e backup tiverem liberação no TRE. Registro de titulares em log com folha de continuação; revisão por evento, sem data agendada. |
| POT | Parte 1, plano: decisões reservadas ao PI, oito gatilhos de escalonamento, reuniões. Parte 2, registro de cada revisão: lê SRR, PIR, FUCR, IMC, SART e SCML e as escalações. | Decisão por fonte: No signal / Monitor / Action routed / Escalated. Conclusão: No action needed / Actions routed / Escalated to the sponsor / Hold. Ações vão para o registro dono, e a eficácia é verificada só na CAPA. |

## 4. O processo de revisão (skill `instrument-review`)

Os passos e os critérios completos estão em `03_Skills_e_regras/instrument-review/SKILL.md`. Em resumo:

1. **Ler o que o texto da tese exige.** É o passo principal. Use as versões antigas e detalhadas do Chapter 4 (mais ricas) e a versão atual dos Chapters 3 a 5. Extraia requisitos numerados com a fonte de cada um: o que deve ser feito, as dificuldades que o texto nomeia, gatilhos, cláusulas e limites. Grave em `requirements/<SIGLA>.md`.
2. **Ler as referências secundárias:** a linha da Table 4.4, a camada na Figure 4.3, as marcas nas Figuras 4.4 (CtQ) e 4.5 (DR).
3. **Ler o HTML inteiro e ver cada página**, procurando conteúdo cortado.
4. **Cobertura:** cada requisito recebe COBERTO, PARCIAL ou FALTANDO, com o lugar no instrumento e a mudança proposta.
5. **Critérios:**
   - T1 a T9: coerência com a tese;
   - D1 a D6: dependências e alimentações;
   - P1 a P6: praticidade;
   - I1 a I5: coerência interna;
   - V1 a V7: visual.
6. **Ligações nos dois sentidos** com os outros instrumentos.
7. **Regras comuns** (`standards.md`).
8. **Relatório em português**, num HTML com veredito, pontos fortes, cobertura, critérios, mudanças por gravidade, consequências para outros instrumentos, mudanças sugeridas na tese, decisões para o Felipe e regras comuns propostas.

**Gravidade:** B bloqueante (contradiz a tese ou uma regulação, ou quebra a cadeia), I importante, M menor. **Veredito:** qualquer B dá BLOCKED; qualquer I dá NEEDS REVISION; só M dá READY AFTER MINOR CHANGES; nenhum dá READY.

Não edite o instrumento sem que o Felipe peça. Quando ele aprova, faça a nova versão (em branco e simulada), confira as páginas e mostre.

## 5. Preferências de desenho de formulário (aprendidas nas revisões)

- **Cabeçalho em todas as páginas,** no formato "SIGLA - Full Name", com subtítulo da página e a marca "BLANK / SIMULATED · v0.x". Rodapé "SIGLA v0.x | conteúdo da página" e "Page n of N".
- **A Seção A é sempre "Purpose and use":** texto curto e objetivo, mais uma tabela Element / Content / Record-link com as linhas Unit of analysis, Decision supported, Inputs e Outputs.
- **Versão em branco:**
  - deixa vazio o conteúdo próprio do centro: IDs, funções e limites;
  - só fica impresso o que é universal do framework, como a linha do PI, os quatro julgamentos do PI e os oito gatilhos de escalonamento.
- **Opções:**
  - as mesmas opções em todas as linhas de uma tabela, com N/A como opção quando algo não se aplica;
  - no campo de achado que não precisa de nota, escreve-se N/A, sem repetir o check.
- **Códigos e colunas:**
  - regras de códigos em tabela compacta ligada aos códigos, nunca em lista de bullets numa caixa;
  - cores distintas por código;
  - colunas separadas para dados distintos (por exemplo, código e supervisão);
  - cabeçalhos por extenso ("Accountable", não "A").
- **Espaço para escrever:** linhas altas o bastante para escrever à mão e uso do espaço até o rodapé. Assinatura simulada com cara de assinatura (fonte manuscrita), com a data separada.
- **Assinaturas:**
  - padrão: duas caixas, "<Documento> owner" e "PI / accountable approver", cada uma com "Name / role" e "Signature / date";
  - registros individuais (TRE, SCR): avaliador, PI e a pessoa avaliada (o TRE acrescenta o supervisor).
- **Folhas de continuação** depois da assinatura, com cabeçalho que liga a folha ao registro aprovado (ID, revisão, data efetiva, folha n de N).
- **O que não usar:** opção "Combined", tabela de revisão compensatória e caixa de revisão agendada em documentos disparados por evento.

## 6. O universo do exemplo simulado (manter coerente em todos os instrumentos)

| Item | Valor |
|---|---|
| Estudo | GLENOS-01 / GS-2026-01; dispositivo GLENOS reverse shoulder system, IFU v2.0; CIP v4.2 |
| Centro | Riverside Orthopedic Center / 014 (Type B) |
| Pessoas (Role ID do DTRM / RACI) | P-01 PI Dr Alex Morgan (TRE-014-01). P-02 cirurgião: titular Dr Lina Costa (senior shoulder surgeon, TRE-014-02) e backup Dr Paulo Teixeira (TRE-014-03, liberação condicional no T03; SCR-014-03 condicional, cinco primeiros casos com proctoring da Dr Costa). P-03 OR nurse / device custodian: Sofia Mendes; backup Tiago Nunes, que saiu em 8 Oct, substituído por Inês Rocha (TRE-014-13) a partir de 9 Oct. P-04 radiology liaison (perfil DTRM "Radiographer"): Helena Duarte; backup Pedro Lopes, que a cobriu de 6 a 17 Oct. P-05 functional assessor: Ana Ribeiro (TRE-014-11, liberada para T06 em 30 Sep 2026); backup Jamie Park (physiotherapy lead, TRE-014-12). P-06 study coordinator: Maria Silva (dona do CCDM e do RACI). P-07 data QA: Tomás Ferreira. |
| Tarefas do CCDM (CCDM-014 v0.2, efetivo em 30 Sep 2026) | T01 Final eligibility decision (C1/S0); T02 Final clinical safety classification and causality (C1/S0); T03 Reverse shoulder arthroplasty per surgical technique (C2/S1+S2); T04 Implant identification and substitution record (C2/S2); T05 Postoperative radiographs per imaging charter (C2/S1+S2); T06 ROM measurement and PROM administration (C2/S2); T07 Follow-up scheduling and window tracking (C3/S3); T08 eCRF transcription and data filing (C3/S3); T09 Device accountability, returns and explants (C2/S1+S2); T10 Safety intake and initial reporting route (C2/S2) |
| Registros | DTRM-014-2026-02 v0.2; RACI-014 r2 (dona assina em 29 Sep, PI em 30 Sep); SCR-014-03 r1 (25 Sep); POT-014 v0.2 (30 Sep; revisão mensal POT-014-R-2026-10 em 6 Oct; próxima em 3 Nov); SRR-014 v0.3 (riscos SRR-014-12 e SRR-014-13); MRL-014-M2 (marco dos primeiros casos incluídos) |
| Eventos | PD-014-07: substituição de baseplate glenoidal não escalonada, que gerou a CAPA-014-2026-003, a revisão do CCDM para v0.2, uma reciclagem no DTRM e o POT v0.2. SART-014-002: fratura de tubérculo maior no caso 2 do Dr Teixeira, fixada no intraoperatório, relacionada ao procedimento e não ao dispositivo, não grave. |

## 7. Estado atual (25/10/2026)

| Instrumento | Versão | Estado |
|---|---|---|
| CCDM | v0.2 (revised) | Pronto, com PDFs |
| DTRM | v0.2 | Pronto, com PDFs |
| TRE | v0.4 | Pronto, com PDFs; v0.3 preservada |
| RACI | v0.3 | Pronto, com PDFs; v0.2 preservada |
| SCR | v0.5 | Pronto (aceito pelo Felipe), com PDFs; v0.4 preservada |
| POT | v0.9 | Em branco e simulada feitas com todas as propostas da revisão, aguardando a avaliação do Felipe; v0.8 preservada |
| MRL | ainda não revisado | Próximo da fila: último de Governance |
| Os outros 17 | não revisados | Ordem sugerida: Risk Management (SRR, SLCT, SCML, SART, CSST), Operational Controls, Performance Oversight |

### Pendências registradas

- **TRE:** a "mudança 3" (tratar o SCR além da nota na Seção B) ficou para depois, por decisão do Felipe. Opcional: na linha do SCR da Seção B, usar as quatro saídas do SCR em vez de "Suitable / Gap".
- **DTRM:** o perfil P-04 se chama "Radiographer", enquanto a função da tese é "radiology liaison". O DTRM não foi alterado.
- **CCDM:** alinhar a coluna de gatilhos de escalonamento com os oito gatilhos do POT.
- **Futuras revisões:**
  - MRL: receber do POT os "items carried to the next MRL milestone";
  - CAPA: único lugar de verificação de eficácia;
  - SRR: proposta de um "CtQ profile of the investigation" no início, ainda não decidida (ver o item 8), e conferir se a lista de domínios do rascunho bate com a Table 3.2;
  - SLCT e CSST: as saídas devem chegar como gatilho à reavaliação do SCR;
  - ICDL: checagem do cirurgião antes de cada caso contra o SCR e o TRE.
- **Tese, mudanças opcionais sugeridas:**
  - Table 4.4, linha B (RACI): Inputs passam a ser "The CCDM task list, the DTRM role profiles, and each person's TRE release";
  - linha E (SCR): "prior training";
  - linha F (POT): acrescentar as escalações vindas do CCDM, do SCR e do RACI;
  - frase na 3.3 dizendo que os domínios CtQ são um vocabulário fixo e que o centro liga a eles os CtQ factors do patrocinador.
- **Regras comuns:** S17, S18, S19 e S21 estão propostas e não aprovadas; S20 foi aprovada. Ver `standards.md`.

## 8. Decisões conceituais importantes (e por quê)

- **Os 12 são domínios CtQ do centro, não os CtQ factors do estudo.** Os factors são do patrocinador (ICH E8(R1)), e o centro não refaz essa análise, porque duplicaria o patrocinador e não teria recursos para isso. O centro prioriza os domínios para a investigação e acha os seus riscos dentro deles. A recomendação é manter os 12 como estrutura fixa e criar no SRR um perfil de CtQ: os CtQ factors do patrocinador ligados aos domínios, a relevância de cada domínio e uma linha "Unmapped factor" para o que não couber, sem criar domínios novos. A justificativa dos domínios é a derivação rastreável (2.2.2 e 3.3); o ponto fraco é que não houve validação externa. Para reforçar, foram sugeridos cruzamentos com os 18 itens da ICH E8(R1) e com exemplos do CTTI e do MDIC.
- **Lógica de governance e não prescritiva:** os instrumentos de Governance já mostram desenho pelo centro, proporcionalidade e gatilhos. O "aprender" sistemático fica nos instrumentos de Risk Management e de Performance Oversight, ainda não revisados. Os campos de julgamento (incerteza residual no SCR, escopo condicional no TRE, gatilhos no CCDM) devem ser protegidos.
- **Uma ação, um dono (S21, proposta):** ações levantadas em qualquer instrumento são encaminhadas ao registro dono, e só a CAPA verifica eficácia.

## 9. Como os arquivos foram produzidos (para referência)

Os instrumentos são HTML de página A4 (retrato ou paisagem, com `main.page`). Têm um script "Modo editor" que permite editar no navegador e não sai na impressão. O Claude gerou as versões com scripts Python e imprimiu os PDFs com o Chrome headless. Se você produzir HTML, mantenha o mesmo padrão visual: barra azul-marinho #1f4173, cabeçalhos de seção numerados por letra, tabelas com cabeçalho azul #3478ad e texto simulado em fonte manuscrita azul.
