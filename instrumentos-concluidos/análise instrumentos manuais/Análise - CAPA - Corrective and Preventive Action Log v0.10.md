# Análise crítica — CAPA: Corrective and Preventive Action Log v0.10

**Status:** análise manual para orientar a próxima revisão do instrumento. O HTML v0.10 não foi alterado nesta etapa.

## 1. Veredito executivo

O CAPA Log v0.10 está conceitualmente muito mais próximo do instrumento necessário do que as versões anteriores. O acerto mais importante foi reconhecer que ele é um **portfolio log**: registra e acompanha vários CAPAs dentro de um período, em vez de tentar investigar e administrar um único caso inteiro em uma tabela.

A unidade de análise correta é:

```text
one CAPA record within one defined portfolio review period
```

O documento recebe uma população de CAPAs já abertos em registros autorizados e produz uma visão reconciliada sobre:

- quais CAPAs existem;
- quais foram abertos, fechados, reabertos ou continuam ativos;
- quais categorias, criticidades e domínios estão concentrados;
- quais padrões sistêmicos aparecem ao longo do tempo;
- quais CAPAs ativos exigem acompanhamento;
- quais foram avaliados quanto à efetividade;
- quais podem ser fechados ou precisam ser reabertos;
- quais decisões ou atualizações controladas foram produzidas pela revisão do portfólio.

O CAPA Log **não deve substituir**:

- o CAPA individual autorizado pelo QMS;
- o deviation record;
- a investigação de causa;
- o safety case/SART;
- a análise de complicações/CSST;
- o SRR;
- o POT;
- o PIR;
- o registro de eficácia de um controle operacional.

A versão v0.10 já declara essa fronteira. O trabalho restante é principalmente fortalecer a rastreabilidade, garantir que o log comporte uma população real de CAPAs e evitar que as seções D–H recriem o CAPA individual ou o PIR.

---

## 2. Decisão que o CAPA Log deve suportar

Depois de preencher o documento, o responsável deve conseguir decidir:

> **Is the complete CAPA population for the defined review period reconciled, are recurring or systemic patterns visible, are active CAPAs progressing against their authorised plans, and can any evaluated CAPA be considered effective, closed, limited or reopened?**

Essa decisão tem duas camadas:

### Camada 1 — Portfólio

- a população está completa;
- os registros do log batem com a fonte autorizada;
- há concentração por categoria, criticidade, domínio ou período;
- há recorrência ou deterioração;
- há risco sistêmico ou interface com segurança, dispositivo, CIP, endpoint ou processo.

### Camada 2 — CAPA individual dentro do portfólio

- o CAPA ativo está avançando;
- o próximo milestone está definido;
- existe owner e prazo;
- a evidência de implementação ou efetividade existe;
- o CAPA pode ser fechado, permanece limitado ou precisa ser reaberto.

A primeira camada pertence ao CAPA Log. A segunda acompanha o CAPA individual sem duplicar sua investigação.

---

## 3. Base na tese e função dentro da framework

A tese coloca o CAPA no pilar de **Performance Oversight**, como o mecanismo que fecha o ciclo de melhoria:

```text
finding / signal
→ initial response
→ recurrence or unresolved failure
→ cause investigation
→ corrective and preventive action
→ implementation
→ effectiveness review
→ closure or reopening
→ risk/process update
```

A tese descreve que o CAPA pode receber entradas de:

- PIR;
- IMC;
- sponsor monitoring;
- audits or inspections;
- complication monitoring;
- surgeon learning-curve review;
- SRR;
- outras revisões controladas que identifiquem uma falha persistente ou sistêmica.

O CAPA Log não é o lugar onde toda essa investigação é refeita. Ele é o lugar onde a organização local mantém o **portfólio reconciliado e revisável** e onde as decisões de continuidade, efetividade, fechamento e reabertura podem ser acompanhadas de maneira transversal.

A tese também é clara em dois pontos:

1. CAPA deve ser aberto quando a resposta inicial não resolveu o problema, quando há recorrência, materialidade, tendência ou vulnerabilidade sistêmica.
2. Uma ação só fecha quando há evidência de efetividade ou uma limitação documentada que explique por que seu efeito ainda não pode ser julgado.

Esses dois princípios precisam permanecer visíveis no instrumento.

---

## 4. O que está correto na versão v0.10

### 4.1. O documento é um log de portfólio

