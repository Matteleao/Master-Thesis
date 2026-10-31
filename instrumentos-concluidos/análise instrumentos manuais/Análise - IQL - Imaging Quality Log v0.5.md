# Análise crítica — IQL: Imaging Quality Log v0.5

**Status:** análise manual para orientar a próxima revisão do instrumento. O HTML v0.5 não foi alterado nesta etapa.

## 1. Veredito executivo

O IQL v0.5 tem uma função necessária e relativamente bem delimitada: registrar cada conjunto de imagens exigido pelo protocolo, avaliar se ele foi adquirido no momento aplicável, se está completo, se possui qualidade técnica suficiente e se pode ser usado para a finalidade local definida.

A unidade de análise está correta:

```text
one required image set + one participant + one protocol time point
```

O IQL não deve ser transformado em:

- uma ficha clínica do participante;
- um registro de elegibilidade;
- um registro completo de follow-up;
- um log de transferência central do sponsor;
- um instrumento de adjudicação de endpoint;
- um indicador agregado de imaging performance;
- um CAPA ou registro de risco.

A versão v0.5 já acerta a separação principal entre:

1. **Timing** — quando o conjunto foi adquirido;
2. **Set completeness** — se todas as vistas/sequências exigidas estão presentes;
3. **Technical quality** — se a aquisição atende aos critérios técnicos;
4. **Local use decision** — para que finalidade o conjunto pode ser usado localmente.

O principal trabalho da próxima versão deve ser de clarificação e rastreabilidade, não de reconstrução completa.

---

## 2. Decisão que o IQL deve suportar

Depois de preencher o IQL, o responsável deve conseguir decidir:

> **For this participant and protocol time point, was the required image set acquired within the applicable window, is the set complete and technically adequate, and can it be used for the defined local purpose without an unresolved restriction?**

Essa decisão deve ser tomada por image set. O IQL pode conter muitos sets, mas cada linha da seção C representa um conjunto independente.

A decisão de uso local pode ser, por exemplo:

- supporting eligibility review;
- supporting follow-up assessment;
- supporting a local clinical assessment;
- supporting a local endpoint-related review;
- restricted use with a documented limitation;
- pending second review or repeat acquisition;
- not usable for the intended local purpose.

O IQL não deve concluir que o conjunto foi aceito para adjudicação central ou que o endpoint é clinicamente positivo. A própria versão v0.5 já declara essa fronteira, e ela deve ser preservada.

---

## 3. Papel do IQL na framework

A tese coloca o IQL dentro de **Operational Controls**, no domínio de imaging acquisition, interpretation and endpoint control.

A lógica operacional é:

```text
Sponsor imaging charter / CIP
        ↓
SIRR: site readiness and local implementation
        ↓
IQL: image-set acquisition and local usability record
        ↓
PSEAR or PFVR: eligibility/follow-up consequence and linked reference
        ↓
FUCR / IMC / PIR: aggregated or process-level review
```

O IQL é um dos registros que precisa ser preenchido no momento clínico ou imediatamente quando o image set se torna disponível. A razão é a mesma indicada na tese: qualidade técnica, timing, completude e condições de aquisição podem não ser reconstruíveis com segurança posteriormente.

O IQL é, portanto, um **source-adjacent operational record**, não apenas um relatório periódico.

---

## 4. O que está correto na versão v0.5

### 4.1. Purpose and Use

A primeira página define corretamente:

- a unidade de análise;
- a decisão suportada;
- os inputs;
- os outputs;
- a ligação com PSEAR e PFVR;
- a separação entre uso local e aceitação central.

Essa estrutura deve permanecer.

### 4.2. O guia de classificação tem quatro dimensões úteis

A seção B evita que o reviewer trate “imagem disponível” como sinônimo de “imagem utilizável”. A distinção entre timing, completude, qualidade técnica e decisão de uso é necessária.

Exemplo correto:

- o conjunto pode estar `In window`;
- mas `Partial` em completude;
- `Limited` em qualidade técnica;
- e `Pending` em decisão de uso local.

