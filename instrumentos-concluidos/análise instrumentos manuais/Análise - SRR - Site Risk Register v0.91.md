# Análise crítica — SRR: Site Risk Register v0.91

**Status:** análise manual para orientar a próxima revisão do instrumento. O HTML v0.91 não foi alterado nesta etapa.

## 1. Veredito executivo

O SRR v0.91 tem a base conceitual correta e não deve ser descartado. Ele já representa adequadamente o instrumento que a tese descreve: um registro prospectivo de riscos criados ou agravados pela execução local da investigação, ligado ao fator CtQ específico que pode ser comprometido.

O ponto mais importante é que o SRR não deve ser um catálogo genérico de perigos, uma cópia do risk assessment do sponsor, uma lista de CAPAs ou uma ata de oversight. Seu objeto é mais específico:

```text
site condition / vulnerability
→ risk to an investigation-specific CtQ factor
→ existing control and evidence
→ residual risk
→ owner and review trigger
→ mitigation / escalation / reassessment
```

A versão atual já contém quase todos esses elementos. Ela preserva:

- foco nos riscos internos do site;
- ligação entre risco e fator CtQ;
- distinção entre controles existentes e mitigação planejada;
- avaliação por probabilidade, impactos e detectabilidade;
- owner, trigger, ação e status;
- revisão periódica e entrada urgente;
- critérios de downgrade e fechamento;
- possibilidade de referências a CAPA, POT, MRL, IMC, SART, CSST, device records e outros instrumentos.

O principal problema não é falta de conteúdo. É que algumas decisões ainda podem ser interpretadas de maneiras diferentes por quem preenche o documento:

1. o que exatamente é o fator CtQ;
2. qual a diferença entre vulnerabilidade, risco, controle e consequência;
3. se a prioridade apresentada é risco inerente ou risco residual;
4. se o status descreve o risco ou a ação;
5. quando a entrada deve ser encaminhada para CAPA, POT, MRL, sponsor ou outro instrumento;
6. como a avaliação de detecção participa da prioridade;
7. como o SRR alimenta o IMP e como o IMC devolve evidência ao SRR.

**Recomendação geral:** manter a estrutura e a identidade do SRR v0.91, fazendo uma revisão focal de linguagem, scoring, risco residual, estado, integração e critérios de fechamento. Não recomendo transformar o registro em um sistema de gestão de risco do sponsor nem criar uma nova taxonomia paralela de fatores.

---

## 2. A decisão que o SRR deve suportar

Depois de preencher ou revisar uma entrada do SRR, o responsável deve conseguir decidir:

> **What local site condition threatens an investigation-specific CtQ factor, what risk remains after the controls already implemented, what must happen next, who owns it, and when the risk must be reassessed or escalated?**

Essa decisão contém cinco perguntas:

1. Qual condição local pode falhar?
2. Qual fator CtQ específico essa condição ameaça?
3. Qual consequência pode ocorrer para segurança, procedimento, dispositivo ou dados?
4. Quais controles já existem e qual risco permanece?
5. Qual resposta, owner, trigger e evidência serão necessários?

O SRR não precisa responder sozinho se um evento individual é um AE, ADE, SAE, SADE ou device deficiency. Essa classificação pertence ao registro de safety aplicável. O SRR deve registrar a vulnerabilidade sistêmica ou processual e apontar para o caso ou registro de origem.

---

## 3. Unidade de análise e granularidade

A unidade de análise é:

```text
one prospective site-level risk threatening one investigation-specific CtQ factor or linked group of factors
```

Uma entrada pode ser relacionada a um processo, equipe, infraestrutura, dispositivo, fluxo de dados, agenda ou capacidade do site. Ela não deve ser simplesmente “CtQ4” ou “follow-up” sem descrever a condição concreta.

### 3.1. Diferença entre domínio, fator, vulnerabilidade e risco

| Elemento | Função |
|---|---|
| CtQ domain | Área operacional ampla que organiza o risco. |
| CtQ factor | Condição importante desta investigação que precisa ser protegida. |
| Local vulnerability | Condição do site que pode impedir ou enfraquecer o controle dessa condição. |
| Risk statement | Como a vulnerabilidade pode comprometer o fator e qual consequência pode resultar. |
| Existing control | Controle já implementado e sustentado por evidência. |
| Planned mitigation | Ação ainda não plenamente implementada para reduzir a vulnerabilidade ou o risco. |
| Residual risk | Risco que permanece depois dos controles implementados e verificados. |

