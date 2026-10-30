# Análise — PSEAR: Participant Screening and Eligibility Assessment Record v0.91

## Instrução de trabalho vigente — seguir nesta entrega

**Status:** manter o PSEAR como registro individual universal de screening e elegibilidade; melhorar a versão v0.91 sem alterar o seu papel fundamental.
**Não fazer nesta entrega:** não renomear o instrumento, não o tornar condicional, não o converter em assurance-only, não transferir a decisão para o sistema do sponsor e não eliminar as seções de evidência clínica/imaging por uma mudança arquitetural ampla.

A versão atual pode ser longa e conter redundâncias, mas a prioridade desta entrega é aperfeiçoá-la de forma conservadora, preservando a sua utilidade como registro reconstruível de uma decisão de elegibilidade por participante. A crítica mais ampla sobre potencial duplicação com o sponsor está registrada separadamente na Parte II deste documento **somente como dívida de arquitetura futura**. A IA que reconstruir o HTML agora deve ignorar essa alternativa e seguir a Parte I.

---

# Parte I — Manter e melhorar o PSEAR v0.91

## 1. Decisão e unidade de análise a preservar

> **For this coded candidate, was consent appropriately in place where required, were the applicable eligibility requirements assessed against the current CIP using evidence available before the decision, and may the candidate be enrolled, not enrolled or held pending resolution?**

Unidade de análise: **uma pessoa codificada e uma decisão de elegibilidade**.

O PSEAR continua sendo o registro que demonstra, antes do enrollment:

- a configuração aplicável do CIP e a rota de consentimento;
- a realização ou disponibilidade das avaliações necessárias;
- a localização da evidência clínica, funcional, objetiva e de imagem;
- a interpretação de elegibilidade necessária para aquele participante;
- a avaliação critério a critério;
- revisão independente quando exigida;
- exceções, discrepâncias ou informação pendente;
- decisão final, handoff, assinatura e filing controlado.

A tese sustenta este modelo: exige decisão critério a critério contra o CIP vigente, identificação da fonte e da data em que a evidência se tornou disponível, revisão independente para critérios dependentes de imagem ou múltiplas fontes quando aplicável, resolução de desacordo pelo PI e decisão antes do enrollment.

## 2. Limite de conteúdo: melhorar sem transformar o PSEAR em segunda ficha clínica

Mesmo mantendo o modelo atual, cada seção deve ser editada para registrar apenas o **mínimo necessário para tornar a decisão de elegibilidade inteligível e reconstruível**. Não copiar textos integrais ou narrativas que já pertencem à fonte.

| Informação | Registro proprietário | Papel mantido para o PSEAR |
|---|---|---|
| Consent process, signed ICF, ICF version, re-consent and understanding documentation | Controlled consent source / site source record | Confirmar rota, versão, sequência e localização. Não copiar conversa, formulário ou narrativa de consentimento. |
| Clinical history, examination, laboratory result, functional score or PRO | Clinical/source record, eCRF ou instrumento específico | Registrar somente o dado ou conclusão estritamente necessário para leitura da elegibilidade e citar a fonte. Não copiar narrativa clínica extensa. |
| Imaging acquisition, image-set quality and imaging report | IQL, radiology source/report ou fonte controlada | Registrar referência, utilizabilidade e interpretação limitada à elegibilidade. Não copiar o laudo integral. |
| Planned-procedure/device compatibility | Fonte clínica, imaging review e regra CIP aplicável | Registrar a síntese de compatibilidade quando o CIP exigir, com referência às fontes. |
| Every candidate, screening outcome and non-inclusion reason | SIFSL | Manter ligação e reconciliação; não duplicar a função populacional do log. |
| Final pre-enrollment decision | PSEAR | Produto central do instrumento. |

A regra prática para cada célula narrativa é:

```text
Write only what changes, explains or qualifies the eligibility decision.
Otherwise, cite the controlled source location.
```

## 3. Melhorias obrigatórias por seção — manter a arquitetura A–K

### A — Purpose and Use

