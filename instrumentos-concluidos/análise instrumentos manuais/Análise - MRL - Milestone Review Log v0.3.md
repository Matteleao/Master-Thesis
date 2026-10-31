# Análise crítica — MRL: Milestone Review Log v0.3

**Status:** análise manual para orientar a próxima revisão do instrumento. O HTML v0.3 não foi alterado nesta etapa.

## 1. Veredito executivo

O MRL v0.3 está conceitualmente muito mais próximo do instrumento necessário do que a versão antiga. A mudança mais importante foi correta: o MRL deixou de ser um log genérico de revisão periódica e passou a ser um **gate record**. Sua função é registrar a decisão formal do PI sobre se uma unidade de implementação pode passar por um marco configurado, passar com condições ou permanecer bloqueada.

A tese sustenta essa função. Ela descreve milestone review como uma revisão formal em pontos nos quais ameaças consequentes se concentram, com decisão suficientemente precoce para corrigir um padrão antes que ele afete casos posteriores. A tese também descreve gates de saída das fases do lifecycle e afirma que, embora os participantes avancem em tempos diferentes, o site precisa confirmar as condições de passagem antes de prosseguir para uma próxima etapa organizacional.

A versão atual já preserva várias decisões importantes:

- não repete o conteúdo clínico, operacional, de safety, risco, CAPA ou performance dos instrumentos de origem;
- exige um trigger observável e um denominador explícito;
- separa configuração do milestone, índice de decisões e registro detalhado;
- exige um pacote de evidências rastreável;
- distingue implementação, rastreabilidade e suficiência;
- permite Pass, Pass with Conditions e Blocked;
- obriga que uma condição tenha destino, evidência de clearance e trigger de re-review;
- permite continuidade após a decisão sem duplicar o plano de ação do instrumento de origem.

**Recomendação geral:** manter a arquitetura do v0.3 e fazer uma revisão focal. O principal trabalho não é criar mais tabelas. É tornar absolutamente explícito:

1. qual decisão o MRL toma;
2. qual unidade está passando pelo gate;
3. quais condições mínimas precisam estar demonstradas;
4. como o MRL se relaciona com POT, IMP, IMC, SRR e os instrumentos especialistas;
5. quando um milestone é realmente atingido;
6. o que significa passar com condições;
7. como a decisão é aplicada quando participantes estão simultaneamente em fases diferentes.

---

## 2. A decisão que o MRL deve suportar

Depois de preencher um registro MRL, o PI deve conseguir decidir:

> **For the defined implementation unit and configured milestone, is the current evidence sufficient to permit the defined next step, permit it only within stated conditions, or block the transition until specified evidence is available?**

Essa decisão tem quatro elementos que não podem desaparecer:

```text
configured milestone
→ defined implementation unit
→ evidence package and sufficiency assessment
→ permitted scope / restriction / block
```

O MRL não decide se todo o estudo está “bom”. Ele não certifica que todos os resultados clínicos são favoráveis, não encerra uma CAPA, não substitui a avaliação de safety, não libera automaticamente uma pessoa para uma tarefa e não determina sozinho que um indicador está dentro do limite.

Ele decide se, para aquele milestone e aquela unidade definida, a implementação atual permite a próxima ação organizacional especificada.

### 2.1. Unidade de análise

A unidade de análise não é simplesmente “o estudo” nem “a data da revisão”. Deve ser definida pelo milestone. Exemplos:

- site 014 no gate de start-up para release to enroll;
- surgeon S-03 nos cinco primeiros procedimentos;
- cohort of first five participants completing the immediate postoperative pathway;
- follow-up pathway after the configured number or proportion of due assessments;
- endpoint assessment process after the defined evidence package is available;
- site close-out readiness.

A configuração deve obrigar o preenchimento de:

- milestone ID;
- implementation unit;
- population or cohort;
- denominator;
- trigger achieved date;
- evidence period and cut-off;
- permitted next step.

“Review type”, “quarterly review” ou “milestone review” não são substitutos de unidade de análise.

---

## 3. O que a tese realmente exige do MRL

A tese apresenta quatro ideias que devem governar o desenho:

### 3.1. Revisão em pontos de concentração de ameaça

A tese descreve milestone review em quatro pontos principais:

1. procedural implementation;
2. immediate postoperative period;
3. approach to endpoint assessment;
4. close-out.

