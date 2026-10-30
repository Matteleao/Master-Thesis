# Análise — PSEAR: Participant Screening and Eligibility Assessment Record v0.91

**Status:** reconstrução focal recomendada; não criar ou alterar o HTML nesta etapa.  
**Decisão central:** o PSEAR deve continuar sendo um registro individual e contemporâneo de elegibilidade, mas precisa ser substancialmente reduzido. A sua função é demonstrar uma decisão auditável antes do enrollment, **não repetir anamnese, resultados de exame, scores, laudos de imagem, relatórios clínicos ou narrativas que já pertencem aos registros-fonte**.

---

## 1. O que o PSEAR deve decidir

> **For this coded candidate, was consent appropriately in place where required, was each applicable eligibility criterion assessed against the current CIP using evidence available before the decision, and may the candidate be enrolled, not enrolled or held pending resolution?**

Unidade de análise: **uma pessoa codificada e uma decisão de elegibilidade**.

O PSEAR deve registrar somente:

- que o gate de consentimento e de uso do CIP atual foi confirmado antes da atividade que o exigia;
- qual regra/critério de elegibilidade foi analisado;
- onde está a evidência autoritativa;
- quando a evidência estava disponível;
- o resultado por critério: met / not met / pending or not assessable;
- quem fez a avaliação e, quando necessário, a confirmação independente;
- discrepância, exceção ou informação pendente;
- decisão final anterior ao enrollment, assinatura e handoff controlado.

O PSEAR não deve repetir o que a fonte já contém.

---

## 2. Fronteira entre PSEAR e registros-fonte

| Informação | Registro proprietário | Papel do PSEAR |
|---|---|---|
| Consent process, signed ICF, ICF version, re-consent and understanding documentation | Controlled consent source / site source record | Verificar que a rota está válida e citar version/location. Não copiar conversa, compreensão ou narrativa de consentimento. |
| Clinical history, examination, laboratory result, functional score or PRO | Clinical/source record, eCRF ou instrumento específico | Citar source ID/location e usar apenas o resultado de elegibilidade do critério. Não transcrever resultado, score ou narrativa clínica. |
| Imaging acquisition, image-set quality and imaging report | IQL, radiology source/report ou fonte controlada | Citar ID/source. Registrar que o critério foi met/not met/pending e, quando aplicável, que a revisão independente foi feita. Não repetir imagem, laudo ou interpretação clínica. |
| Planned-procedure/device compatibility | Fonte clínica, imaging review e regra CIP aplicável | Tratar como um critério de elegibilidade dentro da matriz, quando aplicável. Não manter um resumo narrativo separado. |
| Every candidate, screening outcome and non-inclusion reason | SIFSL | Receber/fornecer identificador e atualizar outcome. Não duplicar o log populacional no PSEAR. |
| Final pre-enrollment decision | PSEAR | É o produto principal do PSEAR. |

A tese pede exatamente o núcleo acima: decisão de elegibilidade critério a critério, fonte e data de disponibilidade da evidência, segundo revisor para imagem ou múltiplas fontes quando aplicável, escalonamento de desacordo ao PI e decisão antes do enrollment. Ela também estabelece que os demais instrumentos usam records existentes. Portanto, a compactação não reduz auditabilidade; ela remove transcrição que não acrescenta decisão.

---

## 3. Problema do PSEAR v0.91

O documento atual ocupa **sete páginas**, das quais as páginas 3 e 4 criam camadas sucessivas de conteúdo clínico que já existe em fonte:

```text
D  — clinical, functional and participant-reported assessments
E1 — objective evidence / imaging with concise finding
E2 — imaging eligibility interpretation
F  — indication and planned procedure compatibility
G  — criterion-by-criterion evidence crosswalk and outcome
```

Isto obriga o usuário a percorrer uma sequência inadequada para o clinical moment:

```text
source finding → source finding rewritten → source finding interpreted again
→ compatibility synthesis → actual criterion decision
```

A decisão que importa só aparece em G. As seções D, E1, E2 e F tornam o PSEAR parecido com uma segunda ficha clínica — exatamente o problema identificado pelo autor — e aumentam a chance de:

- transcrição divergente da fonte;
- texto clínico abreviado que perde nuance;
- preenchimento tardio, porque o documento parece longo demais;
- inconsistência entre PSEAR, IQL, source note, eCRF e imaging report;
- auditoria concentrada numa cópia de segunda ordem, em vez de na fonte autoritativa.

A instrução interna “do not copy source narratives” é correta, mas a estrutura visual ainda incentiva cópia de finding/score/interpretação. Isso precisa ser corrigido pela própria arquitetura, não apenas por mais guidance text.

---

## 4. Elementos que devem permanecer

