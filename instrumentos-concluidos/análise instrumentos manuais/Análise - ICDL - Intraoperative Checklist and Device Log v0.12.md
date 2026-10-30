# Análise — ICDL: Intraoperative Checklist and Device Log v0.12

**Tipo de documento:** análise manual para orientar uma futura revisão do HTML.  
**Fonte analisada:** `ICDL_Intraoperative_Checklist_and_Device_Log_v0.12.html` (versão de trabalho fornecida na sessão).  
**Escopo desta análise:** arquitetura, fluxo operacional, interfaces com SLCT e PIR e ajustes mínimos recomendados. **Não é uma instrução para redesenhar o instrumento.**

---

## Conclusão executiva

O **ICDL v0.12 está estruturalmente maduro e substancialmente alinhado com a tese**. Ele funciona como o registro contemporâneo de **um procedimento de um participante**, preservando no momento em que ocorre:

- a liberação pré-procedimento;
- os passos técnicos críticos;
- os tempos do procedimento;
- a rastreabilidade e reconciliação dos componentes/dispositivo;
- desvios, substituições e eventos intraoperatórios;
- a revisão pós-procedimento e o fechamento do caso;
- o handoff para os registros especializados e a revisão accountable.

A tese posiciona o ICDL no nível de **registro individual do evento/procedimento**. O **SLCT** revisa posteriormente uma sequência de casos de um mesmo cirurgião; o **PIR** produz a síntese por cirurgião e período. Esses três instrumentos não devem ser fundidos nem repetir narrativas uns dos outros.

**Decisão recomendada:** produzir apenas uma versão de microajustes — por exemplo, v0.13 — preservando integralmente a arquitetura, as onze seções, a identidade visual e a paginação atual. Não reconstruir o formulário.

---

## 1. O que deve permanecer como está

### Estrutura clínica e operacional

| Seção | Avaliação | Decisão |
|---|---|---|
| **A — Scope, decision and interfaces** | Define corretamente a unidade de análise, decisão, entradas e saídas. | Manter; somente atualizar as rotas de saída listadas. |
| **B — Pre-procedure Release-to-Start and Critical Controls** | É um gate operacional legítimo, não redundância. Confirma autorização, identificação, elegibilidade, disponibilidade/compatibilidade do sistema, condição estéril e materiais de imagem ou mensuração. | Manter. |
| **C — Critical Technique Checklist** | Limita-se corretamente aos passos técnicos críticos e evita reproduzir toda a nota operatória. | Manter. |
| **D — Procedure Time Points and Operating Conditions** | Já capta os marcos necessários para derivar duração operatória. | Manter; acrescentar apenas o handoff mínimo para SLCT. |
| **E — Device Accountability and Component-Level Traceability** | É forte e proporcional ao contexto de dispositivo médico: UDI, lote/série, disposição, configuração final e reconciliação. | Manter. |
| **F — Technical Deviation, Substitution and Exception Route** | Registra o fato técnico, causa, impacto e rota sem substituir a classificação formal de desvio definida pelo CIP. | Manter. |
| **G — Intraoperative Complications and Device Performance** | Diferencia adequadamente evento/deficiência de segurança da exceção técnica e encaminha ao registro de safety aplicável. | Manter. |
| **H — Immediate Post-procedure Review** | Faz a ponte necessária entre o registro intraoperatório, a nota operatória, accountability, imagem e rotas de segurança/desvio. | Manter; fazer uma precisão pontual sobre configuração/posição. |
| **I — Case Closure Decision** | Possui lógica de fechamento adequada: `Complete`, `Complete with open action` e `Hold`. | Manter. |
| **J — Open Action, Escalation and Effectiveness Follow-up** | Preserva ownership, destino, prazo e evidência de efetividade sem se tornar um segundo CAPA Log. | Manter. |
| **K — Accountable Review, Approval and Controlled Record Location** | Fecha corretamente com autoria, revisão cirúrgica/PI quando requerida e localização controlada. | Manter; acrescentar referência ao SLCT no texto de linkage. |

### Granularidade e separação de responsabilidades

Manter as seguintes fronteiras:

- **ICDL:** registro de um caso/procedimento, preenchido no ponto de cuidado.
- **SLCT:** revisão longitudinal de casos comparáveis de um mesmo cirurgião.
- **PIR:** síntese de performance por cirurgião e período de revisão.
- **SCML/SART:** evento de complicação, efeito adverso, deficiência de dispositivo e suas rotas de segurança.
- **Registro formal de desvio definido pelo CIP:** classificação autoritativa de protocol deviation.
- **Device accountability record e operative note:** registros autoritativos para seu conteúdo próprio; o ICDL captura o que é registrado primeiro nele e faz a reconciliação/referência necessária.

