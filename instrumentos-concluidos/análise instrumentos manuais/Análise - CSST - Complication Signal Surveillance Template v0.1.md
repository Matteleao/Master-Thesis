# Análise — CSST: Complication Signal Surveillance Template v0.1

**Status:** recomendação de revisão estrutural importante; não criar ou alterar o HTML nesta etapa.  
**Ponto de partida:** o CSST v0.1 tem uma boa espinha dorsal e não precisa ser reconstruído do zero. Deve ser reposicionado como instrumento de julgamento analítico e decisão de signal, recebendo snapshots reconciliados do SCML em vez de reconstituir casos individuais.

---

## 1. Decisão central

O CSST é o instrumento que permite decidir:

> **For the defined procedure/device population and review period, do the reconciled complication data indicate no signal, a review trigger, a signal requiring further assessment, or a pattern requiring a defined response?**

A sua unidade de análise é uma **aggregate complication surveillance review**: uma revisão de site, protocolo, device/procedure population e período definidos — ou uma revisão ad hoc iniciada por trigger previamente aprovado.

A cadeia correta é:

```text
ICDL / PFVR / IQL / other source records
                         ↓
SART — individual site safety case coordination
                         ↓
SCML — living reconciled surveillance dataset
       and monthly/quarterly snapshots
                         ↓
CSST — periodic or triggered analytical review
       of rates, changes, strata and signal disposition
                         ↓
SLCT / sponsor device-deficiency route / SRR / CAPA / POT
```

O CSST não deve coletar seis meses de casos individualmente. Ele usa o SCML como população de eventos reconciliada; usa ICDL e fontes controladas para denominadores e contexto técnico; usa SLCT para interpretar qualquer estrato por cirurgião.

---

## 2. O que o CSST atual já faz bem e deve ser preservado

1. **Unidade agregada está clara.** A seção A já distingue o CSST dos registros individuais.
2. **Há um denominador de procedimentos.** A tese exige que cada contagem seja lida contra procedimentos realizados.
3. **Há separação entre contagem, threshold, comparação temporal, assessment e ação.** A sequência C → D → E → F → G → H é conceitualmente correta.
4. **As páginas em paisagem são apropriadas** para as tabelas C–G; a página inicial e o fechamento em retrato funcionam.
5. **O formulário já reconhece estratos importantes:** componente/configuração, cirurgião, indicação, timing e device deficiency.
6. **Há rotas de saída corretas:** SLCT, sponsor/device-deficiency route, SRR, CAPA e POT.
7. **O texto já alerta que não deve concluir causalidade individual ou substituir SART/sponsor/CEC.** Esse boundary deve ser mantido e reforçado.

---

## 3. Problema principal: o CSST precisa receber um dataset fechado, não recolher casos novamente

O CSST atual diz que usa SCML e outras fontes, mas ainda parece preparado para reconstruir a população evento a evento. Após a decisão de manter o SCML como log longitudinal e reconciliado, o CSST deve receber:

- um ou mais SCML snapshots fechados;
- lista deduplicada de SCML Event IDs e SART links;
- categoria, timing, AE/DD state, component/configuration/lot, procedure, surgeon e demais estratos autorizados;
- inclusões, exclusões, pendências e limitações do dataset;
- alterações desde o snapshot anterior;
- totais descritivos reproduzíveis, quando preparados pelo SCML;
- denominadores controlados do ICDL/procedure log;
- contexto da sequência, complexity e support/proctoring do SLCT quando houver estratificação por cirurgião.

A fonte primária de população de eventos é o **SCML snapshot**. SART, PFVR e IQL devem ser usados somente por referência para esclarecer um sinal, uma limitação ou uma linha do dataset; não para recriar todos os casos na revisão.

---

## 4. Ajustes críticos de conteúdo

### 4.1 Falta uma configuração histórica de regras

O formulário atual diz que thresholds vêm de CIP, SOP, IMP ou local rule, o que está correto. Porém, não registra de maneira suficientemente explícita qual conjunto de regras estava em vigor no período analisado.

O CSST precisa conter, no início da revisão, um bloco curto de **review configuration reference**:

- CSST ruleset / version and effective date;
- authorized surveillance category set / version;
- selected review population;
- review interval and data cut-off;
- selected signal tests;
- definition of each numerator and denominator;
- counting rule for an event with multiple attributes or both AE and DD pathways;
- pre-specified trigger for an ad hoc review.

A regra não deve ser criada durante a revisão. A tese exige que thresholds, frequência e triggers sejam definidos no start-up antes de existirem dados, e que mudança posterior só valha para períodos futuros.

### 4.2 Alguns thresholds e exemplos atuais não podem parecer universais

Remover da versão em branco ou converter para campo configurável:

- `example 5%`;
- `example 10%`;
- `five events in one category` como “triage trigger from thesis”.

A tese diz que um serious event ou cluster pode iniciar revisão mais cedo, mas não fixa cinco eventos como trigger universal. Cada regra precisa vir do CIP, SOP, IMP ou local rule aprovada.

### 4.3 Os denominadores precisam variar conforme o fenômeno

A regra atual “event count ÷ applicable procedure denominator” é correta como princípio, mas insuficiente como estrutura.

O CSST deve obrigar o revisor a registrar a população em risco ao lado de cada métrica:

| Métrica | Denominador apropriado |
|---|---|
| Total complication rate | Procedimentos investigacionais elegíveis no período. |
| Rate by surgeon | Procedimentos elegíveis realizados por aquele cirurgião, não o total do site. |
| Component/configuration/lot rate | Procedimentos expostos ao componente/configuração/lote. |
| Early postoperative outcome | Procedimentos que atingiram a janela de follow-up definida no cut-off. |
| Late postoperative outcome | Coorte com maturidade de follow-up suficiente; não todos os procedimentos recentes. |
| DD rate | Exposição definida no ruleset — por exemplo, procedimentos expostos ao device ou unidades aplicáveis — e nunca uma taxa misturada automaticamente com AE. |

Sem isso, o CSST pode produzir taxas formalmente calculadas, porém enganadoras, sobretudo em endpoints tardios e em grupos de baixo volume.

### 4.4 A tabela C mistura complicações e marcadores contextuais

`Unplanned implant configuration change` pode ser extremamente relevante para a interpretação do sinal, mas não é automaticamente uma complicação clínica. Não deve entrar no numerador ou no total de complication rate sem uma regra explícita.

A solução recomendada é separar:

1. **Complication / DD counts and rates** — os outcomes que podem gerar um sinal de segurança/complicação.
2. **Procedure-context markers** — substitution, unplanned configuration change, technical deviation, senior support/proctoring, documentation gap e outros marcadores oriundos do ICDL/SLCT.

Os marcadores contextualizam a análise do CSST, mas não são somados à taxa de complicação.

### 4.5 A comparação temporal não pode alegar “complexity adjusted” sem método

Na seção E, `complexity adjusted` sugere análise estatística ou ajuste formal que a tese não define.

Substituir por formulação operacional, por exemplo:

```text
Comparison basis and relevant context reviewed:
□ same device/procedure population
□ comparable follow-up maturity
□ surgeon sequence / learning-curve stage reviewed
□ case complexity / indication context reviewed
□ component/configuration exposure reviewed
□ comparison limited — rationale recorded
```

O CSST pode considerar esses fatores, mas não deve alegar ajuste estatístico se o site apenas fez uma avaliação estruturada.

### 4.6 O status de signal atual é ambíguo

A frase “signal absent, observed, confirmed” mistura níveis diferentes. `Confirmed` pode parecer confirmação de causalidade ou de falha do cirurgião, o que não é o papel do instrumento.

A decisão deve ocorrer em três gates separados:

1. **Dataset usable for review?**
   - Yes / Yes with limitation / No — reconciliation required.
2. **Did a pre-specified trigger or test occur?**
   - No / Yes / Not assessable.
3. **Disposition after assessment**
   - No material pattern identified;
   - pattern requires enhanced surveillance;
   - signal transferred to SLCT;
   - signal transferred to sponsor/device-deficiency route;
   - signal transferred to SRR/CAPA;
   - PI/POT decision required;
   - urgent individual safety route activated and CSST review initiated;
   - inconclusive because data limitation remains.

Isso mantém uma diferença nítida entre `trigger met`, `signal under assessment` e `route selected`.