Não deve existir um único campo de “image quality” que misture todas essas dimensões.

### 4.3. A seção C é o núcleo correto do instrumento

A tabela de image-set log tem as colunas essenciais:

- Set ID;
- Participant / Time Point;
- PSEAR / PFVR ID;
- Modality / Required Set / Requirement Reference;
- Planned Window / Actual Acquisition Date;
- Timing;
- Required Set Complete;
- Technical Quality;
- Local Use Decision;
- Archive / Transfer / Receipt Reference;
- Reviewer / Date;
- Resolution / Route ID.

A regra de uma linha por image set deve ser preservada.

### 4.4. A seção D agrega sem substituir o log

A seção D é útil porque dá uma visão periódica de qualidade. Ela não deve ser usada como fonte primária: os números devem ser derivados das linhas C e continuar rastreáveis por Image-set ID.

A regra de que categorias podem se sobrepor é correta. Um mesmo set pode ser parcial e tecnicamente limitado; por isso, não se deve obrigar todas as categorias a formar uma classificação mutuamente exclusiva.

### 4.5. A seção E é uma rota de resolução, não outro log de imagens

A seção E cumpre uma função importante:

```text
image-set problem → immediate response → evidence → linked route → owner → status
```

Ela deve permanecer, mas somente para sets com problema, limitação, repetição, segunda revisão, correção de rastreabilidade ou encaminhamento.

### 4.6. A seção F fecha a revisão local

A conclusão distingue:

- controlado sem problema aberto;
- controlado com limitação;
- resolução/handoff pendente;
- uso restrito/escalado.

Essa classificação é melhor que simplesmente `pass/fail`, porque uma limitação documentada pode permitir determinado uso local sem permitir outro.

---

## 5. Principal risco conceitual: misturar qualidade técnica e interpretação clínica

O IQL deve avaliar se a imagem é tecnicamente adequada para a finalidade definida, mas não deve duplicar a interpretação clínica completa.

### O IQL pode registrar

- posição inadequada;
- cobertura incompleta;
- vista ou sequência ausente;
- artefato que limita a avaliação;
- exposição ou aquisição tecnicamente insuficiente;
- imagem fora da janela;
- impossibilidade de confirmar a qualidade;
- necessidade de repetição;
- necessidade de segunda revisão;
- restrição de uso local;
- referência à avaliação clínica ou ao registro de follow-up.

### O IQL não deve registrar como conclusão própria

- diagnóstico clínico completo;
- decisão final de elegibilidade;
- conclusão definitiva de endpoint;
- adjudicação central;
- classificação completa de evento adverso;
- interpretação cirúrgica que pertence ao ICDL ou à fonte clínica.

Quando uma limitação técnica afeta elegibilidade, follow-up ou endpoint, o IQL deve registrar a limitação e apontar para PSEAR, PFVR, SART ou outro registro governado. O instrumento de destino toma a decisão clínica ou operacional correspondente.

---

## 6. Interfaces com outros instrumentos

### 6.1. SIRR → IQL

O SIRR avalia se o site tem capacidade para cumprir o Imaging Charter antes da ativação:

- equipamento;
- pessoal;
- configuração;
- qualificação;
- calibração;
- vistas e sequências;
- fluxo local;
- critérios de revisão;
- rota de imagem não conforme.

O IQL não deve repetir essa avaliação de readiness. Ele recebe a configuração aplicável e registra se cada image set real foi adquirido sob aquela configuração.

A ligação mínima deve incluir:

- Imaging Charter/manual ID;
- versão;
- requisito aplicável;
- equipamento ou modalidade quando necessário;
- reviewer autorizado;
- referência ao SIRR quando a capacidade local estiver em questão.

### 6.2. IQL → PSEAR

No screening/eligibility, o IQL produz:

- Image-set ID;
- participante e time point;
- requisito aplicável;
- timing;
- completude;
- qualidade técnica;
- local use decision;
- restrição ou limitação;
- referência a repetição ou segunda revisão.

