# Análise de reconstrução — SAART: Safety Assessment, Reporting and Tracking Template

**Status:** especificação para reconstrução integral do instrumento.  
**Instrumento substituído:** `SART — Safety and Adverse Effect Reporting Template v0.3`.  
**Novo nome aprovado:** **SAART — Safety Assessment, Reporting and Tracking Template**.  
**Decisão de arquitetura:** o SART v0.3 não deve receber microajustes. O próximo HTML deve ser reconstruído do zero a partir desta análise, preservando somente a linguagem visual comum dos instrumentos e os princípios úteis de abertura precoce, cronologia, proteção e rastreabilidade.

---

## 1. Decisão central

O documento anterior foi construído como se fosse possível combinar, em um único formulário local, a descrição do caso, a classificação de segurança, a comunicação, a reconciliação, o follow-up e o fechamento. A sua sequência tinha elementos corretos, mas a fronteira entre o que o **site** precisa coordenar e o que o **sponsor** precisa avaliar não ficou suficientemente clara.

O novo instrumento deve deixar de ser apresentado como um formulário de adverse-effect reporting e passar a ser um **site safety-case coordination record**.

O seu objetivo não é reproduzir o SAE form, portal de safety, eCRF, sistema de pharmacovigilance/vigilance ou submissão regulatória do sponsor. O seu objetivo é permitir que o centro demonstre, para cada ocorrência individual, que:

1. reconheceu a informação de segurança e registrou quando tomou conhecimento;
2. protegeu o participante, usuário ou outra pessoa quando necessário;
3. preservou os fatos locais e as referências às fontes, sem copiar narrativas inteiras;
4. realizou a avaliação inicial exigida do PI/site;
5. seguiu a rota e a janela estabelecidas no CIP e nos procedimentos do sponsor;
6. submeteu o caso ao sistema formal do sponsor e consegue provar a transmissão/recebimento;
7. acompanhou pedidos, informação nova e pendências até o encerramento local;
8. tornou identificáveis os efeitos do caso nos demais instrumentos do framework;
9. consegue distinguir um atraso de reporting, uma deficiência do processo local e uma decisão formal do sponsor/CEC.

O SAART é, portanto, o **dossiê operacional local do caso de safety**. Ele não é uma segunda base de dados de safety.

---

## 2. Por que o SART v0.3 deixa de funcionar como base

O SART v0.3 possui boas intenções e diversos elementos úteis, mas não deve ser a base estrutural da próxima versão pelos motivos abaixo.

### 2.1 O título e a aparência sugerem um sponsor reporting form paralelo

`Safety and Adverse Effect Reporting Template` faz parecer que o instrumento é o formulário oficial de reporte ao sponsor. Em uma investigação real, o sponsor provavelmente já terá um ou mais destes mecanismos:

- eCRF de segurança;
- SAE form;
- portal de safety;
- device-deficiency form;
- sistema de vigilância, pharmacovigilance ou CRO;
- processo para first report, detailed report, follow-up e query resolution.

Um instrumento local que repete esses conteúdos cria risco de divergência, dupla transcrição e falsa aparência de que o site está substituindo o processo do sponsor.

### 2.2 A classificação local e a classificação formal não estão claramente separadas

O PI/site deve registrar cada AE e DD observada e fazer uma avaliação inicial. Porém, a ISO 14155:2026 atribui ao sponsor a classificação de AEs e a avaliação contínua de safety da investigação. O sponsor revê a avaliação do investigador, determina seriousness e relação com device/procedimento quando aplicável, avalia DDs e pode usar um CEC para avaliação consistente entre centros.

O SART v0.3 usa ideias como `final local classification`, sem distinguir com rigor:

- **current PI / site assessment**;
- **sponsor / CEC determination, if received**;
- **agreement or disagreement**;
- **reference and date of the sponsor/CEC communication**.

Isso faz o formulário local parecer mais definitivo do que ele deve ser.

### 2.3 O documento registra demais, mas controla de menos o processo de reporte

O SART atual contém campos de facts, classification e communication, mas não transforma claramente em dados de processo os elementos necessários para o site responder a uma pergunta simples:

> O caso que era reportável foi reconhecido, escalonado, avaliado, enviado e acompanhado dentro da regra do CIP?

A tese já estabeleceu que o indicador **Safety Reporting Timeliness** depende de:

- escopo de reportabilidade definido pelo CIP;
- momento em que o site tomou conhecimento;
- janela aplicável do CIP;
- envio da initial notification ao sponsor;
- completude do first report;
- follow-up dentro do prazo;
- casos ainda abertos no cut-off;
- identificação da etapa em que um atraso ocorreu.

A versão atual contém partes dessa informação espalhadas, mas não oferece um controle de processo suficientemente claro, compacto e reconciliável com o PIR.

### 2.4 Os handoffs do framework aparecem misturados

O SART atual combina, por exemplo, `SCML / CSST signal review` e `PIR or PI Oversight communication`. Esses destinos têm finalidades diferentes:

- **SCML** indexa um caso/evento individual para a vigilância local;
- **CSST** revisa contagens e padrões agregados por período ou trigger;
- **PIR** usa somente dados de processo para o indicador de timeliness;
- **deviation record** recebe late initial notification;
- **SRR/CAPA** recebem falha recorrente, vulnerabilidade de processo ou risco local;
- **POT** recebe itens que exigem decisão de PI oversight.

O novo instrumento deve tratar cada saída como uma decisão separada, nunca como uma lista genérica de documentos possíveis.

### 2.5 A taxonomia pode ser atualizada de maneira mais precisa

O SART v0.3 antecipou corretamente que AE e DD podem coexistir e que um AE associado a uma DD requer duas vias. Porém, alguns rótulos permanecem vagos ou desatualizados para a ISO 14155:2026:

- `AE + deficiency` deve ser explicitado como **AE associated with an observed device deficiency**;
- `serious ADE` deve ser expresso pela categoria ISO **SADE**;
- `expectedness` não deve ser uma dimensão genérica para qualquer AE;
- `anticipated / unanticipated` deve ser tratado como avaliação de **SADE** frente ao **current risk assessment**;
- a rota de DD deve perguntar de maneira literal se a DD **could have led to a SADE**;
- `serious health threat` deve ser uma avaliação independente e urgente, não apenas mais uma opção de escalation.

### 2.6 O cabeçalho pressupõe sempre um participante e uma visita/procedimento

Um caso pode abrir para uma DD, problema de identificação, informação de produto, malfunction ou informação nova sem estar associado a um participante específico. O novo documento deve suportar isso sem obrigar a criar informação falsa.

### 2.7 A extensão e as páginas do SART v0.3 refletem sua arquitetura antiga

As 11 páginas não são um problema por si. O problema é que elas distribuem longas matrizes de classificação e reconstruções de dados que podem estar em fontes ou sistemas do sponsor. O novo SAART deve alocar o espaço onde ele cria valor local: controle de processo, referências, decisões, pendências, follow-up e saídas. A quantidade final de páginas deve resultar da utilidade e do espaço real de escrita, não de uma obrigação de preservar 11 páginas.

---

## 3. Linha mestre de raciocínio do novo SAART

A lógica não é:

```text
Ocorre um evento → preencher mais um safety form.
```

A lógica correta é:

```text
Ocorre uma informação de safety
        ↓
O site reconhece, protege e preserva os fatos locais
        ↓
O PI/site faz a avaliação inicial, sem esperar o sponsor
        ↓
O site identifica a rota e o prazo que o CIP exige
        ↓
O caso é submetido ao sistema formal do sponsor
        ↓
O site documenta a prova de envio, recebimento, pendências e follow-up
        ↓
O sponsor/CEC realiza a determinação formal de safety
        ↓
O site acompanha as decisões e liga o caso aos seus próprios controles
        ↓
O caso fecha localmente apenas quando a coordenação local está verificável
```

A pergunta que o SAART deve responder ao final de seu preenchimento é:

> **Can the site demonstrate that it recognized, protected, assessed, reported, tracked and locally closed its part of this safety case in accordance with the applicable CIP and sponsor procedure?**

