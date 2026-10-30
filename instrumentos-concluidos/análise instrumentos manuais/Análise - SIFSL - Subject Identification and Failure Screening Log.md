# Análise — SIFSL: Subject Identification and Failure Screening Log

**Status:** instrumento a construir; não foi localizada nenhuma versão HTML, PDF, blank ou filled anterior no workspace, uploads ou branches autorizados.  
**Escopo desta análise:** especificação de construção baseada na tese e nas interfaces já aprovadas para PSEAR e PIR. Não criar ou alterar HTML nesta etapa.

---

## 1. Decisão, unidade de análise e papel no sistema

> **At this cut-off, can the site account for every coded person considered for the investigation, identify the current or final screening outcome, and reconcile every eligibility decision and enrollment with the relevant controlled record?**

Unidade de análise: **uma pessoa codificada considerada para a investigação, em uma linha de log**.

O SIFSL é o registro administrativo e populacional do percurso de screening. Ele mantém o universo de pessoas consideradas para o estudo, qualquer que seja o resultado: pre-screened only, screening active, eligible awaiting enrolment, enrolled, not eligible, withdrew/discontinued before enrolment ou outro outcome controlado.

Ele existe para responder a perguntas que o PSEAR não responde sozinho:

- Quem entrou ou foi considerado no funil de screening?
- Cada candidato tem um outcome atual ou final?
- Cada decisão de elegibilidade possui a referência PSEAR/controlled screening record correspondente?
- Cada pessoa enrolled é localizável no SIFSL e no record de enrollment?
- Qual a categoria de non-inclusion ou withdrawal, sem copiar informação clínica sensível?
- Há linhas pendentes, outcomes ausentes ou desencontro entre SIFSL, PSEAR e enrollment record?
- A distribuição de razões de non-inclusion sugere uma barreira de eligibility, consent, recrutamento ou processo que merece revisão no PIR/IMC/POT?

O SIFSL não decide elegibilidade. O PSEAR decide. O SIFSL não calcula Enrollment Quality. O PIR calcula. O SIFSL mantém a população e os identificadores que tornam ambas as tarefas reconciliáveis.

---

## 2. Fundamento na tese e limite de conteúdo

A tese define que:

- toda pessoa considerada entra em um screening log sob um código;
- o log registra outcome de screening e razão de qualquer non-inclusion ou withdrawal;
- a chave que liga o código à identidade fica separada e controlada;
- o site reconcilia o log com os eligibility records para prestar contas de cada candidato;
- as razões de non-inclusion alimentam a revisão de Enrollment Quality;
- PSEAR documenta a decisão individual de elegibilidade, enquanto o SIFSL registra todos os screened;
- no close-out, a reconciliação final entre screening log e eligibility records faz parte da verificação interna.

Portanto, o SIFSL deve ser conciso. Não deve registrar:

- nome, data de nascimento, telefone, endereço ou outro identificador direto;
- conteúdo do consent conversation ou do ICF;
- critérios de inclusão/exclusão detalhados;
- score, exame clínico, laudo radiológico, imaging finding ou narrativa de fonte;
- decisão clínica que pertence ao PSEAR;
- cálculo de taxa ou interpretação agregada que pertence ao PIR.

A única ligação com identidade é um **coded candidate/subject ID**. A identidade real e a respectiva key pertencem ao sistema autorizado separado, que o SIFSL pode apenas referenciar por controlled location quando isso for necessário para controle documental.

---

## 3. Interfaces corretas

```text
Candidate identification / authorized local source
                 ↓  (coded ID only)
              SIFSL ─────────────→ controlled subject-identification key
                 │
                 ├──→ PSEAR: coded participant, screening reference and outcome link
                 │         (PSEAR holds the individual eligibility decision)
                 │
                 ├──→ enrolment / sponsor screening record: reference only
                 │
                 ├──→ PIR: counts of screened and enrolled candidates, non-inclusion
                 │         category distribution and reconciliation status
                 │
                 └──→ IMC / POT / SRR / CAPA: only when a recurring reconciliation,
                           process or eligibility-control weakness is identified
```

### PSEAR ↔ SIFSL

