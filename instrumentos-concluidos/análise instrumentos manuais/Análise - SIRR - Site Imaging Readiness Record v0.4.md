# Análise crítica — SIRR: Site Imaging Readiness Record v0.4

**Status:** análise manual para orientar a próxima revisão do instrumento. O HTML v0.4 não foi alterado nesta etapa.

## 1. Veredito executivo

O SIRR v0.4 tem uma arquitetura boa e coerente com a tese. Ele não precisa ser reconstruído do zero. O documento já reconhece a fronteira correta com o sponsor: o site avalia se consegue implementar localmente o Imaging Charter e submete essa conclusão ao sponsor ou CRO, mas não autoriza a ativação do site nem substitui a revisão central.

O instrumento deve continuar sendo um **readiness and implementation record**, não um registro de qualidade de cada imagem. A distinção central é:

```text
SIRR: Can this site implement the required imaging process before activation?
IQL: Was this specific image set acquired, complete, traceable and usable?
```

A versão atual já contém os componentes essenciais:

- propósito e decisão produzida;
- mapeamento do Imaging Charter para o workflow local;
- equipamento, manutenção, calibração, arquivo e transferência;
- funções locais e rotas de revisão;
- autoavaliação de readiness;
- histórico de reavaliações;
- conclusão para submissão ao sponsor/CRO;
- assinatura local e ressalva de que a ativação permanece sob controle do sponsor.

Os problemas restantes são principalmente de clareza operacional e integração:

1. o documento ainda pode ser confundido com uma autorização de ativação;
2. status, gap, action e evidence aparecem misturados em algumas tabelas;
3. readiness de infraestrutura, readiness de função e acceptability de imagem não estão sempre separados;
4. a ligação entre SIRR e cada entrada do IQL precisa ser explícita;
5. faltam gatilhos claros para reabrir a avaliação;
6. alguns campos demonstram uma versão preenchida, embora o arquivo seja apresentado como template editável;
7. os estados de execução, evidência e efetividade precisam ser separados.

**Recomendação geral:** manter a estrutura e identidade visual do v0.4, corrigindo apenas as fronteiras decisórias, o controle de versão do charter, a lógica de status, os handoffs para IQL/PFVR/IMC/PIR e os critérios de reavaliação.

---

## 2. A decisão que o SIRR deve suportar

Depois de preencher o SIRR, o responsável deve conseguir decidir:

> **Whether the site has mapped the sponsor-controlled imaging requirements to a feasible, qualified, traceable and reviewable local process, and whether the site may submit that readiness package for sponsor or CRO qualification review.**

Essa decisão não é:

- “a imagem está boa?”;
- “o endpoint foi atingido?”;
- “o sponsor autorizou o site?”;
- “o paciente está elegível?”;
- “a visita está completa?”;
- “a imagem deve ser aceita no banco de dados?”

Essas decisões pertencem, respectivamente, ao IQL, ao processo de revisão de endpoint, ao sponsor/CRO, ao PSEAR, ao PFVR/FUCR e ao fluxo definido no Imaging Charter ou no sistema do sponsor.

O SIRR decide somente se o **arranjo local** está pronto para ser submetido à revisão/qualificação externa e quais limitações precisam ser resolvidas ou visibilizadas antes disso.

---

## 3. Unidade de análise e granularidade

A unidade de análise é:

```text
one site-level imaging implementation requirement or linked readiness package for a defined charter/protocol version
```

O documento não é um log de participantes ou de imagens. Sua população é o conjunto de requisitos de imagem aplicáveis ao site para uma versão controlada do:

- protocol/CIP;
- sponsor Imaging Charter;
- imaging manual;
- central-reading instructions;
- local imaging workflow;
- equipment and archive configuration.

O SIRR deve sempre registrar o **source version** e a data de vigência. Se o Imaging Charter mudar, a mesma avaliação não deve continuar parecendo válida sem reavaliação.

### 3.1. Elementos que devem permanecer separados