Essa separação precisa aparecer no texto de orientação do formulário. Sem ela, o usuário tende a colocar na mesma célula uma mistura de causa, evento, efeito e ação.

### 3.2. Uma linha por risco decisório

Não é necessário criar uma linha para cada microfalha. Também não é adequado agrupar em uma única linha todos os riscos de “follow-up”, “imaging” ou “staffing”.

Uma nova linha deve ser criada quando a diferença mudar:

- o fator CtQ ameaçado;
- a consequência;
- o controle;
- o owner;
- a prioridade;
- o trigger;
- a rota de escalonamento;
- ou a decisão de ação.

Se duas vulnerabilidades têm consequências e controles diferentes, devem ser entradas distintas, mesmo que pertençam ao mesmo domínio.

---

## 4. O que a tese exige do SRR

### 4.1. Abertura antes da primeira inclusão

A tese coloca o SRR antes da primeira inclusão. Ele deve converter os domínios de qualidade em fatores CtQ relevantes para a investigação concreta, considerando:

- o CIP;
- o que o sponsor comunica como crítico ou arriscado;
- o procedimento;
- o dispositivo;
- o fluxo real do site;
- a capacidade da equipe;
- a infraestrutura;
- a jornada de follow-up;
- as fontes de dados e seus pontos de falha.

O SRR não deve esperar que uma falha ocorra para ser aberto. Depois da abertura, ele continua sendo atualizado conforme surgem condições novas, sinais, alterações de equipe, mudanças de workflow e resultados das revisões.

### 4.2. Foco no risco criado pela execução do site

O texto da tese diferencia o risk register local do risk assessment do sponsor e do arquivo de risco do fabricante. O SRR pode usar informações desses sistemas como entrada, mas não deve simplesmente copiar seus riscos.

A pergunta local é:

> **How can this site’s own execution compromise a critical condition of this investigation?**

Exemplos:

- o site não tem cobertura de fisioterapia em determinados dias e isso ameaça a realização de componentes do follow-up dentro da janela;
- materiais do estudo ficam misturados com componentes semelhantes e isso ameaça a seleção ou rastreabilidade do dispositivo;
- existe um ponto único de falha na equipe e isso ameaça a continuidade do registro de safety;
- a radiologia não consegue produzir uma sequência exigida dentro da janela e isso ameaça a interpretabilidade do endpoint.

A falta de um recurso não é automaticamente um risco alto. É preciso identificar a condição afetada, a consequência provável, os controles existentes e o risco que permanece.

### 4.3. Reavaliação e detecção

A tese pede avaliação da probabilidade e dos impactos sobre o fator CtQ, junto com a possibilidade de a falha permanecer não detectada. O SRR deve manter a detecção porque um risco difícil de detectar pode ser mais perigoso que um risco semelhante facilmente identificável.

A detecção, porém, não deve ser tratada como um detalhe visual da tabela. Ela precisa ter uma definição operacional e participar de uma regra clara de prioridade.

---

## 5. O que está correto no SRR v0.91

### 5.1. Purpose and Use

A primeira página explica corretamente que o SRR identifica, prioriza, monitora e reavalia riscos derivados da execução local. Também estabelece a fronteira com:

- sponsor trial-level risk assessment;
- manufacturer device risk file;
- participant-level safety case records;
- detailed CAPA investigations.

Essa fronteira deve permanecer visível porque evita que cada instrumento tente registrar o mesmo risco de maneira diferente.

### 5.2. Integração do fator CtQ na entrada

A decisão de colocar “CtQ Domain / Factor Threatened” dentro da tabela principal é boa. Ela evita criar uma seção burocrática separada somente para registrar fatores.

O campo deve continuar permitindo que o site:

- escolha o domínio operacional;
- escreva o fator específico da investigação;
- cite a fonte quando o sponsor já comunicou o fator;
- indique quando o fator foi derivado do CIP, do endpoint ou do workflow local;
- registre a dúvida quando o requisito ainda não estiver esclarecido.

Não se deve obrigar o site a inventar um fator CtQ quando a documentação do estudo não o torna verificável.

### 5.3. Categorias operacionais

As categorias da seção B são úteis como orientação e navegação. Elas não devem ser confundidas com a taxonomia CtQ da tese.

Uma categoria responde “em que parte da operação local o risco aparece”. O domínio CtQ responde “qual condição de qualidade a operação precisa proteger”. Uma entrada pode estar na categoria Operational / staffing e ameaçar CtQ7, CtQ10 ou CtQ11.

As categorias devem continuar sendo flexíveis. Não é necessário forçar um risco a produzir impacto em todas as categorias.