Esses pontos são específicos do perfil de risco de uma investigação cirúrgica com implante e devem ser adaptados quando o dispositivo, procedimento ou desenho do estudo mudar.

### 3.2. Gates de saída do lifecycle

A tese também descreve fases de lifecycle e condições de saída. Start-up estabelece as condições para enrollment; enrollment cobre screening e consent; surgery cobre device management e procedural delivery; follow-up cobre retenção, outcomes e imaging; data capture e deviation management atravessam todas as fases.

O MRL deve transformar as condições de passagem relevantes em decisões formais. Ele não precisa criar um milestone para cada microfase ou para cada rotina.

### 3.3. Simultaneidade entre participantes

A tese é explícita de que participantes diferentes podem estar em fases diferentes ao mesmo tempo. Um participante pode estar em screening enquanto outro está em follow-up.

Consequentemente, o MRL não deve ser interpretado como uma autorização para o site “fechar” uma fase inteira para todos os participantes antes de qualquer participante entrar na fase seguinte. O gate normalmente é uma decisão sobre:

- readiness do site;
- maturidade de um processo;
- autorização de uma transição organizacional;
- suficiência de uma unidade específica;
- necessidade de restrição ou reforço de controle.

A configuração precisa explicar se o milestone é:

- site-level;
- surgeon-level;
- process-level;
- cohort-level;
- participant-derived but not participant-level;
- close-out-level.

### 3.4. Decisão formal do PI

O MRL é o registro da decisão formal. Os instrumentos especialistas produzem os dados e as revisões que compõem o pacote; o POT pode registrar a discussão de oversight ou o evento que levou à decisão; mas o MRL registra o gate decision propriamente dito.

---

## 4. Fronteira com os outros instrumentos

### 4.1. MRL versus POT

A separação atual está correta, mas deve ficar ainda mais simples:

| Instrumento | Função principal |
|---|---|
| POT | Registra oversight ativo do PI durante a condução: sinais, decisões, ações, escalonamentos e follow-up. |
| MRL | Registra a decisão formal de passagem, passagem condicionada ou bloqueio em um milestone configurado. |

O POT pode identificar que uma decisão precisa ser tomada ou acompanhar uma condição durante a condução. O MRL formaliza o resultado do gate quando o trigger foi atingido.

Não se deve copiar para o MRL:

- a ata completa de uma reunião de oversight;
- a narrativa de um finding já documentado no POT;
- a investigação de uma CAPA;
- a análise de uma complicação;
- a revisão detalhada de uma série de casos.

O MRL deve citar o POT e o registro de origem quando forem relevantes para a decisão.

### 4.2. MRL versus IMP

| Instrumento | Pergunta que responde |
|---|---|
| IMP | Como o site planeja verificar seus controles, com que frequência, amostra, reviewer e trigger? |
| MRL | A evidência disponível permite que esta unidade passe pelo milestone configurado? |

O IMP é prospectivo e operacional. O MRL é uma decisão de gate. O MRL pode consultar o IMP e o IMC, mas não deve executar a verificação planejada pelo IMP nem recalcular o resultado do IMC.

### 4.3. MRL versus IMC

| Instrumento | Papel |
|---|---|
| IMC | Executa um ciclo de internal verification e registra execução, evidência, findings, limitações e ações. |
| MRL | Usa os resultados pertinentes para decidir se a implementação é suficiente para o milestone. |

O MRL deve perguntar se o controle necessário foi verificado e se a evidência é suficiente para o gate. Não deve repetir todas as perguntas do IMC.

### 4.4. MRL versus SRR

O SRR mantém o risco e os controles do site. O MRL não reclassifica todos os riscos. Ele verifica se riscos ou controles relevantes para aquele gate têm status compatível com a passagem.

Quando uma condição do MRL expõe risco residual, o SRR continua sendo o destino da atualização do risco. O MRL registra apenas a decisão de gate e a referência.

### 4.5. MRL versus CAPA Log

O MRL não fecha CAPA. Pode impor como condição que uma CAPA esteja aberta, em progresso, efetiva ou acompanhada por determinada evidência, mas o CAPA Log continua responsável por:

- root cause;
- corrective action;
- preventive action;
- owner;
- milestones da ação;
- effectiveness review;
- closure.