1. **Purpose and Use** na primeira página, incluindo Unit of analysis, Decision support, Inputs e Outputs.
2. **Consent gate fortalecido.** A verificação de ICF atual, sequência temporal e entendimento/re-consent quando requerido deve permanecer antes de uma decisão Eligible; o PSEAR referencia, não duplica, o consent source.
3. **Avaliação critério a critério.** Esta é a tabela nuclear e deve permanecer.
4. **Data de disponibilidade da evidência.** Não basta uma referência: o registro deve mostrar que a evidência existia antes da decisão.
5. **Segundo revisor somente quando aplicável.** Em particular, para critério image-dependent ou julgamento clínico que integra várias fontes, conforme CIP/pathway.
6. **Exceção/discrepância com ação e bloqueio da decisão Eligible.** Manter, mas somente quando aberto.
7. **Decisão final, assinatura do assessor e do PI/accountable reviewer.**
8. **Handoff ao SIFSL e ao registro posterior aplicável.**

---

## 5. Elementos que devem ser removidos, fundidos ou reduzidos

| Elemento atual | Decisão | Motivo / novo destino |
|---|---|---|
| C — Required screening activities and source assessment record | Reduzir muito ou absorver | Um log de todas as atividades repete a matriz de critérios e cria outra lista operacional. Manter somente os gates de prontidão de evidência, se necessários. A matriz de critérios deve indicar os source references usados. |
| D — Clinical, functional and participant-reported assessments | Retirar | Copia resultados, scores e métodos que pertencem ao source/clinical record. O PSEAR só cita a fonte na linha do critério. |
| E1 — Objective evidence register | Retirar | Repete imaging/test source, body region e finding. IQL/radiology source é proprietário dessa informação. |
| E2 — Imaging eligibility interpretation | Retirar como seção separada | A interpretação relevante deve aparecer como resultado de um critério image-dependent na matriz, com fonte e confirmação independente quando exigida. |
| F — Indication and planned procedure compatibility | Fundir | Quando aplicável, é uma regra de elegibilidade. Incluir como critério na matriz, não como síntese narrativa independente. |
| G — Critical eligibility evidence crosswalk | Manter e tornar núcleo | Renomear para **Eligibility Criteria Decision Matrix**. Usar uma linha por critério aplicável e não restringir artificialmente o registro a “critical” se o CIP exige todos os critérios. |
| H — Final eligibility decision | Manter, reduzir | Consolidar os gates e registrar Eligible / Not eligible / Pending — no narrative clinical repetition. |
| I — Open information, exception and immediate action route | Manter como tabela condicional | Só é usada se um item bloqueia ou muda a decisão. Pode ser continuação repetível, não uma página inteira fixa. |
| J — Point of enrolment and controlled handoff | Manter, reduzir | Basta demonstrar decision timestamp, enrolment/SIFSL update e next applicable record. Não precisa de quatro linhas amplas em página exclusiva. |
| K — Review/signatures/filing | Manter, compactar | Assinaturas e controlled location cabem na mesma página da decisão/handoff. |

---

## 6. Nova tabela nuclear: Eligibility Criteria Decision Matrix

A futura versão deve ter uma matriz repetível, em A4 landscape, com uma linha por critério aplicável. Pode ocupar mais de uma folha de continuação quando o CIP tiver muitos critérios; não se deve comprimir fontes ou alturas de linha para caber em um número fixo de páginas.

Colunas propostas:

| Campo | Função |
|---|---|
| No. | Linha de rastreabilidade. |
| CIP criterion ID and short rule | Código e rótulo curto; não copiar o texto integral do CIP. |
| Applicable? | Yes / No, com rationale quando No. |
| Authoritative evidence source(s) | Source record, report, IQL ID, eCRF/source locator, lab report, etc. |
| Evidence available date | Demonstra que a evidência precedeu a decisão. |
| Criterion outcome | Met / Not met / Pending or not assessable. |
| Primary reviewer / date | Quem fez a avaliação. |
| Independent confirmation, if required | Reviewer/date ou N/A according to approved pathway. |
| Exception / discrepancy reference | PSEAR exception ID ou `None`. |

A coluna `CIP criterion ID and short rule` deve permitir que o auditor entenda a lógica sem exigir que o PSEAR replique todas as páginas do protocolo. A fonte controlada de definição completa é o CIP ou uma eligibility criteria schedule aprovada. Se houver tal schedule no estudo, o cabeçalho deve citar ID/version; se não houver, basta a referência CIP section/version configurada no próprio PSEAR.

### Regra de imagem

Um critério que depende de imagem não abre automaticamente um E1/E2. Ele é uma linha na matriz:

```text
Criterion: E-04 — protocol-defined anatomical suitability
Evidence: IQL-042 / radiology report R-88
Outcome: Met
Primary reviewer/date: …
Independent confirmation: …
```

O IQL/radiology report contém qualidade, exame e achado. O PSEAR contém a decisão de critério e a confirmação necessária.

---

## 7. Arquitetura recomendada para a futura versão

```text
Page 1 — portrait
  • control header, with only decision-relevant metadata (maximum 12 cells)
  • A. Purpose and Use
  • B. Decision prerequisites and consent/source boundary
    - current CIP/eligibility ruleset identified
    - coded participant and controlled location established
    - consent pathway confirmed before consent-dependent activity
    - no clinical narrative or result copied

Page 2 — landscape, repeatable continuation sheet
  • C. Eligibility Criteria Decision Matrix
  • one row per applicable inclusion/exclusion/decision rule
  • source reference and evidence-available date, not source finding
  • independent review only where required

Page 3 — portrait
  • D. Exception / discrepancy route — only if opened
  • E. Final eligibility decision and immediate consequences
    Eligible / Not eligible / Pending — do not enroll
  • F. Controlled handoff
    decision date/time; SIFSL update; enrollment date/time if applicable;
    next protocol-defined record
  • G. Accountable review, signatures and controlled filing location
```