### 4.7 A seção F precisa trabalhar com hipóteses, não com causa provável final

A coluna `Likely cause category` é útil, mas é forte demais se não for enquadrada como avaliação inicial agregada.

Renomear para:

> **Initial explanatory hypothesis / competing explanations to test**

Categorias possíveis:

- device/component/configuration/lot;
- procedure/technique;
- operator/learning-curve context;
- indication, case complexity or participant factor;
- data/ascertainment or documentation limitation;
- local process/control weakness;
- undetermined.

A coluna `Events / CAPA IDs` também deve mudar. CAPA é possível saída, não evidência de entrada. Usar:

> **SCML Event IDs / snapshot reference / linked source records**

A existência de concentração por cirurgião deve encaminhar ao SLCT para análise contra volume, sequência, complexidade, duração e suporte. Ela não autoriza o CSST a concluir non-compliance ou incompetência do cirurgião.

### 4.8 A seção G deve ser rota de decisão, não uma lista genérica de destinos

Manter SLCT, SART/sponsor DD route, CAPA, SRR e POT. Mas cada rota deve ser baseada em uma pergunta decisória objetiva:

| Rota | Usar quando a avaliação CSST conclui que… |
|---|---|
| **SLCT** | há padrão que exige revisar a sequência, competência, suporte ou proctoring de um cirurgião; não é conclusão de falha. |
| **Sponsor / DD route** | há sinal centrado em device, component, configuration, lot ou DD que exige informação/ação além do site. |
| **SRR** | existe vulnerabilidade prospectiva de processo ou controle que deve ser reconhecida no risk register. |
| **CAPA** | uma primeira resposta não foi suficiente, há recorrência ou falha sistêmica de processo/control. |
| **POT** | o PI precisa decidir restrição, intensificação de supervisão, continuidade, escalonamento ou outra ação de oversight. |
| **PIR** | o sinal é uma fonte de contexto para o indicador de surgeon procedural consistency; o CSST não deve criar um indicador separado sem regra aprovada. |
| **IMC** | a hipótese envolve execução de um controle que a internal monitoring checklist precisa verificar. |

### 4.9 A seção H deve acompanhar a decisão de signal, não virar CAPA paralelo

O CSST deve poder registrar resposta imediata, recipient, owner, due date e evidence/reference. Porém, quando uma rota proprietária é aberta, o CSST não deve reproduzir todo o action plan nem a effectiveness assessment daquele instrumento.

Proposta:

- manter um **Signal Decision and Transfer Register** no CSST;
- registrar o recipient record ID, owner, due date e proof of transfer;
- quando houver CAPA, SRR, SLCT, SART or sponsor route, acompanhar somente a referência e o estado necessário à decisão de manter/reabrir a vigilância;
- usar uma seção final de **signal reassessment** para registrar se o padrão persiste, diminui, está inconclusivo ou requer novo ciclo — não para substituir a verificação de efetividade do CAPA.

---

## 5. Seções do CSST v0.1: manter, modificar ou retirar

| Seção atual | Decisão | Revisão necessária |
|---|---|---|
| Cabeçalho | Manter, modificar | Incluir `CSST ruleset/version`, `SCML snapshot(s) used`, data cut-off e review type; manter site, protocolo, período, reviewer e controlled location. Máximo de 12 células. |
| A — Purpose and Use | Manter, modificar | Atualizar o input principal para SCML snapshots reconciliados; atualizar o nome completo do SART; definir claramente que CSST faz decisão analítica e não adjudicação individual/sponsor. |
| B — Review scope, denominator and trigger | Manter, ampliar | Adicionar ruleset, counting rule, denominators/risk sets, selected tests e status de comparabilidade com período anterior. |
| C — Case volume and aggregate complication counts | Manter, dividir | Separar denominadores e complication/DD outcomes de procedure-context markers. Exigir fonte e elegibilidade/maturidade do denominador. |
| D — Signal detection and threshold assessment | Manter, reconstruir internamente | Transformar em lista configurável de testes pré-aprovados. Retirar números exemplificativos e trigger “five events”. Registrar result, evidence, limitation e trigger status. |
| E — Comparison with previous period and stratified pattern | Manter, modificar | Comparar somente populações comparáveis. Trocar `complexity adjusted` por contexto revisado. Incluir denominador específico do estrato e limitação de comparabilidade. |
| F — Signal assessment and cluster characterization | Manter, modificar | Trocar CAPA IDs por SCML snapshot/Event IDs. Trocar likely cause por hipóteses concorrentes. Incluir `signal disposition` sem inferir causalidade final. |
| G — Integration with learning curve, safety and quality systems | Manter, modificar | Transformar em decision routes condicionais, cada uma com rationale e recipient record ID. |
| H — Actions, escalation and effectiveness follow-up | Manter, reduzir/renomear | Tornar-se Signal Decision, Transfer and Reassessment. Não duplicar CAPA/SLCT/SART/SRR action logs. |
| I — Reviewer certification and controlled closure | Manter, modificar | Certificar dataset, decisão, limitações e rotas; não declarar que um sinal está “closed” quando a ação proprietária segue aberta. |