| Elemento | Pergunta correta |
|---|---|
| Requirement | O que o sponsor-controlled source exige? |
| Local implementation | Como o site realizará isso? |
| Readiness evidence | Que evidência mostra que o processo está disponível e configurado? |
| Gap/limitation | O que ainda impede ou limita a implementação? |
| Readiness conclusion | O site pode submeter o pacote para review? |
| Sponsor/CRO decision | O sponsor qualificou ou autorizou a utilização? |
| Image-set quality | Este conjunto específico foi adquirido de forma completa e utilizável? |

Misturar esses níveis faz o SIRR parecer um IQL antecipado ou um formulário de ativação do sponsor.

---

## 4. O que a tese exige do SIRR

### 4.1. Readiness antes da ativação

A tese coloca o SIRR antes do primeiro participante e antes da aquisição de imagens. O site deve mapear os requisitos do Imaging Charter para um workflow que a radiologia consiga executar.

Esse mapeamento precisa considerar, conforme aplicável:

- modalidade;
- views, sequences e parâmetros;
- laterality e identificação;
- posicionamento reprodutível;
- janela temporal;
- equipamento;
- manutenção e calibração;
- transfer, display e archive;
- local review;
- second review;
- clinical escalation;
- central review boundary;
- treinamento e delegação;
- tratamento de imagem limitada ou não conforme.

A avaliação deve ser anterior à aquisição rotineira. Ela é uma condição de preparação, não uma decisão sobre uma imagem já adquirida.

### 4.2. O site controla a implementação local, não o charter

O Imaging Charter, o imaging manual e as instruções de central review permanecem sob controle do sponsor. O site demonstra se consegue aplicar os requisitos e identifica dúvidas ou limitações.

O SIRR não deve editar silenciosamente o requisito do sponsor para torná-lo compatível com a capacidade local. Quando o workflow local não consegue cumprir o requisito, o documento deve registrar:

- o requisito original;
- a lacuna local;
- o impacto potencial;
- a ação ou pedido de esclarecimento;
- a referência da resposta do sponsor;
- a conclusão atualizada.

### 4.3. Imagem é sensível à aquisição

A tese justifica o SIRR porque variação de aquisição, posicionamento e timing pode introduzir erro que o banco de dados não diferencia de uma diferença clínica real.

O SIRR deve, portanto, controlar o que pode ser decidido antes do caso:

- se o equipamento e o preset existem;
- se a equipe sabe executar as views;
- se o posicionamento é reproduzível;
- se o exame cabe na janela;
- se o arquivo e a transferência preservam a rastreabilidade;
- se o local sabe reconhecer e encaminhar uma imagem não conforme.

A usabilidade de cada image set continua sendo decisão do IQL e das regras do sponsor.

### 4.4. Qualificação e revisão de pessoas

A tese exige que as pessoas que adquirem ou avaliam imagens sejam qualificadas e treinadas. O SIRR deve apontar para os registros de treinamento, delegação e competência; não deve duplicar o TRE ou o RACI.

Também deve distinguir:

- technical acquisition function;
- local clinical review;
- PI/accountable clinical decision;
- sponsor central review;
- endpoint adjudication, quando aplicável.

O site pode documentar que a rota existe. Isso não significa que o reviewer local substitui o central reviewer ou o adjudication process do sponsor.

---

## 5. O que está correto no SIRR v0.4

### 5.1. Purpose, Decision and Boundary

A primeira seção está conceitualmente correta. Ela diz que o documento confirma se os arranjos locais podem implementar os requisitos e que não substitui o Imaging Charter, o imaging manual ou o protocolo.

Também é importante a frase de que a conclusão é para submissão ao sponsor/CRO e não autoriza activation. Essa ressalva deve permanecer e ser visualmente ainda mais evidente.

### 5.2. Local Implementation Model and Record Linkage

A divisão entre:

- Acquisition;
- Display, transfer and archiving;
- Local review;
- Timing and maintenance;

é útil e acompanha o percurso real da implementação.

O campo de controlled source or linked evidence é especialmente importante porque impede que o site registre apenas “ready” sem indicar de onde veio o requisito e que evidência demonstra a preparação.

### 5.3. Alignment of image-set quality classification and local response

As categorias Acceptable, Limited, Non-conforming e Not assessable ajudam a explicar o que acontecerá quando o processo produzir um image set problemático.

