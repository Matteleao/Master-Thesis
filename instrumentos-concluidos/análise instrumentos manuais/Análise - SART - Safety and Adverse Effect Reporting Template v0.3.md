# Análise — SART: Safety and Adverse Effect Reporting Template v0.3

**Tipo de documento:** análise manual para orientar uma futura revisão do HTML.  
**Fonte analisada:** `SART_Safety_and_Adverse_Effect_Reporting_Template_v0_3_edited_2026-09-21_23-29-58.html`.  
**Escopo desta análise:** estrutura do caso individual de segurança, fluxo de dados para SCML, CSST e PIR e ajustes mínimos recomendados. **Não é uma instrução para redesenhar o instrumento ou inventar uma nova taxonomia regulatória.**

---

## Conclusão executiva

O **SART v0.3 está conceitualmente forte** e já reflete o papel definido na tese: acompanhar **uma ocorrência de segurança, uma device deficiency observada ou uma nova informação material**, desde a abertura até o fechamento controlado.

Ele já faz corretamente o que um registro individual de safety deve fazer:

- abre o caso no momento da awareness, sem esperar classificação completa;
- separa fato observado de classificação e de relação causal;
- mantém as vias de AE e device deficiency independentes e simultâneas quando necessário;
- registra medidas de proteção imediata antes de qualquer conclusão final;
- documenta rota de comunicação, reconciliação, follow-up cronológico e fechamento;
- referencia SCML, CSST, CAPA, SRR, PIR e PI oversight sem substituir os registros que são autoritativos para cada função.

A tese é igualmente clara: **SCML indexa os eventos e suas rotas; SART acompanha o caso individual; CSST analisa contagens e sinais agregados; PIR mede a timeliness e a completude do processo de safety reporting.**

**Decisão recomendada:** manter as seções A–H, a sequência geral e a capacidade de narrativa. A revisão deve ser focal e resultar em um SART v0.4, não em uma reconstrução. O ajuste mais importante é deixar explícitos os dados que permitem calcular a **Safety Reporting Timeliness (ST-01)** no PIR e separar melhor os handoffs para SCML, CSST, PIR e deviation record.

---

## 1. O que deve permanecer como está

| Seção | Avaliação | Decisão |
|---|---|---|
| **A — Case opening, scope and immediate factual record** | Unidade de análise, decision support, inputs e outputs estão adequadamente declarados. | Manter. |
| **B — Initial case facts, detailed facts and device/procedure context** | A abertura por facts, a data de ocorrência e a data de awareness são essenciais. A separação entre fato, fonte e informação ausente é adequada. | Manter. |
| **C — Independent classification axes e relationship assessment** | A separação entre AE, DD, seriousness, anticipated/expected status e fatores de relação é correta. O caso AE + DD pode seguir as duas vias, coerente com a tese e ISO 14155:2026. | Manter a estrutura; atualizar terminologia apenas após fonte controlada. |
| **D — Immediate protection and containment actions / escalation gates** | Coloca proteção do participante, contenção do dispositivo e comunicação imediata antes do fechamento. | Manter. |
| **E — Communication, notification and reconciliation** | O registro de `Date/time known`, `Sent/transmitted`, `Receipt/reference` e das fontes vinculadas é uma base boa para rastreabilidade. | Manter; adicionar um pequeno controle estruturado de timeliness/completude. |
| **F — Follow-up chronology and outcome** | Preserva a cronologia e evita sobrescrever a informação anterior. É particularmente apropriado para casos de safety. | Manter. |
| **G — Final assessment, outputs and controlled closure** | Tem gates de fechamento claros e reconhece que o closure local não substitui decisão do sponsor, EC, CEC ou autoridade. | Manter; tornar os destinatários de saída mais específicos. |
| **H — Accountable review, signatures and controlled location** | Garante autoria, revisão accountable e localização controlada do caso. | Manter. |

### Estrutura visual