Uma decisão “Pass with Conditions” não deve ser usada como uma forma informal de encerrar uma CAPA.

### 4.6. MRL versus registros especialistas

Os registros especialistas continuam sendo autoritativos para seu objeto:

- TRE, DTRM, CCDM, RACI e SCR para pessoas, tarefas, release, supervisão e qualificação;
- ICDL para dados intraoperatórios e device/procedure traceability;
- IQL/SIRR para image-set quality e readiness;
- PFVR/FUCR para follow-up individual e agregado;
- SART/SCML/CSST para safety, complication indexing e signal surveillance;
- PIR para indicadores e tendências;
- PIDLR para debrief e lessons learned.

O MRL deve montar uma visão de suficiência usando referências, não reescrever esses registros.

---

## 5. O que está correto no MRL v0.3

### 5.1. Purpose and Use e boundary

A primeira página declara corretamente que o MRL é um gate record e que não substitui os registros especialistas. Essa frase deve ser preservada.

A regra de que um calendário sozinho não cria um milestone também é correta. Um milestone precisa de trigger, threshold, unidade, escopo, evidência esperada e janela de revisão previamente configurados.

### 5.2. Milestone Configuration Register

A seção C é uma boa solução porque separa o desenho do gate da decisão que ocorrerá depois. A tabela permite adaptar o MRL à investigação, em vez de impor uma sequência fixa.

Os campos corretos são:

- ID;
- configured gate decision;
- lifecycle alignment;
- use/no use;
- implementation unit;
- objective trigger/threshold;
- scope/denominator;
- PI review window.

A possibilidade de repetir a página quando a configuração mudar prospectivamente também é importante.

### 5.3. Milestone Decision Index

A seção D é útil como índice de todas as decisões formais do estudo. Ela não deve substituir o registro detalhado, e o texto atual deixa isso claro.

A coluna “Next milestone or re-review trigger” é especialmente importante porque transforma a decisão em continuidade operacional.

### 5.4. Evidence Reference Register

A seção E está no caminho correto: uma linha por elemento de evidência, com fonte autoritativa, cobertura, status e observação relevante para a decisão.

A regra de citar `[instrument] | [record or entry ID] | [version or signed date] | [case, cohort, surgeon or period] | [controlled location]` deve ser preservada. Referências vagas como “checked in the system” não são suficientes.

### 5.5. Implementation Sufficiency Assessment

A seção F é necessária porque o MRL precisa de uma síntese de gate, mas deve continuar sendo uma síntese, não uma nova auditoria.

As perguntas atuais são adequadas:

- trigger atingido;
- controles implementados;
- role release, authorization and supervision;
- source records criados e recuperáveis;
- internal verification ou maturity review realizada;
- evidência rastreável e suficiente;
- sinais, exceções e limitações com rota definida.

A distinção entre “controle existe”, “controle foi usado” e “evidência sustenta a próxima decisão” deve ser mantida.

### 5.6. Pass, Pass with Conditions e Blocked

A lógica de três resultados é apropriada:

- **Pass:** o próximo passo definido está permitido no escopo especificado;
- **Pass with Conditions:** o próximo passo é permitido apenas dentro das restrições escritas e com evidência de clearance definida;
- **Blocked:** a transição não é permitida até que a lacuna seja resolvida ou uma nova decisão formal seja tomada.

O MRL deve evitar que “Pass” seja interpretado como “todos os resultados são bons”. Pass significa suficiência para aquele gate, não sucesso clínico global.

### 5.7. Condition Clearance and Re-review

A seção J é uma boa extensão porque permite fechar condições sem copiar a CAPA ou o action plan. Ela deve continuar sendo usada somente quando houve condição ou bloqueio.

---

## 6. Problemas críticos que ainda precisam de ajuste

### 6.1. A lista M0–M6 parece mais obrigatória do que deveria

A seção C chama a lista de base reutilizável e diz que milestones podem ser omitidos. Isso é correto, mas a presença de M0–M6 em linhas sucessivas pode fazer o usuário interpretar que existe uma sequência obrigatória.

Recomendação:

- mudar o título de “base set” para “illustrative configuration options” ou equivalente;
- incluir uma coluna “Decision enabled by this gate”;
- incluir uma coluna “Why this gate is needed for this study”;
- deixar claro que um milestone só deve ser ativado se mudar uma decisão;
- não exigir M0, M2 ou qualquer outro milestone sem justificativa no risk assessment ou na arquitetura do estudo.