Entretanto, essa parte deve ser rotulada cuidadosamente como **local response boundary** ou **interface with IQL**, porque a decisão formal de usability de um image set não pertence ao SIRR.

O SIRR pode explicar a rota. O IQL registra a aplicação dessa rota a cada conjunto de imagens.

### 5.4. Mapping table

A tabela da página 2 é o núcleo mais importante do SIRR. Ela conecta:

```text
sponsor source / section
→ time point / purpose
→ modality / views / parameters
→ local equipment / workflow
→ implementation status
→ gap, action or evidence
```

A estrutura é correta. Ela deve apenas separar melhor os campos finais para que “gap”, “action” e “evidence” não sejam escritos juntos em uma mesma célula.

### 5.5. Technical controls

A tabela de equipamentos, archive, transfer, radiology liaison e review route é necessária. O SIRR não deve considerar apenas a existência física do equipamento; deve exigir evidência de:

- maintenance/calibration validity;
- test dataset or transfer test;
- retrievability;
- named role;
- applicable training/release;
- route tested.

### 5.6. Roles and boundary

A página 3 está correta ao nomear:

- radiology liaison/technical acquisition;
- local clinical imaging reviewer;
- PI/accountable clinical decision.

Também está correta a frase de que esses papéis não substituem sponsor oversight, central review ou endpoint adjudication.

O ponto a reforçar é que o SIRR não deve decidir sozinho se a pessoa está autorizada. Ele referencia o registro de delegação, treinamento ou credentialing que contém essa decisão.

### 5.7. Assessment and reassessment record

O histórico de avaliações é um bom componente. Ele evita que o site sobrescreva a conclusão anterior quando:

- o charter muda;
- o equipamento muda;
- o reviewer muda;
- o workflow é alterado;
- um transfer test falha;
- o sponsor responde a uma dúvida;
- um IQL ou IMC identifica uma falha recorrente.

Essa seção deve continuar sendo um log de versões e decisões, não apenas uma lista de datas.

### 5.8. Site attestation and sponsor/CRO activation reference

A separação entre attestation local e activation decision do sponsor/CRO está correta. O SIRR deve deixar claro que a assinatura local atesta a autoavaliação, e não a autorização para iniciar.

---

## 6. Problemas críticos que precisam de ajuste

### 6.1. SIRR v0.4 é uma demonstração preenchida, não um blank template

O arquivo disponível contém valores e nomes específicos, por exemplo:

- IMG-MAN v2.0;
- CT-2 e XR-3;
- Elena Martin;
- Dr Helen Meyer;
- Dr Sofia Chen;
- dates and test references;
- “Ready for sponsor review”.

Isso é adequado para um **simulated editable version**, mas não para o HTML em branco destinado ao apêndice ou uso real.

Na próxima montagem, devem existir claramente:

- uma versão em branco, com campos editáveis vazios;
- uma versão preenchida, com dados fictícios explicitamente marcados como example;
- o mesmo fluxo e a mesma geometria entre as versões.

Não remover os exemplos do conceito; apenas separar o exemplo contínuo do documento operacional em branco.

### 6.2. “Ready for sponsor review” não é “ready for use”

A conclusão atual é boa, mas precisa ser protegida contra interpretação equivocada.

O estado “Ready for sponsor review” significa:

> o site acredita que mapeou e evidenciou a implementação local e está pronto para submeter o pacote à qualificação/revisão do sponsor ou CRO.

Não significa:

- sponsor approval;
- activation;
- green light;
- permission to enroll;
- permission to acquire images for the trial;
- endpoint acceptance.

A tabela de conclusão deve separar:

```text
Site self-assessment conclusion
Sponsor/CRO review status
Sponsor/CRO decision reference
Activation status, if available in another controlled record
```

A última linha pode ser apenas uma referência, não uma decisão preenchida pelo site.

### 6.3. Status único mistura execução, evidência e efetividade

Na tabela de mapping, “Implementation status” parece concentrar várias perguntas. Na tabela de readiness, “Confirmed / Pending / N/A” também pode significar coisas diferentes.

A próxima versão deve separar pelo menos:

- **Implementation:** Ready / Partial / Not ready / N/A;
- **Evidence:** Adequate / Partial / Missing / N/A;
- **Action:** None / Open / Completed / Escalated;
- **Review status:** Not assessed / Site assessed / Submitted / Sponsor response pending / Sponsor decision referenced.