Não adicionar ao ICDL:

- classificação completa de safety ou de adverse event;
- tempos de notificação de safety;
- narrativa clínica longitudinal;
- classificação formal paralela de protocol deviation;
- um indicador agregado de device traceability;
- metas numéricas fixas de proficiência cirúrgica;
- um ranking de cirurgiões.

---

## 2. Base conceitual na tese

A tese define o ICDL como o registro intraoperatório de cada procedimento, necessário porque os dados produzidos na sala operatória não podem ser reconstruídos de modo confiável depois. Ele deve capturar os identificadores dos componentes implantados, os checks de etapas críticas, desvios ou substituições e a revisão imediata após a cirurgia.

A mesma tese separa os níveis de revisão:

```text
ICDL: caso/procedimento individual
          ↓
SLCT: sequência de casos do mesmo cirurgião
          ↓
PIR SP-01: síntese da consistência procedimental por cirurgião e período
          ↓
POT / SCR / SRR / CAPA: decisão de governança, autorização, risco ou resposta
```

A tese exige que cada caso que entra no learning curve record tenha, no mínimo:

- complexidade;
- duração;
- evento não planejado, como substituição de componente;
- necessidade de suporte sénior ou proctoring;
- ligação ao caso e à evidência associada.

Ela também define que o indicador de **Surgeon Procedural Consistency (SP-01)** considera em conjunto substituições não planejadas, desvios procedimentais, duração de casos comparáveis, suporte/proctoring, documentação de configuração e posição do implante e complicações técnicas precoces. Nenhum sinal isolado prova pior desempenho.

---

## 3. Ajustes prioritários recomendados

### MUST — 1. Tornar explícito o handoff por caso para o SLCT

**Problema:** o ICDL atual já fornece ICDL ID, procedimento, data, cirurgião, dispositivo, tempos, substituições, desvios e referências. Contudo, ele não expõe explicitamente:

1. o **nível de complexidade predefinido** do caso; e
2. se **suporte sénior/proctoring** foi utilizado como planejado, não planejado ou não utilizado.

Esses dois campos são necessários para que o SLCT compare casos equivalentes e interprete duração e eventos sem confundir case mix ou apoio planejado com drift técnico.

**Implementação mínima recomendada:** ao final da **Seção D — Procedure Time Points and Operating Conditions**, inserir uma pequena faixa ou linha adicional, sem abrir nova página e sem criar uma seção nova extensa:

```text
SLCT case handoff
• Pre-defined complexity level / source: ______________________________
• Senior support or proctoring:  □ None  □ Planned  □ Unplanned
• ICDL case reference / linked SLCT entry: ___________________________
```

**Limites de implementação:**

- Não criar uma tabela narrativa adicional.
- Não duplicar tempos: a duração é derivada de `Procedure start / first incision` e `Closure / procedure end` já existentes na Seção D.
- Não estabelecer número fixo de casos ou thresholds de proficiência.
- A definição do nível de complexidade vem da base predefinida para o SLCT; o ICDL apenas registra o nível aplicável ou sua fonte.

### MUST — 2. Declarar o SLCT como destinatário de saída

**Problema:** a Seção A lista vários outputs, mas não nomeia o SLCT. A Seção K também não o menciona no texto de system linkage.

**Implementação mínima recomendada:**

- Na linha **Outputs** da Seção A, acrescentar `SLCT case entry / reference` como saída quando aplicável.
- Na nota de **System linkage** da Seção K, acrescentar que os dados por caso de complexidade, duração, suporte, substituição e exceção alimentam a entrada correspondente no SLCT.

**Regra:** o ICDL fornece a referência e os flags do caso; não transfere ou repete toda a narrativa das Seções C, F, G ou H.

### SHOULD — 3. Tornar explícita a documentação de posição do implante

**Problema:** o ICDL contém configuração final, reconciliação e referência a imagem, mas a documentação da **posição** está implícita. O SP-01 precisa conseguir demonstrar se configuração e posição foram documentadas.

**Implementação mínima recomendada:** substituir ou complementar a primeira linha da Seção H com formulação que inclua posição, por exemplo:

> `Final implant configuration and position are documented in the operative note and linked image/source record.`

Ou, se for visualmente mais claro, usar duas linhas curtas:

1. `Final implant configuration is documented and reconciled.`
2. `Implant position is documented or linked to the required immediate postoperative image/source record.`

**Limites de implementação:**

