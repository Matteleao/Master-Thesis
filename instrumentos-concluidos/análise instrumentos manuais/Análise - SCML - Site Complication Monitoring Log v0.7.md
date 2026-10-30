# Análise — SCML: Site Complication Monitoring Log v0.7

**Status:** manter o instrumento, mas reconstruir a sua função como camada intermediária de consolidação e reconciliação.  
**Não criar ou alterar o HTML nesta etapa.** Esta análise orienta a próxima IA que fará a nova versão.

---

## 1. Decisão de arquitetura

O **SCML deve permanecer**. Ele não é um segundo SART e não é um CSST simplificado.

A sua função é manter um **índice longitudinal, padronizado e reconciliado de eventos/deficiências elegíveis para vigilância de complicações procedure/device-specific**. Cada entrada mantém o mesmo SCML Event ID ao longo do tempo; quando surgem informações novas, a entrada é atualizada e a fonte é citada.

O SCML resolve a lacuna entre os casos individuais e a revisão analítica:

```text
Clinical/source records — ICDL / PFVR / IQL
                         ↓
SART — one individual site safety case
                         ↓
SCML — living, reconciled surveillance dataset
       with monthly or quarterly snapshots
                         ↓
CSST — semiannual or triggered analytical review
       of patterns, rates, thresholds and action routes
                         ↓
SLCT / sponsor device-deficiency route / SRR / CAPA / POT
```

A decisão que o SCML deve permitir é simples:

> **At the selected cut-off, is the site’s complication-surveillance dataset complete enough, deduplicated, categorized consistently and reconciled to its source records for the CSST to use it without recreating the historical data collection?**

O SCML **não** decide se existe um signal, se um cirurgião está non-compliant, se uma ação é eficaz ou se um caso de safety está fechado.

---

## 2. Diferença prática entre SART, SCML e CSST

| Instrumento | Unidade | Frequência | O que faz | O que não faz |
|---|---|---|---|---|
| **SART** | Um site safety case: AE, observed DD ou material new safety information | Quando o caso é reconhecido e sempre que há atualização material | Coordena reconhecimento, proteção, avaliação atual do PI/site, rota/prazo do sponsor, transmissão, receipt, follow-up e closure local. | Não calcula taxa, não compara casos e não declara signal. |
| **SCML** | Um distinct event or deficiency eligible for complication surveillance | Contínuo; snapshot/reconciliation mensal ou trimestral | Indexa, deduplica, padroniza e reconcilia os atributos necessários para comparar eventos entre procedimentos, componentes e cirurgiões. | Não repete cronologia/reporting do SART; não aplica threshold nem conclui causalidade ou performance. |
| **CSST** | Uma population-level complication review, por período ou trigger imediato | Semestral, conforme regra definida no start-up, ou ad hoc quando há trigger | Integra o dataset SCML com denominadores de procedimento, ICDL, SLCT e fontes autorizadas; calcula, compara, testa triggers, interpreta padrão e decide a rota de resposta. | Não deve reconstruir linha a linha seis meses de casos individuais nem substituir SART/SCML. |

O CSST pode analisar se existe concentração por cirurgião. **Isto não prova não conformidade, erro técnico ou incompetência do cirurgião.** É apenas um estrato que pode justificar revisão pelo SLCT, levando em conta volume, sequência da learning curve, complexidade, indicação, componente/configuração e outras explicações plausíveis.

---

## 3. Escopo do SCML

O SCML continua **device- and procedure-specific**. Não se converte em um log geral de qualquer problema do site.

Inclui:

- complicações potencialmente relacionadas ao device, procedimento ou à sua interação em uso;
- AEs, ADEs e DDs com relevância para a vigilância de complicações;
- complicação reconhecida no intraoperatório ou mais tarde, por exemplo durante uma visita PFVR ou uma imagem IQL;
- eventos cuja relação ainda é incerta, desde que possam entrar na população de vigilância;
- informações atualizadas que mudem a categoria, estrato, inclusão, exclusão ou interpretação da fonte.

Não inclui como objeto principal:

- visit-window compliance, missed visits, visitas incompletas ou atraso de follow-up sem complicação clínica procedure/device-specific: estes pertencem a PFVR/FUCR;
- um atraso administrativo de reporting por si só: este permanece em SART, deviation record e PIR ST-01;
- toda narrativa clínica, query, evidência de transmissão ou closure do caso SART;
- qualquer hipótese de sinal ainda não sustentada por uma revisão CSST.

---

## 4. Novo fluxo SART → SCML

O novo SART continua sendo a fonte individual e coordenadora do safety case. Ele deve abrir uma interface explícita ao SCML quando um caso é elegível para complication surveillance.

### 4.1 Regra de inclusão

Ao abrir ou atualizar o SART, o site registra uma decisão curta:

```text
Eligible for SCML complication surveillance?
□ Yes — enter / update SCML Event ID
□ Pending — information or relationship assessment incomplete
□ No — not a device/procedure complication-surveillance event

Rationale / source reference:
SCML Event ID, if assigned:
Date / owner:
```

**Não é preciso esperar a determinação do sponsor/CEC** para entrar no SCML. A entrada deve usar `Pending` quando a avaliação ainda estiver aberta e deve ser atualizada depois.

### 4.2 Dados mínimos enviados do SART ao SCML

O SCML recebe somente a informação necessária para indexar e comparar. O SART mantém a evidência, a cronologia e o processo de reporting.

| Grupo | Dados que o SART deve disponibilizar ao SCML |
|---|---|
| Identificação | SART Case ID; specific event reference; participant code ou `N/A context`; event term/study code; occurrence/detection date e nível de certeza se aplicável. |
| Contexto procedimental | Procedure date; days from procedure; ICDL/procedure reference; surgeon code. |
| Exposição técnica | Investigational device/comparator; component/configuration; lote/identifier quando controlado pela fonte; IQL/imaging reference quando relevante. |
| Estado AE/DD | `AE`; `DD without AE`; `AE associated with an observed DD`; `DD that could have led to a SADE`; `Pending`; `N/A`, conforme fonte disponível. |
| Perfil de vigilância | Primary surveillance category autorizada; timing group; regra de contagem quando o caso tiver mais de um atributo. |
| Contexto de relação atual | Device; procedure/technique; operator/use context; participant condition; concomitant treatment/other factor; undetermined. Estes são contextos ou hipóteses atuais, não causalidade final. |
| Maturidade da fonte | Current PI/site assessment; sponsor/CEC determination received / not received; agreement/disagreement/pending; source reference; date/initials of last source check. |
| Inclusão no dataset | Included; pending inclusion; excluded with rationale; SCML Event ID; latest SCML reconciliation/snapshot reference. |

O SART **não deve transferir** ao SCML:

- narrativa completa de AE/DD;
- atendimento clínico ou documentação de proteção;
- cronologia de follow-up, queries e informação pendente detalhada;
- regra, prazo, transmissão, receipt ou completeness do reporting ao sponsor;
- evidência de closure local;
- determinação global do sponsor/CEC além de uma referência e estado recebido.

---

## 5. SCML → CSST: o pacote que o CSST deve receber

O SCML é atualizado continuamente, mas cada mês ou trimestre deve fechar um **snapshot de reconciliação**. O CSST pode então usar um ou mais snapshots fechados em uma revisão semestral ou em uma análise ad hoc.

O pacote de entrada do CSST deve conter:

1. **Metadados do corte**
   - site, protocolo, device/system, procedure family e CIP/category-set version;
   - período coberto, date of data cut-off e date of snapshot freeze;
   - SCML owner/reviewer e last reconciliation date.

2. **População de eventos elegíveis e deduplicada**
   - lista de SCML Event IDs incluídos;
   - SART Case/Event ID correspondente;
   - referência ICDL, PFVR e IQL quando existente;
   - participant code/context quando necessário para rastreabilidade;
   - exclusões e pendências com rationale.

3. **Atributos comparáveis por evento**
   - event term/code;
   - data e timing group;
   - primary surveillance category;
   - AE/DD state atual;
   - device/component/configuration/lot quando disponível;
   - procedure and surgeon code;
   - estratos autorizados pelo estudo, como indicação ou complexidade, se existirem em fonte controlada;
   - contexts of relationship como informação corrente, nunca como conclusão final.