| PSEAR | SIFSL |
|---|---|
| Uma pessoa e uma decisão de elegibilidade | Todas as pessoas consideradas, qualquer outcome |
| Fonte da decisão/evidência | Índice populacional e reconciliação |
| Pode ter narrativa mínima de evidência | Não registra dados clínicos ou de imagem |
| Produz Eligible / Not eligible e exceções | Registra status/outcome e referência PSEAR |

A ligação deve usar código, PSEAR ID/control record ID e data da decisão/outcome. O SIFSL não deve tentar resumir os critérios avaliados no PSEAR.

### SIFSL → PIR

O SIFSL fornece ao PIR:

- número de candidatos considerados, pre-screened, screening-active, eligible, enrolled, not eligible e withdrawn/discontinued;
- identificação de linhas sem outcome ou sem ligação ao PSEAR quando aplicável;
- categorias agregáveis de non-inclusion/withdrawal;
- evidência de reconciliação da população de screening;
- intervalos de IDs/registros a usar na source reconciliation.

O PSEAR e os deviation records continuam sendo as fontes que demonstram se cada inclusão foi correta e devidamente evidenciada. O SIFSL contribui para recruitment volume, population completeness e padrões de non-inclusion; ele não substitui a revisão de qualidade de elegibilidade do PSEAR.

---

## 4. Lógica de status e outcome

A versão futura precisa separar **status atual** de **outcome final**, porque um candidato pode estar no fluxo sem decisão final ainda.

### Status de trajetória

| Status | Uso | Regra |
|---|---|---|
| Pre-screened / considered | Pessoa foi considerada sob código, sem screening formal concluído | Não registrar motivo clínico detalhado. |
| Screening active | Screening aplicável está em curso | Deve ter responsible function e referência controlada quando PSEAR/controlled screening record já existir. |
| Awaiting eligibility decision | Evidência ou revisão ainda pendente | Não pode ser tratada como Eligible ou Enrolled. |
| Eligible — awaiting enrolment | PSEAR/controlled decision permite seguir, mas enrollment ainda não ocorreu | Deve ter decision record/date. |
| Enrolled | Enrollment ocorreu | Deve ter enrollment date/record reference. |
| Not eligible / screen failure | Critério ou decisão não permite inclusion | Exige categoria controlada de non-inclusion e PSEAR/control record reference quando aplicável. |
| Withdrawn / discontinued before enrolment | Pessoa ou processo deixou o screening antes de inclusion | Exige categoria controlada; não registrar narrativa pessoal detalhada. |
| Closed — other controlled outcome | Outcome não coberto acima | Exige categoria `Other` e controlled note/reference. |

### Categorias de non-inclusion / withdrawal

O SIFSL deve usar um catálogo curto e pré-definido. O objetivo é permitir contagem e tendência sem expor dados clínicos em excesso.

| Código | Categoria | Quando usar |
|---|---|---|
| NI-01 | Eligibility criterion not met | Um ou mais critérios não foram atendidos; detalhes permanecem no PSEAR/source. |
| NI-02 | Required assessment incomplete or unavailable | Avaliação necessária não foi concluída ou não ficou disponível dentro da decisão aplicável. |
| NI-03 | Consent / participant decision | Recusa, withdrawal ou impossibilidade de seguir pela rota de consentimento; sem detalhe pessoal. |
| NI-04 | Screening stopped before decision | Screening não chegou a uma decisão de elegibilidade por motivo controlado. |
| NI-05 | Sponsor, site or study-status constraint | Situação operacional autorizada: recrutamento fechado, quota, sponsor/site decision ou condição equivalente. |
| NI-06 | Other controlled reason | Exige referência a record controlado e texto mínimo não identificável. |

A categoria não é uma conclusão clínica nova. Ela resume o outcome administrativo. Onde for necessário demonstrar a razão detalhada, o SIFSL aponta para PSEAR, source record ou record controlado — não replica conteúdo.

---

## 5. Arquitetura recomendada para o primeiro HTML

### Page 1 — Portrait: control, purpose and taxonomy

- Cabeçalho com até 12 células, somente metadados úteis: study/protocol, CIP version, site code, log ID/version, period/cut-off, responsible role, controlled location of identification key e review status.
- **A. Purpose and Use**, com Unit of analysis, Decision support, Inputs e Outputs.
- **B. Coding, confidentiality and use rules**:
  - use coded ID only;
  - do not enter direct identifiers;
  - location of the identity key is controlled separately;
  - one candidate occupies one log line; update the same line rather than create duplicates;
  - PSEAR/control record is cited rather than copied.