A configuração deve evitar a criação de milestones apenas porque o formulário oferece uma linha.

### 6.2. M0 precisa de fronteira explícita

A tese permite uma decisão de feasibility/capability registrada no MRL em determinados níveis, mas feasibility também se relaciona ao processo do sponsor e à avaliação de capacidade do site.

O MRL deve esclarecer que M0, quando usado, não substitui:

- sponsor site selection;
- feasibility questionnaire;
- contract/budget assessment;
- institutional authorization;
- formal qualification of the site.

Ele registra apenas a decisão local/controlada de que a capacidade necessária para a implementação escolhida foi avaliada e qual nível de implementação foi adotado.

### 6.3. M1 deve ser o gate de start-up mais importante

A tese afirma que a revisão que fecha start-up confirma que as dependências estão completas, registra o nível de implementação e confirma os instrumentos adicionais exigidos pelo risco.

Por isso, M1 precisa ser explicitamente descrito como:

```text
site readiness / release to enroll
```

Sua evidência deve poder demonstrar, conforme aplicável:

- RACI com holders e backups;
- DTRM/TRE e liberações;
- CCDM e limites de supervisão;
- SCR para qualificação cirúrgica;
- SRR aberto e controles definidos;
- IMP aprovado;
- fontes críticas e regras de dados mapeadas;
- IQL/SIRR ou readiness de imaging;
- regras de safety e complicações prontas;
- instrumentos e capacidades compatíveis com o nível escolhido.

M1 não deve ser apenas “forms completed”. Deve ser uma decisão sobre capacidade executável.

### 6.4. M3 não deve ser confundido com learning curve completo

O exemplo de M3 usa os primeiros cinco procedimentos de um surgeon. Isso é útil, mas “early procedural implementation maturity” não significa que a curva de aprendizagem terminou.

O milestone deve avaliar se:

- o processo foi implementado como configurado;
- os registros conseguem reconstruir os procedimentos;
- os controles críticos funcionaram;
- há limitações que exigem restrição, proctoring, supervisão ou repetição;
- o próximo escopo é permitido.

O SLCT continua sendo responsável pela análise da learning curve. O MRL só decide se a evidência permite o próximo passo.

### 6.5. M4 mistura surgery e follow-up

“Postoperative and follow-up pathway maturity” pode ser um gate válido, mas a frase mistura dois objetos diferentes:

- execução imediata pós-operatória;
- desempenho longitudinal do follow-up.

Recomendação: manter M4 se o estudo realmente precisar de um gate integrado, mas obrigar o usuário a declarar se o milestone está avaliando:

1. immediate postoperative pathway;
2. first follow-up pathway;
3. retention/completeness pathway;
4. uma combinação justificada.

Não usar “follow-up maturity” sem definir a população, a janela e os componentes necessários.

### 6.6. M5 precisa definir “endpoint assessment readiness”

O milestone de endpoint não deve esperar necessariamente que todos os participantes tenham terminado. A tese reconhece condução simultânea.

M5 deve ser definido como readiness ou evidence maturity do processo, por exemplo:

- endpoint-critical fields têm fonte definida;
- método de avaliação é aplicável;
- image sets necessários são utilizáveis;
- follow-up necessário está sendo executado;
- reconciliação de dados funciona;
- limitações são conhecidas e tratáveis.

O MRL não deve ser transformado em uma análise final de resultados clínicos. O PIR e os instrumentos especialistas continuam responsáveis pelos resultados e indicadores.

### 6.7. M6 deve ser um gate de close-out, não apenas uma lista de pendências

M6 deve responder se o site pode entrar em close-out ou se ainda existem condições que impedem o encerramento controlado.

A evidência pode incluir:

- participants accounted for;
- follow-up obligations resolved or formally transferred;
- safety and deviation records reconciled;
- open CAPAs routed or closed according to their own system;
- data and source records filed;
- device accountability reconciled;
- outstanding limitations documented;
- archive and retention route confirmed.

O MRL não deve declarar CAPAs ou safety cases encerrados se esses registros ainda estiverem abertos.

### 6.8. F pode ficar redundante com IMC se não limitar sua pergunta

A seção F deve sempre começar com “for this milestone and implementation unit”.

