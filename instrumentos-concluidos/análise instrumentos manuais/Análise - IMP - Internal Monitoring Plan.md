# Análise e especificação estrutural — IMP: Internal Monitoring Plan

**Status:** documento criado do zero para orientar a construção futura do HTML. Não existe, nesta etapa, um HTML anterior do IMP para revisar.

## 1. O que é o IMP em termos simples

O **Internal Monitoring Plan (IMP)** é o documento que responde, antes do início da inclusão, à seguinte pergunta:

> **Como este site vai verificar, por conta própria e de forma proporcional ao risco, se os seus controles críticos estão sendo executados, documentados e funcionando durante a investigação?**

Ele não é o documento que faz a revisão. Ele define a revisão.

A distinção essencial é:

```text
IMP = planeja o monitoramento interno
IMC = executa uma revisão prevista no plano
PIR/FUCR/CSST = produzem análises específicas que podem alimentar a decisão
POT/MRL = registram decisões de oversight quando necessário
CAPA/SRR = recebem problemas que exigem correção ou atualização de risco
```

Se o IMP estiver corretamente preenchido, outra pessoa deve conseguir abrir o IMC e saber:

- quais domínios precisam ser verificados;
- com que frequência;
- em que momento ou após qual trigger;
- qual população ou amostra deve ser examinada;
- qual fonte autoritativa deve ser usada;
- quem pode revisar;
- qual é a regra para decidir se o controle funcionou;
- o que deve acontecer quando o resultado for negativo ou incerto.

Sem o IMP, o IMC corre o risco de virar uma revisão improvisada, feita de maneira diferente em cada ciclo e depois de os resultados já serem conhecidos.

---

## 2. O que o IMP não é

O IMP não deve ser:

- um checklist preenchido depois da revisão;
- uma segunda versão do IMC;
- uma lista genérica de SOPs;
- uma cópia do sponsor Monitoring Plan;
- um plano estatístico;
- um registro de findings;
- um registro de CAPAs;
- um indicador de performance;
- um risk register completo;
- um calendário sem regras de amostragem;
- uma justificativa para alterar thresholds depois de ver os resultados.

O sponsor continua responsável pelo sistema de monitoring independente do site. O IMP complementa esse sistema ao organizar a **verificação interna daquilo que o site consegue controlar** entre as visitas ou revisões do sponsor.

O IMP também não deve prometer que o site detectará antes do sponsor todos os problemas. Sua função é garantir que o site tenha um método próprio, proporcional e pré-definido para reconhecer falhas dentro das suas responsabilidades.

---

## 3. Decisão que o IMP deve suportar

Depois de preencher e aprovar o IMP, o responsável deve conseguir decidir:

> **Is the site's internal verification system sufficiently defined to detect, at appropriate intervals or triggers, failures in the controls that the site is responsible for, using named reviewers, defined samples, authoritative sources, fixed criteria and controlled escalation routes?**

O IMP não decide se o controle funcionou em um ciclo específico. Essa decisão pertence ao IMC.

O IMP decide se o sistema de revisão está suficientemente planejado para que o IMC possa produzir uma conclusão reproduzível.

---

## 4. Unidade de análise

A unidade principal do IMP é:

```text
one site + one investigation + one approved monitoring plan + one period of validity
```

Dentro do plano, cada linha operacional representa:

```text
one internal verification check + its scope + frequency/trigger + sample rule + reviewer + response route
```

O plano deve ter:

- um ID próprio;
- site e investigation identificados;
- versão;
- data de aprovação;
- período de validade;
- status: draft, approved, superseded ou retired;
- relação com a versão anterior, quando aplicável.

O IMP pode ser atualizado, mas uma alteração depois do início da investigação deve ser controlada e aplicada somente de forma prospectiva, salvo quando uma decisão formal determinar outra coisa e documentar o motivo.

---

## 5. Base na tese