O PSEAR deve registrar apenas a consequência da imagem para a decisão de elegibilidade e apontar para o IQL. Não deve copiar a avaliação técnica completa.

Exemplo:

```text
PSEAR: eligibility imaging requirement — supported / not supported / pending,
with IQL-014 as the source reference.

IQL: technical details, missing view, reviewer, local use restriction and
resolution route.
```

### 6.3. IQL → PFVR

Em follow-up, o PFVR registra que o componente de imaging foi requerido e aponta para o IQL. O PFVR pode usar a consequência da decisão:

- component completed;
- component incomplete;
- image pending;
- image usable with limitation;
- image not usable;
- repeat or second review required.

O PFVR não deve reavaliar a qualidade técnica se ela já foi documentada no IQL.

Essa é a interface mais importante para evitar redundância:

```text
PFVR records the visit/component consequence.
IQL records the image-set quality and local-use assessment.
```

### 6.4. IQL → FUCR

O FUCR deve usar o PFVR para suas contagens de visitas e componentes. O IQL pode ser uma fonte de reconciliação ou de detalhe, mas não deve alimentar diretamente o FUCR como se fosse uma segunda contagem de visitas.

O IQL pode apoiar medidas como:

- número de image sets requeridos;
- número adquirido;
- número completo;
- número dentro da janela;
- número utilizável;
- número repetido;
- número pendente ou restrito.

Quando o fenômeno é visit-level, o PFVR continua sendo a fonte de denominação. Quando o fenômeno é image-set-level, o IQL é a fonte adequada.

### 6.5. IQL → IMC

O IMC verifica se o controle de imaging do site foi executado e funcionou. Não deve repetir os image sets individualmente.

Exemplos de achados do IMC:

- IQL não foi preenchido no momento de aquisição;
- image sets não têm reviewer ou requirement reference;
- repeat acquisition ocorre, mas não há resolução documentada;
- os sets são registrados, mas o fluxo de segunda revisão não é executado;
- recurring limitations indicam que o site não consegue cumprir o charter;
- os dados do IQL não são reconciliados com PFVR/PSEAR.

### 6.6. IQL → PIR

O PIR não deve receber somente “image quality good/bad”. Deve receber dados agregados e rastreáveis, como:

- total de image sets requeridos;
- total adquirido;
- total within window;
- total complete;
- total technically adequate;
- total locally usable;
- total with limitation;
- total pending/not usable;
- repeat/second review count;
- recurring issue categories;
- source range and IQL IDs.

O PIR interpreta o indicador e sua tendência. O IQL fornece a origem dos dados.

### 6.7. IQL → SRR / CAPA / SART

O IQL encaminha para SRR quando a limitação é persistente ou demonstra uma vulnerabilidade de capacidade do site.

Encaminha para CAPA quando a causa é recorrente, material ou não resolvida por resposta local.

Só deve encaminhar para SART quando a questão de imagem fizer parte de um caso de segurança ou de uma suspeita de dano/evento adverso. Uma imagem tecnicamente limitada não é automaticamente um safety case.

---

## 7. Pontos que precisam ser melhorados

### 7.1. Separar “local use” por finalidade

`Local Use Decision` é correto, mas pode ficar ambíguo porque um conjunto pode ser utilizável para uma finalidade e não para outra.

Recomendação: incluir ou explicitar um campo `Purpose / use context`, por exemplo:

- eligibility;
- follow-up;
- local clinical review;
- endpoint-supporting review;
- other approved purpose.

A decisão de uso deve ser interpretada em relação a essa finalidade.

Não se deve registrar simplesmente `Usable` sem dizer “usable for what?”.

### 7.2. Explicitar a diferença entre “not assessed” e “not usable”

O guia atual usa `Not assessed` em Technical Quality e `Not usable` em Local Use Decision. Essa distinção é boa, mas precisa ser mais explícita:

- `Not assessed`: a qualidade ainda não foi avaliada ou não há informação suficiente para avaliar;
- `Not usable`: a avaliação foi feita e concluiu que o conjunto não pode cumprir a finalidade definida.

`Not assessed` deve normalmente produzir `Pending` em Local Use Decision, e não `Not usable`, salvo quando a ausência da avaliação já impede o uso.

### 7.3. Explicitar a relação entre timing do set e timing da visita

O IQL deve deixar claro que o timing do image set pode diferir do timing da visita:

- a visita pode ocorrer dentro da janela;
- o image set pode ser adquirido fora da janela;
- o image set pode ser repetido depois;
- a repetição não apaga o estado original.

O campo `Planned Window / Actual Acquisition Date` já permite isso, mas a nota de orientação deve dizer explicitamente que um repeat set recebe novo Set ID e permanece ligado ao set original.

### 7.4. A tabela C precisa de um campo de finalidade ou purpose

A tabela atual possui `Modality / Required Set / Requirement Ref.`. Recomenda-se incluir `Purpose / local use context` ou incorporá-lo de modo controlado nessa coluna.

Sem esse campo, o reviewer pode marcar `Usable` sem deixar claro se o uso é para screening, follow-up ou avaliação local.

### 7.5. Tornar explícito o status do repeat set

A seção E menciona repeat acquisition, mas a seção C deve permitir identificar:

- original set;
- repeat set;
- second review;
- supplemental set;
- replacement not permitted / original retained.

Não é necessário criar uma grande taxonomia. Pode ser uma coluna curta `Set relationship` com `Original / Repeat / Supplemental / Second review` e um campo para `Related Set ID`.

### 7.6. Melhorar a rastreabilidade de archive/transfer/receipt

`Archive / Transfer / Receipt Ref.` é importante, mas deve ficar claro que o IQL registra a referência, não confirma a aceitação central do sponsor.

Deve distinguir, quando aplicável:

- local archive reference;
- transfer reference;
- receipt confirmation;
- central review reference;
- not applicable.

Se tudo ficar em um campo livre, a auditoria pode não conseguir saber se o conjunto foi arquivado, transferido ou apenas preparado para transferência.

### 7.7. A seção D deve conter denominador e período claramente

A tabela D pede `Count / N and Image-set IDs`, o que é bom, mas a seção deve declarar de forma visível:

- review period;
- number of image sets in scope;
- whether counts are set-based or participant-based;
- whether categories overlap;
- source range.

A distinção `image-set count` versus `participant count` é obrigatória. O IQL deve evitar que uma contagem de sets seja interpretada como uma taxa por participante.

### 7.8. A conclusão F deve depender do uso pretendido

A conclusão local deve ser derivada da maior restrição ainda não resolvida dentro do escopo. Isso já está parcialmente escrito, mas a regra pode ser explicitada:

```text
If all sets support their defined purpose: Controlled / no open issue.
If sets support a limited purpose with documented conditions: Controlled with limitation.
If repeat, second review, traceability or response remains open: Resolution / handoff pending.
If a set cannot support its intended use or requires governed review: Use restricted / escalated.
```

A conclusão não deve afirmar que “imaging quality for the site is acceptable” quando apenas um pequeno conjunto foi revisado.

---

## 8. Redundâncias que devem ser evitadas

### 8.1. IQL e PSEAR

Não copiar a avaliação técnica inteira para o PSEAR. PSEAR registra a consequência para elegibilidade e o IQL é a fonte especializada.

### 8.2. IQL e PFVR

Não copiar a avaliação de qualidade técnica para o PFVR. PFVR registra a consequência do componente na visita e a referência ao IQL.

### 8.3. IQL e FUCR

Não usar o IQL para gerar diretamente métricas de completude de visitas. O FUCR usa PFVR para o denominador de visitas e pode usar IQL para análise específica de image-set quando necessário.

### 8.4. IQL e IMC

Não listar todos os image sets dentro do IMC. O IMC avalia se o processo de imaging foi executado, evidenciado e eficaz.