---

## 6. Ajustes de visual e editor para a futura versão HTML

- A identidade visual, as páginas 2–4 em paisagem e a estrutura de cinco páginas são boas referências; não há necessidade de mudança drástica de orientação.
- O conteúdo das tabelas C–F deve ser reequilibrado depois da separação entre counts, denominators, context markers e judgement. Não reduzir fonte para manter a estrutura atual.
- A versão em branco não deve conter linhas com números, thresholds ou decisões simuladas. Instruções curtas ficam em notes/guidance; qualquer preenchimento fictício pertence a uma versão filled demonstration separada.
- O editor existente contém referências residuais a outros instrumentos (`SIFSL`, `CAPA`) e deve ser substituído pelo Editor v2 canônico no momento da reconstrução. Não manter editor legado e v2 ao mesmo tempo.

---

## 7. Arquitetura funcional recomendada para a próxima versão

```text
Page 1 — control header; Purpose and Use; review configuration, scope, ruleset,
         SCML snapshots, data cut-off, denominators and trigger.

Page 2 — landscape: denominator and data-quality reconciliation; aggregate
         complication/DD counts; separate procedure-context markers.

Page 3 — landscape: selected signal tests; previous-period comparison;
         surgeon/component/configuration/lot strata with denominator and limitation.

Page 4 — landscape: signal assessment, competing explanations, signal disposition
         and conditional route to SLCT / sponsor / SRR / CAPA / POT / PIR / IMC.

Page 5 — portrait: signal decision/transfer register; reassessment and continued
         surveillance plan; aggregate conclusion, limitation and accountable sign-off.
```

---

## 8. Checklist para a IA que futuramente criará o HTML

1. Preservar o CSST como revisão agregada procedure/device-specific.
2. Receber snapshots SCML reconciliados; não recolher casos individuais novamente.
3. Separar complication/DD outcomes de procedure-context markers do ICDL/SLCT.
4. Fazer cada taxa registrar numerador, denominador correto, população em risco, período e fonte.
5. Não fixar thresholds, timing windows ou accumulation triggers universais; usar ruleset pré-aprovado e referência controlada.
6. Separar dataset quality, trigger result e signal disposition.
7. Não inferir causalidade formal, non-compliance de cirurgião ou action effectiveness apenas a partir de um padrão agregado.
8. Direcionar sinal por rota clara, preservando o registro proprietário da ação.
9. Atualizar todas as referências para `SART — Safety Assessment, Reporting and Tracking Template`.
10. Manter identidade visual e orientação funcional; aplicar Editor v2 canônico; entregar HTML em branco e pré-visualização interativa antes de qualquer PDF ou filled demo.

---

## 9. Fontes verificadas

- Tese completa (29-10), seção 4.3.3: monitoramento de complicações, denominadores, thresholds, estratificação, sinais e rotas.
- Tese completa (29-10), implementação e oversight: SART/SCML no clinical moment; CSST como síntese periódica; interface com SLCT, SRR, CAPA e POT.
- CSST v0.1 atual: estrutura A–I e distribuição visual em cinco páginas.
- Análise SCML v0.7: definição de snapshots reconciliados e pacote de entrada do CSST.
- Análise SART: boundary do individual safety case e saída de dados mínimos ao SCML/CSST.