O instrumento não deve responder à pergunta:

> **What is the sponsor’s final global safety conclusion for the clinical investigation?**

Essa segunda pergunta pertence ao sponsor e, quando aplicável, ao CEC/DMC.

---

## 4. Fronteira formal entre SAART e o sistema do sponsor

| Elemento | SAART deve fazer | SAART não deve fazer |
|---|---|---|
| Fato clínico e técnico | Registrar um resumo factual local e a localização da fonte. | Copiar integralmente prontuário, narrativa de eCRF ou SAE form. |
| Atendimento/proteção | Registrar que medida imediata foi tomada, por quem e onde está a evidência. | Substituir o prontuário ou a documentação assistencial. |
| Avaliação do PI/site | Registrar a avaliação local atual, sua incerteza e a referência. | Declarar que sua avaliação é a classificação formal final do estudo. |
| Sponsor safety system | Registrar nome/identificador da rota, submission reference, transmissão e receipt. | Substituir o portal, eCRF, SAE form ou DD form do sponsor. |
| Classificação formal | Registrar a determinação do sponsor/CEC se recebida, inclusive discordância. | Fazer adjudicação multicêntrica ou avaliação global de safety. |
| Prazos | Aplicar a janela que o CIP/procedimento controlado define para o caso. | Fixar universalmente 24 h, 7 dias ou qualquer prazo não previsto. |
| EC/autoridade | Registrar referência de comunicação quando o CIP, EC, sponsor ou regra aplicável atribuir isso ao site. | Assumir que todo caso exige reporte direto local a EC/autoridade. |
| Padrões locais | Ligar a SCML, CSST, SRR, CAPA e POT quando o trigger existir. | Calcular taxas, concluir sinal agregado ou abrir CAPA automaticamente por um caso isolado. |

### Formulação obrigatória de boundary na primeira página

A primeira página deve conter uma frase equivalente a:

> **This is a controlled site coordination record. It does not replace source records, the sponsor safety form, eCRF, sponsor safety portal, device-accountability record, deviation record, SCML, CSST, CAPA Log, regulatory submission or sponsor/CEC safety determination. It records the site’s local safety-case process and the references linking it to those authoritative records.**

---

## 5. Taxonomia obrigatória da ISO 14155:2026

A reconstrução deve usar a nomenclatura abaixo. As definições completas continuam controladas pela ISO, CIP, risk assessment, IB e procedimento do sponsor; o SAART deve apresentar uma síntese operacional e referências, não reproduzir o texto da norma integralmente.

| Termo | Uso no SAART |
|---|---|
| **AE — Adverse Event** | Ocorrência médica adversa, doença/lesão não intencional ou sinal clínico adverso em subject, user ou other person, relacionada ou não ao device. É o ponto de entrada do caminho de evento. |
| **ADE — Adverse Device Effect** | AE relacionado ao uso do investigational device ou comparator device, incluindo situação ligada a IFU inadequada, deployment, implantation, installation, operation, malfunction, use error ou misuse intencional. |
| **SAE — Serious Adverse Event** | AE que atende o critério de seriedade da ISO. É uma dimensão regulatória distinta da intensidade/severidade clínica. |
| **SADE — Serious Adverse Device Effect** | ADE que também é SAE. |
| **ASADE — Anticipated SADE** | SADE identificado no current risk assessment por natureza, incidência, severidade ou desfecho. |
| **USADE — Unanticipated SADE** | SADE não identificado no current risk assessment por natureza, incidência, severidade ou desfecho. |
| **DD — Device Deficiency** | Inadequação de identidade, qualidade, durabilidade, confiabilidade, usabilidade, segurança ou performance; inclui malfunction, use error e informação/label inadequado(a). |
| **DD that could have led to a SADE** | DD que não gerou AE, mas poderia ter levado a SADE se não houvesse ação adequada, intervenção ou circunstância mais favorável. É uma rota reportável própria. |
| **Serious health threat** | Sinal de AE ou DD que indica risco iminente de morte ou deterioração séria e exige ação corretiva rápida para proteger outras pessoas. |