Se a pergunta puder ser respondida com uma repetição do IMC, ela está mal formulada. O F deve responder apenas:

> A evidência já existente é suficiente para a decisão de gate?

Ele não deve perguntar novamente se cada controle foi realizado em todos os casos quando o IMC já fez essa avaliação.

### 6.9. A condição precisa ter escopo permitido explícito

A coluna “Effect on permitted scope / restriction” é correta, mas precisa ser obrigatória e concreta.

“Proceed with monitoring” é vago. Melhor:

- proceed with surgeon S-03 only under second-person UDI reconciliation;
- do not expand to additional operators;
- continue enrollment but hold endpoint declaration;
- repeat the gate after the first two additional procedures;
- allow follow-up but not close-out.

A condição precisa dizer o que pode acontecer agora e o que continua proibido.

### 6.10. Re-review trigger não deve ser apenas uma data

A data máxima é útil, mas o trigger objetivo é mais importante:

- after two consecutive reconciled procedures;
- after all first five participants complete the defined window;
- after CAPA effectiveness review;
- after the next IMC cycle;
- after evidence from the specified source is available.

“Before next review” não é suficiente sem explicar qual evento cria a próxima revisão.

---

## 7. Arquitetura recomendada para a próxima revisão

A arquitetura atual pode ser mantida com estes ajustes de conteúdo:

### Página 1 — Purpose, boundary and decision model

Deve conter:

- Purpose and Use;
- Unit of analysis;
- Decision support;
- Inputs;
- Outputs;
- diferença entre MRL, POT e IMP;
- regra de que milestone precisa de trigger configurado;
- regra de que o MRL não fecha os registros de origem.

### Página 2 — Milestone Configuration Register

Adicionar ou explicitar:

- gate decision enabled;
- implementation unit type;
- reason this gate is needed;
- trigger/threshold;
- denominator;
- evidence expected;
- review window;
- permitted next step;
- version/effective date.

M0–M6 devem ser opções configuráveis, não uma sequência obrigatória.

### Página 3 — Decision Index

Manter como índice de todas as decisões. Acrescentar, se houver espaço:

- current scope permitted;
- decision date;
- condition/block status.

### Página 4 — Decision context and evidence package

Manter uma entrada por gate e uma linha por evidência. A fonte deve ser citada com ID, versão/data, período, unidade e localização controlada.

Adicionar uma pequena regra:

```text
The evidence package supports the gate decision; it does not replace the originating record.
```

### Página 5 — Sufficiency assessment

Manter as perguntas F, mas agrupá-las em três dimensões:

1. **Trigger and scope:** o milestone foi atingido para a unidade correta?
2. **Control and evidence:** os controles relevantes existiam, foram usados e podem ser reconstruídos?
3. **Decision sufficiency:** a evidência permite a transição sem impacto material desconhecido?

Isso reduz a aparência de checklist genérico.

### Página 6 — Formal PI decision and conditions

Manter Pass, Pass with Conditions e Blocked. O painel deve exigir:

- permitted scope;
- prohibited scope, quando aplicável;
- condition ID;
- destination record;
- evidence required;
- trigger for re-review;
- latest acceptable review window;
- PI interpretation.

### Página 7 — Authentication, clearance and filing

Manter a seção de clearance para condições e bloqueios. O bloco de filing deve declarar:

- MRL entry ID;
- milestone configuration version;
- linked records;
- controlled location;
- reviewer/PI;
- date;
- whether the next milestone is open, pending or blocked.

---

## 8. Estados de decisão recomendados

### Pass

Usar somente quando:

- trigger foi atingido;
- unidade e denominador estão corretos;
- evidência relevante está disponível;
- limitações conhecidas não impedem o próximo passo;
- não existe impacto material desconhecido;
- a scope permitted está clara.

### Pass with Conditions

Usar quando o próximo passo pode ocorrer, mas apenas com uma restrição controlada.

Deve indicar:

- o que pode continuar;
- o que não pode ser expandido;
- owner da condição;
- destino da ação;
- evidência de clearance;
- trigger de re-review;
- consequência se a condição não for cumprida.

### Blocked

Usar quando:

- o trigger não foi realmente atingido;
- evidência crítica está ausente ou não é reconstruível;
- o controle essencial não foi implementado;
- há impacto material desconhecido;
- a autorização ou qualificação necessária não existe;
- a condição anterior não foi efetiva;
- não há base suficiente para permitir a transição.