A seção A declara que o documento cobre todos os CAPAs abertos dentro de um período definido e que cada CAPA deve ser registrado uma vez no Master CAPA Register. Isso resolve a principal falha das versões anteriores.

A seção C é corretamente identificada como:

> **Master CAPA Register — one row per CAPA opened**

Essa frase deve ser preservada.

### 4.2. O registro mestre vem antes da análise

A ordem atual é lógica:

```text
A — Purpose and Use
B — completion sequence and classifications
C — master population
D — reconciliation and distributions
E — recurring/systemic patterns
F — active follow-up
G — effectiveness and closure
H — outputs and conclusion
```

A análise não começa antes de a população ser registrada e reconciliada. Isso é essencial para não produzir contagens sem base.

### 4.3. A seção C separa finding curto de investigação completa

A instrução para registrar um problema factual e curto e apontar para o QMS CAPA/investigation como fonte é adequada. O CAPA Log deve responder “qual CAPA existe e como está no portfólio”, não copiar a narrativa de causa raiz.

### 4.4. Category, Criticality e Lifecycle status estão separados

Essa separação é necessária porque são dimensões diferentes:

- **Category:** que tipo de problema é;
- **Criticality:** qual a consequência ou urgência do problema;
- **Lifecycle status:** em que fase administrativa/operacional o CAPA está.

Misturar essas dimensões produz contagens inúteis e dificulta a leitura do portfólio.

### 4.5. A reconciliação é uma etapa obrigatória

A seção D exige comparar o Master CAPA Register com a população autorizada do QMS e resolver diferenças antes de fechar a revisão. Essa é uma exigência de auditabilidade, não apenas uma boa prática visual.

Sem reconciliação, os counts de categoria, criticidade e status não são confiáveis.

### 4.6. O log separa padrão de CAPA individual

A seção E permite observar padrões de recorrência e sinais sistêmicos sem transformar a própria seção em uma nova investigação de causa. A instrução de usar a investigação autorizada como fonte para causal analysis está correta.

### 4.7. O Active CAPA Follow-up Index não recria o plano

A seção F aponta para o QMS CAPA e registra apenas:

- próximo milestone;
- owner;
- due/next review;
- evidence expected or missing;
- escalation/decision.

Essa é a granularidade correta para um portfolio log.

### 4.8. A seção G não reduz efetividade a “closed”

A seção de effectiveness, closure and reopening exige:

- critério de efetividade;
- população/período;
- evidência;
- resultado;
- decisão;
- limitação ou risco residual;
- avaliador e data.

Isso está alinhado com a tese e evita o fechamento administrativo sem demonstração de resultado.

---

## 5. Problema mais importante: o log precisa sustentar uma população real

O CAPA Log é um instrumento populacional. Portanto, a seção C deve ter linhas suficientes para registrar vários CAPAs e deve permitir folhas de continuação.

### Requisito funcional

A seção C deve ser uma página própria, preferencialmente em portrait, com:

- tabela de registro mestre;
- quantidade de linhas plausível para o período;
- nota explícita de que a página pode ser reproduzida;
- continuidade de CAPA IDs;
- referência ao mesmo Review Period e CAPA Log ID;
- confirmação de que as páginas de continuação fazem parte do mesmo documento controlado.

A regra recomendada é:

> If additional CAPAs are opened or identified, reproduce the Master CAPA Register page, continue the CAPA IDs and attach the continuation page to the same controlled record. Do not create a second portfolio without an explicit period or version boundary.

### Por que isso é importante

As seções D–H não devem ser a única forma de acomodar a população. Elas são análises derivadas. A fonte das contagens é a seção C e suas folhas de continuação.

A seção D deve ter menos linhas porque é uma síntese. As seções E, F e G também podem ser menores porque trabalham com subsets:

- E: padrões ou sinais;
- F: CAPAs ativos;
- G: CAPAs avaliados quanto à eficácia/fechamento/reabertura.

Isso preserva a distinção entre:

```text
C = population register
D = portfolio analysis
E = pattern/systemic assessment
F = active subset
G = effectiveness/closure subset
```

---

## 6. Revisão das seções

### A — Purpose and Use

**Manter.** A seção está bem delimitada, mas deve declarar de maneira ainda mais direta:

- se a revisão é mensal, trimestral ou triggered;
- qual é o Review Period;
- qual é a população fonte;
- qual sistema ou registro é authoritative;
- qual é a diferença entre CAPA Log e CAPA individual.

O texto está correto ao dizer que o CAPA Log não substitui o QMS CAPA, deviation, investigation ou safety record.

### B — Completion sequence and review boundary

**Manter, com redução de repetição.** A seção contém um guia de sequência e uma tabela de passos. A informação é importante, mas a redação pode ser mais curta. O usuário do log não precisa de uma SOP inteira dentro do documento.

O essencial é deixar inequívoco:

1. definir período e fonte;
2. registrar a população completa;
3. reconciliar;
4. analisar padrões;
5. acompanhar ativos;
6. avaliar eficácia/fechamento quando aplicável;
7. documentar outputs e conclusão.

### B — Controlled classifications

**Manter.** As definições de Category, Criticality e Lifecycle status devem ficar antes da seção C.

A classificação deve evitar texto livre quando uma opção controlada existir. Porém, o instrumento precisa permitir `Other / defined locally` ou `Unclassified pending review` quando a taxonomia não cobrir um caso. Essa opção exige justificativa e revisão posterior; não deve ser usada como atalho.

### C — Master CAPA Register

**Manter como núcleo e reforçar a capacidade populacional.** A tabela atual contém:

- CAPA ID;
- opened/closed date;
- short problem statement;
- source record;
- CTQ/operational domain;
- category;
- criticality;
- lifecycle status.

Esses campos são adequados para o registro mestre. Recomenda-se acrescentar ou tornar explícitos:

- Review Period inclusion basis;
- CAPA owner/accountable function, se não estiver disponível na fonte;
- original source type;
- reopened flag ou status já controlado;
- continuation page number quando houver folhas adicionais.

Não acrescentar uma coluna extensa para causa raiz ou plano de ação. Isso pertence ao CAPA individual.

### D — Portfolio reconciliation and distribution

**Manter.** A seção deve permitir confirmar:

- número de CAPAs no QMS/source population;
- número de CAPAs no Master Register;
- diferença;
- CAPAs sem fonte;
- CAPAs duplicados;
- CAPAs fora do período;
- CAPAs incluídos por carry-forward;
- data e responsável pela reconciliação.

A distribuição por Category, Criticality e Lifecycle status deve sempre apontar para CAPA IDs, não somente para counts.

Se o período tiver poucos CAPAs, o número absoluto é mais importante que a porcentagem. Percentuais só devem aparecer quando o denominador for suficientemente estável e sempre devem acompanhar `n/N`.

### D3 — Historical carry-forward and cumulative trend baseline

**Manter, mas limitar.** Essa seção é útil porque um CAPA aberto no período anterior pode continuar ativo e alterar a leitura do período atual. Porém, o registro histórico deve ser controlado.

A tabela deve distinguir:

- CAPAs opened in period;
- CAPAs closed in period;
- CAPAs active at period start;
- CAPAs active at period end;
- reopened CAPAs;
- cumulative population.

Não transformar D3 em um segundo Master Register histórico. O histórico pode apontar para os registros dos períodos anteriores.

### E — Portfolio signal assessment and systemic interface

**Manter como seção triggered.** A seção não deve exigir uma investigação sistêmica em cada ciclo.

Se não houver sinal, basta registrar:

```text
No systemic pattern identified.
Population reviewed: [n/N and source].
Rule applied: [predefined rule/version].
```

Se houver sinal, E1 deve responder:

- quais CAPA IDs formam o padrão;
- qual denominador foi usado;
- qual período foi comparado;
- qual regra ou threshold foi aplicado;
- se existe concentração por categoria, domínio, processo, owner, fase ou dispositivo.

E2 deve ser preenchida apenas quando houver interface material com:

- safety;
- device deficiency;
- CIP/protocol compliance;
- endpoint reliability;
- SRR;
- PI oversight;
- sponsor reporting.

A seção não deve fazer novamente a causa raiz individual.

### F — Active CAPA Follow-up Index

**Manter.** É uma camada de acompanhamento do subconjunto ativo.

O status deve permanecer ligado ao status controlado da fonte. O log pode indicar uma situação administrativa de acompanhamento, mas não deve criar um status paralelo que contradiga o QMS CAPA.

O campo `Next required milestone` deve ser concreto. Exemplos:

- root-cause review due;
- corrective action implementation evidence due;
- preventive action rollout due;
- effectiveness sample complete;
- PI decision required;
- sponsor response pending;
- closure package pending.

`Evidence expected or missing` deve apontar para a evidência esperada, não apenas dizer “evidence pending”.

### G — Effectiveness, closure and reopening decision

**Manter e reforçar.** Esta seção deve ser uma tabela de decisões de efetividade, não um segundo plano de ação.

O critério precisa ser mensurável ou verificável. Exemplos:

- indicador voltou ao limite definido em dois ciclos subsequentes;
- nenhuma recorrência no período amostrado;
- todos os registros da amostra seguiram o novo processo;
- discrepâncias endpoint-critical foram resolvidas;
- nenhum novo caso ocorreu após a implementação, dentro da população definida.

Não aceitar conclusões como `effective` sem:

- população;
- período;
- fonte;
- critério;
- resultado;
- avaliador.

### H — Controlled outputs, portfolio conclusion and accountable review

**Manter.** A seção deve registrar somente outputs criados pela revisão do portfólio:

- atualização controlada do SRR;
- atualização de PIR/IMC;
- escalonamento ao PI;
- comunicação formal;
- mudança de procedimento;
- abertura ou atualização de CAPA;
- handoff de safety/device/CIP;
- decisão de revisão extraordinária.

Não repetir as ações do QMS CAPA nessa tabela.

A conclusão deve mencionar:

- população reconciliada;
- número de CAPAs ativos;
- CAPAs de alta criticidade ativos;
- padrões encontrados ou ausência de padrão;
- residual risk;
- próxima revisão.

---

## 7. Interfaces com outros instrumentos

### 7.1. IMC → CAPA Log

O IMC identifica uma falha de controle. O CAPA Log recebe somente quando a resposta inicial não resolve a falha, quando há recorrência, materialidade ou uma vulnerabilidade que exige ação corretiva/preventiva.

O IMC não deve abrir automaticamente um CAPA para cada observation. O CAPA Log também não deve tratar toda observação do IMC como CAPA.

### 7.2. PIR → CAPA Log

O PIR identifica indicadores fora de controle, deterioração, recorrência ou concentração. O CAPA Log recebe a ação quando o problema exige investigação e prevenção além da resposta inicial.

O PIR fornece:

- indicador;
- regra;
- período;
- resultado;
- denominador;
- threshold;
- decisão de ação;
- source records.

O CAPA Log acompanha a ação, não recalcula o PIR.

### 7.3. SRR → CAPA Log

O SRR pode identificar risco residual ou controle insuficiente. O CAPA Log pode documentar a ação para corrigir a causa ou fortalecer o controle.

Quando o CAPA revela uma vulnerabilidade nova, ele deve devolver ao SRR:

- risco novo ou alterado;
- controle requerido;
- owner;
- trigger;
- residual risk;
- data da atualização.

O CAPA Log não deve manter uma cópia paralela do risk register.

### 7.4. POT → CAPA Log

O POT registra a decisão do PI quando a questão exige oversight, aceitação formal de limitação, restrição, escalonamento ou decisão sobre recursos.

O CAPA Log registra a ação e seu status. Não deve substituir o POT nem registrar uma decisão do PI sem referência ao POT.

### 7.5. SART/SCML/CSST → CAPA Log

Uma safety case ou complication signal pode gerar CAPA quando a análise aponta para falha de processo recorrente ou prevenção necessária.

O CAPA Log não reclassifica o evento, não repete a análise clínica e não substitui SART, SCML ou CSST.

### 7.6. PIDLR → CAPA Log

O PIDLR ocorre na fase de encerramento e transforma aprendizado em lição controlada. O CAPA Log pode fornecer:

- CAPAs fechados;
- CAPAs reabertos;
- ações efetivas ou não efetivas;
- mudanças de procedimento;
- residual risks;
- lessons requiring transfer.

O PIDLR não deve reabrir um CAPA sem referência; se uma ação nova for necessária, deve existir CAPA ou outro registro controlado apropriado.

### 7.7. MRL/POT → CAPA Log

Reviews periódicos e decisões de oversight podem abrir, priorizar ou escalonar CAPAs. O CAPA Log fornece o status do portfólio para que a decisão não se baseie apenas em casos isolados.

---

## 8. Diferença entre CAPA individual e CAPA Log

Essa distinção precisa aparecer claramente no documento e na prática.