Manter Purpose and Use e a tabela de Unit of analysis, Decision support, Inputs e Outputs. Ajustar apenas para deixar ainda mais claro que:

- o PSEAR documenta a decisão de elegibilidade e seu encadeamento de evidências;
- ele referencia, mas não substitui, consent source, clinical source, IQL/imaging report, SIFSL, CIP, CRF/eCRF e sponsor records;
- o auditor deve encontrar evidência suficiente para reconstruir a decisão sem precisar que a folha replique narrativas clínicas.

### B — Pre-screening gates and record boundaries

Manter os três gates atuais:

1. CIP/amendment and eligibility requirements available;
2. participant code and controlled record location established;
3. consent pathway valid before consent-dependent activity.

Melhorar somente a clareza e o espaço de preenchimento. O consent gate deve permanecer forte: versão atual de ICF, sequência temporal e evidência de understanding/re-consent quando requerido. O PSEAR verifica e aponta a fonte; não duplica a documentação de consentimento.

### C — Required screening activities and source assessment record

**Manter.** Não remover esta seção nesta entrega.

Ela deve funcionar como o índice de completude do screening, não como cópia de resultados. Cada linha representa uma atividade ou família de assessment realmente exigida pelo CIP, com:

- atividade requerida;
- data completed;
- função que realizou;
- source or linked detail location;
- completion status.

Melhorias:

- não inserir finding clínico, score, resultado laboratorial ou narrativa de imagem nesta tabela;
- usar apenas atividades que são de fato necessárias para a decisão do participante; não preencher linhas por hábito;
- manter espaço legível para `Source or linked detail location`;
- preservar a primeira linha de exemplo apenas se a versão solicitada for uma versão de guidance. Para a versão blank definitiva, deixar as linhas em branco e mover o exemplo para a versão filled demonstration, se houver;
- permitir folha de continuação se o CIP exigir mais atividades do que as linhas disponíveis.

### D — Clinical, functional and participant-reported assessments

**Manter.** Não retirar nesta entrega.

A seção D existe para permitir que o avaliador veja quais domínios clínicos/funcionais sustentaram a decisão, sem precisar abrir todos os records antes de localizar a fonte correta. A melhoria é de disciplina de conteúdo:

- `Finding / score` deve conter somente o valor, faixa, conclusão ou descrição curta que é material para elegibilidade;
- não transcrever a avaliação completa, a anamnese ou a narrativa clínica;
- `Source record reference` é obrigatório sempre que houver finding/score;
- manter somente os componentes exigidos pelo CIP ou relevantes para os critérios aplicáveis daquele participante;
- quando a fonte for suficiente e o dado não precisar de repetição mínima para entendimento da decisão, preferir uma referência clara em vez de narrativa.

### E1 — Objective evidence register

**Manter.** Não retirar nesta entrega.

A seção E1 deve registrar exames objetivos e imagem usados no screening, mas de modo enxuto:

- registrar exame, data, região/alvo, report/source reference e utilizabilidade;
- o campo `Concise objective finding` deve ter uma frase factual curta, apenas quando necessária para compreender o vínculo com a decisão;
- nunca copiar laudo radiológico completo, técnica de aquisição ou narrativa clínica extensa;
- `Usable for review?` deve permanecer, porque protege contra uma decisão baseada em exame não utilizável;
- qualidade detalhada do image set pertence ao IQL; E1 só referencia o IQL ou o report quando necessário.

### E2 — Imaging eligibility interpretation

**Manter.** Não retirar nesta entrega.

Esta é a ponte curta entre um achado de imagem e seu significado de elegibilidade. Para evitar repetição:

- completar somente para domínios de imagem que efetivamente sustentam um critério;
- uma linha deve conter uma interpretação de elegibilidade curta e o source/reviewer;
- não repetir o texto do laudo, nem repetir a decisão final de critério que pertence a G;
- não usar linhas vazias como obrigação. Se somente um domínio de imagem for relevante, uma linha é suficiente.

### F — Indication and planned procedure compatibility — when applicable