Não é necessário transformar cada linha em uma matriz enorme. Pode haver uma coluna curta de status principal e campos complementares na mesma linha, desde que a orientação diga qual pergunta cada campo responde.

### 6.4. Gap, action e evidence estão misturados

A tabela de mapping usa “Gap / action / evidence”. Isso economiza espaço, mas reduz a rastreabilidade.

Para um auditor ou para o próprio site, é importante distinguir:

- o que falta;
- o que será feito;
- quem fará;
- até quando;
- que evidência já existe;
- que evidência ainda será produzida;
- se o gap impede submission.

Recomendação mínima:

```text
Gap or limitation | Evidence/reference | Action/owner/due date | Impact on readiness
```

Se a tabela ficar larga, a ação pode ir para a seção de readiness/action log, desde que o Requirement ID seja preservado.

### 6.5. Falta um identificador de requisito estável

A tabela usa o número da linha, mas o IQL e os outros registros precisam apontar para o requisito correto. O SIRR deve criar um identificador estável, por exemplo:

```text
SIRR-IMG-01
SIRR-IMG-02
SIRR-IMG-03
```

Esse ID deve aparecer, quando aplicável, em:

- SIRR mapping;
- IQL row;
- IMC review item;
- PFVR imaging component reference;
- PIR source reconciliation;
- action or deviation record.

O ID não deve ser confundido com o PACS accession, participant ID ou IQL record ID.

### 6.6. O controlled source precisa de versão e data de vigência

“IMG-MAN v2.0 §4.1” é um bom começo, mas a readiness não pode depender apenas do nome do documento. Deve ser possível saber:

- source name;
- source version;
- effective date;
- section/page or requirement ID;
- date received/confirmed by site;
- whether a later amendment triggered reassessment.

Uma alteração do Imaging Charter ou do CIP deve ser um trigger formal para reabrir o SIRR.

### 6.7. A relação com o IQL precisa ser obrigatória e bidirecional

O SIRR deve alimentar o IQL com:

- SIRR ID;
- charter/protocol version;
- requirement ID;
- modality/views/parameters;
- timing requirement;
- local workflow or equipment reference;
- local review route;
- exception route.

O IQL deve devolver ao SIRR apenas informação de processo e sinal, não duplicar todos os image sets:

- repeated missing view;
- recurrent positioning limitation;
- transfer failure;
- inability to retrieve;
- repeated timing problem;
- recurrent non-conforming status;
- local review route not functioning.

Quando o IQL mostra falha recorrente, o SIRR deve ser reavaliado. O IQL não deve reescrever o SIRR inteiro.

### 6.8. O SIRR não deve decidir a qualidade de cada imagem

A seção de classificação é útil, mas “Acceptable” pode ser interpretado como uma decisão individual de qualidade. O SIRR deve usar essa parte para definir a rota local:

- quem reconhece a limitação;
- quando repetir;
- quando obter second review;
- quando encaminhar ao PI;
- quando referenciar IQL, deviation, SART ou sponsor;
- como fechar a ação.

A decisão sobre um image set específico deve permanecer no IQL e no processo do sponsor.

### 6.9. Os limites entre local reviewer, central reviewer e PI precisam ser ainda mais visíveis

O documento nomeia as funções, mas deveria responder de forma direta:

- quem avalia technical completeness;
- quem avalia local clinical concern;
- quem decide se uma repeat acquisition é possível;
- quem decide se a decisão clínica pode prosseguir;
- quem encaminha para central review;
- quem recebe uma discordância do central reader;
- quem pode encerrar uma limitation.

O SIRR não precisa criar um novo sistema de adjudication. Ele precisa apenas mapear a rota local e apontar para o documento controlado que define a decisão final.

### 6.10. Equipment readiness precisa mostrar validade

“Maintenance 15-Jun-2026” e “calibration 03-Aug-2026” são exemplos úteis, mas uma auditoria precisa saber:

- qual equipamento;
- qual certificado ou record;
- qual validade/next due;
- qual modalidade e preset são afetados;
- quem verificou;
- se o equipamento mudou depois da avaliação.