Blocked não significa necessariamente que o estudo inteiro deve parar. O escopo bloqueado deve ser explícito.

---

## 9. Pacote mínimo de evidências por tipo de milestone

| Milestone | Evidência normalmente relevante |
|---|---|
| M0 Feasibility/capability | capability decision, SRR, implementation level, staffing/capacity, sponsor or institutional boundary |
| M1 Start-up release to enroll | RACI, DTRM/TRE, CCDM, SCR, SRR, IMP, readiness records, source/data map, safety route |
| M2 Early enrollment | SIFSL/PSEAR references, consent/screening process, early enrollment completeness, deviations and readiness limitations |
| M3 Procedural implementation | ICDL, SLCT, SCR, TRE/CCDM/RACI, device traceability, IMC, relevant CAPA/POT/SRR records |
| M4 Postoperative/follow-up pathway | PFVR, FUCR, SART/SCML where relevant, IQL, IMC and endpoint-critical follow-up evidence |
| M5 Endpoint assessment/evidence maturity | PFVR/FUCR, IQL/SIRR, PIR, endpoint data agreement, source reconciliation, limitations and data usability |
| M6 Close-out readiness | outstanding participant obligations, safety/deviation reconciliation, device accountability, CAPA/PIDLR status, archive and filing evidence |

Essa tabela é um guia de planejamento. O usuário deve citar somente as fontes realmente aplicáveis ao estudo e ao milestone.

---

## 10. Interfaces de saída

Cada decisão MRL deve produzir uma saída clara:

| Saída | Destino |
|---|---|
| Gate passed | RACI/POT/operational plan as applicable; next milestone opened |
| Gate passed with condition | destination record named in the condition table |
| Gate blocked | PI/POT route, SRR or CAPA route, and re-review trigger |
| Evidence limitation | originating record and limitation register/route |
| Risk increase | SRR |
| Recurrent control failure | CAPA Log and potentially IMP change |
| Safety concern | SART/SCML/CSST and sponsor route as applicable |
| Performance concern | PIR, FUCR, IMC or relevant indicator route |
| Implementation-level change | POT/MRL and the applicable controlled configuration |

Não deixar “action required” sem destino.

---

## 11. Exemplo contínuo recomendado

O exemplo atual MRL-EX-001 / M3 / S-03 é útil e deve ser preservado, mas precisa demonstrar a cadeia completa.

### Configuração

```text
M3 — early procedural implementation gate
Unit: Surgeon S-03
Trigger: first five procedures completed
Denominator: 5 of 5
Review window: within 10 business days
Permitted next step: continue the configured procedural scope
```

### Evidence package

```text
ICDL cases 001–005 → procedure and device traceability
TRE/T-07 → role release
SCR → surgeon scope decision
IMC-03 → internal verification of reconciliation control
CAPA-014 → open action related to UDI reconciliation
```

### Sufficiency assessment

```text
Trigger achieved: Complete
Controls implemented: Complete
Evidence reconstructable: Complete
Open issue: UDI reconciliation weakness
Material unknown impact: not demonstrated for future cases
```

### PI decision

```text
Pass with Conditions
Permitted: S-03 may continue within the defined scope
Restriction: second-person UDI reconciliation before case closure
Destination: CAPA-014 and IMC follow-up
Clearance: two consecutive reconciled procedures
Re-review: before expansion or at the defined trigger
```

### Clearance

```text
IMC follow-up reviewed
ICDL cases 006–007 reconciled
CAPA evidence reviewed
Condition cleared by PI
```

O exemplo demonstra que o MRL não reescreve a CAPA nem o ICDL. Ele apenas usa suas referências para formular e depois reavaliar a decisão de gate.

---

## 12. Recomendações finais de conteúdo