A distribuição em **11 páginas** é aceitável para um caso individual que pode se estender por dias ou semanas. Não comprimir o instrumento apenas para reduzir páginas:

- páginas 3–8 em paisagem são justificadas para classification, relationship, action, communication e reconciliation;
- páginas 7, 9 e 10 têm espaço livre útil para os pequenos controles propostos abaixo, sem criar novas páginas;
- páginas 10 e 11 possuem áreas amplas que favorecem closure e assinatura manuscrita.

Não remover espaço narrativo de B, F, G ou H para tornar o documento artificialmente curto.

---

## 2. Fluxo correto na arquitetura da tese

```text
Uma ocorrência, DD observada ou nova informação material
                         ↓
SART: abertura, proteção, classificação, comunicação, follow-up e closure
                         ↓
SCML: índice do evento e perfil de vigilância entre casos
                         ↓
CSST: contagens, taxas, distribuição e decisão de sinal por período
                         ↓
SLCT / SRR / CAPA / POT: rota conforme o padrão identificado

Em paralelo:
SART: awareness, reportabilidade, prazo CIP, envio, completude e follow-up
                         ↓
PIR ST-01: Safety Reporting Timeliness por período
```

### Papéis que não podem se confundir

| Instrumento | Papel | O SART deve fazer? |
|---|---|---|
| **SART** | Segue um caso individual da abertura ao fechamento. | Sim. |
| **SCML** | Indexa eventos e sua rota, sem copiar narrativa clínica. | O SART fornece SART ID/event reference, status e links. |
| **CSST** | Conta categorias, distribuições por componente/cirurgião e decide se há sinal agregado. | O SART é fonte individual; não deve calcular taxa ou concluir sinal. |
| **PIR ST-01** | Mede se cada evento reportável foi comunicado no prazo CIP, com primeiro reporte completo e follow-up no prazo. | O SART fornece campos estruturados por caso reportável. |
| **Deviation record** | Mantém a classificação formal de um atraso/erro de processo conforme CIP. | O SART deve referenciar quando houver late initial notification. |
| **CAPA / SRR** | Trata recorrência de falha de processo ou risco local. | Não abrir automaticamente por um caso isolado. |

---

## 3. Ajustes prioritários recomendados

### MUST — 1. Criar um controle estruturado de Safety Reporting Timeliness

**Problema:** a Seção E já registra `Date/time known`, `Sent/transmitted` e receipt/reference. Porém, ela não torna explícitos, por caso:

- se o caso é reportável dentro do escopo do CIP;
- qual regra/janela do CIP foi aplicada;
- qual era a data/hora de vencimento;
- se a initial notification foi enviada dentro da janela;
- se o primeiro reporte estava completo;
- se a informação de follow-up foi entregue no prazo;
- se o caso permanecia aberto no cut-off da revisão.

Sem esses campos estruturados, o PIR consegue recuperar a informação por leitura manual, mas não consegue reconciliar facilmente o denominador e os componentes de **ST-01 — Safety Reporting Timeliness**.

A tese define que o ST-01 mede, para cada evento reportável:

1. initial notification to sponsor dentro do intervalo do CIP, a partir de awareness do site;
2. completude do first report;
3. informação de follow-up no prazo;
4. casos ainda abertos ao final do período.

**Implementação mínima recomendada:** inserir ao final da página 7, usando o espaço livre existente, uma tabela curta chamada:

> **CIP Timeliness and First-Report Control**

Campos recomendados:

| Campo | Conteúdo esperado |
|---|---|
| Reportable under current CIP / procedure? | Yes / No / Pending, com referência à regra aplicável. |
| Site awareness date/time | Referência ao campo de awareness da Seção B. |
| Applicable CIP reporting window / due date-time | Regra e vencimento calculado/documentado. Não hard-code prazo universal. |
| Initial notification sent date/time | Referência à linha de comunicação para sponsor. |
| Initial notification timely? | Yes / No / Pending / N/A. |
| First report complete? | Complete / Incomplete / Pending / N/A. |
| Follow-up information due / sent / timely? | Referência ou status resumido; detalhes continuam na Seção F. |
| Case open at review cut-off? | Yes / No, com data de corte quando aplicável. |

