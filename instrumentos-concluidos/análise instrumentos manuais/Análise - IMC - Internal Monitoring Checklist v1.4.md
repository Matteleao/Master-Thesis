# Análise crítica — IMC: Internal Monitoring Checklist v1.4

**Status:** análise manual para orientar a próxima revisão do instrumento. O HTML v1.4 não foi alterado nesta etapa.

## 1. Veredito executivo

O IMC é necessário e está conceitualmente bem posicionado dentro da framework. Ele não é um sponsor monitoring report, não é uma auditoria externa e não é um segundo PIR. Sua função é permitir que o próprio site verifique, em intervalos definidos e entre as visitas do sponsor, se os controles operacionais críticos:

1. foram executados;
2. deixaram evidência suficiente para reconstruir o que ocorreu; e
3. produziram o efeito esperado ou exigem resposta.

A versão v1.4 já incorpora essa lógica de maneira clara. O texto de Purpose and Use, a separação entre Execution, Evidence e Effectiveness / Response, a seleção de domínios, o action log e a effectiveness verification estão alinhados com a tese.

Entretanto, há uma lacuna importante: a tese define **dez verificações de internal monitoring**, mas o IMC v1.4 apresenta somente **nove domínios operacionais**. O check omitido é:

> **Endpoint data agreement** — para uma amostra de campos endpoint-critical registrados inicialmente fora do CRF, confirmar que o CRF concorda com a fonte e que as discrepâncias foram corrigidas e explicadas.

Essa não é uma diferença meramente editorial. A omissão retira do IMC a verificação direta de uma parte do CtQ relacionado à confiabilidade dos dados e enfraquece a ligação entre internal verification e o indicador de critical data completeness do PIR.

**Recomendação geral:** manter a arquitetura do IMC v1.4, corrigir a lacuna do décimo check, tornar explícitos os limites de amostra e fonte por domínio, e reduzir algumas ambiguidades de interface com FUCR, IQL, ICDL, CSST, PIR, SRR e POT. Não é necessária uma reconstrução conceitual do instrumento.

---

## 2. O que o IMC deve decidir

Depois de preencher o IMC, o reviewer deve conseguir responder:

> **For the stated site, review period or trigger, were the selected operational controls executed, sufficiently evidenced and effective, and what must be corrected, escalated or verified next?**

A decisão é sobre o **funcionamento dos controles do site**, não sobre o desempenho clínico de um participante, a qualidade de uma imagem isolada, a classificação de um evento individual ou o resultado global de todos os indicadores do estudo.

### Unidade de análise

A unidade correta é:

```text
one site + one defined review period or trigger + one approved monitoring scope
```

Um único IMC pode cobrir todos os domínios selecionados ou somente um subconjunto, desde que a exclusão seja aprovada e documentada.

O IMC não é:

- um checklist de cada participante;
- um log individual de visita;
- uma investigação clínica de complicação;
- um CAPA completo;
- uma revisão agregada de follow-up;
- uma auditoria independente do sponsor.

### O que o IMC acrescenta ao sistema

O sponsor continua responsável pelo monitoring independente definido em seu sistema de qualidade. O IMC cobre o intervalo de controle local entre sponsor visits e cria uma verificação proporcional ao risco, com escopo, frequência, amostra, reviewer e gatilhos definidos antes do conduct.

O princípio é complementaridade, não substituição:

```text
IMP defines the monitoring plan
IMC executes one review cycle
PIR receives selected performance findings
SRR receives persistent process vulnerabilities
POT receives decisions requiring PI oversight
CAPA receives recurring or material failures
```

---

## 3. O que está correto na versão v1.4

### 3.1. Purpose and Use está bem colocado

A primeira página explica que o IMC cobre um site, um ciclo de review e os domínios aplicáveis ao período ou trigger. Também declara corretamente que o documento não substitui source review, SRR, POT, specialized records, safety reporting, deviations ou CAPA.

Essa fronteira deve ser preservada.

### 3.2. A separação Execution / Evidence / Effectiveness é o principal acerto

A tese exige que o site não confunda três perguntas diferentes:

| Dimensão | Pergunta correta |
|---|---|
| Execution | O controle planejado foi executado? |
| Evidence | Existe evidência suficiente para confirmar o que ocorreu e o resultado? |
| Effectiveness / response | O controle funcionou e os sinais relevantes foram tratados? |