| CAPA individual | CAPA Log |
|---|---|
| Investiga o problema específico. | Registra a população de CAPAs. |
| Documenta análise causal. | Reconcilia, classifica e acompanha o portfólio. |
| Define corrective/preventive actions detalhadas. | Aponta para o plano autorizado. |
| Define evidência de implementação. | Registra milestone e evidência esperada. |
| Avalia a efetividade do caso. | Registra a decisão de efetividade, fechamento ou reabertura. |
| Mantém a documentação completa. | Mantém referência, status e visão transversal. |
| Pode ser mantido no QMS. | Pode ser específico do site/investigação/período. |

O CAPA Log não deve ser reduzido a uma planilha de `CAPA ID / status`. Mas também não deve virar um segundo QMS CAPA.

---

## 9. Questões de classificação

### Category

A categoria deve responder ao tipo predominante de problema, por exemplo:

- participant protection;
- consent/eligibility;
- protocol/deviation;
- safety reporting;
- data/source documentation;
- follow-up/retention;
- imaging;
- procedure/device traceability;
- training/role/authorization;
- equipment/facility;
- external/vendor interface;
- other defined category.

A lista final precisa corresponder ao desenho aprovado do instrumento. Uma CAPA pode ter vários CtQs relacionados, mas deve ter uma categoria primária para permitir contagem consistente.

### CTQ / operational domain

Esse campo não deve ser confundido com Category. O domínio informa onde o problema afeta a qualidade; a categoria informa que tipo de problema é.

### Criticality

A definição precisa se apoiar na consequência, não apenas no tamanho do problema. Uma única falha de consentimento, safety reporting ou implant traceability pode ser de alta criticidade, mesmo com frequência baixa.

O critério deve explicar:

- impacto potencial sobre participant protection;
- impacto sobre confiabilidade dos dados;
- impacto sobre integridade do dispositivo/procedimento;
- necessidade de PI/sponsor escalation;
- urgência mínima de review.

### Lifecycle status

Deve ter um vocabulário controlado, por exemplo:

- analysis/plan pending;
- implementation in progress;
- effectiveness pending;
- closed effective;
- closed with documented limitation;
- reopened.

O log deve apontar para o status da fonte autorizada. Não deve permitir que o usuário marque `closed` apenas porque uma ação foi executada.

---

## 10. Periodicidade e escopo

O CAPA Log deve funcionar como:

- revisão mensal;
- revisão trimestral;
- revisão triggered;
- revisão de close-out;
- revisão extraordinária após sinal material.

O cabeçalho deve declarar:

- CAPA Log ID;
- site/investigation;
- review period;
- date of cut-off;
- source system or controlled register;
- reviewer;
- review trigger;
- previous portfolio review reference.

Uma revisão triggered não deve ser confundida com uma nova população. Ela deve declarar o trigger e o período de atualização.

CAPAs fechados antes do início do período podem ser incluídos como historical carry-forward quando forem necessários para interpretar recorrência ou tendência, mas a regra de inclusão deve ser explícita.

---

## 11. Critérios de efetividade e fechamento

O CAPA Log deve preservar três estados distintos:

### Implemented

A ação planejada foi executada, mas ainda não há evidência suficiente para dizer se resolveu o problema.

### Effective

O critério predefinido foi testado, a evidência foi revisada e o resultado demonstra controle suficiente no período/população definidos.

### Closed with documented limitation

O CAPA foi encerrado por uma limitação reconhecida, mas a limitação precisa ser descrita e o residual risk deve ser aceito pela função adequada.

### Reopened

A efetividade não foi demonstrada, a falha recorreu, o controle deteriorou ou surgiu nova evidência de que a ação não resolveu a causa.

A regra da tese deve permanecer:

> A CAPA closes only when effectiveness is demonstrated or a documented limitation explains why the effect cannot yet be judged.

Quando o CAPA é reaberto, o log deve manter o histórico da decisão anterior e registrar o novo motivo, não apagar a decisão antiga.

---

## 12. Arquitetura recomendada para a próxima versão

A estrutura de nove páginas do v0.10 é defensável. A próxima versão deve preservar a arquitetura com ajustes focais.

### Página 1 — Purpose, boundary and completion sequence

- cabeçalho;
- A. Purpose and Use;
- Review Period, source, cut-off e trigger;
- completion sequence;
- diferença entre CAPA Log e CAPA individual.