A tabela deve separar current evidence de next due e de status. Um registro antigo não demonstra readiness atual se a validade expirou.

### 6.11. Local archive/transfer precisa de teste reproduzível

A presença de SOP e de um transfer test é adequada. O SIRR deve registrar o resultado mínimo do teste:

- dataset/test ID;
- naming and participant/site identifier logic;
- export/transfer completed;
- receipt confirmed;
- image retrievable locally;
- image retrievable through the intended sponsor route, when testable;
- discrepancy and action.

Não é necessário copiar imagens para o SIRR. Basta apontar para o teste controlado e registrar o resultado.

### 6.12. Readiness conclusion não distingue critical open gaps de observations

“Ready with observation for review” é útil, mas exige critérios claros. O formulário deve explicar que uma observation pode permanecer aberta sem impedir submission somente quando:

- não compromete a implementação de um requisito crítico;
- existe owner e due date;
- existe uma rota de fechamento;
- o sponsor/CRO será informado;
- a limitação não é mascarada como Ready.

Se o gap impede aquisição conforme, transfer, retrievability, reviewer qualification ou required timing, o resultado deve ser “Action required before activation” ou “Not ready / escalated”, conforme o caso.

### 6.13. Falta uma regra explícita para N/A

Alguns requisitos serão aplicáveis somente a certas modalidades, time points ou usos locais. “N/A” deve exigir:

- reason;
- source basis;
- confirmation that the requirement is not applicable to this site/investigation;
- review trigger if the scope changes.

N/A não deve ser usado para ocultar falta de readiness.

### 6.14. Reassessment triggers precisam estar no instrumento

O SIRR deve ser reaberto quando ocorrer, por exemplo:

- Imaging Charter or protocol amendment;
- new modality, equipment or software;
- equipment maintenance/calibration failure;
- change in archive/transfer system;
- change in technical acquisition staff;
- change in local reviewer or escalation route;
- repeated IQL non-conforming image sets;
- IMC finding about imaging control;
- sponsor clarification changing a required view or timing;
- inability to reproduce positioning;
- serious workflow disruption.

Sem triggers explícitos, o site pode tratar o SIRR como documento único e permanente, mesmo quando as condições mudam.

### 6.15. A conclusão não deve encerrar o ciclo

O SIRR precisa mostrar que readiness inicial é apenas o começo. Depois da ativação:

```text
SIRR readiness
→ IQL image-set records
→ IMC or other review of control execution
→ PIR/FUCR where an indicator uses imaging data
→ SRR/POT/CAPA if a process vulnerability recurs
→ SIRR reassessment when the local arrangement changes
```

O SIRR não precisa receber todas as linhas do IQL. Deve receber somente sinais que alterem a validade do arranjo local.

---

## 7. Interfaces operacionais

### 7.1. Sponsor Imaging Charter → SIRR

O Imaging Charter ou imaging manual é a entrada principal. Para cada requisito aplicável, o SIRR deve preservar:

- source/version;
- requirement section or ID;
- time point/purpose;
- modality/views/parameters;
- timing/window;
- central/local review boundary;
- required transfer/archive rule.

O SIRR não deve modificar esse requisito. Ele registra como o site o implementará e onde ainda há dúvidas.

### 7.2. SIRR → IQL

O SIRR fornece ao IQL a configuração contra a qual cada image set será avaliado:

- applicable requirement ID;
- modality and views;
- technical minimum;
- positioning instruction;
- window;
- local review route;
- archive/transfer reference;
- repeat/second-review/escalation route;
- SIRR version or readiness assessment ID.

O IQL precisa conseguir apontar de volta para essa configuração. Sem essa ligação, um auditor não sabe se a imagem foi julgada contra a versão correta do requirement.

### 7.3. IQL → SIRR

O IQL deve alimentar o SIRR somente quando houver impacto no processo de readiness, por exemplo:

- repeated missing view;
- recurring positioning problem;
- recurring inability to acquire within the window;
- repeated transfer or archive failure;
- local reviewer route not functioning;
- repeated use of an unapproved alternative;
- unresolved limitation that requires sponsor clarification.

Um único image set limitado pode permanecer no IQL sem reabrir o SIRR, se a rota já estiver prevista e funcionar.