A tese define a internal verification como uma revisão do próprio conduct e da documentação do site em intervalos definidos, paralela ao monitoring independente do sponsor.

Ela determina que, antes da inclusão, o site deve:

1. definir a frequência e a amostra para cada check;
2. designar um reviewer;
3. definir o trigger para uma revisão antecipada;
4. escolher os dez checks aplicáveis ou um subconjunto justificado;
5. definir as fontes dos dados críticos;
6. estabelecer as regras antes de os resultados existirem;
7. iniciar a primeira revisão após as primeiras inclusões, antes da rotina, para capturar problemas de workflow cedo.

Os dez checks da tese são:

1. **Sterile release to use**;
2. **Implant traceability and component reconciliation**;
3. **Instrumentation and operating-room readiness**;
4. **Operative documentation**;
5. **Imaging usability and timing**;
6. **Follow-up execution**;
7. **Endpoint data agreement**;
8. **Timeliness and closure**;
9. **External context**;
10. **Complication monitoring**.

O IMP deve contemplar os dez checks. Um site pode selecionar um subconjunto quando o nível de implementação ou o risk assessment justificar, mas precisa registrar:

- quais checks foram excluídos;
- por que não se aplicam ou não são necessários;
- qual proxy assume a função;
- quem aprovou a exclusão;
- qual trigger faria o check voltar a ser incluído.

---

## 6. Relação com o ciclo de vida

O IMP é criado durante start-up, depois de o site ter definido:

- RACI e funções;
- treinamento e release;
- credenciamento cirúrgico quando aplicável;
- SRR e controles locais;
- fontes e registros críticos;
- nível de implementação;
- instrumentos especializados que estarão em uso.

O fluxo recomendado é:

```text
Feasibility
→ capacity and risk assessment
→ RACI / training / authorization
→ SRR
→ define critical sources and controls
→ IMP
→ PI/start-up approval
→ first inclusion
→ first triggered IMC
→ routine IMC cycles
→ updates only prospectively
```

O IMP não deve ser aprovado antes de o site saber que instrumentos e fontes realmente estarão disponíveis. Porém, ele deve estar aprovado antes da primeira inclusão, porque sua frequência, amostra e critérios não podem ser definidos depois de observar os primeiros resultados.

---

## 7. Princípios de desenho do IMP

### 7.1. Planejar antes de conhecer o resultado

O IMP deve separar:

- regra planejada;
- resultado observado;
- decisão posterior.

Ele pode ser atualizado por uma mudança controlada, mas não deve ser reescrito para tornar um resultado retrospectivamente aceitável.

### 7.2. Proporcionalidade ao risco

A frequência e o tamanho da amostra devem responder ao risco e à velocidade do fenômeno.

Exemplos:

- safety reporting pode exigir acompanhamento por evento e revisão periódica;
- learning curve pode depender do número de cirurgias, não do calendário;
- imaging pode exigir revisão de cada image set ou uma amostra definida;
- follow-up pode ser revisado mensal ou trimestralmente conforme volume e duração;
- external context pode ser trimestral ou triggered;
- complication monitoring pode ter revisão periódica e trigger imediato para cluster.

Não criar um calendário mensal idêntico para todos os instrumentos.

### 7.3. Independência relativa

O IMP deve nomear quem revisa cada check e quem executa o trabalho.

A regra preferida é:

```text
reviewer ≠ person who performed the activity
```

Se uma equipe pequena não permitir separação completa, o IMP deve registrar:

- a limitação;
- a revisão por peer treinado, quando possível;
- o oversight do PI;
- o critério para reavaliação da separação.

O IMP não deve simplesmente colocar “PI oversight” como substituto genérico de qualquer reviewer.

### 7.4. Fonte autoritativa

Cada check deve informar qual registro será considerado authoritative. Não basta listar “source documents”.

Exemplos:

- sterile release: accountability, storage/temperature, device release record;
- implant traceability: ICDL, labels, UDI/lot record, operative note, CRF;
- imaging: IQL, imaging charter/manual, image archive;
- follow-up: PFVR, FUCR and relevant source record;
- endpoint agreement: source record, CRF and reconciliation record;
- complication monitoring: SCML, SART and CSST;
- timeliness: source timestamp, report, query, closure record;
- external context: controlled search/review record.

O IMP não deve criar uma nova fonte paralela quando já existe um registro especializado.

### 7.5. Regra de ação pré-definida

Cada check deve prever o que acontece quando o resultado for:

- satisfactory/effective;
- partial;
- not performed;
- evidence unavailable;
- not assessable;
- recurrent or material.

O IMP define a rota. O IMC registra o caso concreto.

---

## 8. Arquitetura proposta do documento

A arquitetura recomendada é um plano controlado com uma matriz operacional central, não um texto longo.

### Página 1 — Document identity, Purpose and Use

Conteúdo:

- título e versão;
- IMP ID;
- site/investigation;
- date of approval;
- effective from;
- supersedes;
- prepared by;
- approved by;
- status;
- A. Purpose and Use;
- Unit of analysis;
- Decision support;
- Inputs;
- Outputs.

O Purpose and Use deve explicar que o IMP define o escopo, a frequência, as amostras, os reviewers, os triggers e as rotas de resposta para a internal verification do site.

### Página 2 — Plan boundary and governing inputs

Seção B:

- investigation/site scope;
- implementation level;
- lifecycle phases covered;
- review period or duration;
- sponsor monitoring interface;
- applicable CIP/charter/manual versions;
- SRR version;
- RACI/role structure reference;
- source map reference;
- known constraints;
- excluded responsibilities.

Essa seção deve deixar claro que o IMP planeja controles sob responsabilidade do site e não substitui sponsor monitoring.

### Página 3 — Internal verification domain configuration

Seção C: tabela dos dez checks.

Colunas recomendadas:

| Check ID | Internal verification domain | Applies? | CtQ / risk link | Control to verify | Authoritative source | Scope level |
|---|---|---|---|---|---|---|

O campo `Applies?` deve permitir Yes, No — not applicable, No — covered by proxy, ou Deferred pending condition. Toda exclusão precisa de racional.

### Página 4 — Schedule and trigger matrix

Seção D: frequência planejada.

| Check ID | Routine frequency / timing basis | First review | Earlier-review trigger | Review window | Responsible reviewer | Backup / escalation |
|---|---|---|---|---|---|---|

A coluna `timing basis` deve permitir distinguir:

- calendar-based;
- event-based;
- case-sequence-based;
- threshold-based;
- milestone-based;
- triggered.

Exemplos:

- first review after first inclusions;
- after first five procedures for a surgeon;
- monthly;
- quarterly;
- after a serious or unexpected event;
- after protocol amendment;
- after departure of a key person;
- after equipment failure;
- after a cluster or indicator threshold.

### Página 5 — Sample and evidence plan

Seção E: amostragem e evidência.

| Check ID | Population | Sample rule | Minimum sample / census rule | Review period | Evidence expected | Limitations / replacement rule |
|---|---|---|---|---|---|---|

A regra precisa dizer o que acontece quando:

- a população é menor que a amostra;
- o registro selecionado não está disponível;
- a amostra contém uma exceção;
- há repeat/replacement;
- a revisão de um evento exige census instead of sample;
- a amostra precisa ser aumentada após um sinal.

Não inventar um número universal para todos os checks. O IMP deve permitir que o site defina e justifique o número conforme volume e risco.

### Página 6 — Review method and decision criteria

Seção F: método de revisão.

| Check ID | Review method | Execution criterion | Evidence criterion | Effectiveness / usable criterion | Required record in IMC |
|---|---|---|---|---|---|

Essa seção transforma cada domínio em uma regra executável. O reviewer do IMC não deve ter de inferir o que “adequate” significa.

### Página 7 — Response and escalation routes