### 5.4. Avaliação multidimensional

A separação dos campos é adequada:

- Probability;
- Safety impact;
- Procedure impact;
- Device/accountability impact;
- Data/endpoint impact;
- Detectability.

Isso é superior a um único “impact” porque um risco de agenda pode afetar dados e follow-up sem afetar diretamente o dispositivo, enquanto um risco de rastreabilidade pode afetar device accountability e interpretação causal de forma diferente.

### 5.5. Existing controls versus planned mitigation

A lógica da seção G é essencial e deve ser preservada:

- existing controls são controles já implementados e sustentados por evidência;
- planned mitigation é a resposta que ainda precisa ser implementada ou verificada.

Uma ação planejada não deve reduzir automaticamente a prioridade atual. A redução só ocorre depois de implementação e evidência de que o controle funciona.

### 5.6. Owner e trigger

A entrada tem owner e trigger/KPI para revisão. Isso transforma o SRR de uma lista passiva em um registro operacional.

O trigger deve ser concreto, por exemplo:

- missing UDI;
- reconciliation later than 24 hours;
- two delayed visits in the same process;
- recurrence after CAPA;
- staff departure;
- protocol amendment;
- critical imaging outside window;
- unexpected complication cluster.

“Review when necessary” não é um trigger suficiente.

### 5.7. Revisão e entrada urgente

A seção de Risk Review Log deve ser mantida. Ela registra mudança na evidência, reavaliação e decisão sem apagar o histórico da entrada original.

A seção Emerging / Urgent Risk Entry também é útil, desde que permaneça uma porta de entrada provisória que leve ao registro formal e não se transforme em um segundo risk register.

### 5.8. Critérios de downgrade e closure

A seção F contém uma base correta para distinguir:

- manter risco ativo;
- reduzir prioridade;
- fechar risco.

A lógica precisa apenas ser reforçada para separar risco residual, estado do controle e estado de qualquer CAPA relacionada.

---

## 6. Problemas críticos que precisam de ajuste

### 6.1. A prioridade atual não deixa claro se é inerente ou residual

A tabela de identificação e rating produz uma prioridade, mas não deixa suficientemente claro se ela representa:

- risco antes dos controles;
- risco depois dos controles;
- pior dimensão entre campos;
- prioridade operacional atual;
- ou uma mistura desses elementos.

O relatório de passagem diz que a lógica pretendida é conservar a maior nota dos seis campos e não usar média ou produto. Essa decisão é defensável, mas precisa ser nomeada.

Recomendação:

- chamar a avaliação inicial de **Current / residual risk assessment** quando os controles existentes já forem considerados;
- ou criar explicitamente **Inherent risk** e **Residual/current risk** se a finalidade exigir os dois;
- não manter uma coluna chamada apenas “Overall Priority” sem explicar o momento da avaliação.

Para a maioria dos usos do SRR local, uma avaliação de risco residual/current risk é suficiente, desde que os controles existentes sejam considerados antes da pontuação.

### 6.2. “Max of six fields” precisa de uma regra visível

O formulário deve dizer, de maneira operacional:

```text
Outside the Critical criteria, the highest applicable score among probability, the four impact dimensions and detectability determines the current priority band. Do not average or multiply the fields.
```

Também deve explicar o que acontece quando uma dimensão não é aplicável. “Not applicable” não pode ser confundido com zero ou com impacto ausente.

Se o risco não afeta device accountability, por exemplo, a célula deve indicar N/A com justificativa curta, e a regra deve ignorar a dimensão não aplicável sem convertê-la artificialmente em score 1.

### 6.3. Critical não pode ser apenas o valor mais alto

A categoria Critical deve ter critérios específicos, por exemplo:

- immediate or unresolved participant safety risk;
- unreconciled device traceability break;
- unrecoverable endpoint-critical data loss;
- event requiring immediate PI or sponsor escalation;
- reportable or potentially reportable event requiring the applicable route.

A classificação Critical não deve depender somente de uma soma ou de um 3 em qualquer célula. O formulário precisa distinguir:

- High score;
- Critical condition;
- Mandatory communication;
- Sponsor reporting route.

A obrigação de notificar não deve depender exclusivamente da banda de prioridade do SRR.

### 6.4. O fator CtQ ainda pode ficar vago

A tabela C lista os doze domínios, mas o formulário precisa insistir que o usuário escreva o fator específico da investigação na entrada de risco.

“CtQ4 — Device management” é um domínio, não é um fator suficiente. O fator poderia ser, por exemplo:

> The implanted component can be reconstructed from source documentation and reconciled to the participant and accountability record before case closure.

A seção C pode continuar como referência, mas a seção de registro deve exigir uma formulação concreta do fator ameaçado ou uma referência recuperável ao documento que o define.

### 6.5. A eventual ausência de um CtQ profile precisa ser tratada com cuidado

O requisito X-CtQ no repositório é uma proposta ainda não decidida: criar um perfil curto dos fatores CtQ do estudo, relacionando fatores do sponsor, relevância local e instrumento de controle.

A análise não deve tratá-lo como decisão já aprovada. Porém, a necessidade subjacente é real: se o site não sabe quais fatores da investigação são críticos, pode preencher o SRR apenas com domínios genéricos.

Recomendação conservadora:

- manter o campo CtQ Domain / Factor Threatened dentro de cada entrada;
- permitir uma referência ao CIP, sponsor communication ou risk assessment;
- considerar no futuro um pequeno “investigation CtQ profile” na primeira página apenas se isso não duplicar o sponsor risk assessment;
- não criar uma lista paralela obrigatória de fatores sem aprovação do autor.

### 6.6. Estado do risco e estado da ação estão misturados

“Open — mitigation active” combina dois estados diferentes:

- o risco ainda está ativo;
- a ação de mitigação está em andamento.

Recomendação: separar:

```text
Risk status: Open / Controlled / Escalated / Accepted / Closed
Control/action status: Not started / In progress / Implemented / Effectiveness pending / Effective / Ineffective
```

Isso evita que uma ação em andamento pareça significar que o risco já está controlado.

### 6.7. O risco residual não aparece com força suficiente após a ação

A seção G registra planned mitigation e a seção H registra review. Ainda assim, o usuário pode não saber onde registrar:

- qual foi o controle implementado;
- qual evidência demonstrou implementação;
- se o controle foi efetivo;
- qual é a nova prioridade;
- se o risco permanece ativo.

A revisão deve acrescentar ou tornar explícitos:

- control/action implemented;
- effectiveness evidence;
- current/residual priority;
- current risk status;
- reason for change;
- next due date.

### 6.8. “Existing controls” não deve aceitar promessa futura

O texto atual explica essa distinção, o que é positivo. Na próxima revisão, a tabela deve reforçar visualmente que um controle só entra em “existing controls” quando já existe e pode ser evidenciado.

Exemplo:

- “Coordinator will check UDI” = planned mitigation;
- “Second-person UDI check recorded in cases 006–007” = existing/implemented control with evidence.

### 6.9. Main register está dividido em duas tabelas, mas a continuidade precisa ser mais forte

A separação entre identificação/rating e controls/ownership/follow-up é funcional e deve ser mantida. O mesmo Risk ID deve aparecer de maneira muito visível em ambas as páginas.

A próxima versão deve acrescentar uma nota mais forte:

> Complete Section F before Section G. Use the same Risk ID. Do not create a new risk entry solely because the control or review status changed.

A página de G não deve parecer um segundo registro independente.

### 6.10. Risk Review Log precisa capturar efetividade

A seção H tem “Reassessment Outcome / Current Priority” e “Action or Control Changed?”, mas deve garantir que a pessoa registre a efetividade do controle.

Recomendação de conteúdo:

- evidence reviewed;
- control effectiveness: effective / partially effective / not effective / not assessable;
- current priority;
- risk status;
- reason for change;
- linked action/CAPA;
- next review trigger and due date.

Sem isso, o SRR pode registrar que uma ação foi concluída sem demonstrar que o risco realmente diminuiu.

### 6.11. Entrada urgente precisa de uma ponte controlada

A seção I é adequada como captura provisória, mas deve obrigar:

- provisional entry ID;
- date/time;
- reporter;
- immediate route;
- PI notification;
- sponsor/safety route where applicable;
- formal SRR Risk ID after review;
- whether the urgent entry remains only a pointer or becomes an SRR risk.

Ela não deve duplicar a narrativa do SART, CSST ou outro registro de evento. Deve registrar a condição urgente, a contenção imediata e o encaminhamento.

### 6.12. PI escalation não é igual a sponsor reporting

A coluna “PI Escalation Required?” é útil, mas precisa ser distinguida de:

- PI awareness;
- PI decision;
- sponsor notification;
- safety reporting;
- regulatory reporting;
- CAPA initiation.

Uma entrada pode exigir PI review sem ser reportável ao sponsor. Um evento safety pode exigir rota formal independentemente da prioridade escolhida no SRR.

### 6.13. Critérios de fechamento precisam separar risco e CAPA