**Limites de implementação:**

- Não inserir prazos fixos de 24 horas, 7 dias ou qualquer outro valor universal.
- O prazo aplicável deve sempre vir do **CIP, sponsor safety procedure ou regra local controlada**.
- Não substituir a tabela de comunicações existente; o novo controle é uma síntese auditável dos dados que ela já sustenta.
- Não transferir para o SART os prazos sponsor-to-authority, que não fazem parte do processo site-to-sponsor do PIR.

### MUST — 2. Separar os destinatários SCML, CSST, PIR e deviation record no handoff

**Problema:** a Seção G combina `SCML / CSST signal review` em uma única saída e usa `PIR or PI Oversight communication` como outra. Isso pode induzir a dois erros:

1. tratar o CSST como uma rota individual obrigatória de cada caso, quando ele é a revisão agregada de eventos por período ou trigger; e
2. não registrar de modo específico que uma **late initial notification** deve ir ao deviation record, como a tese estabelece.

**Implementação mínima recomendada:** reestruturar apenas a tabela `Outputs and handoff` da Seção G, sem alterar o resto do instrumento. Usar linhas distintas:

| Saída / interface | Uso correto |
|---|---|
| **SCML Event ID / indexed case reference** | Registrar o ID da entrada do índice para cada SART aplicável. É a ligação da fonte individual ao log agregado. |
| **CSST review period / signal reference** | Registrar o período, review ID ou trigger em que o caso entra na análise agregada; não tratar como notificação individual imediata. |
| **PIR ST-01 source reference** | Apenas para casos reportáveis: registrar a referência do SART e seu status de timeliness/completude. |
| **Deviation record, if initial notification late** | Obrigatório quando houver late initial notification; aplicar critérios do sponsor/CIP para importância. |
| **CAPA or SRR review** | Somente para falha recorrente, padrão de processo ou risco local identificado. |
| **POT / PI oversight communication** | Quando o caso, o atraso ou o padrão requer decisão de oversight. |
| **Controlled local case closure** | Closed / Open follow-up / Transferred, preservando a lógica atual. |

### SHOULD — 3. Tornar explícito o caso sem participante ou sem procedimento

**Problema:** o SART pode ser aberto para uma device deficiency observada, uma nova informação material ou outra ocorrência que não esteja ligada a um participante individual. Contudo, o cabeçalho atual contém `Participant code` e `Procedure / visit / phase` sem explicar a condição de não aplicabilidade.

**Implementação mínima recomendada:** alterar os rótulos para:

```text
Participant code / N/A reason
Procedure / visit / phase / N/A context
```

Ou acrescentar uma nota curta na Seção A:

> `For a deficiency or new information not associated with an enrolled participant, enter N/A and state the device, inventory, procedure or information context that identifies the case.`

Isso evita inventar um participant code e preserva rastreabilidade para DD sem AE.

### SHOULD — 4. Explicitar a relação entre o atraso e sua causa operacional

A tese exige que, quando haja late or incomplete reporting, o site identifique em que etapa ocorreu o atraso: reconhecimento, escalonamento interno, avaliação do investigador, acesso à documentação ou transmissão.

O SART atual permite registrar essa informação narrativamente, mas não a coloca em uma estrutura recuperável para correção direcionada.

**Implementação mínima recomendada:** quando `Initial notification timely? = No`, inserir no mesmo controle de timeliness uma linha curta:

```text
Delay point: □ Recognition  □ Internal escalation  □ PI assessment
             □ Documentation access  □ Transmission  □ Other: ______
Immediate correction / linked deviation record: ______________________
```

