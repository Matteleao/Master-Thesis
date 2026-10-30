# Análise crítica — FUCR: Follow-up Compliance Review v0.3

**Status:** análise manual para orientar a próxima revisão do instrumento. O HTML v0.3 não foi alterado nesta etapa.

## 1. Veredito executivo

O FUCR é necessário e ocupa uma posição diferente do PFVR. O PFVR registra uma visita individual; o FUCR revisa o desempenho do follow-up em uma população e em um período definidos.

A arquitetura atual do FUCR v0.3 está conceitualmente próxima do que a tese exige. Ela já contém:

- uma unidade de revisão site-period aggregate;
- um mapa de denominadores;
- os quatro blocos de medida exigidos para follow-up compliance;
- uma matriz de completude por componente;
- uma análise de timing e causas;
- interpretação de tendência/concentração;
- ação, escalonamento, eficácia e certificação.

O problema principal não é o FUCR existir ou ter muitas seções. O problema é garantir que cada seção agregue informação que já foi registrada no PFVR sem voltar a reavaliar cada visita, copiar resultados clínicos ou criar indicadores paralelos que não pertencem ao FUCR.

**Recomendação geral:** manter o FUCR como revisão agregada, preservar as quatro medidas centrais e fazer uma revisão focal de denominadores, reconciliação de fontes, fronteiras com PFVR/IQL/ICDL/IMC/PIR e interpretação de causas.

---

## 2. Decisão que o FUCR deve suportar

Depois de preencher o documento, o responsável deve conseguir decidir:

> **For the defined population and review period, is the site's follow-up process controlled, partially controlled, or requiring action, based on timely visits, component completeness, endpoint-critical omissions and documented recovery of participants due for follow-up?**

O FUCR não deve decidir se um participante individual era elegível, se uma imagem clínica é adequada ou se um evento é um adverse effect. Essas decisões pertencem aos registros especializados.

### Unidade de análise

A unidade do FUCR é:

```text
one site + one defined follow-up population + one review period + one data cut-off
```

A unidade não é uma visita individual. As visitas individuais entram como registros-fonte e são resumidas por contagens, proporções, tendências, causas e referências.

### População e período obrigatórios

O cabeçalho e a primeira página devem fixar:

- study/protocol and site;
- review period;
- data cut-off;
- population in scope;
- expected visits and participants due;
- previous comparable period, if applicable;
- cadence and trigger;
- source reconciliation boundary;
- reviewer/accountable role.

Sem essa definição, uma proporção no FUCR não é auditável.

---

## 3. O que está correto no v0.3

### 3.1. O documento diferencia PFVR e FUCR

A seção A afirma que o FUCR é uma revisão agregada e que não substitui PFVR, fonte clínica, deviation record, safety reporting, imaging standardization ou internal monitoring. Essa fronteira deve ser mantida e tornada ainda mais operacional.

### 3.2. O mapa de denominadores é necessário

A seção B é útil porque impede que attendance, timing, completeness e usability sejam misturados em uma taxa única. O princípio está correto: participante, visita, componente e assessment não são denominadores intercambiáveis.

### 3.3. As quatro medidas centrais estão presentes

A seção C é o núcleo exigido pela tese:

1. visitas concluídas dentro da janela / visitas esperadas;
2. visitas contendo todos os componentes exigidos / visitas concluídas;
3. visitas com componente necessário para endpoint ausente / visitas que exigiam esse componente;
4. participantes cujo follow-up não pôde ser obtido apesar de esforços documentados / participantes devidos para follow-up.

Essas medidas devem permanecer separadas e com seus denominadores escritos na mesma linha.

### 3.4. A matriz de componentes tem utilidade agregada

A seção D não deve repetir as linhas de cada PFVR. Ela pode consolidar famílias de componentes para mostrar, no período, quais componentes foram esperados, completos, parciais, ausentes ou não aplicáveis.