### 8.5. IQL e PIR

Não transformar a conclusão do período no indicador completo. O PIR recebe dados reconciliados e realiza a análise agregada.

### 8.6. IQL e SIRR

Não repetir a avaliação de readiness no IQL. O IQL registra a execução real sob a configuração previamente considerada adequada.

---

## 9. Arquitetura recomendada para a próxima versão

A estrutura atual de quatro páginas é adequada e pode ser preservada.

### Página 1 — Identity, purpose and classification

- cabeçalho;
- A. Purpose and Use;
- Unit of analysis, decision, inputs, outputs;
- B. Image-Set Classification Guide;
- explicação curta sobre local use versus central acceptance.

### Página 2 — Image-set source log

- C. Image-Set Quality Log;
- uma linha por image set;
- purpose/use context;
- original/repeat/supplemental relationship;
- timing;
- completeness;
- technical quality;
- local use;
- archive/transfer/receipt;
- reviewer;
- route ID.

Esta página é o núcleo do IQL e deve continuar em landscape se necessário.

### Página 3 — Periodic summary and resolution

- D. Periodic Imaging-Quality Summary and Handoff;
- scope, period and denominator;
- counts by image-set ID;
- E. Image-Set Resolution and Linked Route;
- apenas problemas que exigem resposta.

### Página 4 — Conclusion and accountability

- F. Current Period Imaging-Quality Conclusion;
- purpose-specific conclusion;
- outstanding restriction/handoff;
- G. Accountable Local Review and Record Location;
- local reviewer, PI review when required, controlled filing.

Não adicionar uma seção extensa de interpretação clínica. Essa função pertence ao PSEAR, PFVR ou registro clínico correspondente.

---

## 10. Fluxo de preenchimento recomendado

### Antes da aquisição

1. Confirmar o Imaging Charter/manual e a versão aplicável.
2. Confirmar participante, time point e propósito.
3. Confirmar janela e required views/sequences.
4. Confirmar quem fará a revisão local.
5. Confirmar o que ocorrerá se o set for incompleto ou não conforme.

### No momento da aquisição ou primeira disponibilidade

1. Atribuir Set ID.
2. Registrar participante e time point.
3. Registrar PSEAR/PFVR ID quando aplicável.
4. Registrar planned window e actual acquisition date.
5. Registrar se o set é original, repeat ou supplemental.
6. Confirmar required-set completeness.
7. Avaliar technical quality conforme charter/manual.
8. Definir local use decision para a finalidade declarada.
9. Registrar archive/transfer/receipt reference.
10. Abrir E se houver uma limitação ou rota necessária.

### Se houver problema

1. Não apagar a entrada original.
2. Criar Resolution ID.
3. Registrar repeat, second review ou immediate response.
4. Registrar evidence da resolução.
5. Atualizar a decisão de uso local sem apagar a decisão original.
6. Manter o vínculo com o Set ID original.
7. Encaminhar para PSEAR, PFVR, SRR, CAPA, SART ou sponsor route conforme a natureza do problema.

### No fechamento do período

1. Definir o número de sets em escopo.
2. Contar sets, não participantes, quando a unidade for image set.
3. Registrar os Set IDs incluídos nas categorias relevantes.
4. Confirmar se categorias se sobrepõem.
5. Verificar se há resolução ou handoff pendente.
6. Selecionar a conclusão F.
7. Assinar e arquivar.

---

## 11. Saídas do IQL

| Destinatário | Saída correta |
|---|---|
| PSEAR | Status e referência da imagem usada na elegibilidade, sem copiar a avaliação técnica completa. |
| PFVR | Componente de imaging realizado, atrasado, incompleto ou limitado, com referência ao IQL. |
| FUCR | Informação específica de image-set quando necessária; a análise visit-level continua baseada no PFVR. |
| IMC | Evidência sobre execução e efetividade do controle de imaging. |
| PIR | Contagens, proporções, limitações e tendências de imaging, com denominador e source range. |
| SRR | Vulnerabilidade persistente de equipamento, pessoal, processo, janela ou qualidade. |
| CAPA | Problema recorrente, material ou não resolvido. |
| SART | Somente quando a questão de imagem integra uma ocorrência de segurança ou suspeita de dano. |
| Sponsor / central review | Transfer, receipt ou route reference; nunca uma declaração de aceitação central não autorizada. |