- **C. Status and non-inclusion category guide** com a taxonomia acima, curta o suficiente para ser lida durante uso.

### Page 2 — Landscape: Candidate Screening and Outcome Register

Tabela principal e repetível. Uma linha por candidate code. Se forem necessárias mais linhas, a página deve poder ser impressa/duplicada como continuation sheet, mantendo log ID, site code, period e page number.

Colunas propostas:

| Campo | Finalidade |
|---|---|
| Log line | Rastreabilidade da linha. |
| Coded candidate ID | Código; nenhum identificador direto. |
| Date first considered / screening opened | Cronologia básica. |
| Current pathway status | Estado atual da trajetória. |
| PSEAR or controlled screening-record reference | Liga o log à decisão individual quando aplicável. |
| Eligibility decision / outcome date | Data da decisão ou do outcome final. |
| Final outcome | Eligible awaiting enrolment / Enrolled / Not eligible / Withdrawn / other controlled outcome. |
| Non-inclusion / withdrawal category | NI-01 a NI-06 ou N/A quando enrolled/active. |
| Enrolment or next controlled record reference | Somente quando aplicável. |
| Reconciliation note / exception reference | Apenas ID de issue ou `None`; sem narrativa clínica. |

Não adicionar colunas de consent detail, diagnosis, criteria, imaging result, score, assessor clinical judgement ou full reason for failure.

### Page 3 — Portrait: reconciliation and accountable close

- **D. Periodic reconciliation control**:
  - all SIFSL rows have a current/final outcome;
  - all Eligible/Not eligible decisions link to PSEAR or authorized controlled record as applicable;
  - every Enrolled candidate has enrollment reference;
  - no duplicate coded candidate ID or unexplained missing/extra record;
  - unresolved mismatch and immediate correction/reference.
- **E. Review output and routing**:
  - counts at cut-off by pathway status and non-inclusion category;
  - this is a reconciliation summary, not the Enrollment Quality calculation;
  - whether a recurring category or reconciliation weakness is routed to PIR, IMC, POT, SRR or CAPA.
- **F. Accountable review, signature and controlled filing**.

A página 3 pode registrar contagens simples, mas não deve inventar métricas de performance. Taxas, denominadores de Enrollment Quality e interpretação pertencem ao PIR.

---

## 6. Regras de reconciliação e resposta

O SIFSL precisa permitir uma revisão simples, mas controlada, em ciclos definidos pelo site e obrigatoriamente no close-out.

```text
For every SIFSL row at cut-off:
  if status = Enrolled:
      confirm enrolment reference and PSEAR/controlled decision reference;
  if status = Not eligible or Withdrawn:
      confirm final outcome and non-inclusion category;
  if status = Screening active / Awaiting decision:
      confirm responsible follow-up or justified current status;
  if PSEAR/control record exists but no SIFSL line exists:
      add/correct the SIFSL line and record reconciliation reference;
  if SIFSL line has no reconcilable outcome at review cut-off:
      open a local reconciliation issue and route it for resolution.
```

Uma inconsistência individual deve primeiro ser corrigida no log ou record proprietário. Ela não é CAPA automática. A rota só sobe para IMC, PIR, POT, SRR ou CAPA quando houver padrão recorrente, atraso persistente, lacuna de controle ou impacto material.

### Gatilhos úteis

| Achado | Resposta inicial | Escalonamento, se recorrente/material |
|---|---|---|
| Linha sem outcome no cut-off | Confirmar status e completar/reconciliar a linha | IMC/POT se recorrente ou vencida a regra local de revisão. |
| PSEAR/control record sem SIFSL line | Corrigir índice e registrar reconciliação | IMC/PIR se demonstrar quebra de completude de screening population. |
| Enrolled candidate sem record linkage | Segurar confirmação de reconciliação e localizar record | PI/POT; deviation route se aplicável. |
| Repetição de NI-01 em mesmo criterion category | Revisar com PSEAR e regra CIP | PIR; POT/IMC; sponsor clarification quando a regra for ambígua. |
| Repetição de NI-02 | Investigar barreira de assessment/imaging/process | IMC/SRR/CAPA conforme materialidade e repetição. |
| Repetição de NI-03 | Registrar tendência sem expor detalhes pessoais | PIR/POT somente se houver questão relevante de consent/recruitment process. |