A matriz é especialmente importante para detectar que a taxa geral de visitas parece aceitável enquanto um componente específico — imaging, PROM, ROM ou complication review — falha repetidamente.

### 3.5. A análise de causa evita culpa automática do participante

A seção E classifica causas em participant, site, workflow, protocol e unknown. A tese exige essa distinção: uma falha de retenção não deve ser automaticamente tratada como falha de execução do site.

Essa classificação deve ser baseada no que foi documentado nos PFVRs e nos registros de recuperação, não em uma nova investigação narrativa feita no FUCR.

### 3.6. G, H e J fecham o ciclo

A sequência tendência/interpretação → ação/escalonamento/efetividade → certificação é adequada. O FUCR precisa produzir uma decisão e uma rota, não apenas números.

---

## 4. Problemas críticos identificados

### 4.1. A definição das quatro medidas precisa ser literal e estável

A seção C usa expressões como `critical assessment`, `eligible visits` e `key time points`. Elas podem ser úteis, mas podem se afastar da formulação da tese se não forem definidas antes.

A versão final deve usar uma tabela de definição controlada para cada medida:

| Medida | Numerador | Denominador correto |
|---|---|---|
| Within-window visits | Visits completed within their applicable window | Visits expected in the review scope |
| Complete visits | Visits containing every component required by the CIP | Visits completed |
| Endpoint-critical omission | Visits missing a component needed for an endpoint | Visits that required that component |
| Follow-up not obtained | Participants whose follow-up could not be obtained despite documented efforts | Participants due for follow-up |

O FUCR não deve substituir os denominadores por `eligible visits`, `PFVRs reviewed` ou `visits at key time points` sem definir exatamente a relação com o denominador da tese.

### 4.2. C e C1 podem duplicar a mesma população

C registra numerador, denominador, resultado, resultado anterior e supporting count. C1 depois registra eligible participants, expected visits, completed visits, outside-window visits, missed/partial visits e PFVRs available.

Essa duplicação é aceitável somente se C1 for explicitamente uma tabela de reconciliação das bases, e não uma segunda tabela de indicadores.

**Ajuste recomendado:**

- manter C como tabela dos quatro resultados centrais;
- manter C1 como `Source Population Reconciliation`;
- colocar em C1 apenas os counts necessários para demonstrar de onde vieram os denominadores;
- não usar C1 para produzir uma segunda versão das mesmas proporções;
- exigir referência ao intervalo de PFVRs, continuation sheets ou data extract usado.

### 4.3. O FUCR não pode depender de “PFVRs available” sem reconciliação

`PFVRs available for review` não é necessariamente igual a `PFVRs expected`. Se o FUCR somente contar os documentos recebidos, pode produzir uma taxa aparentemente boa enquanto alguns registros não foram localizados.

A reconciliação deve distinguir:

- visits expected according to visit schedule;
- PFVRs expected;
- PFVRs received/located;
- PFVRs complete enough for aggregation;
- PFVRs missing or unresolved;
- visits excluded and the reason for exclusion.

Uma visita sem PFVR não deve desaparecer do denominador sem uma regra de exclusão documentada. Se a ausência do PFVR impedir a classificação, isso deve aparecer como lacuna de fonte e possível problema de data completeness.

### 4.4. D deve agregar componentes pré-definidos, não inventar categorias depois

A matriz D usa `Protocol-required imaging`, `Functional assessment / range of motion`, `Patient-reported outcome measure`, `Complication and interval-event review`, `Reoperation...` e `Rehabilitation...`.

Essas linhas só são auditáveis se o componente e sua aplicabilidade forem configurados antes do período ou extraídos de uma fonte controlada. O FUCR não deve decidir retrospectivamente que algo era “critical” porque falhou.

A configuração precisa identificar:

- component ID/name;
- visit types where required;
- endpoint-critical status;
- expected population/denominator;
- source field in PFVR or linked specialized record;
- rule version;
- responsible reviewer.

### 4.5. E usa faixas de atraso que podem não corresponder ao protocolo