O SRR não deve fechar um risco apenas porque uma CAPA foi marcada como closed. O fechamento exige uma conclusão sobre a vulnerabilidade e a aplicabilidade do risco.

O risco pode ser fechado porque:

- a condição não se aplica mais;
- o workflow mudou e eliminou a vulnerabilidade;
- a fase terminou;
- o processo foi substituído;
- a causa foi removida e a efetividade foi demonstrada.

Se o risco permanece, mas está dentro de controle, o status deve ser Controlled ou Active under control, não Closed.

### 6.14. Aceitação de risco residual deve ser explícita

Um risco não precisa desaparecer para deixar de exigir uma ação imediata. Pode haver risco residual aceito, desde que:

- a justificativa seja registrada;
- o owner seja nomeado;
- o PI ou função autorizada aceite conforme o nível de risco;
- o trigger continue ativo;
- a aceitação tenha prazo ou condição de reavaliação quando necessário.

O formulário deve evitar que “no further action” seja usado sem justificar por que o risco é aceitável.

### 6.15. Categorias e domínios não devem criar duplicação

O risco pode aparecer em uma categoria Operational / staffing e ameaçar CtQ7, CtQ11 e CtQ12. Não é necessário abrir três riscos idênticos apenas para cobrir três domínios.

A entrada deve permitir:

- um domínio principal;
- fatores relacionados ou cross-reference;
- um único risk owner quando a responsabilidade for comum;
- múltiplos destinos quando a ação envolver mais de um processo.

---

## 7. Interfaces operacionais

### 7.1. SRR → IMP

O SRR informa o IMP sobre:

- quais controles precisam ser verificados;
- quais riscos exigem frequência maior;
- quais domínios precisam de census em vez de amostra;
- quais triggers exigem revisão antecipada;
- quais fontes precisam ser incluídas;
- quais owners ou reviewers não podem ser usados por conflito de função;
- quais ações ou CAPAs exigem eficácia monitorada.

O IMP não deve repetir a análise do risco. Ele converte o risco em um plano de verificação.

Exemplo:

```text
SRR: repeated UDI reconciliation vulnerability, difficult to detect and affecting device traceability.
IMP: include implant traceability in every early review, census the first procedures and trigger immediate review for any mismatch.
```

### 7.2. IMP/IMC → SRR

O IMC devolve ao SRR:

- evidence that the control was executed;
- finding or limitation;
- recurrence;
- control effectiveness;
- change in current priority;
- recommendation for new mitigation or escalation.

O SRR permanece como a fonte da decisão de risco. O IMC não deve reescrever o risco inteiro.

### 7.3. SRR → CAPA Log

O SRR pode gerar ou referenciar uma CAPA quando houver:

- recorrência importante;
- falha sistêmica;
- controle ineficaz;
- necessidade de ação corretiva e preventiva;
- vulnerabilidade com múltiplos milestones;
- necessidade de acompanhar efetividade em nível de portfólio.

O CAPA Log é responsável pela investigação e pelas ações detalhadas. O SRR registra o risco, a referência e a evolução do risco residual.

### 7.4. SRR → POT

O POT recebe o risco quando for necessária decisão ativa do PI sobre:

- prioridade ou aceitação do risco;
- restrição de escopo;
- escalonamento;
- recursos;
- suspensão ou alteração de processo;
- condição que precisa de oversight;
- mudança relevante no controle.

O POT não substitui a entrada do SRR. Ele documenta a decisão de oversight e aponta de volta ao Risk ID.

### 7.5. SRR → MRL

O MRL usa o SRR quando um risco ou uma condição de controle interfere em um gate de milestone.

O SRR continua sendo a fonte do risco. O MRL decide se a evidência permite a passagem, passagem condicionada ou bloqueio do milestone.

### 7.6. SRR → PIR

O SRR pode informar o PIR sobre:

- necessidade de indicador;
- mudança de threshold;
- categoria de risco;
- recorrência;
- controle que precisa ser acompanhado quantitativamente.

O PIR pode devolver uma tendência que justifique revisão do SRR. O PIR não substitui a descrição causal e contextual do risco.

### 7.7. SRR e instrumentos de safety

Quando um risco envolve safety, device deficiency, complication ou reporting, o SRR registra a vulnerabilidade local e aponta para o registro competente:

- SART para o caso e a rota de avaliação/reporting;
- SCML para o índice local periódico;
- CSST para a análise de sinal e padrão;
- sponsor route quando aplicável.

O SRR não deve duplicar a narrativa clínica nem decidir a classificação formal do evento no lugar do instrumento apropriado.