O documento pode ter duas, três ou mais páginas de matriz C quando o estudo exigir muitos critérios. A folha de matriz deve ser claramente repetível, mantendo PSEAR ID, participant code e page sequence apropriados. Um PSEAR de caso simples pode ter três páginas; um protocolo com muitos critérios pode gerar uma ou mais continuation sheets sem deixar de ser leve no ponto de uso.

---

## 8. Sequência operacional de preenchimento

1. Criar/identificar participant code e a localização controlada da fonte, sem colocar identificação direta no PSEAR.
2. Confirmar CIP/current eligibility configuration e, antes de qualquer atividade que dependa disso, o consent gate aplicável.
3. Durante screening, apenas citar na matriz o source record que suporta cada critério assim que a evidência estiver disponível.
4. Marcar cada critério como Met, Not met ou Pending/not assessable. Não copiar finding, score, laudo ou narrativa.
5. Solicitar confirmação independente somente para o critério que o CIP/pathway define como image-dependent ou multi-source judgement.
6. Se houver fonte ausente, conflito ou discrepância, abrir a route de exceção e impedir decisão Eligible até a resolução.
7. Registrar decisão final antes do enrollment. Atualizar SIFSL e handoff para o próximo registro somente depois da decisão válida.
8. Assinar, datar e arquivar com referências que permitam reconstrução da decisão.

---

## 9. Interfaces atualizadas

```text
Controlled consent source ─┐
Clinical / source record ──┤
IQL / radiology report ────┤
CIP eligibility rule ──────┼──→ PSEAR: eligibility decision
                           │
SIFSL ─────────────────────┘    ← outcome and non-inclusion/enrollment linkage

PSEAR ──→ SIFSL: screening outcome / reason / PSEAR reference
PSEAR ──→ enrollment / next protocol record: only after valid eligible decision
PSEAR ──→ PIR: aggregate source for Enrollment Quality at periodic review
PSEAR ──→ deviation/CAPA/SRR/POT: only when an error, recurring control weakness
           or material process issue is identified; not for every non-eligibility
```

---

## 10. Direção visual e técnica para o futuro HTML

- Não adaptar o v0.91 somente reduzindo fonte ou juntando tabelas; reconstruir a sequência visual a partir da decisão.
- Preservar a identidade visual comum, Purpose and Use, metadata style, rodapé e editor; não preservar a extensão de sete páginas.
- A página 1 e página final devem ser portrait. A matriz de critérios deve ser landscape apenas pela necessidade de colunas.
- A matriz C deve ter espaço razoável para escrever source locator e reviewer/date; não deve tentar acomodar achado clínico narrativo.
- A versão blank não deve conter example rows preenchidas. Um caso demonstrativo, se necessário, pertence exclusivamente ao filled demo e deve usar o mesmo criterion/source chain em todas as seções.
- Migrar para o Editor v2 canônico quando o HTML for reconstruído; não manter estilos/scripts residuais ou mais de um editor.
- Gerar pré-visualização interativa no navegador em toda entrega futura, antes de PDF ou filled demo.

---

## 11. Checklist para a IA que reconstruirá o PSEAR

1. Não reproduzir clinical findings, PRO scores, imaging findings, radiology reports ou source narratives.
2. Reter a avaliação de todos os critérios aplicáveis, critério a critério, com source reference e evidence-available date.
3. Manter o consent gate como confirmação de rota e fonte controlada; não duplicar consent documentation.
4. Tratar imaging/procedure compatibility como critério dentro da matriz, não como páginas narrativas paralelas.
5. Bloquear `Eligible` enquanto houver critério Pending/not assessable ou exceção relevante aberta.
6. Usar second review apenas onde CIP/pathway requer, sem exigir coassinatura universal.
7. Fazer a folha de matriz repetível, e não alargar o documento com páginas de transcrição.
8. Manter atualização/ligação ao SIFSL, sem duplicar a função populacional do log.
9. Incluir apenas metadados, campos, assinaturas e handoffs que alterem a decisão ou a rastreabilidade.
10. Não inserir referências à tese no instrumento final; citar somente CIP, approved schedule, source record e documentos operacionais controlados.

---

## 12. Fontes verificadas

- Tese completa (29-10), seção 4.3.4: decisão critério a critério, fonte e data de disponibilidade, consentimento anterior à atividade dependente, segundo revisor quando necessário, PI resolve discrepância e decisão antes de enrollment.
- Tese completa (29-10), seção de implementação: PSEAR como um dos cinco registros no clinical moment; os demais instrumentos leem registros existentes.
- PSEAR v0.91: estrutura A–K, distribuição visual de sete páginas e seções D/E1/E2/F/G que repetem a mesma cadeia de evidência em diferentes níveis.