---

## 12. Checklist de correção da próxima versão

1. Cada linha da seção C representa exatamente um image set?
2. O IQL identifica participante, time point, modalidade e requirement reference?
3. A finalidade do uso local está explícita?
4. Timing, completude, qualidade técnica e decisão de uso continuam separados?
5. `Not assessed` está distinguido de `Not usable`?
6. Repeat, supplemental e second-review sets podem ser relacionados ao set original?
7. A aquisição fora da janela permanece visível mesmo quando há repetição?
8. O campo de arquivo/transferência distingue archive, transfer, receipt e central review quando aplicável?
9. O IQL não decide elegibilidade nem adjudica endpoint?
10. PSEAR e PFVR recebem apenas a consequência e a referência, sem duplicação técnica?
11. A seção D declara período, denominador, unidade de contagem e possibilidade de sobreposição?
12. Os Set IDs tornam cada resumo auditável?
13. A seção E é aberta somente quando existe issue, limitation, repeat, second review ou route?
14. Toda ação tem owner, due date, evidence e status?
15. A conclusão F é específica para o uso pretendido e para o escopo revisado?
16. O IQL consegue encaminhar uma limitação para SRR, CAPA, SART ou sponsor route sem duplicar o instrumento de destino?
17. O documento continua utilizável no momento clínico e não se transforma em uma análise periódica excessiva?
18. A tabela C continua legível e dentro dos limites A4, usando landscape quando necessário?

---

## 13. Conclusão

O IQL v0.5 está conceitualmente correto e possui uma boa arquitetura de quatro páginas. O instrumento deve ser mantido, não descartado.

As melhorias prioritárias são:

1. tornar explícita a finalidade para a qual a imagem está sendo avaliada;
2. distinguir claramente `not assessed`, `pending` e `not usable`;
3. registrar a relação entre image sets originais, repeats e supplemental sets;
4. fortalecer archive/transfer/receipt traceability;
5. declarar denominador e período na síntese D;
6. preservar a fronteira entre qualidade técnica da imagem e interpretação clínica;
7. fazer PSEAR e PFVR receberem a consequência da decisão, não uma cópia do IQL;
8. garantir que o PIR receba contagens set-based com source range e denominador explícito.

A linha-mestra recomendada é:

```text
Charter requirement → image-set acquisition → technical assessment
→ local-use decision → linked resolution when needed
→ participant-record consequence → periodic aggregate summary
→ process oversight or escalation when recurring.
```

O IQL deve continuar sendo o registro especializado que preserva a qualidade e a utilizabilidade de cada conjunto de imagens, enquanto os outros instrumentos utilizam sua saída sem repetir o mesmo trabalho.

---

## 14. Fontes verificadas

- Tese completa (29-10), seção 4.4.2: imaging standardization, sponsor imaging charter, local review, repeat acquisition, second review, calibration e papel do IQL.
- Tese completa (29-10), seção 4.4.3: registros de elegibilidade e follow-up e relação com imaging.
- Tese completa (29-10), seção 4.6: instrumentos preenchidos no momento clínico, incluindo IQL.
- Tese completa (29-10), Appendix O: Site Imaging Readiness Record.
- Tese completa (29-10), Appendix P: Imaging Quality Log.
- IQL v0.5 blank e filled: seções A–G, classificação, image-set log, periodic summary, resolution route, conclusion e local accountability.
- PFVR v0.5 analysis: separação entre componente de imaging no PFVR e avaliação técnica especializada no IQL.
- Operational Quality Form Templates skill: distinção entre registro individual, source-adjacent record, revisão operacional e performance agregada.