### Regra que deve aparecer literalmente no novo SAART

> **If an AE is associated with an observed device deficiency, apply both the adverse-event pathway and the device-deficiency pathway.**

A expressão antiga `AE + deficiency` não é suficiente. O novo instrumento deve reconhecer que não são duas caixas independentes: são **duas árvores de avaliação que seguem em paralelo**.

### Rota de AE no novo instrumento

```text
AE identified?
  ├─ No / pending
  └─ Yes
      ├─ Meets SAE criterion?
      │   ├─ No → Non-serious AE
      │   └─ Yes → SAE
      ├─ Related to use of investigational device?
      │   ├─ No → Non-device-use-related AE or CIP-procedure pathway
      │   └─ Yes → ADE
      │           ├─ Non-serious → Non-serious ADE
      │           └─ Serious → SADE
      │                        ├─ identified in current risk assessment → ASADE
      │                        └─ not identified in current risk assessment → USADE
      └─ Related to CIP-required procedure outside routine clinical practice, other than device use?
          └─ Record as separate CIP-procedure-related path when applicable
```

### Rota de DD no novo instrumento

```text
Observed device deficiency?
  ├─ No / pending
  └─ Yes
      ├─ Did it cause or occur with an AE?
      │   └─ Yes → apply both AE and DD pathways
      └─ Could it have led to a SADE?
          ├─ No → DD without SADE potential
          ├─ Yes → DD that could have led to a SADE
          └─ Pending → obtain/track sponsor assessment and information
```

### Critérios de seriedade que devem ser apresentados de forma concisa

O SAART deve conter uma lista de escolha controlada para o current PI/site assessment:

```text
□ Death
□ Life-threatening illness or injury
□ Permanent impairment of body structure or function, including chronic disease
□ In-patient or prolonged hospitalization
□ Medical or surgical intervention to prevent a life-threatening illness/injury or permanent impairment
□ Foetal distress, foetal death, congenital abnormality or birth defect
□ Does not meet seriousness criteria
□ Pending assessment
```

**Não confundir:** clinical severity/intensity e regulatory seriousness são campos distintos. Um evento clinicamente intenso não é automaticamente um SAE; um SAE não deve ser reduzido a uma escala de intensidade.

### Antecipação e expectedness

O novo SAART não deve ter uma coluna genérica de `expectedness` para todos os AEs. A pergunta precisa ser:

```text
For a confirmed or suspected SADE, is the nature, incidence, severity or outcome identified in the current risk assessment?
□ ASADE
□ USADE
□ Pending sponsor / CEC determination
□ N/A — no SADE
```

---

## 6. Arquitetura proposta do novo SAART

A estrutura abaixo é funcional. A IA que construir o HTML pode ajustar a distribuição em retrato/paisagem, altura das linhas e número de páginas, mas não deve alterar a sequência operacional.

### Cabeçalho de controle documental

Máximo de 12 células, organizado em 4 + 4 + 3 quando aplicável. Deve acomodar:

- Study / Protocol;
- Current CIP / version;
- Site / code;
- SAART Case ID / revision;
- Participant code / N/A context;
- Procedure, visit, exposure or N/A context;
- Initial awareness date/time;
- Person receiving first information;
- Current local case status;
- PI / authorized site assessor;
- Sponsor safety system / route;
- Sponsor safety case ID, if issued.

Não repetir esse cabeçalho completo em todas as páginas. Páginas de continuação devem ter somente metadados mínimos quando houver possibilidade real de folha adicional ser separada.

### A — Purpose and Use

Esta seção deve manter a tabela obrigatória:

| Elemento | Conteúdo necessário |
|---|---|
| **Unit of analysis** | One site safety case: one AE, observed DD or material new safety information. |
| **Decision support** | Confirma se o site reconheceu, protegeu, avaliou inicialmente, reportou, acompanhou e fechou sua parte do caso de maneira controlada. |
| **Inputs** | Source record, participant/user contact, device/accountability record, procedure/visit record, sponsor communications, current CIP/risk information. |
| **Outputs** | Local coordination trail; references to sponsor system; SAART data for ST-01; linked SCML, deviation, CSST, SRR/CAPA/POT records where triggered. |