As categorias `Late 1–7 days`, `Late 8–30 days` e `Late more than 30 days` podem ser úteis para análise interna, mas não podem substituir a janela definida pelo CIP.

O principal dado deve ser:

- days early/late relative to the applicable window;
- number of visits outside window;
- cause category;
- impact;
- linked PFVR reference.

As faixas só devem aparecer se forem previamente configuradas como uma estratificação analítica. Caso contrário, elas podem esconder atrasos clinicamente importantes dentro de uma faixa arbitrária.

### 4.6. E não deve repetir a avaliação individual do PFVR

A tabela de timing deve conter contagens e distribuição, não nomes, narrativas ou uma mini-review de cada caso. Referências a PFVR são necessárias para rastreabilidade de exceções, mas não para copiar o conteúdo de todos os PFVRs.

Uma referência pode ser:

```text
PFVR-014 to PFVR-019; PFVR-022; continuation sheet CS-02
```

Para uma tendência, a lista completa pode ficar em uma source reconciliation attachment ou controlled extract, com o FUCR apontando para essa localização.

### 4.7. F é amplo demais e pode invadir outros instrumentos

`Execution Consistency and Scientific Usability` é relevante, mas pode duplicar:

- IQL, quando o assunto é imaging quality;
- ICDL, quando o assunto é procedure/device execution;
- PFVR/E, quando o assunto é um resultado de uma visita;
- IMC, quando o assunto é execução do controle e evidência;
- PIR, quando o assunto é interpretação de performance.

O FUCR pode revisar execução e usability de forma agregada, mas deve fazê-lo por amostra definida ou por source summary. Ele não deve reavaliar cada imagem, cada ROM measurement ou cada PROM.

**Ajuste recomendado:** renomear ou restringir F para `Defined Sample and Usability Review`, com:

- sample/population;
- source groups;
- rule/version;
- conforming/concern;
- impact;
- linked record;
- limitation.

Quando a informação já estiver consolidada por IQL, ICDL ou outro instrumento, usar essa saída como fonte.

### 4.8. G precisa separar trend, concentration e decision

A seção G tem os campos `Signal or trend`, `Status`, `Where concentrated?`, `Current finding / comparison` e `Interpretation / next review`. Isso é adequado, mas a interpretação precisa ser baseada em uma regra previamente definida.

G deve responder:

- o resultado está dentro do rule/threshold?
- houve piora em relação ao período anterior comparável?
- há concentração por visit type, component, participant subgroup, assessor ou causa?
- é uma observação, uma revisão intensificada ou uma ação obrigatória?
- qual documento recebe a saída?

G não deve criar o threshold nem redefinir o conceito de `controlled` durante a revisão. A configuração da regra vem da arquitetura do indicador; o FUCR aplica a regra e documenta a situação.

### 4.9. H precisa distinguir containment, corrective action e preventive action

A tabela H mistura cause, impact/containment, corrective/preventive action, owner, due date, escalation, linked record, effectiveness e status.

Essa concentração é aceitável em um formulário curto, mas deve ficar claro que:

- containment protege as próximas visitas imediatamente;
- corrective action trata o problema observado;
- preventive action trata a causa sistêmica ou recorrente;
- a ação pode ser apenas local, ou ser encaminhada a IMC, SRR, CAPA, sponsor ou POT;
- effectiveness exige evidência em um período posterior.

Um FUCR não deve abrir um CAPA completo dentro de H. Deve registrar o sinal, a ação inicial e o link para o CAPA quando um CAPA for necessário.

### 4.10. I não deve ser apenas “outcome” sem regra de decisão

A seção I oferece `Controlled / Controlled with observation / Action required / Escalated / Not assessable`, o que é útil. Mas cada estado precisa de critérios documentados.

A classificação deve considerar os quatro core measures, a configuração de thresholds e a existência de qualquer endpoint-critical omission ou participant not recovered. A ausência de um componente endpoint-critical pode exigir ação mesmo quando a taxa geral de timing está acima do alvo.