**Manter como seção condicional.**

A seção só é completada quando o CIP exigir compatibilidade de indicação, procedimento ou device para decidir a elegibilidade. Ela deve sintetizar, sem recontar dados:

- elemento de compatibilidade;
- statement curto de compatibilidade;
- fonte/reviewer;
- status compatible / not compatible / N/A.

Não preencher F quando o protocolo não tiver uma regra específica desse tipo. Não usar F para repetir D, E1 ou E2.

### G — Critical eligibility evidence crosswalk

**Manter como núcleo decisório do PSEAR.**

G é a tabela que controla a decisão. Não renomear ou reconstruir a arquitetura de forma radical nesta entrega. Melhorar:

- incluir uma linha para cada critério de inclusão, exclusão ou decision rule material para aquele participante;
- manter `CIP criterion / decision rule`, `Evidence location only`, outcome, primary reviewer/date, secondary confirmation if required e reference à discrepância;
- citar localizações D, E1, E2, F, IQL, report, source note, lab record ou eCRF quando aplicável;
- não transcrever achados nas colunas de evidência;
- manter second reviewer apenas onde CIP/site pathway exige, especialmente quando houver imaging-dependent ou multi-source judgement;
- usar `Incomplete` e encaminhar para I quando uma evidência necessária não estiver disponível ou houver conflito.

### H — Final eligibility decision

Manter os gates e a decisão final. Melhorar a leitura e não duplicar fatos clínicos:

- `Required screening activities complete` deve remeter a C;
- `Critical eligibility criteria resolved` deve remeter a G;
- consent gate deve remeter a B;
- exceções abertas devem remeter a I;
- na rationale final, usar referência curta às seções/records que suportam a conclusão, não uma repetição de clinical findings;
- manter Eligible / Not eligible. Não acrescentar uma mudança ampla de status nesta entrega; se o formulário precisar documentar uma interrupção por informação aberta, usar I e não permitir Eligible.

### I — Open information, exception and immediate action route

Manter. A seção deve ser aberta somente quando houver informação ausente, conflito, indisponibilidade de fonte, discrepância ou item que afete a decisão.

Melhorias:

- manter consequence explícita: no Eligible decision while unresolved;
- manter owner, due date e status/resolution;
- usar `PSEAR I reference` nas seções G e H;
- não usar I para ação clínica rotineira, CAPA ou narrativa de follow-up; é uma rota curta de exceção de elegibilidade.

### J — Point of enrolment and controlled handoff

Manter. Registrar o mínimo controlado:

- final eligibility decision date/time;
- enrolment date/time and enrolment record;
- SIFSL/subject-identification screening-log reference;
- next-phase record opened.

Não repetir a decisão clínica aqui. A finalidade é demonstrar sequência temporal e handoff controlado.

### K — Review, signatures and controlled record location

Manter as assinaturas do primary assessor, investigator/accountable reviewer, secondary reviewer only if required e controlled record location. Melhorar apenas o espaço real para nome, papel, assinatura/initials e date/time.

## 4. Interconexões a preservar

```text
Consent source ─────────────┐
Clinical / source record ───┤
IQL / imaging report ───────┤
CIP eligibility rule ───────┼──→ PSEAR: individual eligibility decision
                            │
SIFSL ──────────────────────┘    ← screening outcome / non-inclusion or enrollment linkage

PSEAR ──→ SIFSL: outcome, reason and PSEAR reference
PSEAR ──→ enrollment / next protocol record: only after an Eligible decision
PSEAR ──→ PIR: source for periodic Enrollment Quality review
PSEAR ──→ IMC / SRR / CAPA / POT: only if a recurring control weakness, error,
           material discrepancy or risk signal is identified
```

## 5. Direção visual e técnica para a melhoria conservadora