---

## 8. Arquitetura recomendada para a próxima revisão

A estrutura A–K pode ser preservada, com ajustes focais.

### Página 1 — Purpose, categories and CtQ linkage

Manter:

- header/document control;
- Purpose and Use;
- Risk Categories;
- Common Review Triggers;
- CtQ Domains.

Melhorar a orientação para dizer:

```text
Choose the operational category, then state the investigation-specific CtQ factor threatened by the local condition. Do not use the domain name as the risk statement.
```

Considerar uma caixa pequena para:

- source of factor: CIP / sponsor communication / local workflow / linked assessment;
- factor status: confirmed / to be clarified.

Não criar obrigatoriamente uma tabela nova de fatores sem decisão posterior do autor.

### Página 2 — Rating guide and worked example

Preservar o exemplo contínuo, porque ele mostra como preencher a entrada. Melhorar:

- definição da regra de prioridade;
- tratamento de N/A;
- diferença entre existing control e planned mitigation;
- diferença entre current/residual risk e action status;
- critérios de Critical;
- exemplo de revisão após o controle ser implementado.

### Página 3 — Main register: identification and rating

Campos mínimos:

- Risk ID;
- Date opened;
- Category;
- Local vulnerability;
- Risk statement;
- CtQ domain;
- Investigation-specific factor threatened;
- Source/foundation of factor;
- Probability;
- four impact dimensions;
- Detectability;
- current/residual priority;
- critical/escalation flag when applicable.

A coluna pode ficar larga o suficiente para a frase de risco e para o fator CtQ.

### Página 4 — Controls, ownership and follow-up

Campos mínimos:

- Risk ID;
- existing control;
- evidence of existing control;
- underlying vulnerability;
- risk owner;
- PI decision/awareness route;
- review trigger;
- planned mitigation or linked action;
- destination record;
- risk status;
- action/control status;
- last review;
- next due.

Não obrigar uma nova CAPA quando já existir uma ação adequada. Referenciar o ID existente.

### Página 5 — Review log and urgent entry

A revisão deve incluir:

- evidence reviewed;
- effectiveness;
- current priority;
- status;
- reason for change;
- action/control change;
- next trigger/due date.

A entrada urgente deve incluir uma ponte para o Risk ID formal e para qualquer instrumento de safety, CAPA ou POT usado na resposta.

### Página 6 — Decision, downgrade, escalation and closure

Preservar a tabela de decision type, mas separar:

- risk status;
- control effectiveness;
- CAPA status;
- PI decision;
- closure rationale.

A certificação deve confirmar que riscos ativos, riscos aceitos, escalonamentos e limitações foram encaminhados, não que todos os riscos foram eliminados.

---

## 9. Classificação recomendada

### 9.1. Probability

- **1 — Low:** unlikely or isolated vulnerability, based on current conditions;
- **2 — Moderate:** plausible during normal site conduct or supported by a known weakness;
- **3 — High:** likely, recurrent, already observed or expected without immediate strengthening of control.

### 9.2. Impact dimensions

A escala deve continuar específica por dimensão:

- **Safety:** potential effect on participant protection, timely assessment or safety documentation;
- **Procedure:** potential effect on procedural consistency, surgical appropriateness, technique, documentation or causality interpretation;
- **Device:** potential effect on selection, accountability, traceability, configuration, return or participant-device linkage;
- **Data/endpoint:** potential effect on completeness, reliability, interpretability, source reconstruction or endpoint usability.

Não preencher impacto em uma dimensão somente porque a tabela oferece a coluna. Usar N/A quando não aplicável e justificar quando a não aplicabilidade possa ser questionada.

### 9.3. Detectability

A escala deve esclarecer que a nota representa dificuldade de detectar uma falha antes que ela cause ou consolide a consequência:

- **1 — Easy to detect:** routine control is likely to detect the issue promptly;
- **2 — Moderate:** detection depends on a review, reconciliation or second-person check;
- **3 — Difficult:** issue may remain hidden until later follow-up, audit, complication, data review or endpoint analysis.

### 9.4. Priority bands

Fora de critérios Critical, a banda pode ser determinada pela maior nota aplicável entre probability, impacts e detectability. O formulário deve mostrar a regra, não exigir que o usuário faça média ou produto.

Suggested interpretation:

- **Low:** all applicable fields are 1 and the issue is readily detectable;
- **Moderate:** at least one applicable field is 2, without a Critical condition;
- **High:** at least one applicable field is 3, or the issue is recurrent, poorly controlled or difficult to detect;
- **Critical:** a defined immediate/unresolved safety, traceability, endpoint loss, reportability or escalation condition exists.