`Not assessable` não pode ser usado para esconder dados ausentes. Deve registrar a limitação, sua causa e a ação para recuperar ou qualificar o dado.

---

## 5. Pontos de atenção na integração PFVR → FUCR

Esta é a parte mais importante da interface.

### 5.1. O PFVR registra; o FUCR conta e interpreta

| Pergunta | PFVR | FUCR |
|---|---|---|
| A visita aconteceu? | Registra a visita individual | Conta visitas esperadas/completadas |
| Estava dentro da janela? | Registra a data real e o estado daquela visita | Calcula a proporção no período |
| Quais componentes eram exigidos? | Lista os componentes da visita | Consolida por componente/visit type |
| Um componente foi completo, parcial, perdido ou tardio? | Registra a linha individual | Conta e compara a distribuição |
| Qual foi a causa? | Registra a causa da exceção | Agrupa causas e identifica concentração |
| Um resultado é utilizável? | Aponta para E/IQL/record especializado | Resume usabilidade por amostra ou fonte agregada |
| O que foi feito agora? | Registra resposta imediata individual | Avalia recorrência e necessidade de ação sistêmica |
| O que fazer a seguir? | J e K definem a rota daquela visita | H/I encaminham tendência, escalonamento e efetividade |

### 5.2. Não duplicar o conteúdo de D no FUCR

O FUCR não deve trazer novamente uma linha por cada participante e componente. Se fizer isso, ele deixa de ser uma revisão agregada e vira um segundo PFVR populacional.

A regra deve ser:

```text
PFVR row → standardized extract/count → FUCR measure
```

O FUCR mantém somente:

- numerador;
- denominador;
- definição e rule version;
- período/cut-off;
- causa agregada;
- supporting count;
- referências de origem;
- interpretação e decisão.

### 5.3. Separar visit-level status de component-level status

O PFVR deve entregar pelo menos duas camadas de estado:

```text
visit-level: completed / late / missed / partial
component-level: complete / partial / not performed / N/A
component timing: within window / outside window / not assessable
```

O FUCR não deve inferir component completeness apenas do status da visita. Uma visita `Completed` pode ter componente `Missing`; uma visita `Late` pode conter todos os componentes; uma visita `Partial` pode ter impacto endpoint-critical ou não.

### 5.4. Preservar os denominadores

Cada saída do PFVR que entra no FUCR precisa informar sua população de referência. O FUCR não deve receber apenas “compliant” ou “non-compliant”. Deve receber a situação que permite reconstruir a contagem:

- expected visit;
- completed visit;
- required component;
- component obtained;
- participant due;
- participant recovered/not recovered.

### 5.5. Reconciliar ausências antes de calcular

Antes de calcular o FUCR, deve existir uma etapa de reconciliação:

1. gerar a lista de participantes e visitas devidas no período;
2. conferir os PFVRs esperados contra os PFVRs localizados;
3. identificar PFVRs sem fechamento ou sem componente essencial;
4. separar missed visit de missing document;
5. registrar exclusões e justificativas;
6. congelar o data cut-off;
7. executar as quatro medidas.

Sem isso, o FUCR pode confundir “a visita não ocorreu” com “o PFVR não foi encontrado”.

### 5.6. Usar referências, não cópias

Para cada medida agregada, o FUCR deve indicar a fonte e o intervalo de registros, por exemplo:

```text
Source group: PFVR v0.5, PFVR-001–PFVR-028, continuation sheet CS-01,
visit schedule rule VS-02 v1.1, cut-off 31 Oct 2026.
```

Se uma linha individual sustenta uma decisão importante, referenciar o PFVR específico. Não copiar a narrativa clínica, o resultado de imagem ou o relato do participante para dentro do FUCR.

### 5.7. Manter exceções no PFVR e tendências no FUCR

Uma exceção individual permanece no PFVR/J e no record especializado correspondente. O FUCR registra somente:

- que a exceção entrou na contagem;
- sua categoria de causa;
- seu efeito sobre a medida;
- sua referência;
- se ela se repetiu ou formou concentração;
- se uma ação sistêmica foi necessária.

### 5.8. Não transformar o FUCR em PIR

O FUCR produz a revisão operacional de follow-up. O PIR pode receber os resultados do FUCR e integrá-los com enrollment, deviations, safety, procedure consistency e data completeness.

O FUCR pode aplicar thresholds próprios de follow-up definidos no início do estudo, mas não deve interpretar o desempenho global do site nem decidir entre todos os indicadores do framework. Essa integração pertence ao PIR/POT.

---

## 6. Arquitetura recomendada para a próxima versão

### Página 1 — Scope, Purpose and denominator configuration

- cabeçalho com estudo, site, período, cut-off, população e reviewer;
- A. Purpose and Use;
- B. source population and denominator map;
- definição curta dos quatro core measures;
- source reconciliation boundary;
- previous period comparability rule.

### Página 2 — Core measures and population reconciliation

- C. quatro medidas centrais;
- C1. counts usados para reconciliar numeradores e denominadores;
- PFVR source group, record range, continuation sheets e exclusions.

### Página 3 — Component and timing aggregation

- D. component completeness matrix;
- E. timing/window analysis;
- atraso em dias relativos à regra aplicável;
- causa e referência agregada/individual quando necessário.

### Página 4 — Defined sample, trend and decision

- F. defined sample and scientific usability review;
- G. trend/concentration and interpretation;
- regra aplicada, status, concentration e next review.

### Página 5 — Action, effectiveness and sign-off

- H. action/escalation/effectiveness;
- I. overall outcome and cadence;
- J. certification/accountability;
- output linkage para IMC, SRR, CAPA, PIR, POT ou sponsor.

A estrutura atual de cinco páginas pode ser mantida, desde que a paginação preserve espaço de escrita e não reduza a legibilidade da tabela central.

---

## 7. Saídas corretas do FUCR

O FUCR deve produzir:

1. quatro medidas com numerador, denominador, resultado e interpretação;
2. reconciliação da população e dos PFVRs;
3. distribuição de componentes completos, parciais, missing, N/A e not assessable;
4. distribuição de visitas early/late/missed conforme regra aplicável;
5. causas agrupadas por participant, site/process, protocol/design e unknown;
6. tendências ou concentrações por visit type, component, period ou causa;
7. decisão operacional: controlled, controlled with observation, action required, escalated ou not assessable;
8. ações com owner, prazo, linked record e evidência de efetividade;
9. referências que permitam retornar aos PFVRs sem copiar o conteúdo deles.

### Saídas para outros instrumentos

| Destinatário | Saída do FUCR |
|---|---|
| PIR | Core measures, denominators, trend, interpretation e source group. |
| IMC | Falha operacional do controle de follow-up que exige verificação focal. |
| SRR | Vulnerabilidade persistente de processo, retenção, janela ou componente. |
| CAPA | Problema recorrente/material que não foi resolvido pela resposta local. |
| POT | Tema que requer decisão ou oversight do PI. |
| Sponsor | Problema de desenho do protocolo, janela, componente ou requirement externo. |
| PFVR | Não há retroalimentação para reescrever registros fechados, salvo correção documental controlada. |

---

## 8. O que deve ser mantido, reduzido ou alterado