Seção G:

| Finding state | Immediate route | Owner | Linked instrument | Escalation trigger | Effectiveness follow-up |
|---|---|---|---|---|---|

Rotas possíveis:

- no further action;
- IMC action log;
- PFVR/FUCR clarification;
- IQL/ICDL/SART/SCML update;
- PIR review;
- SRR update;
- CAPA;
- POT/PI decision;
- MRL review;
- sponsor notification or sponsor decision.

O IMP deve diferenciar resposta imediata de CAPA. Nem todo finding abre CAPA.

### Página 8 — Plan approval, change control and implementation check

Seção H:

- reviewer role and backup confirmation;
- staff communication/training required;
- first review due;
- readiness confirmation;
- approval signatures;
- change log;
- effective date of changes;
- reason for revision;
- impact on future cycles;
- confirmation that previous periods are not silently rewritten.

A aprovação do PI deve confirmar que o plano é executável com os recursos disponíveis, não que todos os resultados futuros serão bons.

---

## 9. Os dez checks como linhas do IMP

### IMP-01 — Sterile release to use

O plano deve definir:

- qual registro demonstra integrity, expiry and storage;
- quando a verificação ocorre;
- se é census ou amostra;
- quem revisa;
- trigger para breach, substitution or temperature excursion;
- rota para ICDL, deviation, device route, SRR ou CAPA.

### IMP-02 — Implant traceability and component reconciliation

Deve definir como comparar:

- operative note;
- implant labels/UDI/lot/serial;
- accountability record;
- ICDL;
- CRF.

Amostragem pode ser por procedimento, componente ou census conforme risco. A regra deve preservar a reconciliação entre configuração planejada e implantada.

### IMP-03 — Instrumentation and operating-room readiness

Deve definir quando verificar:

- availability;
- compatibility;
- malfunction;
- substitutions;
- readiness record;
- procedural issue/device-deficiency route.

O IMP não substitui o ICDL; define como o site verificará se a preparação e a documentação estão funcionando.

### IMP-04 — Operative documentation

Deve definir amostra, fonte e critério para confirmar que o operative note permite interpretar:

- final configuration;
- intraoperative decisions;
- substitutions;
- deviations;
- complications;
- relevant times and identifiers.

A ausência de detalhes não deve ser tratada como simples atraso documental se impedir reconstrução posterior.

### IMP-05 — Imaging usability and timing

Deve referenciar SIRR, Imaging Charter, IQL e PFVR/PSEAR quando aplicável. Deve definir:

- image-set sample/census;
- timing;
- required views/sequences;
- technical quality;
- local-use decision;
- repeat/second-review trigger.

O IMP não avalia cada imagem; define o método pelo qual o IMC verificará o processo.

### IMP-06 — Follow-up execution

Deve referenciar PFVR e FUCR. Deve definir:

- periodicidade;
- população de visitas;
- amostra ou census;
- window and component completeness;
- endpoint-critical component treatment;
- lost-to-follow-up trigger;
- escalation route.

O IMC verifica o controle; o FUCR calcula a performance agregada.

### IMP-07 — Endpoint data agreement

Deve definir:

- quais fields são endpoint-critical;
- qual foi a fonte inicial fora do CRF;
- como será selecionada a amostra;
- como será feita a comparação;
- tolerância para discrepância;
- reconciliação e explicação;
- rota para PIR, deviation, CAPA ou sponsor.

Esse check não pode ser omitido, pois está expressamente na tese e no desenho revisado do IMC.

### IMP-08 — Timeliness and closure

Deve definir os tempos que serão verificados:

- operative notes;
- data entry;
- queries;
- safety follow-up;
- corrective actions;
- other CIP-defined timelines.

A regra deve distinguir atraso que é somente sinal de investigação de atraso que exige ação imediata ou escalonamento.

### IMP-09 — External context

Deve definir:

- quais fontes externas serão revistas;
- periodicidade;
- owner;
- escopo do implant/procedure;
- safety alerts, field notices, literature or registry findings;
- como documentar que a busca foi feita;
- quando uma informação externa altera SRR, POT, sponsor communication or monitoring scope.

O IMP não deve transformar o site em um sistema de vigilância regulatória completo sem definir limites.

### IMP-10 — Complication monitoring

Deve definir:

- frequência da revisão;
- relação com SART, SCML e CSST;
- quando usar census e quando usar aggregate review;
- trigger para serious event, cluster, concentration by surgeon/component;
- route to SLCT, sponsor/device deficiency, SRR, CAPA or POT.

A análise do padrão pertence ao CSST. O IMP apenas define quando e como a verificação de que a monitoring ocorreu será feita.

---

## 10. Agendamento: calendário não é suficiente

O IMP deve combinar três tipos de regra.

### 10.1. Routine schedule

Exemplos:

- monthly;
- quarterly;
- annually;
- after each defined case milestone;
- at each phase gate.

### 10.2. First review rule

A tese exige uma primeira revisão após as primeiras inclusões, antes da rotina, para detectar falhas de workflow quando poucos participantes foram expostos.

O IMP deve ter um campo explícito:

```text
First internal verification due after: ______
```

### 10.3. Early trigger

A revisão deve ocorrer antes do próximo ciclo quando houver:

- serious adverse device effect or serious safety signal;
- complication cluster;
- important protocol deviation;
- repeated endpoint discrepancy;
- imaging failure pattern;
- device or equipment malfunction;
- protocol amendment;
- departure of a key person;
- change in reviewer or service;
- sponsor finding requiring local response;
- CAPA failure or reopening;
- change in risk rating or implementation level.

A lista deve ser adaptável. O IMP não deve transformar qualquer observação menor em trigger automático.

---

## 11. Amostragem e census

A qualidade do IMP depende mais da regra de amostragem do que de um número fixo.

Cada linha deve responder:

- qual é a população;
- qual é a unidade da população;
- qual é a regra de seleção;
- qual é o mínimo;
- quando é census;
- como documentar seleção;
- quando aumentar a amostra;
- como lidar com registros indisponíveis.

Exemplos de população correta:

- procedures, não participants, para implant traceability;
- image sets, não somente visits, para imaging;
- visits, não components isolados, para uma revisão geral de follow-up;
- endpoint-critical fields, não todos os fields do CRF, para endpoint agreement;
- reportable events, normalmente census, para safety timeliness;
- complications, cases or events conforme o objetivo do CSST/SCML.

Nunca misturar participantes, visitas, procedimentos e eventos no mesmo denominador.

---

## 12. Mudança de plano

O IMP deve incluir uma change-control table:

| Change ID | Section/check affected | Previous rule | New rule | Reason | Effective from | Approved by |
|---|---|---|---|---|---|---|

Regras:

1. mudança feita antes do novo período pode valer prospectivamente;
2. resultado já conhecido não pode ser o motivo oculto da mudança;
3. uma mudança triggered deve preservar o plano original;
4. alteração de escopo, frequência, threshold, reviewer ou sample rule exige aprovação;
5. o IMC deve registrar a versão do IMP executada;
6. períodos anteriores não devem ser reescritos silenciosamente.

---

## 13. Interfaces com outros instrumentos

### IMP → IMC

Esta é a relação principal.

O IMP entrega ao IMC:

- check em escopo;
- período/trigger;
- sample rule;
- reviewer;
- source map;
- execution criterion;
- evidence criterion;
- effectiveness criterion;
- escalation rule;
- IMP version.

O IMC devolve:

- review completed;
- findings;
- limitations;
- actions;
- effectiveness follow-up;
- recommendation for plan change.

### SRR → IMP

O SRR informa quais riscos e controles precisam de maior frequência, sample ou trigger. O IMP não deve substituir o SRR nem inventar criticidade sem referência.