O IMC v1.4 torna essa separação visível na seção B e aplica a lógica na seção E. Isso é melhor do que um único `Compliant / Non-compliant`, porque uma atividade pode ter ocorrido sem que a evidência seja reconstruível, ou pode ter evidência suficiente mas revelar que o controle não foi efetivo.

### 3.3. A escala de classificação é adequada

As classificações `Complete`, `Partial`, `Not performed` e `Not applicable` para execução são úteis. O mesmo vale para `Adequate`, `Partial`, `Insufficient / unavailable` e `Not applicable` para evidência, e para `Effective`, `Observation`, `Not effective` e `Not assessable` para efetividade.

A exigência de resposta para resultados negativos ou incertos é correta e deve permanecer.

### 3.4. O Domain-Specific Interpretation Guide é necessário

A seção C evita que o reviewer interprete “adequate” de maneira diferente em sterile release, implant traceability, imaging, follow-up ou complications. O guia também faz uma boa ligação entre cada domínio e seus registros primários.

O guia deve continuar curto. Ele não deve se transformar em uma SOP completa dentro do checklist.

### 3.5. A seleção explícita de escopo é correta

A seção D permite uma revisão periódica completa ou uma revisão focal/triggered. Isso está alinhado com a tese, que permite cobrir os dez checks integralmente ou selecionar um subconjunto conforme risco e trigger.

A regra de registrar o motivo da exclusão deve ser mantida.

### 3.6. O Action Log e a Effectiveness Verification fecham o ciclo

A versão atual não fecha um achado simplesmente porque alguém marcou a ação como complete. A seção I exige evidência posterior de efetividade. Isso é essencial:

```text
finding → response → implementation → effectiveness evidence → closure
```

Esse mecanismo é uma das partes mais fortes do documento.

---

## 4. Lacuna crítica: o décimo check da tese foi omitido

### 4.1. O que a tese define

A seção 4.4.1 da tese define dez verificações:

1. Sterile release to use;
2. Implant traceability and component reconciliation;
3. Instrumentation and operating-room readiness;
4. Operative documentation;
5. Imaging usability and timing;
6. Follow-up execution;
7. **Endpoint data agreement**;
8. Timeliness and closure;
9. External context;
10. Complication monitoring.

O IMC v1.4 contém os itens 1–6 e 8–10, mas não contém o item 7.

### 4.2. Como corrigir

Adicionar `Endpoint data agreement` como domínio próprio no:

- Domain-Specific Interpretation Guide;
- Domains Included in This Review;
- Operational Control Domain Review;
- linked-template map;
- worked example, se houver;
- escopo de saída para PIR.

### 4.3. Definição recomendada

**Operational control domain:** Endpoint data agreement

**Execution means:**

> A predefined sample of endpoint-critical fields first recorded outside the CRF was compared with the corresponding source and the comparison was completed for the review period or trigger.

**Adequate evidence may include:**

- source record;
- CRF/database entry;
- source-to-CRF comparison sheet;
- query or correction record;
- ICDL, PFVR, IQL, SART or other originating record, where applicable;
- sample definition and selection rule;
- discrepancy log.

**Effective / usable when:**

> Sampled endpoint-critical entries agree with the source, discrepancies are corrected and explained, and unresolved disagreement is linked to the appropriate record or action.

**Periodic monitoring question:**

> Were endpoint-critical fields sampled according to the predefined rule, compared with their authoritative source and reconciled when discrepancies were identified?

### 4.4. Interface with the PIR

The IMC should not calculate the full critical data completeness indicator. It should produce the component that belongs to internal verification:

- sample definition;
- number sampled;
- number agreeing with source;
- number discrepant;
- number unresolved;
- source group and record references;
- action or limitation.

The PIR then incorporates this result into the broader critical data completeness review, together with timely completion, open queries and operative note finalization.

---

## 5. Problemas de rastreabilidade e amostragem

### 5.1. A seção D define escopo, mas não define suficientemente a base da revisão

A seleção `In scope: Yes / No` é necessária, mas não é suficiente para tornar o review reproducible. Para cada domínio em escopo, o IMC precisa conseguir responder:

- qual população ou conjunto de registros foi revisado;
- qual período foi coberto;
- qual cut-off foi usado;
- qual amostra foi selecionada;
- qual regra de seleção foi aplicada;
- quais registros foram vistos;
- qual é a versão da regra ou SOP;
- quem executou a atividade primária e quem revisou.

O cabeçalho não precisa conter todos esses dados. Pode existir uma pequena tabela de `Domain review boundary` entre D e E, ou campos adicionais na tabela E.

### 5.2. A tabela E está sem um campo explícito de sample/source boundary

