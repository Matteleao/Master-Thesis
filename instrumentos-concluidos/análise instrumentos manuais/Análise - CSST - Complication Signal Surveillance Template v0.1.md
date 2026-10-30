# Análise — CSST: Complication Signal Surveillance Template v0.1

**Status:** recomenda-se uma reconcepção guiada pela arquitetura; não criar ou alterar o HTML nesta etapa.
**Ponto de partida:** o CSST v0.1 é um esboço inicial. As suas decisões conceituais úteis devem ser preservadas, mas não a sua sequência de seções, tabela por tabela, cabeçalho ou geometria visual. A próxima versão deve ser redesenhada como um relatório analítico de vigilância, alimentado por dados reconciliados e cálculos reproduzíveis feitos fora do formulário.

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

## 2. O que do CSST atual deve ser preservado — e o que não deve

Devem ser preservadas apenas as decisões conceituais abaixo:

1. **Unidade agregada.** O CSST é uma revisão de população, não um registro de caso individual.
2. **Denominadores.** Toda contagem precisa ser lida contra a população apropriada em risco.
3. **Cadeia de raciocínio.** Dados reconciliados → teste/regra → padrão/estrato → avaliação → rota de decisão.
4. **Estratos relevantes.** Componente/configuração, lote quando aplicável, cirurgião, timing, indicação, complexidade e device deficiency.
5. **Rotas de saída.** SLCT, sponsor/device-deficiency route, SRR, CAPA, POT, PIR e IMC.
6. **Limite de interpretação.** O CSST não substitui SART, sponsor, CEC ou adjudicação individual de causalidade.

Não devem ser preservados como referência de desenho: o cabeçalho atual, a distribuição visual, os tamanhos de coluna, a paginação, os exemplos numéricos, a ordem C–I nem a aparência rústica das tabelas. A versão v0.1 é uma fonte de ideias, não um esqueleto visual ou estrutural a ser ajustado incrementalmente.

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

Fontes que não pertençam a este conjunto de instrumentos podem ser usadas quando forem registros normais e controlados do estudo ou da prática clínica — por exemplo, um procedimento count mantido pelo sponsor/site, um relatório de exposição do sistema ou uma tabela de extração de eCRF. O CSST não deve exigir a criação de uma fonte exótica apenas para conseguir calcular uma métrica; deve identificar a fonte comum usada, a data de extração e a sua limitação.

O **cálculo bruto e a análise reproduzível** podem ficar em uma planilha controlada, relatório de sponsor ou outro arquivo analítico autorizado. O CSST é o relatório de resultados e decisão. Ele deve registrar: `analysis file/reference`, versão, data de extração/cut-off, responsável pela preparação, verificação/review e os outputs/tabelas citados. Não deve fingir que contém todas as fórmulas, tabelas de cálculo ou dados linha a linha.

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

O HTML não pode conter a expressão `from thesis`, citações à tese ou qualquer outra referência ao documento acadêmico. Ele deve apontar apenas para o documento operacional que realmente controla a regra: CIP, approved local monitoring plan, SOP, IMP, sponsor procedure, CSST ruleset ou outro documento controlado aplicável.

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

Quando houver análise estatística ou cálculo adicional, o formulário deve reportar o resultado e citar o arquivo analítico controlado. Não deve impor um modelo estatístico universal. A regra é:

```text
If an approved analysis method applies:
  report method/reference, result, assumptions/limitations and workbook/report ID.

If no approved inferential method applies:
  report descriptive result, comparison basis, limitations and decision.
```

### 4.5a O instrumento deve enfrentar clustering, não produzir conclusões simplistas

Uma finalidade essencial do CSST é tornar visível se eventos aparentemente separados se acumulam no mesmo contexto. A análise precisa examinar clustering por:

- período/tempo desde o procedimento;
- categoria e termo do evento;
- componente, configuração, modelo ou lote, quando disponível;
- cirurgião e posição na sua sequência de casos;
- indicação, complexidade, exposição e maturidade de follow-up;
- contexto técnico documentado no ICDL/SLCT.

O objetivo não é declarar que toda concentração é causalidade. É distinguir, de forma documentada, entre: uma variação casual possível; uma concentração que requer vigilância reforçada; uma hipótese que deve ser testada pelo SLCT ou pela rota de device deficiency; e uma limitação de dados que impede conclusão. Isso reduz tanto o risco de ignorar um cluster real quanto o risco de transformar uma coincidência, um pequeno denominador ou case-mix em acusação de falha do cirurgião ou do device.

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

## 5. Elementos do CSST v0.1: destino na nova arquitetura