Não adicionar essa linha aos casos timely.

### SHOULD — 5. Atualizar o Editor para o Editor v2 canônico

O SART possui um editor próprio legado, mas não o Editor v2 canônico adotado para os demais templates. A próxima versão deve receber o Editor v2 completo, incluindo painel flutuante arrastável, multiseleção, edição de fonte/estilo, ajustes coletivos de linhas e colunas, edição de boxes e caixas de seleção, undo e save.

**Regra:** a migração técnica do editor não autoriza modificar a estrutura, página, cores, seções ou áreas de escrita do SART.

---

## 4. Dependência aberta: terminologia da ISO 14155:2026

A Seção C atual já tem a arquitetura correta para lidar com a mudança de classificação dos eventos em device trials:

- AE e device deficiency avaliados separadamente;
- AE associado a DD segue as duas vias;
- seriouness, anticipated/expected status e relações são avaliados de forma independente;
- incerteza é preservada como `Not yet determined`, em vez de impor conclusão precoce.

A tese confirma essas premissas. Contudo, o próprio autor informou que o SART deve ser o último instrumento a receber atualização terminológica definitiva, após fornecimento da documentação específica sobre a ISO 14155:2026.

**Decisão para a próxima IA:**

- não substituir nem redefinir `AE`, `ADE`, `SADE`, `DD`, `seriousness`, `anticipated/unanticipated` ou `expectedness` com base em suposição;
- preservar por enquanto a nota `Controlled taxonomy required` e a referência ao CIP, risk information e sponsor procedures;
- quando o autor fornecer a documentação da ISO 14155:2026, atualizar somente os rótulos e as regras necessárias na Seção C e nos escalation gates, mantendo a arquitetura de eixos independentes.

A lacuna atual é de **fonte terminológica controlada**, não de desenho do fluxo de safety.

---

## 5. Interação detalhada com SCML, CSST e PIR

### SART → SCML

O SART é a fonte individual. O SCML não deve copiar a narrativa clínica, as decisões de comunicação ou a cronologia inteira do caso.

O SART deve transmitir ao SCML:

- SART Case ID / event reference;
- participant code ou N/A context;
- event term/source term;
- date of event e timing relativo ao procedimento, quando aplicável;
- device/component and ICDL/imaging references, quando aplicável;
- current event type: AE, DD without AE, AE + DD ou pending;
- relationship context and DD status atuais;
- status de assessment: pending, preliminary ou final.

A atualização de informação nova ocorre no SART. O SCML atualiza apenas a entrada de índice/profiling correspondente.

### SCML → CSST

O CSST é o local onde o site conta eventos por categoria, componente e cirurgião, compara com procedimentos e decide se existe sinal. Não colocar denominadores, taxas ou decisão de sinal dentro do SART.

Um caso individual no SART pode:

- entrar na próxima revisão programada do CSST;
- disparar uma revisão antecipada se for sério ou se fizer parte de um cluster;
- ser referenciado em um signal review, mas não produzir sozinho uma conclusão agregada.

### SART → PIR ST-01

O PIR recebe do SART somente dados de processo de safety reporting, não a narrativa clínica inteira:

| Elemento para ST-01 | Campo fonte no SART após microajuste |
|---|---|
| Denominador: reportable events in period | `Reportable under current CIP / procedure?` e data de awareness/cut-off. |
| Initial notification timely | Awareness, due date/time, sent date/time e status `timely`. |
| First report complete | Status estruturado `Complete / Incomplete / Pending`. |
| Follow-up information on time | Due/sent/timely status e referências na Seção F. |
| Open cases at cut-off | `Case open at review cut-off?` e closure/follow-up status. |
| Causa do atraso | Delay point estruturado, quando aplicável. |
| Correção e desvio | Linked deviation record e action/reference. |

O PIR calcula e interpreta os resultados por período. O SART apenas preserva o caso e seus dados auditáveis.