A tabela principal contém `Domain`, `Periodic monitoring question`, `Execution`, `Evidence`, `Effectiveness / response`, `Finding, signal or limitation` e `Action / route / owner / due date`.

O campo `Finding` pode carregar referência, mas isso deixa a rastreabilidade dependente de texto livre. Recomenda-se acrescentar ou separar:

- `Review population / sample`;
- `Source records / range / cut-off`;
- `Finding, signal or limitation`;
- `Action / route / owner / due date`.

Se a tabela ficar excessivamente larga, usar uma pequena tabela de boundary por domínio antes da review, ou uma continuação controlada. O problema é funcional, não deve ser resolvido comprimindo a fonte até ficar ilegível.

### 5.3. O IMC não deve copiar narrativas dos registros especializados

O texto da versão v1.4 corretamente diz para registrar IDs e localizações controladas, sem copiar source narratives. Essa regra deve ser reforçada.

Exemplos:

- em imaging, referenciar IQL/ICQL e o conjunto de imagens; não repetir a análise técnica;
- em follow-up, referenciar PFVR/FUCR; não repetir cada visita;
- em complication monitoring, referenciar SART/SCML/CSST; não reclassificar o evento individual;
- em implant traceability, referenciar ICDL/accountability/operative note; não reconstruir a cirurgia no IMC;
- em endpoint agreement, registrar a amostra e discrepâncias; não copiar todos os valores do CRF.

---

## 6. Fronteiras com os outros instrumentos

### 6.1. IMC e IMP

A relação deve ser explícita:

| IMP | IMC |
|---|---|
| Define frequência, escopo, amostra, reviewer e triggers antes do conduct. | Executa um ciclo específico de review e documenta resultado. |
| Define quais dos dez checks se aplicam e quando. | Confirma se o check ocorreu, se existe evidência e se funcionou. |
| É o plano controlado. | É o registro da execução do plano. |

O IMC não deve permitir ao reviewer alterar silenciosamente a regra do IMP depois de observar o resultado. Se o escopo ou a frequência mudarem, a mudança deve ser documentada como uma atualização prospectiva do IMP ou como uma decisão controlada de PI.

### 6.2. IMC e FUCR

O FUCR agrega follow-up e mede timing, completude de componentes, endpoint-critical omissions e follow-up not obtained. O IMC verifica se o controle de follow-up foi executado, evidenciado e efetivo.

Exemplo:

- FUCR: três de 28 visitas ficaram fora da janela;
- IMC: a rotina de revisão e recuperação de visitas estava definida, os registros demonstram sua execução, e a resposta funcionou ou não;
- PIR: integra a medida de follow-up com os demais indicadores.

O IMC não deve recalcular o FUCR inteiro nem transformar a revisão do domínio de follow-up em uma segunda tabela populacional.

### 6.3. IMC e IQL/ICDL

IQL e ICDL são registros especializados ou fontes de execução. O IMC verifica se o processo previsto de revisão, reconciliação e resposta está funcionando.

O IMC pode encontrar, por exemplo:

- o IQL existe, mas não há evidência de revisão de imagens não utilizáveis;
- o ICDL registra substituições, mas a reconciliação com accountability não ocorre;
- os registros existem, mas não estão sendo revisados no intervalo definido.

Ele não deve substituir a avaliação técnica do IQL ou o registro intraoperatório do ICDL.

### 6.4. IMC e SART/SCML/CSST

O IMC verifica se os casos de safety e complicações foram encaminhados, revisados e fechados conforme o processo. O SCML agrega casos e o CSST analisa sinais/padrões.

O IMC não deve adjudicar o evento nem gerar o sinal clínico que pertence ao CSST. O seu achado pode ser processual:

> “SART cases existed, but two required local review actions were not documented within the defined interval.”

### 6.5. IMC e PIR

O IMC fornece findings, control status, action status e effectiveness evidence para o PIR. O PIR não deve receber somente `effective` ou `not effective`; precisa receber o domínio, período, fonte, limitação e ação vinculada.

O IMC também não deve duplicar todos os indicadores do PIR. Um PIR pode mostrar uma tendência de protocol deviation rate; o IMC pode verificar se o controle operacional destinado a evitar ou detectar aquele desvio foi executado e funcionou.

### 6.6. IMC e SRR

O SRR contém riscos, controles, owners, thresholds e estado de risco. O IMC verifica a execução e efetividade dos controles existentes.

Um problema isolado não deve automaticamente abrir uma nova entrada de risco. Deve haver uma regra para distinguir:

- finding local isolado;
- controle parcialmente efetivo;
- vulnerabilidade persistente;
- risco novo ou alteração do risco existente.

A seção F pode enviar um sinal ao SRR quando a falha é recorrente, transversal ou evidencia que o controle desenhado não é suficiente.

### 6.7. IMC e POT

O POT recebe questões que exigem decisão, restrição, aceitação formal de limitação ou intervenção do PI. O IMC não substitui essa decisão.

Um IMC pode registrar `PI Review Required: Yes` e indicar o ID do POT, mas não deve preencher retrospectivamente a decisão do PI como se fosse uma conclusão operacional do reviewer.

### 6.8. IMC e CAPA

O IMC identifica e acompanha a falha. O CAPA documenta a investigação causal e a ação corretiva/preventiva quando o problema é recorrente, material ou não resolvido pela resposta inicial.

O IMC deve registrar:

- finding ID;
- containment;
- route to CAPA;
- CAPA ID;
- effectiveness check.

Não deve duplicar o CAPA inteiro em sua tabela de ações.

---

## 7. Análise das seções atuais

### A — Purpose and Use

**Manter.** Está clara e define unidade, decisão, inputs e outputs. Acrescentar apenas uma frase explícita de que o IMC executa a revisão prevista no IMP e não redefine suas regras após o resultado.

### B — Monitoring Classification Guide

**Manter com pequena redução.** A separação das classificações é excelente, mas a seção ocupa duas páginas e tem texto suficiente para parecer uma mini-SOP. O guia deve permanecer instrutivo, porém enxuto.

A tabela de combinação `Execution / Evidence / Effectiveness` é útil. Recomenda-se acrescentar uma combinação explícita para:

- `Complete / Adequate / Not effective`;
- `Complete / Insufficient / Not assessable`;
- `Not performed / Adequate` somente quando a evidência demonstra que a atividade não ocorreu, deixando claro que evidência de ausência não é evidência de execução.

Não é necessário listar todas as combinações matemáticas. Basta explicitar as combinações que alteram a resposta.

### C — Domain-Specific Interpretation Guide

**Manter e completar com Endpoint Data Agreement.** Também revisar o rótulo `Effective / usable when` para não sugerir que todos os domínios produzem “usability” no mesmo sentido. Em alguns domínios, o resultado é control effectiveness; em outros, é data or record usability.

### D — Domains Included in This Review

**Manter.** Acrescentar o décimo domínio. Acrescentar campos para:

- IMP version;
- review frequency/trigger;
- sample rule;
- reviewer;
- approved scope date.

Não colocar todos esses campos em cada linha se eles forem comuns ao ciclo. Um bloco de configuração pode ficar acima da tabela.

### E — Operational Control Domain Review

**Manter como núcleo do IMC, mas reforçar rastreabilidade.** Acrescentar sample/source boundary ou criar uma tabela imediatamente anterior.

A redação das perguntas é boa porque usa a forma “Were...?”. Deve-se evitar perguntas que misturem duas decisões independentes. Por exemplo, `Follow-up execution quality` reúne timing, imaging, functional/PROM data e complications. Isso pode permanecer como um domínio amplo, mas a resposta deve apontar qual dimensão falhou; não basta marcar `Partial`.

### F — Cross-Domain Signals and Escalation

**Manter, mas limitar ao que realmente cruza domínios.** O bloco é útil quando uma falha não cabe em uma única linha de E. Não deve ser preenchido apenas porque existe qualquer finding.

O campo `Decision / Route` deve permitir rotas controladas: SRR, POT, MRL, CSST, PDTR, CAPA, PIR, sponsor/safety ou other. Deve haver espaço para `Not required` com justificativa, evitando forçar uma escalada.

### G — Open Action Log

**Manter.** É o registro de ações do ciclo, não um substituto do CAPA. Acrescentar, se houver espaço:

- source finding ID;
- action type: containment / corrective / preventive / verification;
- effectiveness due date;
- closure evidence.

A coluna `Initials` sozinha não substitui owner, signature ou accountability. O owner e a data devem permanecer obrigatórios para toda ação aberta.

### H — Review Outcome

**Manter com critérios mais objetivos.** `Controls effective`, `Observations only`, `Action required` e `Escalation required` são resultados úteis. A página deve indicar que o outcome é derivado dos domínios em escopo e não de domínios excluídos.

A opção `PI Review Required?` deve ser ligada a um POT ID quando marcada Yes, ou registrar por que o review não foi necessário.