### RACI/CCDM/TRE → IMP

O IMP usa:

- função accountable;
- reviewer autorizado;
- backup;
- requisito de treinamento;
- limitação de autoridade.

Não deve atribuir uma tarefa a uma pessoa que não esteja liberada para ela.

### IQL/ICDL/PFVR/SART/SCML/FUCR → IMP

Esses instrumentos fornecem as fontes e unidades de análise que o IMP precisa planejar. O IMP não deve duplicar seus registros.

### PIR → IMP

PIR pode informar quais indicadores ou tendências exigem aumento temporário de verificação. O IMP define prospectivamente o trigger, enquanto o PIR registra o resultado.

### POT → IMP

O POT aprova decisões de PI e pode receber uma proposta de alteração do IMP quando o risco, a capacidade ou o oversight mudarem.

### MRL → IMP

No gate de start-up, o MRL ou POT, conforme o nível de implementação, pode confirmar que o IMP foi aprovado e está executável. O MRL não substitui o plano.

### CAPA → IMP

Um CAPA pode exigir aumento temporário de sample, revisão triggered ou novo check. A mudança deve ser registrada no change control do IMP e aplicada prospectivamente.

---

## 14. Escalabilidade

O IMP precisa funcionar em diferentes níveis de implementação.

### Nível mínimo

Um site pode não manter todos os instrumentos especializados, mas ainda precisa definir como os controles serão verificados. O proxy pode ser:

- oversight meeting;
- CRF/source review;
- existing QMS record;
- PI review;
- sponsor-supported review.

O IMP deve registrar o proxy e a evidência mínima exigida.

### Nível intermediário

O site usa IMP e IMC com registros especializados para imaging, follow-up, safety, complications e indicators conforme o risk assessment.

### Nível completo

O site mantém os dez checks e usa as fontes especializadas com periodicidade, amostragem e triggers próprios.

A forma muda, mas a obrigação de demonstrar que a verificação ocorreu e que os findings tiveram destino não desaparece.

---

## 15. Arquitetura da decisão no IMP

Cada linha operacional precisa seguir esta cadeia:

```text
CtQ / risk
→ control to verify
→ authoritative source
→ population and sample
→ routine frequency
→ early trigger
→ reviewer
→ criteria
→ IMC record
→ response route
```

Se uma linha não puder completar essa cadeia, ela ainda não é um plano operacional; é apenas um tópico.

Exemplo de linha adequada:

| Check | Control | Source | Sample | Frequency | Trigger | Reviewer | IMC output |
|---|---|---|---|---|---|---|---|
| Endpoint data agreement | Sampled endpoint-critical fields agree with source and CRF; discrepancies are corrected and explained | source record + CRF + reconciliation record | 5 fields per first 10 participants, then 10% per quarter, with census after discrepancy trigger | After first inclusions and quarterly | unresolved discrepancy or recurrence | trained peer reviewer | IMC domain result; PIR/CAPA route if needed |

O exemplo serve para demonstrar a lógica, não para impor esses números a todos os estudos. Os valores finais devem ser definidos pelo site e justificados pelo risco, volume e CIP.

---

## 16. O que o IMP deve produzir

O IMP produz cinco resultados controlados:

1. **Scope decision** — quais checks serão executados e quais são excluídos;
2. **Schedule decision** — quando cada check será revisado;
3. **Sampling decision** — qual população e amostra serão usadas;
4. **Responsibility decision** — quem revisa, quem substitui e quem escala;
5. **Response decision** — o que acontece para cada estado de resultado.

Não produz findings ou counts do estudo. Isso será produzido pelo IMC, PIR, FUCR, CSST ou outros instrumentos.

---

## 17. Checklist de validação do futuro HTML