### 7.4. SIRR → PFVR

O PFVR registra que os componentes de uma visita ocorreram e se foram completados no timing adequado. Para um componente de imagem, ele deve apontar ao IQL ou à fonte de imagem e, quando necessário, ao SIRR requirement ID.

O PFVR não deve copiar a avaliação técnica do image set. Deve registrar:

- component completed/missed/late;
- timing;
- source/reference;
- exception when needed.

### 7.5. SIRR → IMC

O IMP pode selecionar a readiness de imaging e a execução dos controles como área de review. O IMC pode verificar:

- se o workflow foi seguido;
- se os registros de IQL existem;
- se o archive/transfer funciona;
- se a calibração permanece válida;
- se as ações sobre non-conforming sets foram resolvidas;
- se o local reviewer e second-review route estão sendo usados corretamente.

O IMC não deve refazer o mapeamento inicial do SIRR. Ele verifica se o controle implementado continua funcionando.

### 7.6. SIRR → PIR

O SIRR não calcula indicadores. Ele fornece a configuração e os requisitos. O PIR pode usar os resultados do IQL, PFVR, FUCR ou IMC para medir:

- imaging completeness;
- critical data completeness;
- imaging-related deviations;
- follow-up component completion;
- recurring non-conforming image sets.

A reconciliação do PIR deve apontar para os IDs ou intervalos dos registros de origem, não apenas dizer “IQL” ou “imaging review”.

### 7.7. SIRR → SRR/POT/CAPA

Uma vulnerabilidade persistente de equipamento, staffing, workflow, transfer ou reviewer route pode alimentar:

- SRR, quando se trata de risco local recorrente;
- POT, quando exige decisão do PI;
- CAPA, quando exige investigação e ação corretiva/preventiva;
- sponsor/CRO route, quando o site não consegue cumprir o requisito controlado.

Um problema individual de uma imagem não deve abrir automaticamente uma nova entrada no SRR. O gatilho é a recorrência, a gravidade, a falha sistêmica ou a incapacidade de o processo local funcionar.

---

## 8. Arquitetura recomendada para a próxima revisão

A estrutura atual de quatro páginas pode ser preservada.

### Página 1 — Purpose, boundary and implementation model

Manter:

- header and document control;
- Purpose, Decision and Boundary;
- Unit of analysis, Decision support, Inputs and Outputs;
- Local Implementation Model and Record Linkage;
- classification/interface note.

Adicionar de forma curta:

- charter/protocol version;
- effective date;
- SIRR assessment ID;
- initial or reassessment trigger.

A página 1 deve dizer de forma inequívoca:

> This record supports site submission for sponsor/CRO review. It does not authorize activation or replace sponsor-controlled imaging qualification.

### Página 2 — Requirement mapping and technical controls

Manter a tabela de mapping, mas preferir:

```text
Requirement ID | Sponsor source/version | Time point/purpose | Modality/views/parameters | Local workflow/equipment | Implementation status | Evidence/reference | Gap/action/owner/due
```

Se isso ficar largo, dividir a tabela em duas partes mantendo o mesmo Requirement ID.

Na tabela de technical controls, separar:

- control;
- current evidence;
- status;
- limitation/action;
- owner;
- next review/due.

### Página 3 — Roles, review boundary and documentation pathways

Manter as funções nomeadas, mas incluir campos curtos para:

- delegation/training reference;
- role scope;
- independence or second-review condition;
- central review handoff;
- escalation owner.

A tabela de documentation pathways deve incluir o SIRR Requirement ID e o IQL action/exception route.

### Página 4 — Readiness conclusion, reassessment and attestation

Manter as opções de conclusão, mas separar:

1. site self-assessment conclusion;
2. open critical gaps;
3. sponsor/CRO submission reference;
4. sponsor/CRO response/decision reference;
5. next reassessment trigger/date;
6. local attestation.

Não permitir que “Ready for sponsor review” seja interpretado como activation.

---

## 9. Estados recomendados

### Implementation status

- **Ready:** local process is mapped and evidence supports implementation;
- **Partial:** process exists but a limitation or incomplete control remains;
- **Not ready:** required local implementation is absent or cannot currently meet the source requirement;
- **N/A:** requirement does not apply, with documented reason.