A seção deve incluir a boundary formal definida na seção 4 desta análise.

### B — Initial awareness, immediate protection and factual source map

**Objetivo:** abrir o caso no momento da awareness, sem esperar classificação completa ou contato do sponsor.

Campos necessários:

- date/time of occurrence, DD detection or new information, com `Known / Estimated / Not yet known`;
- date/time first known to site;
- initial trigger: `AE / observed DD / AE associated with observed DD / material new safety information / other CIP-defined trigger`;
- person and source that brought information to the site;
- immediate participant/user/other-person safety concern;
- immediate clinical, device containment or communication action;
- factual local summary com referência à fonte;
- known missing information e owner/next step;
- participant / procedure / device context, usando `N/A reason` quando não houver participante específico.

**Regra:** o SAART registra fatos e localizações das fontes. Não copia toda a narrativa do prontuário ou do sponsor form.

### C — Current PI/site assessment against the ISO pathways

**Objetivo:** registrar uma avaliação local atual, sempre provisória quando a informação ainda não permite conclusão, e diferente da determinação formal do sponsor/CEC.

Subseções recomendadas:

1. **AE pathway**
   - AE identified?
   - seriousness criterion / pending;
   - device-use related?;
   - comparator related, if applicable?;
   - CIP-required procedure outside routine clinical practice related, if applicable?;
   - current local category: non-serious AE, SAE, ADE, SADE, ASADE, USADE, pending or N/A.

2. **DD pathway**
   - observed DD?;
   - DD category/context: identity, quality, durability, reliability, usability, safety, performance, malfunction, use error, information/label;
   - associated with an AE?;
   - could have led to a SADE? `Yes / No / Pending`;
   - device containment/return/analysis reference when applicable.

3. **Serious health threat screen**
   - signal indicates imminent risk?;
   - immediate action and communication route;
   - sponsor/PI informed date/time;
   - active or resolved status.

4. **Assessment authority and reconciliation**
   - current PI/site assessment;
   - sponsor/CEC determination, if received;
   - agreement / disagreement / not yet received;
   - date and reference of communication;
   - unresolved classification question and owner.

**Regra:** a tabela deve mostrar que a classificação local é uma avaliação e que a determinação do sponsor/CEC é uma saída externa registrada por referência. Não criar uma falsa “final local classification”.

### D — CIP reporting-control and formal sponsor submission

**Objetivo:** transformar o caso em um processo de reporting rastreável, sem duplicar o formulário do sponsor.

Campos necessários:

| Campo | Regra |
|---|---|
| Reportable under current CIP / sponsor procedure? | `Yes / No / Pending`, com referência à regra aplicável. |
| Applicable reporting route | Sponsor portal, eCRF, SAE form, DD form, emergency route ou outro caminho controlado. |
| Site awareness date/time | Referência da Seção B. |
| CIP reporting window and due date/time | Registrar a regra e o vencimento; não hard-code prazo universal. |
| Initial notification transmitted | Date/time, person, system/reference. |
| Receipt / sponsor safety case ID | Confirmation, case ID, submission ID ou reference. |
| Initial notification timely? | `Yes / No / Pending / N/A`. |
| First report complete? | `Complete / Incomplete / Pending / N/A`. |
| If late or incomplete, where did the delay arise? | Recognition; internal escalation; PI assessment; access to documentation; transmission; other. |
| Immediate correction / linked deviation record | Reference e action owner. |

**Regra:** não pedir que o site reescreva todos os campos do SAE form. Registrar somente a prova processual de que o report formal foi submetido, recebido e acompanhado.

### E — Follow-up, sponsor queries and active information tracking

**Objetivo:** manter a cronologia de uma ocorrência sem sobrescrever o que foi conhecido antes.

Uma linha por atualização material:

- date/time of new information;
- new clinical, technical or device information;
- source/reference;
- impact on current PI/site assessment;
- sponsor request/query or communication reference;
- follow-up due date/time under CIP or sponsor procedure;
- follow-up transmitted date/time and receipt reference;
- follow-up timely?;
- owner and next action;
- status: open / awaiting site information / submitted / awaiting sponsor determination / locally complete / closed.

Deve haver uma pequena caixa de síntese para:

- current clinical outcome;
- current device outcome / return / analysis, if applicable;
- outstanding information;
- active follow-up plan.

### F — Framework interfaces and local process learning

**Objetivo:** impedir que um caso individual seja perdido entre os instrumentos sem transformar o SAART em instrumento agregado.

Cada saída deve ter uma linha distinta:

| Interface | Quando usar | Registro exigido |
|---|---|---|
| **SCML** | Caso/evento entra no índice de vigilância local. | SCML Event ID / date / owner. |
| **CSST** | Caso entra em review period ou trigger de surveillance. Não é uma notificação individual obrigatória. | CSST review period, trigger or signal reference. |
| **PIR ST-01** | Caso reportável contribui para Safety Reporting Timeliness. | Reporting-control reference / review period. |
| **Deviation record** | Initial notification late; aplicar critérios do sponsor para importância. | Deviation ID / owner / status. |
| **SRR / CAPA** | Falha recorrente, risco local ou controle ineficaz. Não abrir automaticamente por caso isolado. | Linked record / rationale. |
| **POT / PI oversight** | Caso, atraso, cluster ou decisão exige oversight do PI. | Meeting/review reference and decision. |
| **Sponsor device-deficiency route** | DD ou information signal exige retorno, análise ou ação do sponsor. | Route/case ID and status. |

### G — Local coordination closure and accountable review

**Objetivo:** fechar a coordenação local sem declarar que processos externos estão encerrados.

Gates de fechamento:

- immediate protection and care documented or N/A with rationale;
- source and local factual references sufficient to reconstruct the case;
- current PI/site assessment documented;
- required sponsor submission/reference documented;
- reporting timeliness/completeness status known or limitation documented;
- follow-up obligations transferred, completed or explicitly open;
- sponsor/CEC determination recorded when received, or documented as still pending;
- required framework interfaces linked;
- local closure status: `Closed locally / Open follow-up / Transferred / Not eligible for local closure`;
- limitation statement: local closure does not override sponsor, CEC, EC or regulatory process.

Assinaturas:

- initial site assessor/case reporter;
- PI or accountable investigator;
- safety coordinator or authorized site function, if applicable;
- controlled record location and linked-system references.

---

## 7. Relação do SAART com os demais instrumentos

```text
Source record / clinical record / ICDL / PFVR / IQL
                         ↓
        SAART — individual site safety case coordination
                         ↓
        ├── Sponsor safety system / SAE-DD form / eCRF
        ├── SCML — indexed local event reference
        ├── PIR — Safety Reporting Timeliness data
        ├── Deviation record — late initial notification
        └── POT / SRR / CAPA / CSST — only when a defined trigger exists
```

### SAART → SCML

O SAART envia ao SCML apenas o suficiente para indexar e comparar casos:

- SAART Case ID / event reference;
- participant code or N/A context;
- event term/source term;
- event date/timing;
- device/component reference;
- current AE/DD status;
- relevant relationship context;
- current assessment status.

O SCML não deve reproduzir a cronologia, os reports e as pendências do SAART.

### SAART → CSST

O SAART não calcula taxas nem decide sinais. O CSST recebe referências dos casos que entram em uma revisão agregada e compara eventos contra procedimentos por categoria, componente e cirurgião.

Um caso pode disparar uma revisão antecipada do CSST quando houver:

- serious health threat;
- cluster;
- nova categoria relevante;
- concentração por componente ou cirurgião;
- trigger previamente definido.

### SAART → PIR, Safety Reporting Timeliness

O SAART é a fonte individual do processo de reporting. O PIR recebe contagens e interpretações periódicas, não a narrativa inteira do caso.