4. **Qualidade do dataset no cut-off**
   - reconciled / source pending / information missing / reclassified / duplicate resolved;
   - motivo de qualquer exclusão ou limitação;
   - alterações desde o snapshot anterior: novo evento, correção, atualização de categoria, resolução de duplicidade ou informação recebida.

5. **Contagens descritivas opcionais e reproduzíveis**
   - totais mecânicos por categoria, timing group, component/configuration, surgeon ou outro estrato aprovado;
   - sempre identificados como `descriptive reconciliation totals`;
   - acompanhados de regra de contagem e referências aos Event IDs que os originam.

Esses totais podem reduzir trabalho manual no CSST, mas **não são ainda uma análise de performance ou de signal**.

### O que o SCML não deve fazer

O SCML não deve:

- calcular taxa por procedimento;
- receber ou calcular denominador de procedimentos;
- comparar uma taxa ao período anterior;
- aplicar threshold ou marcar signal Yes/No;
- afirmar que há cluster, tendência ou aumento relevante;
- atribuir causa provável ou performance inadequada a cirurgião, device ou técnica;
- decidir escalonamento a SLCT, CAPA, SRR, POT, sponsor ou CEC;
- controlar ações, due dates, effectiveness ou closure que pertencem a outro instrumento;
- fechar um SART case.

Essas decisões pertencem ao **CSST** e, depois, ao registro que é dono da ação ou da decisão.

---

## 6. Ajustes necessários no SCML v0.7

### Manter, com ajuste focal

| Elemento atual | Decisão | Alteração necessária |
|---|---|---|
| Cabeçalho | Manter, modificar | Preservar study/protocol, site, SCML ID/revision, owner, device/system, procedure family, CIP e category set. Substituir `CSST Review Period / Next Review Date` por `Current SCML snapshot period / data cut-off` e `Next SCML reconciliation due`. A agenda do CSST pode ser uma referência, não o estado do log. |
| A — Purpose and Use | Manter, modificar | Declarar que o SCML é o dataset longitudinal reconciliado da vigilância local. Atualizar SART para **Safety Assessment, Reporting and Tracking Template**. Declarar que o CSST, e não o SCML, calcula, interpreta e decide signal. |
| B — Recording and Source-Link Guide | Manter, simplificar | Manter a regra de um SCML Event ID por distinct event/deficiency e atualização da mesma entrada. Incluir a regra `included / pending / excluded with rationale`. Remover a sugestão de acompanhamento de conclusão/efetividade de ações. |
| C — Event and Source Index | Manter, fortalecer | É o núcleo. Manter IDs, participant/context, event term, date/days from procedure, device/component, surgeon, ICDL e imaging. Incluir PFVR/clinical follow-up reference e `last reconciled / snapshot status`. Não inserir narrativa clínica. |
| D — Structured Surveillance Profile | Manter, modificar substancialmente | Manter category, timing group e relationship contexts. Atualizar `AE + DD` para **AE associated with an observed DD**. Acrescentar **DD that could have led to a SADE** onde aplicável. Remover a coluna redundante `Observed DD?`, porque o estado AE/DD já responde isso. Trocar `Final` por `current PI/site assessment documented`, `sponsor/CEC determination received`, `pending` e respectiva referência/data. |
| H — Accountable Review and Controlled Record Location | Manter, modificar | A assinatura deve confirmar integridade, rastreabilidade, reconciliação e pendências do dataset. Não deve certificar safety assessment final, signal, causalidade, action effectiveness ou closure do SART. |

### Retirar ou transformar

| Elemento atual | Decisão | Motivo e novo destino |
|---|---|---|
| E — Local Review and Handoff | Transformar completamente | Tornar-se **SCML Snapshot Reconciliation and CSST Handoff**. Registra período/cut-off, Event IDs incluídos, fontes reconciliadas, pendências/exclusões, change log e CSST review reference. Não distribui ações a SLCT/CAPA/SRR/POT. |
| F — Linked Action and Handoff Follow-up | Retirar | Duplica o registro proprietário da ação e indevidamente transforma o SCML em action log. Referências externas podem aparecer no CSST ou no registro proprietário. |
| G — Current Index Status and Review Conclusion | Transformar | Renomear para **Current Dataset Reconciliation Status**. Estados possíveis: `reconciled for snapshot`; `source check pending`; `missing/uncertain information`; `correction/reclassification pending`; `dataset not ready for CSST`, com affected Event IDs e limitation note. Remover `control action active` e `escalated review active`. |