---

## 6. O que não deve ser alterado na próxima versão

- Não transformar o SART em log populacional ou registro agregado.
- Não substituir o SCML, CSST ou PIR.
- Não remover as páginas de facts, classification, relationship, action, notification, reconciliation, follow-up, closure ou assinatura.
- Não condensar páginas à custa de espaço de escrita ou da sequência cronológica.
- Não criar uma timeline regulatória universal dentro do template.
- Não hard-code uma lista universal de critérios de seriousness ou terminologia ISO 2026 sem a documentação específica que o autor ainda fornecerá.
- Não transformar a rota para authority em obrigação do site em todo caso; ela permanece `if required`, conforme atribuição do CIP, sponsor procedure e regra aplicável.
- Não abrir CAPA automaticamente por um primeiro caso isolado; CAPA deve seguir falha recorrente após resposta inicial ou outro gatilho controlado.
- Não atribuir ao SART uma decisão agregada de causalidade sobre cirurgião, dispositivo ou processo local.

---

## 7. Instrução de implementação para a próxima IA

1. Começar no **SART v0.3 atual**; não reconstruir o formulário a partir de outro template.
2. Preservar as 11 páginas, a identidade visual, as seções A–H, as áreas narrativas e as páginas paisagem atuais.
3. Aplicar somente os ajustes 1–5 desta análise.
4. Usar o espaço livre existente nas páginas 7, 9 ou 10 para novos controles; evitar criar páginas adicionais sem necessidade.
5. Na página 7, manter a tabela de communication route e acrescentar o bloco de timeliness/completude abaixo dela.
6. Na página 10, desagregar o handoff de SCML, CSST, PIR ST-01 e deviation record conforme a tabela de saídas desta análise.
7. Preservar a classificação atual de eixos independentes até que o autor forneça a documentação de terminologia ISO 14155:2026.
8. Migrar o editor para o Editor v2 canônico sem alterar a geometria quando o editor estiver desligado.
9. Validar em A4 que nenhum conteúdo invade rodapé e que as páginas em paisagem continuam legíveis.
10. Gerar inicialmente apenas o HTML em branco editável. Não gerar PDF ou versão preenchida nesta etapa, salvo pedido expresso do autor.

---

## 8. Checklist de aceitação da próxima versão

- [ ] O SART continua sendo um registro individual de uma ocorrência de safety, DD ou nova informação material.
- [ ] A abertura do caso continua possível antes da classificação final.
- [ ] AE e DD continuam como vias independentes e simultâneas quando aplicável.
- [ ] Cada caso reportável possui uma regra CIP, due date/time, send time, timeliness e first-report completeness recuperáveis.
- [ ] Follow-up due/sent/timely e open-at-cut-off são recuperáveis para ST-01.
- [ ] Late initial notification possui delay point e linked deviation record.
- [ ] SCML Event ID, CSST review, PIR ST-01 e CAPA/SRR/POT são destinos distintos e auditáveis.
- [ ] Nenhum prazo universal foi hard-coded.
- [ ] Nenhum termo da ISO 14155:2026 foi atualizado por suposição antes da documentação do autor.
- [ ] O Editor v2 está funcional e não altera visual/paginação fora do modo editor.
- [ ] A renderização A4 preserva espaço de escrita e não invade rodapés.

---

## Fontes verificadas nesta análise

- Tese completa, especialmente a seção 4.3.3 sobre device-specific complication monitoring, a seção 4.5.4 sobre safety reporting timeliness e a sequência operacional do lifecycle.
- `SART_Safety_and_Adverse_Effect_Reporting_Template_v0_3_edited_2026-09-21_23-29-58.html`.
- `SCML_v0.7_blank.html`, para confirmar a divisão entre caso individual, índice de eventos e vigilância agregada.
- Regras de interconexão e granularidade dos instrumentos da Quality Lifecycle Framework.