### Evidence status

- **Adequate:** current, traceable and sufficient for the stated purpose;
- **Partial:** some evidence exists but a limitation remains;
- **Missing/unavailable:** readiness cannot be confirmed;
- **Not assessable:** the source, system or reviewer is unavailable.

### Action status

- **None required**;
- **Open**;
- **In progress**;
- **Implemented — effectiveness pending**;
- **Closed with evidence**;
- **Escalated**.

### Site conclusion

- **Ready for sponsor/CRO review**;
- **Ready for sponsor/CRO review with documented observation**;
- **Action required before submission/activation review**;
- **Not ready / sponsor clarification or escalation required**.

A sponsor/CRO activation decision must be referenced separately and never inferred from the site conclusion.

---

## 10. Exemplo contínuo recomendado

O exemplo de IMG-MAN v2.0 pode ser preservado, mas deve demonstrar o fluxo sem fazer o site parecer autorizado.

### Requirement mapping

```text
Requirement ID: SIRR-IMG-03
Sponsor source: IMG-MAN v2.0 §4.3, effective 01-Jun-2026
Time point: 6-week follow-up
Requirement: X-ray with true AP, axillary lateral and scapular-Y views within Day 42 ±7 days
Local workflow: XR-3, three-view shoulder order set, radiology scheduling rule
Implementation: Ready
Evidence: workflow test TEST-SIRR-07; local instruction WI-IMG-04 v5
Gap/action: none open
```

### Role and review route

```text
Technical acquisition: Lead Imaging Technologist, training COMP-IMG-06
Local technical review: defined in IQL route
Clinical escalation: PI when a clinically meaningful concern is identified
Central review: sponsor-controlled route, not replaced by local review
```

### Site conclusion

```text
Site conclusion: Ready for sponsor/CRO review
Open observation: none
Submission reference: SIRR-014-2026-01
Sponsor/CRO activation decision: pending / referenced in separate controlled record
Next reassessment trigger: charter amendment, equipment change, reviewer change, recurrent IQL limitation or scheduled review
```

Esse exemplo mostra a diferença entre “site ready to submit” e “sponsor authorized”.

---

## 11. Recomendações finais de conteúdo

1. Manter o SIRR v0.4 como base.
2. Preservar o foco em readiness de implementação local.
3. Não transformar o SIRR em um IQL antecipado.
4. Não transformar o SIRR em uma autorização de ativação do sponsor.
5. Manter o Imaging Charter e o imaging manual como fontes controladas externas.
6. Registrar source version, effective date e requirement ID.
7. Separar implementation, evidence, action e sponsor review status.
8. Separar gap, evidence, action, owner e due date.
9. Criar um identificador estável para cada requirement mapping.
10. Fazer o IQL apontar para o requisito SIRR contra o qual o image set foi julgado.
11. Fazer o IQL devolver ao SIRR somente falhas recorrentes ou sistêmicas.
12. Fazer o PFVR referenciar IQL/SIRR sem copiar avaliação técnica.
13. Fazer o IMC verificar a execução e efetividade dos controles definidos pelo SIRR.
14. Fazer o PIR receber dados agregados de IQL, PFVR, FUCR ou IMC, não a conclusão de readiness como indicador de imagem.
15. Encaminhar vulnerabilidades persistentes ao SRR e decisões do PI ao POT.
16. Exigir critérios para Limited, Non-conforming e Not assessable.
17. Exigir justificativa para N/A.
18. Registrar gatilhos de reassessment.
19. Registrar a decisão do sponsor/CRO separadamente da autoavaliação do site.
20. Manter a versão em branco livre de nomes, datas e valores específicos do exemplo.

---

## 12. Checklist de validação do futuro HTML

### Propósito e fronteira

- O documento diz claramente que é uma self-assessment de site readiness?
- A conclusão está limitada à submissão para sponsor/CRO review?
- Está explícito que o SIRR não autoriza activation ou enrollment?
- A diferença entre SIRR e IQL está explicada?

### Requisitos