### Página 2 — Controlled classifications

- Category;
- Criticality;
- Lifecycle status;
- domínio CtQ separado;
- regras de seleção e justificativa.

### Página 3 — Master CAPA Register

- uma linha por CAPA;
- linhas suficientes para vários CAPAs;
- página portrait dedicada;
- nota de continuidade/reimpressão;
- CAPA IDs e source reference.

### Página 4 — Reconciliation and distribution

- reconciliação com a fonte autorizada;
- distribuição por category;
- counts, IDs e observations.

### Página 5 — Historical and cumulative portfolio view

- carry-forward;
- opened/closed/active/reopened;
- cumulative baseline;
- trend interpretation.

### Página 6 — Recurrence and systemic interface

- pattern screen;
- denominator;
- rule;
- CAPA IDs;
- systemic route only when triggered.

### Página 7 — Active CAPA Follow-up Index

- um row por CAPA ativo;
- next milestone;
- owner;
- evidence;
- due/next review;
- escalation.

### Página 8 — Effectiveness, closure and reopening

- um row por CAPA avaliado;
- criterion;
- population/period;
- evidence;
- decision;
- residual risk;
- evaluator/date.

### Página 9 — Outputs and conclusion

- outputs controlados;
- portfolio conclusion;
- residual-risk statement;
- next review;
- accountable review and signature.

As páginas C e F/G devem ser entendidas como folhas repetíveis quando a população exceder as linhas disponíveis. O arquivo deve indicar claramente se a continuação pertence ao mesmo CAPA Log.

---

## 13. Fluxo de preenchimento recomendado

### Antes da revisão

1. Definir Review Period, trigger e cut-off.
2. Identificar o authoritative CAPA population.
3. Confirmar categorias, criticity rules e lifecycle vocabulary.
4. Identificar a última revisão do portfólio.
5. Definir reviewer e accountable reviewer.

### Registrar a população

1. Inserir cada CAPA aberto dentro do período.
2. Incluir carry-forward conforme a regra definida.
3. Não excluir CAPAs que fecharam durante o período.
4. Usar CAPA ID único.
5. Registrar source record.
6. Manter o problem statement curto e factual.
7. Completar CTQ/domain, category, criticality e lifecycle status.
8. Reproduzir a página de continuação se necessário.

### Reconciliar

1. Comparar com a fonte autorizada.
2. Identificar faltantes, duplicados e CAPAs fora do período.
3. Corrigir divergências antes da análise.
4. Registrar a data e o responsável pela reconciliação.

### Analisar o portfólio

1. Contar por category.
2. Contar por criticality.
3. Contar por lifecycle status.
4. Comparar com períodos anteriores.
5. Identificar recorrência, concentração ou deterioração.
6. Registrar “no systemic pattern identified” quando aplicável.

### Acompanhar ativos

1. Listar todos os CAPAs ativos.
2. Confirmar próximo milestone.
3. Confirmar owner e due date.
4. Identificar evidência esperada ou ausente.
5. Registrar escalation ou decision.

### Avaliar efetividade

1. Usar o critério definido no CAPA individual.
2. Confirmar população e período avaliados.
3. Registrar evidência e resultado.
4. Decidir effective, limitation, reopen ou pending.
5. Manter histórico da decisão anterior.

### Fechar a revisão do portfólio

1. Registrar outputs criados pela revisão.
2. Atualizar SRR/PIR/IMC/POT ou outros registros quando aplicável.
3. Documentar residual risk.
4. Definir próxima revisão.
5. Assinar e arquivar.

---

## 14. Saídas do CAPA Log

| Destinatário | Saída correta |
|---|---|
| QMS CAPA individual | Status de acompanhamento, referência, milestone, efetividade, fechamento ou reabertura. |
| PIR | Tendências e ações relacionadas aos indicadores, sem duplicar a regra do indicador. |
| IMC | Evidência de que um controle falhou, foi corrigido e tornou-se efetivo. |
| SRR | Risco novo/alterado, controle insuficiente, trigger e residual risk. |
| POT | Questão que exige decisão ou oversight do PI. |
| MRL | Estado de ações ou padrões relevantes para mudança de fase ou milestone. |
| SART/SCML/CSST | Apenas interface de segurança/complicação quando o CAPA deriva de falha de processo relacionada ao caso. |
| PIDLR | Lições, mudanças de procedimento e ações efetivas ou não efetivas ao encerramento. |
| Sponsor | Informação formal quando a ação, o risco ou o evento exige comunicação ou decisão externa. |