---

## 7. Frequência e ciclos

A frequência não deve ser fixa universalmente. Ela é definida no start-up pelo protocolo, volume esperado, risco do device/procedure e regra local aprovada.

O modelo plausível é:

```text
SART entry / update            → at recognition and when material information changes
SCML update                    → promptly after eligible SART/source change
SCML reconciliation snapshot   → monthly or quarterly
CSST periodic review           → semiannual, or the protocol-defined interval
CSST ad hoc review             → serious health threat, pre-specified trigger, concerning accumulation, or other defined trigger
```

O CSST pode usar vários snapshots SCML fechados. Assim, uma revisão semestral não precisa reconstruir seis meses de casos e não depende de memória ou transcrição retrospectiva.

---

## 8. Guard-rails de interpretação

1. **Uma complicação não prova falha do cirurgião.** Concentração por cirurgião é um estrato para o CSST investigar com SLCT, volume, learning curve, complexidade, indicação, componente e outros dados.
2. **Contexto não é causalidade formal.** `Device`, `procedure`, `operator`, `patient` e semelhantes refletem a avaliação corrente; não substituem o sponsor/CEC.
3. **AE e DD podem coexistir sem criar dois eventos clínicos.** Um AE associado a DD observada pode seguir duas vias no SART e ainda ter uma única entrada SCML com regra de contagem clara.
4. **O SCML não cria dupla fonte de verdade.** Quando existir divergência, SART, ICDL, PFVR, IQL ou a fonte clínica apropriada permanece autoritativa para o seu dado; o SCML registra a correção e data do check.
5. **O SCML não substitui CSST.** Não há threshold, signal conclusion, action decision ou effectiveness assessment no log.

---

## 9. Ajuste de interface exigido no futuro SART

A próxima versão do SART deve preservar a seção de interface com o SCML, mas substituí-la por uma linha explícita de elegibilidade e pelos campos mínimos descritos na seção 4 desta análise.

O SART continua a listar `SCML Event ID / date / owner` como saída individual. Porém, o SART não deve tentar produzir uma decisão de signal ou assumir que o case precisa ser incluído no CSST; essa decisão é feita no snapshot SCML e no CSST conforme escopo e trigger.

---

## 10. Instrução para a IA que reconstruirá o HTML do SCML

1. Não reconstruir o SCML como SART ou como CSST em miniatura.
2. Manter uma linha por distinct event/deficiency e preservar um SCML Event ID estável.
3. Fazer da seção C o registro-fonte de indexação e da D o perfil de comparabilidade para vigilância.
4. Criar uma seção de snapshot/reconciliation que permita fechar e transmitir um dataset confiável ao CSST.
5. Não criar tabelas de ação, effectiveness, CAPA follow-up ou formal signal decision.
6. Atualizar toda referência ao SART para `Safety Assessment, Reporting and Tracking Template`.
7. Aplicar a taxonomia ISO 14155:2026 sem substituir as avaliações formais do sponsor/CEC.
8. Manter a identidade visual comum e, quando chegar a fase de HTML, migrar para o Editor v2 canônico sem alterar silenciosamente as decisões desta análise.

---

## 11. Fontes verificadas

- Tese completa (29-10), seção 4.3.3: monitoramento device-specific, cadeia SART → SCML → CSST e relação com o denominador de procedimentos.
- Tese completa (29-10), seção de implementação: SART e SCML são atualizados no clinical moment; CSST realiza a síntese periódica.
- SCML v0.7 em branco: estrutura atual C–H e campos de índice, perfil, handoff e status.
- CSST v0.1: unidade de análise, denominadores, thresholds, estratificação, signal assessment e rotas de ação.
- Análise de reconstrução do SART: escopo do novo site safety-case coordination record e taxonomia ISO 14155:2026.