1. Manter o MRL v0.3 como base.
2. Tornar o MRL explicitamente um gate record, não um review log periódico.
3. Explicar na seção C que M0–M6 são opções configuráveis, não sequência universal.
4. Tornar M1 o gate explícito de start-up readiness/release to enroll.
5. Diferenciar procedural implementation maturity de learning curve analysis.
6. Separar, em M4, immediate postoperative pathway de follow-up pathway quando necessário.
7. Definir M5 como readiness/evidence maturity, não como resultado clínico final.
8. Fazer com que M6 avalie close-out readiness sem fechar registros de origem.
9. Limitar F à suficiência para aquele gate, evitando repetir IMC.
10. Exigir permitted scope e prohibited scope na decisão.
11. Exigir trigger objetivo para re-review, não apenas uma data.
12. Manter a condição vinculada a um registro de destino, owner e evidência de clearance.
13. Exigir unidade, denominador e data de corte em cada decisão.
14. Preservar o índice D como visão de continuidade, sem substituir os registros detalhados.
15. Não transformar o MRL em uma ata de reunião, um action log ou um checklist de todos os instrumentos.

---

## 13. Checklist de validação do futuro HTML

O futuro HTML revisado deve permitir responder “sim” a todas as perguntas abaixo:

### Função e fronteira

- O documento explica que o MRL decide uma passagem de gate?
- Está claro que ele não substitui POT, IMP, IMC, SRR, CAPA ou registros especialistas?
- Está claro que o MRL não fecha os registros de origem?

### Configuração

- Cada milestone tem ID e versão?
- Está claro se é site-level, surgeon-level, process-level, cohort-level ou close-out-level?
- O trigger é observável?
- O denominador está explicitamente definido?
- A janela de revisão está definida?
- O próximo passo permitido está escrito?
- M0–M6 aparecem como opções e não como sequência obrigatória?

### Evidência

- Cada referência é recuperável?
- A fonte inclui ID, versão/data, período e localização?
- A cobertura/denominador está registrado?
- O pacote evidencia o gate sem duplicar o documento de origem?
- As limitações são identificadas?

### Decisão

- Pass, Pass with Conditions e Blocked estão definidos?
- O escopo permitido está explícito?
- A restrição ou bloqueio está explícito?
- Cada condição tem ID, owner/destino, evidência de clearance e trigger de re-review?
- A decisão não pode ser interpretada como uma conclusão clínica global?

### Continuidade

- O índice conecta cada decisão ao próximo milestone?
- O clearance da condição aponta para a evidência realmente revisada?
- O filing identifica a versão da configuração e os registros vinculados?
- Uma mudança de configuração vale prospectivamente?

### Usabilidade visual

- A primeira página possui Purpose and Use com Unit of analysis, Decision support, Inputs e Outputs?
- A tabela de evidências tem espaço suficiente para referências reais?
- A área de decisão tem espaço suficiente para permitted scope, restriction e rationale?
- A seção de clearance é repetível sem criar um segundo action log?
- Nenhuma tabela ou assinatura ultrapassa o rodapé?
- O Editor v2 permite editar todas as células, caixas, linhas, colunas, fontes e opções?

---

## 14. Conclusão

O MRL v0.3 deve ser mantido. A ideia central está correta e alinhada à tese: ele é o documento que transforma uma concentração de risco em uma decisão formal de passagem, passagem condicionada ou bloqueio.

O principal risco atual é de interpretação, não de ausência de estrutura. Sem definições mais fortes, o usuário pode:

- usar o MRL como calendário periódico;
- tratar M0–M6 como uma sequência obrigatória;
- repetir a análise do IMC;
- interpretar Pass with Conditions como uma CAPA fechada;
- usar “maturity” como sinônimo de learning curve completa;
- bloquear ou liberar o estudo inteiro sem definir o escopo da decisão;
- registrar uma condição sem trigger objetivo de clearance.

A próxima versão deve, portanto, ser uma revisão focal de conteúdo e clareza. Não recomendo reconstruir o instrumento do zero nem acrescentar mais camadas analíticas. O objetivo é tornar cada milestone uma decisão operacional reproduzível:

```text
configured gate
→ defined implementation unit
→ objective trigger and denominator
→ retrievable evidence package
→ sufficiency assessment
→ permitted scope or block
→ linked condition and re-review
```

## 15. Fontes verificadas

- Tese completa, seção de milestone review, lifecycle phases, gates, implementation levels e sequência operacional.
- `MRL_Milestone_Review_Log_v0.3.html`.
- Contexto do branch `codex/thesis-work`, especialmente a separação entre MRL, POT, IMP, IMC e os instrumentos especialistas.
- `Operational Quality Form Templates` skill, incluindo unidade de análise, interconexão, separação de granularidades, decisão e evidência.