- Não acrescentar interpretação radiológica ao ICDL.
- Não duplicar o IQL; registrar somente o status e a referência ao IQL/source record.

### SHOULD — 4. Corrigir a sigla ICQL para IQL

**Problema:** o ICDL usa a sigla antiga `ICQL` em três lugares:

- Outputs da Seção A;
- item de imagem pós-operatória na Seção H;
- nota de System linkage na Seção K.

**Implementação:** substituir `ICQL` por **`IQL — Imaging Quality Log`** de forma consistente.

### SHOULD — 5. Tornar a consequência dos estados negativos explícita

**Problema:** as opções `Partial`, `Not performed`, `Not acceptable` e `Not assessable` são adequadas, mas a conexão com F, J ou registro vinculado não está explicitada junto à tabela de técnica.

**Implementação mínima recomendada:** inserir abaixo da Seção C uma nota curta:

> `N/A requires a documented reason. Partial, Not performed, Not acceptable or Not assessable require a reference to Section F, Section J or an applicable linked record when they affect case closure, safety, traceability or data usability.`

Isso torna a lógica de fechamento auditável sem expandir a tabela central.

### SHOULD — 6. Padronizar N/A

**Problema:** a Seção B usa `N-A`, enquanto as demais usam `N/A`.

**Implementação:** usar **`N/A`** de forma uniforme em todas as seções. Não usar sinal de menos ou símbolo negativo.

### TECHNICAL REQUIRED — 7. Migrar para o Editor v2 sem alterar o visual

**Problema:** o ICDL v0.12 não contém o Editor v2 canônico adotado para os demais templates.

**Implementação:** anexar o Editor v2 completo — painel flutuante arrastável, multiseleção, fonte, estilo, dimensões de linhas/colunas, edição de boxes, caixas de escolha, undo e save — preservando:

- todas as seis páginas;
- as orientações retrato/paisagem existentes;
- as alturas de linha aprovadas;
- o visual, cores, cabeçalhos e rodapés atuais;
- as seções A–K e sua ordem;
- a densidade de informações das páginas 2 e 3 em paisagem.

**Regra essencial:** a migração do editor não autoriza reprojetar o documento.

---

## 4. Como o ICDL alimenta o SLCT

O SLCT deve receber apenas a chave e os sinais necessários para revisar a sequência de casos do **mesmo cirurgião**, sem copiar descrições completas do caso.

| Dado produzido ou confirmado no ICDL | Uso no SLCT | Forma de transmissão recomendada |
|---|---|---|
| ICDL Record ID, Participant/Case Code, procedure date, procedure/side, primary surgeon, device/system | Identifica e ordena o caso na sequência apropriada. | Uma linha de entrada do SLCT referencia o ICDL ID. |
| Complexity level | Permite comparar o caso apenas com casos do mesmo cirurgião e complexidade equivalente. | Novo handoff curto na Seção D; código ou fonte predefinida. |
| Procedure start e closure/procedure end | Permite derivar a duração operatória. | Duração derivada no SLCT; não criar outro campo de tempo no ICDL. |
| Component substitution, technical deviation, omission, repetition ou incerteza | Permite identificar padrões ou sinais precoces de drift. | Flag/categoria + referência à Seção F e ao registro formal quando aplicável. |
| Senior support/proctoring | Permite distinguir suporte planejado nos primeiros casos de suporte não planejado. | Novo campo curto: `None / Planned / Unplanned`. |
| Final configuration e posição documentadas | Permite demonstrar adequação documental no painel de consistência. | Status curto + referência a E/H e IQL/source record. |
| Complicação técnica precoce ou concern de device performance | Permite revisar o padrão junto ao SCML/complication review. | Link ao SCML/SART; sem repetir a descrição clínica no SLCT. |

### Regras para o SLCT

- O SLCT não deve copiar o texto narrativo de F, G ou H.
- O SLCT revisa padrões, não reabre o registro individual.
- Comparar cada caso com casos anteriores do mesmo cirurgião, para a mesma complexidade e considerando experiência com o dispositivo.
- Uma substituição isolada pode decorrer de disponibilidade, planejamento ou complexidade; não representa por si só falha de desempenho.
- Mudança de autorização, restrição de escopo ou necessidade de proctoring adicional retorna ao SCR/estrutura de governança, não é decidida pelo ICDL.

---

## 5. Como o ICDL alimenta o PIR

O destino principal do ICDL no PIR é o indicador:

> **SP-01 — Surgeon Procedural Consistency**