### I — Effectiveness Verification / Follow-up

**Manter.** É necessário para impedir fechamento administrativo. Diferenciar:

- ação implementada;
- ação efetiva;
- ação parcialmente efetiva;
- ação não efetiva;
- não assessável.

O campo `Evidence reviewed / linked record` deve exigir uma referência controlada, não apenas uma frase narrativa.

### J — Reviewer Certification

**Manter.** A declaração está adequada. Acrescentar, quando aplicável, uma confirmação de que o reviewer não foi a pessoa que executou o controle revisado ou que a exceção foi justificada sob documented PI oversight.

### K — Document Control Note

**Manter.** A nota sobre targeted/triggered review não substituir o próximo scheduled IMC é importante e deve permanecer.

---

## 8. A revisão não deve transformar o IMC em uma auditoria completa

Há um risco de expansão excessiva porque os dez domínios cobrem boa parte da operação do site. O IMC deve continuar sendo uma revisão proporcional, não uma inspeção de tudo em cada ciclo.

A versão final deve permitir:

- revisão completa periódica;
- revisão focal por domínio;
- revisão triggered por sinal;
- amostragem por risco;
- aumento temporário de amostra;
- transferência de uma investigação para outro instrumento.

A regra precisa estar no IMP ou no bloco de scope control. O IMC registra qual regra foi aplicada.

Uma linha por domínio é apropriada. Não criar uma linha por cada participant, image, implant ou query. Quando o domínio exigir detalhes, usar o registro especializado e referenciá-lo.

---

## 9. Arquitetura recomendada para a próxima versão

Não é necessário reescrever o instrumento do zero. A arquitetura recomendada é:

### Página 1 — Scope, purpose and review boundary

- cabeçalho;
- A. Purpose and Use;
- review period, trigger, cut-off, reviewer;
- IMP version and scope reference;
- inputs/outputs;
- início do classification guide.

### Página 2 — Classification guide

- Execution;
- Evidence;
- Effectiveness / response;
- combinações que exigem ação;
- nota curta sobre N/A, Not assessable e limitação.

### Página 3 — Domain interpretation guide

- dez domínios;
- definição de execution;
- evidência esperada;
- condição de effectiveness/usable;
- referências primárias.

### Página 4 — Scope and sampling configuration

- dez domínios com Yes/No;
- sample/population;
- rule/version;
- exclusion rationale;
- reviewer and approval;
- source/cut-off boundary.

### Página 5 — Operational control review

- tabela principal dos dez domínios;
- Execution;
- Evidence;
- Effectiveness/response;
- finding/limitation;
- action/route/owner/due date.

Esta página pode exigir orientação landscape ou uma divisão controlada em duas páginas. Não reduzir excessivamente a fonte apenas para manter uma tabela portrait.

### Página 6 — Signals and action log

- F. Cross-domain signals and escalation;
- G. Open action log;
- linked records e owners.

### Página 7 — Outcome and effectiveness

- H. Review outcome;
- I. Effectiveness verification;
- J. Reviewer certification;
- K. Document control note.

A estrutura de sete páginas pode ser mantida. O principal ajuste de conteúdo é a inclusão do décimo domínio e de limites de amostra; não é necessário adicionar páginas apenas para aumentar texto explicativo.

---

## 10. Fluxo de uso recomendado

### Antes do review

1. Confirmar IMP version, período e trigger.
2. Confirmar reviewer e independência relativa à execução.
3. Definir os domínios em escopo.
4. Confirmar sample rule, population e cut-off.
5. Fixar os registros controlados que serão utilizados.
6. Não alterar thresholds ou critérios depois de observar os resultados.

### Durante o review

Para cada domínio:

1. verificar se o controle planejado foi executado;
2. identificar a população/amostra revisada;
3. conferir se a evidência permite reconstruir a execução e o resultado;
4. avaliar se o controle foi efetivo;
5. registrar finding, signal ou limitation;
6. abrir uma ação ou indicar a rota correta;
7. registrar o ID do registro relacionado.

### Após o review

1. consolidar sinais que cruzam domínios;
2. registrar ações e owners;
3. decidir se é necessário POT, SRR, CAPA, PIR, CSST, PDTR ou sponsor route;
4. estabelecer a data da effectiveness verification;
5. definir o resultado geral;
6. assinar;
7. arquivar com as evidências controladas.

### No follow-up

O reviewer deve verificar a implementação e a efetividade, não apenas a existência da ação. Se a ação falhar ou o finding se repetir, a rota deve ser escalada para CAPA, SRR, POT ou outro instrumento apropriado.