- Preservar a identidade visual, cabeçalho, Purpose and Use, seções A–K, rodapé e lógica de páginas do v0.91.
- Não fazer uma reconstrução radical de três páginas nesta entrega.
- Corrigir somente densidade, legibilidade, altura de linhas, clareza de guidance e alinhamento de caixas quando a inspeção visual demonstrar necessidade.
- Manter portrait/landscape de cada página quando isso servir às tabelas existentes.
- Usar páginas/folhas de continuação para C ou G quando necessário, em vez de reduzir a fonte ou apagar linhas necessárias.
- Na versão blank definitiva, não deixar uma linha simulada preenchida. A demonstração contínua pertence a uma versão filled demo separada.
- Quando o HTML for de fato revisado, manter um único Editor v2 canônico e validar a pré-visualização interativa antes de qualquer PDF.
- Não inserir referências à tese no instrumento final; citar somente CIP, controlled source records, IQL, report, eCRF/CRF, SIFSL e documentos operacionais controlados.

## 6. Checklist para a IA que fará a melhoria agora

1. Manter o PSEAR, seu nome, sua unidade de análise e a arquitetura A–K.
2. Manter C, D, E1, E2 e F; não os apagar nem fundir como parte desta entrega.
3. Reduzir textos e achados repetidos dentro de D/E1/E2/F, mas preservar a informação mínima que torna a decisão de G compreensível.
4. Manter G como evidência criterion-by-criterion e H como decisão final.
5. Manter B como gate de consentimento e configuração; não duplicar a fonte de consentimento.
6. Manter I como rota de exceção e bloqueio de Eligible enquanto um item relevante estiver em aberto.
7. Manter J/K para sequência de enrollment, handoff, assinatura e filing.
8. Não transformar o PSEAR em instrumento opcional, addendum de assurance ou proxy do record do sponsor nesta entrega.
9. Não diminuir fonte ou sacrificar espaço de escrita para encurtar visualmente o documento.
10. Gerar e disponibilizar pré-visualização interativa do HTML revisado antes de entregar.

---

# Parte II — Questão arquitetural identificada, mas deliberadamente adiada

## 7. Problema de fronteira com o sistema do sponsor

Existe uma questão arquitetural real: em muitos estudos, o sponsor já controla no eCRF, EDC, screening worksheet ou sistema equivalente:

- critérios de inclusão e exclusão;
- dados de screening;
- decisão de elegibilidade;
- confirmação do investigador;
- status de screening/enrollment;
- parte da rastreabilidade de consentimento e das fontes.

Por isso, a versão extensa do PSEAR pode, em alguns contextos, duplicar um workflow de sponsor, produzir divergências entre fonte/eCRF/form local e entrar em tensão com o princípio de reutilizar a documentação existente.

Uma alternativa futura seria transformar o PSEAR em um registro condicional de assurance local, aberto apenas para imaging-dependent review, discrepância, evidência tardia, consent issue, lacuna do sistema do sponsor ou necessidade de decisão explícita do PI. Nessa alternativa, o sponsor screening record seria o registro individual principal, o SIFSL continuaria a reconciliação populacional e o PSEAR funcionaria como addendum de exceção.

## 8. Diretriz explícita: não seguir essa alternativa agora

Esta alternativa **não está aprovada para a entrega atual**. Não deve orientar a próxima revisão de HTML, não deve gerar mudança de sigla, não deve remover a decisão individual por participante e não deve reescrever a tese nesta fase.

Para a entrega atual, assumir como premissa operacional que o PSEAR v0.91 é necessário e melhorar a sua versão existente nos termos da Parte I. A discussão de sobreposição com sponsor deve ser tratada como dívida de arquitetura a revisar somente depois da entrega.

---

## 9. Fontes verificadas

- Tese completa (29-10), seção 4.3.4: decisão critério a critério, fonte e data de disponibilidade, consentimento anterior à atividade dependente, segundo revisor quando necessário, PI resolve discrepância e decisão antes de enrollment.
- Tese completa (29-10), seção de implementação: PSEAR como um dos cinco registros no clinical moment; os demais instrumentos leem registros existentes.
- PSEAR v0.91: estrutura A–K, distribuição visual de sete páginas e seções D/E1/E2/F/G.