| Dado do PIR | Campo fonte do SAART |
|---|---|
| Denominador do período | `Reportable under current CIP / sponsor procedure?` e date of site awareness. |
| Initial notification timely | Awareness, applicable due date/time, transmission, receipt and timeliness status. |
| First report complete | Status `Complete / Incomplete / Pending`. |
| Follow-up on time | Follow-up due/transmitted/timely status. |
| Open at cut-off | Status atual e active follow-up plan. |
| Causa do atraso | Delay point. |
| Ação/deviation | Correction and deviation record reference. |

### SAART → Deviation record

Uma initial notification tardia deve gerar avaliação no deviation record assim que identificada. O SAART registra a referência e o ponto do processo em que o atraso surgiu. O deviation record mantém a avaliação formal de desvio conforme CIP/procedimento do sponsor.

### SAART → SRR, CAPA e POT

- Um caso único não abre automaticamente SRR ou CAPA.
- Um padrão de atrasos, falha de comunicação, vulnerabilidade de processo ou controlo ineficaz pode alimentar o SRR.
- Recorrência após resposta inicial pode abrir CAPA.
- Caso grave, atraso relevante, tendência ou decisão pendente pode ser levado ao POT.

---

## 8. O que deve mudar na tese quando o SAART for efetivamente aprovado

A alteração do nome e da função exige revisão de consistência, mas não deve ser feita agora nesta análise. Quando o instrumento estiver aprovado, revisar pelo menos:

1. lista de abreviaturas: `SART` → `SAART`;
2. Table 4.4 ou outra tabela que lista os instrumentos;
3. seção 4.3.3 sobre Device-specific complication monitoring;
4. seção 4.5.4 sobre Safety reporting timeliness;
5. fluxogramas, mapa de interações e ordem de preenchimento;
6. Appendix K, seu título e sua descrição;
7. qualquer referência a `Safety and Adverse Effect Reporting Template` no texto, figuras, tabelas e apêndices;
8. a descrição de inputs/outputs: explicitar que o SAART é coordenação local e interface com o sponsor safety system, não substituto deste.

A tese já fornece a base conceitual da mudança: o SART acompanhava um caso individual da abertura ao fechamento, o SCML indexava eventos e o CSST registrava a revisão agregada. A alteração necessária é refinar a fronteira do caso individual para não duplicar a função formal do sponsor.

---

## 9. Requisitos visuais e técnicos da reconstrução

### Linguagem visual

- Usar a identidade visual comum: fonte, azul escuro, azul médio, azul claro, bordas, cabeçalhos de seção, rodapé, tipografia e proporções reconhecíveis nos instrumentos finalizados.
- Não reutilizar literalmente a distribuição de páginas, as matrizes extensas ou a geometria do SART v0.3.
- Usar retrato para opening, process control, follow-up e closure; usar paisagem apenas onde a tabela realmente precise de largura, como classificação/rotas de reporte ou tracking cronológico.
- Ajustar a altura de cada linha à necessidade real de escrita; não aplicar uma altura idêntica a todas as tabelas.
- Priorizar espaço de escrita real para fatos, pendências, sponsor references, rationale e follow-up.
- Cabeçalho completo apenas na primeira página; páginas internas usam faixa azul e identificação mínima somente quando a folha puder ser separada ou repetida.
- Incluir rodapé seguro em todas as páginas e validar renderização A4 antes da entrega.

### Versão em branco

- O HTML inicial será em branco e editável.
- Não inserir nomes, IDs, datas, marcas de X, letra cursiva ou dados simulados na versão em branco.
- Não preencher `example rows` dentro das tabelas do template em branco. Se for necessário demonstrar o uso, gerar uma versão filled demonstration separada, com o mesmo caso fictício contínuo e fonte cursiva.

### Editor

- Incorporar o **Editor v2 canônico completo**.
- O painel deve ser flutuante e arrastável.
- Deve permitir seleção de uma ou mais células/linhas/colunas, fonte, tamanho de fonte, negrito, itálico, sublinhado, alinhamento, altura de linha, largura de coluna, caixas/opções, remoção/redimensionamento de boxes, undo/redo e save/export do HTML editado.
- O editor desligado não pode alterar a aparência visual ou a paginação do formulário.