1. O documento deixa claro, na primeira página, que IMP planeja e IMC executa?
2. Existe um IMP ID e uma versão controlada?
3. Há site, investigation, effective date, status e período de validade?
4. O plano foi desenhado antes da primeira inclusão?
5. Os dez checks da tese aparecem ou cada exclusão tem justificativa e proxy?
6. Cada check tem CtQ/risk link?
7. Cada check tem controle observável?
8. Cada check tem fonte autoritativa?
9. A população e a unidade de amostragem estão explícitas?
10. A regra de amostra, census e aumento de amostra está definida?
11. Existe first review rule?
12. Existe rotina calendar-based, event-based ou case-based quando aplicável?
13. Existem early triggers objetivos?
14. O reviewer e o backup estão nomeados por função?
15. A independência relativa está documentada?
16. O método de review está definido?
17. Execution, evidence e effectiveness criteria estão separados?
18. Cada estado negativo ou incerto tem response route?
19. As rotas distinguem IMC action, CAPA, SRR, POT, sponsor, safety e other?
20. O IMP referencia RACI/CCDM/TRE sem atribuir tarefas a pessoas não liberadas?
21. A versão do IMP executada aparece no IMC?
22. Há change-control table?
23. Mudanças valem prospectivamente?
24. O plano distingue sponsor monitoring de internal verification?
25. O site pode usar proxy quando a implementação for menor?
26. A aprovação do PI está prevista?
27. A comunicação/treinamento do plano está documentada?
28. O documento possui espaço suficiente para matriz e justificativas?
29. A matriz pode ser continuada em páginas adicionais sem perder o mesmo IMP ID?
30. O futuro editor v2 permitirá editar todas as linhas, caixas, justificativas e páginas de continuação?

---

## 18. Conclusão

O IMP é o documento que transforma a intenção de “o site vai se monitorar” em um compromisso operacional verificável.

Ele deve ser criado antes da primeira inclusão, depois de o site entender seus riscos, responsabilidades, fontes e capacidade. Seu trabalho é fixar antecipadamente:

```text
what will be checked
when it will be checked
how much will be checked
who will check it
which source will be authoritative
what counts as adequate
what triggers earlier review
what happens when the result is negative
```

O IMP não deve ser longo por ser conceitualmente importante. Ele deve ser uma matriz clara de decisões prévias, com notas curtas para explicar exceções, proxies e mudanças.

A recomendação é construir o primeiro HTML do IMP como um **plano controlado de oito páginas**, com uma matriz central landscape e blocos de aprovação, change control e implementação. Não tentar transformar o IMP em uma narrativa acadêmica nem em um IMC antecipado.

A linha-mestra é:

```text
SRR and site capacity
→ IMP defines internal verification
→ IMC executes the defined review
→ findings go to the appropriate instrument
→ effectiveness and plan changes are controlled prospectively
```

---

## 19. Fontes verificadas

- Tese completa (29-10), seção 4.4.1: internal verification, dez checks, frequência, amostra, reviewer, triggers e relação IMP–IMC.
- Tese completa (29-10), seção 4.5: performance indicators, regras fixadas antes da inclusão, thresholds e relação com CAPA.
- Tese completa (29-10), seção 4.5.7: corrective/preventive action, effectiveness, closure, risk update e mudança de processo.
- Tese completa (29-10), seção 5.3.1: ordem de implementação dos instrumentos, definição do escopo de internal verification antes da inclusão e first review after first inclusions.
- Tese completa (29-10), seção 5.3.2: review cycle, calendário proporcional, review triggers e relação com oversight meeting.
- Tese completa (29-10), Appendix M: Internal Monitoring Plan — documento que define como o site monitora internamente.
- Tese completa (29-10), Appendix N: Internal Monitoring Checklist — documento que executa a revisão definida no IMP.
- Análise do IMC v1.4: distinção entre IMP como plano e IMC como execução; dez checks e necessidade de endpoint data agreement.
- Operational Quality Form Templates skill: CTQ → risco/controle → evidência → resultado → ação → efetividade, separação entre desenho de controle e monitorização operacional.