- Cada requisito tem source, version, effective date e section/ID?
- Cada requisito tem um Requirement ID estável?
- A modalidade, views, parâmetros e janela podem ser identificados?
- O workflow local está separado do requisito do sponsor?
- O site pode registrar uma dúvida sem alterar o requisito original?

### Evidência e status

- Implementation status e evidence status são distinguíveis?
- Gap, action, owner e due date podem ser registrados?
- Maintenance/calibration tem validade e next due?
- Archive/transfer tem teste ou referência recuperável?
- N/A exige justificativa?
- “Ready” não significa “authorized”?

### Pessoas e revisão

- Technical acquisition, local review, PI decision e central review estão separados?
- Os papéis apontam para training/delegation records?
- A rota de second review está definida quando necessária?
- A rota de clinical escalation está definida?
- O SIRR não duplica TRE, RACI ou adjudication records?

### Integração

- O IQL consegue apontar para o SIRR Requirement ID?
- O PFVR consegue referenciar o IQL sem copiar o resultado técnico?
- O IMC consegue testar execução e eficácia dos controles?
- Falhas recorrentes podem alimentar SRR, POT ou CAPA?
- PIR consegue reconciliar seus números com IQL/PFVR/IMC?

### Reassessment

- Charter amendment é trigger?
- Equipment/software change é trigger?
- Staff/reviewer change é trigger?
- Recurrent IQL non-conformance é trigger?
- IMC finding é trigger?
- Existe next reassessment date ou condição objetiva?

### Fechamento

- A conclusão registra site assessment, submission reference e sponsor/CRO decision separately?
- Observations têm owner, due date e impacto na readiness?
- Gaps críticos impedem uma conclusão enganosa de Ready?
- A assinatura atesta a self-assessment, não a autorização do sponsor?

### Usabilidade visual

- A primeira página possui Purpose and Use com Unit of analysis, Decision support, Inputs e Outputs?
- O header contém charter/protocol version e assessment ID sem exceder 12 células?
- As tabelas de mapping têm espaço para texto real?
- O mesmo Requirement ID aparece no mapping e nas interfaces?
- A orientação landscape é usada somente quando a tabela exige largura?
- Nenhuma tabela ultrapassa o rodapé?
- O Editor v2 permite editar células, caixas, linhas, colunas, fontes e opções?

---

## 13. Conclusão

O SIRR v0.4 é um dos instrumentos mais claramente delimitados do conjunto. Seu valor não é avaliar cada imagem nem autorizar o estudo. Seu valor é demonstrar, antes da aquisição rotineira, que o site traduziu os requisitos de imagem do sponsor em um processo local que pode ser executado, revisado, transferido, arquivado e escalado.

A cadeia correta é:

```text
Imaging Charter / CIP
→ SIRR requirement mapping
→ local imaging workflow and readiness evidence
→ sponsor/CRO review and activation decision
→ IQL record for each image set
→ PFVR/FUCR or PIR aggregation where applicable
→ IMC review of control execution
→ SRR/POT/CAPA if local vulnerability recurs
→ SIRR reassessment when the arrangement changes
```

Os ajustes prioritários são:

- separar readiness de image-set usability;
- separar site conclusion de sponsor activation;
- separar implementation, evidence, action e review status;
- criar Requirement IDs e referências de versão;
- tornar o handoff SIRR–IQL explícito;
- registrar gatilhos de reassessment;
- demonstrar validade de manutenção, calibração, arquivo e transferência;
- preservar os limites entre revisão local, PI, central review e adjudication.

Com esses ajustes, o SIRR será um registro de prontidão realmente auditável e operacional, sem duplicar o IQL, o PFVR, o IMC, o PIR ou os sistemas controlados pelo sponsor.

## 14. Fontes verificadas

- `SIRR_Site_Imaging_Readiness_Record_v0.4_simulated_editable.html`.
- Tese completa, especialmente a seção 4.4.2 sobre imaging standardization.
- Appendix O da tese: função do Site Imaging Readiness Record.
- Passagens da tese sobre IQL, PFVR, ICDL, IMC, IMP, PIR e source documentation.
- `SKILL.md` de Operational Quality Form Templates.
- Contexto do branch `codex/thesis-work` e interfaces já definidas entre SIRR, IQL, PFVR, IMC, PIR e SRR.