---

## 10. Instrução de execução para a IA que criará o HTML

1. **Não editar o SART v0.3 por patch.** Criar um novo arquivo de SAART do zero, usando somente a identidade visual comum como referência.
2. Usar `SAART — Safety Assessment, Reporting and Tracking Template` no título, cabeçalhos e metadados do documento.
3. Construir o formulário como **site safety-case coordination record**, não como sponsor form duplicado.
4. Incluir a boundary statement na primeira página.
5. Implementar as seções A–G na ordem definida nesta análise.
6. Aplicar a taxonomia ISO 14155:2026 para AE, ADE, SAE, SADE, ASADE, USADE, DD, DD that could have led to a SADE e serious health threat.
7. Separar `current PI/site assessment` de `sponsor/CEC determination` e registrar concordância, discordância ou pendência.
8. Não hard-code reporting timelines: cada prazo vem do CIP ou procedimento controlado do sponsor.
9. Registrar o system/form/reference do sponsor e a prova de transmission/receipt, sem duplicar a narrativa do report formal.
10. Criar campos recuperáveis para o PIR medir Safety Reporting Timeliness.
11. Manter SCML, CSST, PIR, deviation record, SRR/CAPA e POT como handoffs distintos, cada um condicionado ao seu trigger.
12. Não calcular taxas, não concluir sinal agregado e não abrir CAPA automaticamente.
13. Não criar versão PDF ou filled demonstration nesta primeira entrega; entregar HTML em branco editável e pré-visualização web interativa.
14. Validar visualmente a versão A4, incluindo rodapés e páginas retrato/paisagem, antes de apresentar ao autor.

---

## 11. Checklist de aceitação

- [ ] A sigla e o nome são `SAART — Safety Assessment, Reporting and Tracking Template`.
- [ ] O primeiro propósito do SAART é coordenação local do caso, não duplicação do sponsor safety form.
- [ ] O documento tem statement explícito de boundary frente a source records, eCRF, sponsor portal, regulatory submission e sponsor/CEC determination.
- [ ] A unidade é um único site safety case: AE, DD observada ou material new safety information.
- [ ] A abertura ocorre na awareness e não espera classificação completa.
- [ ] Immediate protection, care, containment e communication são registrados antes da submissão/closure.
- [ ] AE, ADE, SAE, SADE, ASADE, USADE, DD e DD that could have led to a SADE estão aplicados de forma correta.
- [ ] Um AE associado a DD aplica os dois caminhos, explicitamente.
- [ ] Seriedade e severity clínica permanecem distintas.
- [ ] A avaliação atual do PI/site está separada da determinação do sponsor/CEC.
- [ ] Nenhum prazo universal de reporte foi inserido.
- [ ] A submissão formal ao sponsor é rastreável por route, due date/time, transmission, receipt/reference, timeliness e completeness.
- [ ] Um atraso identifica a etapa do processo, a correção e a referência ao deviation record.
- [ ] O follow-up preserva cronologia e referências, sem sobrescrever informações anteriores.
- [ ] SCML, CSST, PIR, deviation, SRR, CAPA e POT têm rotas separadas e condicionais.
- [ ] A closure local não afirma encerramento de processo do sponsor, CEC, EC ou autoridade.
- [ ] A versão inicial é um HTML em branco com Editor v2 e pré-visualização web interativa.
- [ ] A renderização A4 não invade rodapés e conserva espaço real de escrita.

---

## 12. Fontes verificadas

- **ISO 14155:2026:** Clauses 3.1, 3.2, 3.19, 3.45–3.47, 3.52, 7.4, 9.2.5, 10.8, Annex A.14 e Annex F.
- **Tese completa (29-10):** Sections 4.3.3 e 4.5.4; descrição dos instrumentos SCML, SART/SAART, CSST e PIR; fluxos de lifecycle e interfaces.
- **SART v0.3 atual:** analisado como fonte histórica a ser substituída, não como estrutura a ser preservada.