---

## 11. Saídas do IMC

| Destinatário | Saída correta do IMC |
|---|---|
| IMP | Evidência de que o ciclo foi executado; possível necessidade de atualização prospectiva do plano. |
| PIR | Finding, status do controle, sample, período, limitação, ação e effectiveness result. |
| SRR | Vulnerabilidade persistente, controle insuficiente ou risco novo/alterado. |
| FUCR | Informação processual sobre a execução do controle de follow-up, sem duplicar as medidas agregadas. |
| POT | Questão que exige decisão ou oversight formal do PI. |
| MRL | Finding relevante para uma revisão de milestone ou mudança de fase. |
| CAPA | Falha recorrente, material ou não resolvida pela resposta inicial. |
| CSST | Somente quando o IMC identifica que o circuito de complication surveillance falhou; não gera o sinal clínico. |
| Sponsor / safety route | Questão que excede a responsabilidade local ou exige notificação/decisão externa. |

---

## 12. Checklist de correção da próxima versão

1. O décimo domínio, **Endpoint Data Agreement**, foi acrescentado em todas as tabelas aplicáveis?
2. O IMC identifica claramente o IMP version e a regra que está executando?
3. Cada domínio tem population/sample, cut-off e source boundary identificáveis?
4. A revisão diferencia execution, evidence e effectiveness?
5. `Not applicable` exige justificativa?
6. `Not performed`, `Insufficient`, `Not effective` e `Not assessable` exigem resposta ou limitação?
7. O IMC não copia narrativas de PFVR, IQL, ICDL, SART ou source records?
8. A seção de follow-up usa FUCR como fonte agregada, sem recalcular todo o FUCR?
9. O endpoint data agreement alimenta o PIR sem duplicar seu indicador completo?
10. F só é usado para sinais verdadeiramente cross-domain?
11. Toda ação tem owner, due date, linked record e effectiveness route?
12. `PI Review Required` aponta para POT ou justifica a ausência de POT?
13. O resultado geral considera somente os domínios em escopo?
14. O reviewer pode ser diferente da pessoa que executou o controle, ou a exceção está documentada?
15. A versão pode ser usada como periodic review, focused review e triggered review?
16. A tabela principal continua legível e dentro do rodapé, sem reduzir a fonte de maneira excessiva?
17. O Editor v2 permite editar todas as células, classificações, caixas, linhas e campos de ação relevantes?

---

## 13. Conclusão

O IMC v1.4 não está errado em sua lógica central. Pelo contrário: é um dos instrumentos mais bem alinhados com a tese porque transforma a internal verification em uma sequência verificável de execução, evidência, efetividade, ação e follow-up.

A correção mais importante é recuperar o check omitido de **Endpoint Data Agreement**. Depois disso, a revisão deve melhorar a auditabilidade do processo, principalmente por meio de:

- sample e source boundary explícitos;
- ligação controlada ao IMP;
- referências em vez de cópias de narrativas;
- critérios de outcome ligados aos domínios em escopo;
- fronteira clara com FUCR, IQL, ICDL, SART, SCML, CSST, PIR, SRR, POT e CAPA.

A recomendação final é, portanto:

```text
preserve the IMC architecture;
add the missing tenth check;
make sampling and source boundaries explicit;
strengthen interfaces;
do not turn the IMC into a participant-level audit or a second PIR.
```

---

## 14. Fontes verificadas

- Tese completa (29-10), seção 4.4.1: internal verification of site conduct, dez checks, frequência, amostra, reviewer, trigger, action e effectiveness.
- Tese completa (29-10), seção 4.4.4: source documentation, authoritative records e uso de referências em vez de registros paralelos.
- Tese completa (29-10), seção 4.5.6: critical data completeness e reconciliação entre CRF e source.
- Tese completa (29-10), seção 4.5.7: CAPA e fechamento da ação com evidência de efetividade.
- Tese completa (29-10), Appendix M: Internal Monitoring Plan, que define escopo e schedule.
- Tese completa (29-10), Appendix N: Internal Monitoring Checklist, que executa o review periódico definido pelo IMP.
- IMC v1.4: seções A–K, classificação, guia por domínio, seleção de escopo, review, cross-domain signals, action log, outcome, effectiveness verification e certification.
- Operational Quality Form Templates skill: distinção entre desenho de controle, monitorização operacional, revisão individual e performance agregada; cadeia CTQ → controle → evidência → resultado → ação → efetividade.