---

## 15. Checklist de correção da próxima versão

1. O documento declara claramente que é um portfolio log?
2. A seção C tem uma linha por CAPA e espaço para vários registros?
3. Existe uma nota clara sobre folhas de continuação?
4. A população fonte e o Review Period estão definidos?
5. A seção C inclui CAPAs fechados no período e carry-forward conforme regra explícita?
6. Category, Criticality, CTQ/domain e Lifecycle status estão separados?
7. A reconciliação compara o log com uma fonte autorizada?
8. Todas as contagens podem ser reproduzidas a partir da seção C?
9. Distingue-se contagem absoluta de percentual e todos os percentuais têm denominador?
10. E é preenchida apenas quando há recorrência, cluster, deterioração ou interface sistêmica?
11. O CAPA Log evita repetir a análise de causa raiz do CAPA individual?
12. F contém todos os CAPAs ativos e somente eles?
13. Cada CAPA ativo tem milestone, owner, due date e evidência esperada?
14. G exige critério, população, período e fonte para efetividade?
15. `Implemented` está distinguido de `Effective`?
16. A decisão de reabertura preserva o histórico anterior?
17. O fechamento com limitação registra residual risk e responsável pela aceitação?
18. H registra somente outputs criados pela revisão do portfólio?
19. O CAPA Log aponta para POT, SRR, PIR, IMC, MRL ou PIDLR sem duplicar esses instrumentos?
20. A conclusão identifica a população reconciliada, CAPAs ativos, high-criticality CAPAs, padrões e próxima revisão?
21. O Editor v2 permite editar todas as linhas, classificações, caixas, tabelas e páginas de continuação?
22. A página C pode ser repetida sem quebrar o controle documental?
23. O documento permanece legível e dentro dos rodapés quando impresso?

---

## 16. Conclusão

O CAPA Log v0.10 já tem a arquitetura certa: é um **log populacional de portfólio**, não uma ficha de CAPA individual. A versão deve ser aprimorada conservadoramente, sem voltar ao modelo antigo.

As prioridades são:

1. preservar a seção C como Master CAPA Register;
2. garantir linhas suficientes e folhas de continuação para vários CAPAs;
3. tornar a reconciliação com a fonte autorizada incontornável;
4. manter D como análise derivada do registro mestre;
5. usar E somente para padrões recorrentes e interfaces sistêmicas;
6. manter F como índice de CAPAs ativos;
7. manter G como decisão de efetividade, fechamento ou reabertura;
8. usar H somente para outputs e conclusão do portfólio;
9. separar rigorosamente CAPA Log de CAPA individual, PIR, IMC, SRR e POT.

A linha-mestra do instrumento deve ser:

```text
complete CAPA population
→ reconciliation
→ controlled classification
→ portfolio distribution
→ recurrence/systemic screen
→ active follow-up
→ effectiveness decision
→ closure/reopening
→ controlled output and residual-risk update
```

O CAPA Log fecha o ciclo de melhoria da framework, mas não substitui os registros especializados que identificam o problema, investigam a causa ou executam a ação.

---

## 17. Fontes verificadas

- Tese completa (29-10), seção 4.5.7: closing the loop through corrective and preventive action.
- Tese completa (29-10), seção 4.5: Performance Oversight, indicadores, thresholds, recurrence e action cycle.
- Tese completa (29-10), seção 4.6: lifecycle, close-out, lessons e continuidade das ações.
- Tese completa (29-10), seção 5.3.2: review cycle, relação entre indicators, oversight, risk register e corrective action.
- Tese completa (29-10), Appendix W: Corrective and Preventive Action Log, que trata problema sistêmico, recorrência ou tendência que exige correção e prevenção.
- CAPA v0.10: seções A–H, Master CAPA Register, classificação, reconciliação, distribuição, systemic signal, active follow-up, effectiveness/closure e controlled outputs.
- CAPA v0.5: versão histórica usada para confirmar a evolução da arquitetura e a separação entre população, análise e acompanhamento.
- Operational Quality Form Templates skill: cadeia CTQ → risco/sinal → controle → evidência → resultado → ação → efetividade e separação entre revisão operacional e performance agregada.