| Elemento | Decisão | Motivo |
|---|---|---|
| FUCR como revisão site-period aggregate | Manter | É a função prevista na tese. |
| Purpose and Use | Manter | Define a fronteira com PFVR. |
| Denominator Map | Manter e formalizar | Evita indicadores não auditáveis. |
| Four Core Measures | Manter integralmente | São o núcleo do follow-up compliance da tese. |
| Supporting Counts | Manter como reconciliação | Não criar uma segunda camada de indicadores. |
| Component Matrix | Manter com configuração prévia | Agrega o PFVR sem inventar criticality retrospectiva. |
| Timing Analysis | Manter, retirar arbitrariedade | Usar janela CIP e dias fora da janela; bins apenas se configurados. |
| Execution/Usability | Manter como amostra/fonte agregada | Não duplicar IQL, PFVR, ICDL ou IMC. |
| Trend/Concentration | Manter | É a ponte entre resultado e ação. |
| Action Log | Manter | Deve distinguir containment, corrective, preventive e effectiveness. |
| Overall Outcome | Manter com critérios | Resultado precisa ser justificável pela regra. |
| Certification | Manter | Confirma população, fontes, denominadores e ações. |

---

## 9. Checklist para a reconstrução do FUCR

1. A população, período e cut-off estão definidos antes dos indicadores?
2. Os quatro denominadores da tese aparecem literalmente e separadamente?
3. C1 é reconciliação de fontes, e não uma segunda tabela de indicadores?
4. O documento distingue expected visits de PFVRs localizados?
5. Uma missing PFVR não desaparece do denominador sem justificativa?
6. D usa componentes configurados antes do período de revisão?
7. E usa a janela do CIP e não faixas arbitrárias como substituto?
8. F não reavalia individualmente imagens, PROMs, ROM ou clinical findings?
9. G aplica uma regra de interpretação já definida?
10. H registra ação e aponta para CAPA/IMC/SRR/POT sem duplicá-los?
11. I diferencia controlled, observation, action required, escalated e not assessable?
12. Cada indicador consegue apontar para PFVR IDs, extracts e continuation sheets?
13. O PIR recebe resultados e referências, não uma cópia inteira do FUCR?
14. O documento não transforma falha de retenção em falha do site sem evidência de causa?
15. Todas as tabelas permanecem dentro dos rodapés e o Editor v2 permite editar todas as células e linhas relevantes?

---

## 10. Conclusão

O FUCR é um instrumento necessário e não deve ser eliminado ou fundido com o PFVR. A diferença essencial é de granularidade e de decisão:

```text
PFVR = what happened at one participant visit?
FUCR = what does the pattern across the defined population and period show?
PIR = what does this follow-up result mean within overall site performance?
```

A integração correta exige que o PFVR forneça estados e referências suficientemente estruturados para que o FUCR conte sem reinterpretar, enquanto o FUCR deve permanecer agregado e não copiar o registro clínico individual.

A revisão do FUCR deve, portanto, ser uma revisão de precisão e fronteira, não uma reconstrução radical. O núcleo dos quatro indicadores deve ser preservado. Os principais ajustes são: reforçar a reconciliação PFVR esperados versus localizados, estabilizar denominadores, impedir duplicação entre C/C1/D/E, restringir F a uma amostra ou fonte agregada e deixar explícita a ponte de saída para PIR, IMC, SRR, CAPA e POT.

---

## 11. Fontes verificadas

- Tese completa (29-10), seção 4.5.3: follow-up compliance, quatro medidas com denominadores próprios, atribuição de causa, thresholds e rota de ação.
- Tese completa (29-10), seção 4.4.3: cada visita documentada no PFVR; componentes, janela, exceções e ação registrados no nível individual.
- Tese completa (29-10), seção 4.6.2: FUCR fornece indicadores de drift a partir de registros produzidos por outros instrumentos.
- Tese completa (29-10), Appendix T: PFVR registra uma visita de um participante.
- Tese completa (29-10), Appendix U: FUCR mede follow-up performance across a cohort and a period, not one visit at a time.
- PFVR v0.5 e sua análise formal: D como registro primário de componentes; E como avaliação de utilizabilidade; J como rota de exceção; K como outcome individual.
- FUCR v0.3: seções A–J, mapa de denominadores, quatro core measures, matriz de componentes, timing, consistência/usabilidade, tendência, ações e certificação.
- Operational Quality Form Templates skill: separação entre revisão individual e performance agregada, regra de não duplicação, denominadores e interfaces de saída.