O PIR deve receber a **síntese do SLCT** e da revisão de complicações, mantendo o intervalo de ICDL IDs como trilha auditável. A unidade de análise é:

```text
um cirurgião + um período de revisão + procedimentos comparáveis
```

### Componentes do SP-01

| Componente do PIR SP-01 | Fonte principal | Papel do ICDL |
|---|---|---|
| Unplanned component substitution | ICDL F, sintetizado no SLCT | Identifica e referencia a substituição por caso. |
| Technical or protocol-relevant deviation | ICDL F + registro formal de deviation | Detecta e referencia; não substitui a classificação autoritativa. |
| Operative duration by comparable case type | ICDL D, analisado pelo SLCT | Fornece os marcos temporais. |
| Senior assistance or proctoring | Handoff novo do ICDL + SLCT | Registra o suporte efetivamente utilizado. |
| Implant configuration / position documentation adequacy | ICDL E/H + IQL/source record | Demonstra status de documentação e referência. |
| Early technical complication pattern | SCML/complication review, ligado ao ICDL | Faz a conexão do caso individual à revisão de complicações. |

### Contribuições secundárias do ICDL ao PIR

1. **PD-01 — Protocol Deviation Rate**
   - Contar apenas desvios procedimentais classificados no registro formal definido pelo CIP.
   - A Seção F do ICDL é detecção e referência; não criar uma taxa paralela baseada apenas nela.
   - Denominador específico: procedimentos aplicáveis no período.

2. **DC-01 — Critical Data Completeness**
   - O ICDL referencia a nota operatória e pode confirmar reconciliação.
   - A medida de notas finalizadas dentro do prazo deve usar a fonte/timestamp da nota operatória; o horário de encerramento do ICDL não substitui esse timestamp.

### Não criar indicadores adicionais no PIR

Não criar um indicador autônomo de UDI, componente, lot/serial ou device traceability. A tese define um conjunto pequeno de indicadores; rastreabilidade é um controle/reconciliação do ICDL e da accountability, verificável por IMC quando necessário.

---

## 6. Instrução de implementação para a próxima IA

1. Começar a partir do **ICDL v0.12 atual**; não reconstruir a partir de outro template.
2. Aplicar exclusivamente os sete ajustes desta análise.
3. Preservar todas as seções, sua ordem, as páginas em paisagem, os rodapés e a identidade visual existente.
4. Não remover B, C, D, E, F, G, H, I, J ou K.
5. Não mover conteúdo de safety, deviations, accountability, imaging ou CAPA para dentro do SLCT ou PIR.
6. Não adicionar thresholds fixos de proficiência, metas de número de casos ou comparações/rankings entre cirurgiões.
7. Validar o HTML impresso em A4 após o ajuste, sem conteúdo ultrapassar o rodapé.
8. Validar que o Editor v2 está operacional em células, caixas, tabelas e elementos de seleção sem alterar a geometria do formulário quando o modo editor estiver desligado.
9. Gerar primeiro apenas o HTML em branco editável. Não gerar PDF ou versão preenchida nesta fase, salvo pedido posterior do autor.

---

## 7. Checklist de aceitação da próxima versão

- [ ] O ICDL continua claramente sendo um registro de **um procedimento**.
- [ ] A Seção D contém complexidade e suporte/proctoring em formato curto e utilizável pelo SLCT.
- [ ] A lista de outputs e o System linkage mencionam o SLCT quando aplicável.
- [ ] A Seção H confirma configuration **and position** documented, sem duplicar o IQL.
- [ ] Todas as menções a `ICQL` foram corrigidas para `IQL`.
- [ ] `N/A` está uniforme em todo o documento.
- [ ] A nota sob C torna rastreável a consequência de estados negativos.
- [ ] O Editor v2 está incorporado e funcional.
- [ ] Nenhuma seção clínica, tabela central, área de assinatura ou rota de safety foi removida ou redesenhada sem autorização.
- [ ] A impressão A4 preserva as seis páginas, com segurança de rodapé e páginas 2–3 em paisagem.

---

## Fontes verificadas nesta análise

- Tese completa, especialmente as seções sobre operator-dependent risk and learning curve (4.3.2), intraoperative data capture, surgeon procedural consistency (4.5.5) e critical data completeness (4.5.6).
- `ICDL_Intraoperative_Checklist_and_Device_Log_v0.12.html`.
- `Performance_Indicator_Record_v0.8_filled_demo.html`, para confirmar a estrutura atual do SP-01 e do DC-01.
- Requisito interno já registrado: `materiais/2026-10-25/03_Skills_e_regras/instrument-review/reference/requirements/ICDL.md`.