| Seção atual | Decisão | Revisão necessária |
|---|---|---|
| Cabeçalho atual | Substituir | Criar um cabeçalho limpo, com até 12 células, ordenado pela decisão: site/protocol, review ID/version, period/cut-off, review type/trigger, ruleset, analysis reference, reviewer e controlled location. |
| A — Purpose and Use | Manter como princípio | Atualizar inputs para SCML snapshots e fontes controladas; atualizar SART; definir CSST como relatório analítico, não adjudicação individual. |
| B — Review scope, denominator and trigger | Reconstruir | Dividir entre scope/configuration e data-source/analysis-reference. Acrescentar ruleset, counting rule, risk sets, selected tests e status de comparabilidade. |
| C — Case volume and aggregate complication counts | Reposicionar e dividir | Tornar-se a exposição consolidada dos outputs analíticos: denominadores/risk sets, complication/DD outcomes e procedure-context markers em tabelas separadas. |
| D — Signal detection and threshold assessment | Reconstruir em nova página | Criar um reporte curto dos testes pré-aprovados, com rule ID, output calculado, source/analysis reference, limitation e trigger status. Não usar páginas largas nem exemplos numéricos sem necessidade. |
| E — Comparison with previous period and stratified pattern | Manter como princípio, redesenhar | Tornar-se a página analítica principal: comparabilidade, tendência, estratos e visualização de clustering, com denominador e limitação em cada leitura. |
| F — Signal assessment and cluster characterization | Manter, modificar | Usar SCML snapshot/Event IDs, hipóteses concorrentes e disposição de signal; nunca causa final. |
| G — Integration with learning curve, safety and quality systems | Transformar | Usar rotas condicionais de decisão, rationale, recipient record ID e data de transferência. |
| H — Actions, escalation and effectiveness follow-up | Renomear e reduzir | Tornar-se Signal Decision, Transfer and Reassessment. Não duplicar CAPA/SLCT/SART/SRR action logs. |
| I — Reviewer certification and controlled closure | Manter, modificar | Certificar dataset, análise, decisão, limitações e rotas; não encerrar artificialmente uma ação proprietária ainda aberta. |

---

## 6. Direção visual e editor para a futura versão HTML

- O visual atual é rústico e não deve ser replicado. Aplicar a identidade visual comum, mas com composição específica: hierarquia de leitura, larguras que correspondam ao conteúdo, alturas de linha variáveis e espaço real para interpretação.
- A primeira página deve ser **portrait** e cumprir Purpose and Use, scope/configuration e source/input map. As tabelas mais largas devem usar **landscape apenas quando necessário**; signal tests curtos, por exemplo, podem ser portrait.
- A tabela atual da seção D não justifica largura landscape: Signal ID não pode ocupar uma coluna desproporcional. Ela deve ser refeita como uma tabela compacta, com rule/test, output reportado, trigger status, referência e limitation.
- A versão em branco não deve conter números, thresholds, decisões simuladas, linhas exemplificativas preenchidas ou referências à tese. Guidance curto pode ficar em caixas/notas; um preenchimento fictício pertence exclusivamente a um future filled demonstration.
- O editor existente contém referências residuais a outros instrumentos (`SIFSL`, `CAPA`) e deve ser substituído pelo Editor v2 canônico no momento da reconstrução. Não manter editor legado e v2 ao mesmo tempo.

---

## 7. Arquitetura funcional recomendada para a próxima versão

```text
Page 1 — portrait: control header; Purpose and Use; review scope/configuration;
         source, input and calculation-reference map; SCML snapshot(s), cut-off
         and dataset readiness.

Page 2 — landscape: compiled analytical outputs — denominators/risk sets,
         complication/DD counts and rates, and separate procedure-context markers.

Page 3 — portrait: selected signal tests and rule outputs; each result shows
         ruleset reference, calculation/report reference, trigger status and limitation.

Page 4 — landscape: temporal comparison, strata and clustering-aware pattern
         assessment by surgeon, component/configuration/lot, timing, complexity
         or other authorized factor; signal disposition and competing explanations.

Page 5 — portrait: decision routes and proof of transfer; reassessment/continued
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
11. Proibir toda referência à tese dentro do formulário final; citar somente documentos operacionais controlados.
12. Separar o arquivo de cálculo/análise do CSST, registrando no relatório a sua referência, versão, cut-off, responsável e outputs usados.
13. Tornar a avaliação de clustering explícita, sem confundir concentração com causalidade ou com prova de falha do cirurgião/device.

---

## 9. Fontes verificadas

- Tese completa (29-10), seção 4.3.3: monitoramento de complicações, denominadores, thresholds, estratificação, sinais e rotas.
- Tese completa (29-10), implementação e oversight: SART/SCML no clinical moment; CSST como síntese periódica; interface com SLCT, SRR, CAPA e POT.
- CSST v0.1 atual: estrutura A–I e distribuição visual em cinco páginas.
- Análise SCML v0.7: definição de snapshots reconciliados e pacote de entrada do CSST.
- Análise SART: boundary do individual safety case e saída de dados mínimos ao SCML/CSST.
