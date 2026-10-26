# Varredura de split brain no capítulo 4 (4.1 a 4.5.6), 26/10

Critério: há split brain quando o mesmo dado fica em dois registros sem regra que diga qual vale. Comparar o CRF com a fonte não cria split brain: a ISO 14155:2026 (7.8.2) manda que os dados do CRF derivem dos documentos fonte e sejam consistentes com eles, com toda discrepância explicada por escrito, e que o CIP diga quais dados podem ser registrados direto no CRF. O E6(R3) (2.12.2 e 2.12.6) pede que o investigador defina antes o que é fonte e evite transcrição desnecessária. A hierarquia já existe: a fonte vale, e o CRF é derivado dela, a não ser quando o CIP permite entrada direta (aí o CRF é a fonte e não há o que comparar).

Status: a 4.1 a 4.5.2 já estão no docx de trabalho; a 4.5.3 a 4.5.6 estão prontas e não aplicadas. O autor está editando a versão local. Nada abaixo foi aplicado.

## Trocas (texto antigo → texto novo)

### 1. 4.4.4, 3º parágrafo: a regra central (a mais importante)
Antigo:
> No instrument may become a parallel record of a datum that already has a defined source, so an instrument that needs participant-level information refers to the source and does not copy it.

Novo:
> No instrument may become a parallel record of a datum that already has a defined source, so an instrument that needs participant-level information refers to the source. Where an instrument has to carry a value for a count or a comparison, such as the operative duration in the learning curve log, it cites the source of that value, any correction is made in the source, and if the two ever differ the source prevails.

### 2. 4.4.4, 1º parágrafo: o CRF como fonte
Antigo:
> The site therefore decides, for each critical datum, which record is its source, and it adapts

Novo:
> The site therefore decides, for each critical datum, which record is its source, whether a clinical record or, where the CIP allows it, the CRF itself [8], and it adapts

### 3. 4.4.4, 2º parágrafo: ICDL
Antigo:
> The log is the source for what it captures first and points to the operative note and the device accountability record for everything else, so it supports both without replacing either,

Novo:
> The log is the source only for the data that the site’s source definition assigns to it, and for everything else it points to the operative note and the device accountability record, so it supports both without replacing either,

### 4. 4.4.3, 4º parágrafo: PFVR
Antigo:
> with the result of each and any exception with the action it triggered.

Novo:
> with the result of each or a reference to the record that holds it, as the site’s source definition sets, and any exception with the action it triggered.

### 5. 4.4.3, 2º parágrafo: PSEAR (frase nova no fim)
Depois de "…without relying on undocumented knowledge." acrescentar:
> Where the sponsor supplies its own eligibility checklist, that checklist holds the decision, and the site adds to it only the evidence and the review it lacks.

### 6. 4.4.3, 3º parágrafo: SIFSL (frase nova)
Depois de "…and it allows the log to cover everyone pre-screened [8]." acrescentar:
> This log is that record, so a site that already keeps the sponsor’s log uses it and opens no other.

### 7. 4.4.1: verificação nova (substitui a versão passada antes)
Item 7 da lista, entre "Follow-up execution" e "Timeliness and closure":
> Endpoint data agreement. For the endpoint-critical fields that are recorded first outside the CRF, a sample of CRF entries agrees with the source, and any discrepancy is corrected and explained.

E no 2º parágrafo: "nine checks" → "ten checks". No 5º parágrafo (o que começa com "Before the first participant…"): "across all nine checks" → "across all ten checks".

### 8. 4.3.3, 4º parágrafo: SCML
Antigo:
> At entry the site records a preliminary assessment of what the event may relate to, which the investigator’s final classification later confirms or replaces.

Novo:
> At entry the site records a preliminary assessment of what the event may relate to, marked as preliminary, and the investigator’s final classification, recorded in the safety report, later replaces it in the log.

### 9. 4.3.3, último parágrafo: SART
Antigo:
> and the Safety and Adverse Effect Reporting Template (SART) follows each safety case from opening to closure (Appendix K).

Novo:
> and the Safety and Adverse Effect Reporting Template (SART) follows each safety case from opening to closure, referring to the source and to the sponsor’s safety forms for its clinical content (Appendix K).

### 10. 4.2.2, último parágrafo: RACI e delegation log
Depois de "…with the limit of that holder’s authority (Appendix D)." acrescentar:
> The RACI serves as the site’s delegation log, so the site keeps one record of who is authorized for each task, and where the sponsor requires its own log, the site completes that log and the RACI refers to it.

### 11. 4.2.3, último parágrafo: TRE
Antigo:
> and the Training Record Evaluation and Release (TRE) holds each person’s training and release (Appendices E and F).

Novo:
> and the Training Record Evaluation and Release (TRE) holds each person’s training and release, referring to the sponsor’s training log for any session it already records (Appendices E and F).

### 12. 4.2.4, último parágrafo: SCR
Antigo:
> holds each decision with its evidence

Novo:
> holds each decision with references to its evidence

### 13. 4.5.6 (texto ainda não aplicado; t456.json já atualizado)
Quarta medida:
> The fourth is read at each cycle of internal verification, as the share of sampled CRF entries that agree with their source, among the endpoint-critical fields that are recorded first outside the CRF.

E no 3º parágrafo: "every sampled record agrees with its source" → "every sampled entry agrees with its source".

## Conferido e sem risco
- 4.1: a regra de usar o registro existente já está lá.
- CCDM, MRL, POT e SRR guardam decisões e riscos do site, que não existem em nenhum outro registro.
- SLCT (duração operatória) e IQL (momento da imagem): carregam valores para comparação e ficam cobertos pela regra nova da troca 1.
- PIR, FUCR e CSST: são contagens derivadas, também cobertas pela troca 1.
- 4.5.2 e 4.5.4: um registro de desvios só, seja do site ou do sponsor.
- 4.5.3 e 4.5.5: leem os registros e não guardam uma segunda cópia.