Essas bandas devem ser compatíveis com os procedimentos do estudo e não devem ser apresentadas como limiares universais independentes do contexto.

---

## 10. Estados e respostas recomendados

### Risk status

- **Open:** risk remains under active management;
- **Controlled:** current controls are implemented and evidence supports the present control state, but the risk remains applicable;
- **Escalated:** risk requires PI, sponsor, CAPA, safety or milestone decision;
- **Accepted:** residual risk is explicitly accepted by the authorized role with rationale and next review;
- **Closed:** risk no longer applies or the underlying vulnerability has been removed and closure is justified.

### Control/action status

- **Not started**;
- **In progress**;
- **Implemented — effectiveness pending**;
- **Effective**;
- **Partially effective**;
- **Ineffective**;
- **Not assessable**.

Não permitir que “Implemented” seja interpretado automaticamente como “Effective”.

### Destinos de resposta

A entrada deve permitir pelo menos:

- no further action with rationale;
- maintain and monitor;
- increase control or review frequency;
- IMC review;
- CAPA Log;
- POT PI decision;
- MRL gate decision;
- SART/SCML/CSST route;
- sponsor notification/decision;
- protocol deviation or other controlled record;
- source/process correction.

---

## 11. Exemplo contínuo recomendado

O exemplo de UDI/implant accountability é adequado porque demonstra a diferença entre risco, controle e ação.

### Identification

```text
Risk ID: SRR-003
Category: Device accountability
Local vulnerability: UDI entries are copied from the OR team without second-person verification before case closure.
CtQ factor threatened: The implanted component can be reconstructed and reconciled to the participant and accountability record.
Risk: Implant lot number or UDI may not be captured and reconciled in both source and accountability records before workflow closure.
```

### Rating

```text
Probability: 2
Safety: 2
Procedure: 2
Device: 3
Data/endpoint: 3
Detectability: 2
Current priority: High
```

### Existing control

```text
OR implant sticker
Device accountability log
Coordinator same-day reconciliation
Evidence: cases 001–005; accountability records; signed reconciliation entries
```

### Planned mitigation

```text
Add second-person verification before case closure.
Destination: CAPA-014 / IMC follow-up.
Owner: Quality Representative or assigned accountable role.
Trigger: any missing or conflicting UDI, or reconciliation later than 24 hours.
```

### Review

```text
Evidence reviewed: IMC-03 and ICDL cases 006–007
Control effectiveness: Effective for the reviewed cases
Current priority: Moderate, subject to continued monitoring
Risk status: Controlled, not Closed
Next trigger: any new mismatch or next scheduled review
```

O exemplo demonstra que a correção pode reduzir a prioridade sem eliminar automaticamente o risco. O risco permanece aplicável enquanto a condição de rastreabilidade continua relevante.

---

## 12. Recomendações finais de conteúdo

1. Manter o SRR v0.91 como base.
2. Preservar o foco em riscos da execução local do site.
3. Preservar a ligação direta entre cada entrada e o fator CtQ específico.
4. Não transformar o SRR em cópia do sponsor risk assessment ou do manufacturer risk file.
5. Tornar explícita a diferença entre domínio, fator, vulnerabilidade, risco e consequência.
6. Nomear a prioridade como current/residual risk ou separar claramente inherent e residual risk.
7. Manter a regra do maior score aplicável, sem média ou produto, mas escrevê-la no próprio instrumento.
8. Definir N/A e justificar dimensões não aplicáveis.
9. Refinar os critérios de Critical sem transformar qualquer score 3 em Critical automaticamente.
10. Separar risk status de control/action status.
11. Registrar eficácia do controle, não apenas conclusão da ação.
12. Exigir prioridade atual, status e evidência na revisão.
13. Fazer a entrada urgente apontar para o Risk ID formal e para os instrumentos responsáveis.
14. Separar PI escalation de sponsor reporting e safety reporting.
15. Exigir permitted route, owner, due date e trigger para cada resposta.
16. Não fechar risco apenas porque uma CAPA foi encerrada.
17. Permitir aceitação explícita de risco residual quando autorizada e justificada.
18. Usar o IMP para transformar risco em plano de verificação.
19. Usar o IMC para devolver evidência, findings e eficácia ao SRR.
20. Usar POT para decisões de oversight, MRL para gates e CAPA para investigação/ação detalhada.
21. Manter o mesmo Risk ID entre identificação, controles, revisão e fechamento.

---