---

## 7. Pontos de atenção para o desenho

1. **Não confundir candidate volume com enrollment quality.** O SIFSL conta e reconcilia pessoas; o PIR avalia se inclusões foram corretas e evidenciadas.
2. **Não transformar a categoria de non-inclusion em diagnóstico.** O código é administrativo e agregável; a fonte clínica continua no PSEAR/source record.
3. **Não exigir PSEAR para pre-screen-only candidate quando ainda não houver avaliação formal.** O SIFSL precisa acomodar a trajetória sem forçar documentos inexistentes.
4. **Não usar “screen failure” para qualquer pessoa que não entrou sem distinguir estado.** `Not eligible`, `withdrawn`, `screening stopped before decision` e `operational constraint` têm significados diferentes e devem permanecer distintos.
5. **Não expor identidade direta.** Mesmo o screening log precisa operar por código; a chave fica em localização separada controlada.
6. **Não criar uma ação individual para toda non-inclusion.** O log descreve um outcome. Ação e escalonamento só surgem com discrepancy, falta de reconciliação, repetição ou risco.
7. **Não descrever a tese no formulário.** O HTML final deve citar somente CIP, controlled sources, PSEAR, SIFSL ruleset e outros documentos operacionais aplicáveis.

---

## 8. Direção visual e técnica

- Como não há template histórico, a primeira versão pode adotar integralmente a identidade visual comum: papel branco, navy topbar, metadata azul-claro, cabeçalhos de tabela azul médio, bordas cinza finas, rodapé com código/versão/página.
- A página 1 e 3 devem ser portrait; a tabela central é landscape apenas pela largura necessária.
- A main register table deve ter linhas úteis para atualização real, sem altura idêntica artificial em todas as caixas; usar altura adequada a códigos, status e referência curta.
- Disponibilizar continuation sheet da tabela principal. Não tentar comprimir muitos candidatos em uma única página por fonte menor.
- A versão blank não deve conter exemplo preenchido na tabela principal. Uma versão filled demo separada pode mostrar uma pequena coorte coerente e usar fonte cursiva apenas nos dados demonstrativos.
- Incorporar um único Editor v2 canônico e validar seus recursos; a pré-visualização interativa deve ser disponibilizada antes de PDF ou filled demo.

---

## 9. Checklist para a IA que construirá o SIFSL

1. Tratar o SIFSL como log populacional codificado de candidatos, não como record de elegibilidade individual.
2. Incluir cada pessoa considerada, qualquer que seja o outcome, sem identificadores diretos.
3. Preservar uma linha por candidate code e atualizar essa linha; não gerar duplicatas a cada mudança de status.
4. Usar uma taxonomia controlada para non-inclusion/withdrawal, sem detalhes clínicos.
5. Ligar PSEAR/control record e enrollment record somente por referência/ID.
6. Construir reconciliation controls claros para completar população e identificar mismatch.
7. Entregar ao PIR contagens, categorias e population completeness — não uma taxa ou interpretação de Enrollment Quality.
8. Reservar escalonamento para gaps materiais ou recorrentes, não para todo screen failure.
9. Manter a tabela principal repetível em landscape e as regras/resumo em portrait.
10. Gerar pré-visualização interativa antes da entrega de qualquer HTML final.

---

## 10. Fontes verificadas

- Tese completa (29-10), seção 4.4.3: screening log sob código, outcome e razão de non-inclusion/withdrawal, chave de identidade separada, reconciliação com eligibility records e alimentação do Enrollment Quality.
- Tese completa (29-10), seção 4.5.1: recruitment volume separado no screening log; Enrollment Quality usa eligibility records e flags de ambiguidade, erro e deviation.
- Tese completa (29-10), implementação/close-out: todos os candidatos entram no screening log; no close-out, screening log e eligibility records são reconciliados.
- PSEAR v0.91 and its current manual analysis: decisão individual de elegibilidade e interface obrigatória com SIFSL.
- PIR v0.8 filled demo: Enrollment Quality uses PSEAR, SIFSL and eligibility deviations as distinct source interfaces.