## 13. Checklist de validação do futuro HTML

### Identificação

- O formulário explica a diferença entre domínio, fator, vulnerabilidade e risco?
- A entrada identifica um fator CtQ específico da investigação?
- A fonte do fator pode ser citada?
- O risco descreve causa/vulnerabilidade, consequência e objeto ameaçado?
- A unidade é site-level e prospectiva?

### Avaliação

- Probability, quatro impactos e detectability têm definições claras?
- N/A é possível e exige justificativa quando necessário?
- A regra de prioridade está escrita no documento?
- Está claro se a prioridade é residual/current ou inerente?
- Critical tem critérios próprios?
- PI escalation, sponsor notification e safety reporting estão separados?

### Controles e ação

- Existing controls são distinguíveis de planned mitigation?
- O formulário impede que uma promessa futura reduza a prioridade atual?
- Existe evidence of implementation?
- Existe control effectiveness?
- Risk status e action/control status são independentes?
- A ação já existente pode ser referenciada sem criar outra CAPA?

### Revisão

- Cada Risk ID permanece igual em F, G e H?
- A revisão registra evidência, eficácia, prioridade atual e motivo da mudança?
- A entrada urgente tem ponte para o risco formal?
- A data de próxima revisão vem acompanhada de trigger objetivo?
- A ação concluída não é confundida com risco fechado?

### Integração

- O SRR informa o IMP sobre frequência, amostra e triggers?
- O IMC devolve findings e efetividade ao SRR?
- CAPA, POT, MRL, PIR e safety records aparecem como destinos quando aplicável?
- O SRR não copia narrativas clínicas ou investigações de ações?
- Cada saída tem owner, prazo e destino?

### Fechamento

- O risco é fechado apenas quando a vulnerabilidade deixa de se aplicar ou foi removida com evidência?
- Risco residual aceito possui justificativa e responsável?
- Riscos High/Critical exigem a revisão definida?
- A certificação confirma revisão e encaminhamento, não eliminação de todos os riscos?

### Usabilidade visual

- A primeira página possui Purpose and Use com Unit of analysis, Decision support, Inputs e Outputs?
- Há espaço suficiente para uma frase real de fator CtQ e risco?
- A tabela F e a tabela G preservam visualmente o mesmo Risk ID?
- A seção H permite escrever evidência de eficácia e prioridade atual?
- A entrada urgente é claramente provisória e ligada à entrada formal?
- Nenhuma tabela ultrapassa o rodapé?
- O Editor v2 permite editar células, caixas, linhas, colunas, fontes e opções?

---

## 14. Conclusão

O SRR v0.91 já contém a estrutura essencial do registro de risco local. O seu valor está em fazer uma coisa que os outros instrumentos não fazem: manter, ao longo do lifecycle, a ligação entre a condição local do site e o fator CtQ específico que essa condição pode comprometer.

A próxima revisão não deve adicionar uma camada extensa de burocracia. Deve tornar a cadeia já existente mais difícil de interpretar incorretamente:

```text
CtQ factor
→ local vulnerability
→ risk consequence
→ existing control and evidence
→ current/residual risk
→ owner and trigger
→ mitigation or escalation
→ effectiveness review
→ updated risk status
```

Os principais ajustes recomendados são:

- explicitar o fator CtQ específico;
- distinguir risco residual de risco inerente;
- separar estado do risco de estado da ação;
- registrar efetividade e prioridade atual;
- definir Critical e N/A de forma operacional;
- tornar a entrada urgente uma ponte controlada;
- conectar SRR, IMP e IMC sem duplicação;
- impedir fechamento automático por encerramento de CAPA;
- manter referências em vez de copiar dados de origem.

Com esses ajustes, o SRR será um instrumento de desenho e manutenção de controles, não apenas uma tabela de preocupações. Ele poderá alimentar o IMP, orientar o IMC, fornecer contexto ao POT e ao MRL, disparar CAPA quando necessário e preservar uma visão longitudinal do risco local.

## 15. Fontes verificadas

- `SRR_Site_Risk_Register_v0.91.html`.
- `SRR_relatorio_de_passagem_2026-10-27.md`.
- `SRR_referencia_tese_2026-10-27.md`.
- `SRR.md`, requisito específico carregado no repositório.
- Tese completa, especialmente as passagens sobre CtQ domains, site-level risk identification, controls, residual risk, triggers, CAPA e lifecycle.
- Contexto do branch `codex/thesis-work`, incluindo as interfaces aprovadas entre SRR, POT, MRL, IMP, IMC e instrumentos especialistas.
