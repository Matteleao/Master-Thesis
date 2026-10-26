# Imagens e tabelas: o que muda e o que é novo (26/10)

Vale para o capítulo 4 a partir da 4.6, e inclui as pendências antigas de imagem do capítulo 3 e da 4.2. O texto das legendas sai junto com o texto de cada seção.

## 1. Numeração depois das mudanças

Saem a Fig. 4.2 (instrumentos por pilar) e a Fig. 4.5 (instrumentos × DRs). Entram uma figura nova na 4.6 e duas tabelas novas, uma na 4.6 e outra na 4.7.

| Hoje | Depois | Onde |
|---|---|---|
| Fig. 4.1 lifecycle | Fig. 4.1 | 4.6.1 |
| (nova) matriz instrumento × fase | Fig. 4.2 | 4.6.2 |
| Fig. 4.3 granularidade | Fig. 4.3 (o número não muda) | 4.8 |
| Fig. 4.4 instrumentos × domínios | Fig. 4.4 (o número não muda) | 4.8 |
| Fig. 4.2 por pilar | sai | — |
| Fig. 4.5 instrumentos × DRs | sai | — |
| Tabela 4.1 funções | Tabela 4.1 | 4.2.2 |
| (nova) portas do lifecycle | Tabela 4.2 | 4.6.1 |
| Tabela 4.2 escalabilidade | Tabela 4.3 | 4.7.1 |
| (nova) registros invariantes | Tabela 4.4 | 4.7.2 |
| Tabela 4.3 instrumentos | Tabela 4.5 | 4.8 |
| Tabela 4.4 DR × componente | Tabela 4.6 | 4.8 |

As remissões no texto e as listas de figuras e de tabelas mudam junto (Ctrl+A, F9 no fim).

## 2. Novas

### Fig. 4.2: matriz instrumento × fase (DR9). Eu gero.
- **Linhas:** os 24 instrumentos agrupados por pilar, na ordem da Tabela 4.5:
  - Governance: CCDM, MRL, POT, RACI, DTRM, TRE, SCR;
  - Risk Management: SRR, SLCT, SCML, SART, CSST;
  - Operational Controls: IMP, IMC, SIRR, IQL, PSEAR, SIFSL, PFVR, ICDL;
  - Performance Oversight: PIR, FUCR, CAPA, PIDLR.
- **Colunas:** fases 1 Feasibility, 2 Start-up, 3 Enrollment, 4 Surgery, 5 Follow-up, 6 Close-out e 7 Continuous improvement, mais uma coluna para a corrente de segurança (fases 3 a 5).
- **Marcadores:** vazio = montado (preparado, regras fixadas); cheio = em uso.
- **Conteúdo:** o mapa aprovado (`mapa-instrumento-fase.md`) no formato montado / em uso. A coluna da fase 2 mostra que quase tudo é montado ali.
- **Estilo:** a mesma família visual da Fig. 4.4.

### Tabela 4.2: portas do lifecycle (Word, sem imagem)
- **Colunas:** fase | entra quando | sai quando | revisão no MRL.
- **Linhas:** as 7 fases. As fases 3 a 5 têm a fronteira do site no primeiro e no último caso.
- O conteúdo sai com o texto da 4.6.1.

### Tabela 4.4: registros invariantes (Word, sem imagem)
- **Colunas:** registro | onde fica no framework | fonte.
- **Linhas:** consentimento, delegação e treino, contabilidade do dispositivo, desvios, eventos adversos, calibração, essential records, documentos fonte.
- Cada cláusula é conferida na ISO 14155:2026 e no MDR antes de entrar. O conteúdo sai com o texto da 4.7.2.

## 3. Existentes que mudam

### Fig. 4.1 lifecycle (sua imagem)
- **Fase 2:**
  - entram o SRR (aberto antes do primeiro participante), o SLCT (base de comparação), o IMP, as regras do PIR, e o SCML, o SART e o CSST preparados (critérios e limiares);
  - a ordem passa a ser treino e liberação (DTRM, TRE) e depois credenciamento (SCR);
  - "Delegation log created, criticality codes assigned" → CCDM e RACI;
  - "PI oversight plan" → PI Oversight Template (POT).
- **Fase 1:** a análise de lacunas da imagem passa a ter o nome do instrumento (SIRR).
- **Fase 4:** entra a revisão da imagem pós-operatória imediata (IQL, DR6).
- **Fase 6:**
  - sai "Final safety report for the whole study period", que é do sponsor;
  - entra "Site safety records reconciled with the sponsor's".
- **Fase 7:** entra o PIDLR (debrief e lições).
- **Corrente de segurança:**
  - "Structured causality assessment separating device, procedure and patient factors" → "Event categorization: related to device use, to a CIP-required procedure, or to neither";
  - "recognise" → "recognize";
  - "at least monthly" fica.
- **Legenda:** deixa de prometer "entry conditions" na figura. Elas ficam na Tabela 4.2.

### Tabela 4.3 escalabilidade (antiga 4.2; sua imagem)
- **Colunas:** nonhospital (nível mínimo, centro-alvo) | nonacademic hospital | academic. Saem "Type A/B/C" e as descrições por porte ("Large or complex research hospital", "Medium private clinic/hospital", "Small surgical centre").
- **Sai** qualquer menção a pessoal dedicado, função de qualidade, "imaging liaison" e "formal multidisciplinary reviews".
- **Os 24 instrumentos em uso nos três níveis.** O que muda por coluna é a cadência, a independência da revisão e a separação ou combinação de registros.
- **"Role architecture and controlled instruments"** → "Role structure and instruments".
- **Grafia:** specialised, programme, authorisation, centre → americano.
- O SCML não pode aparecer só numa coluna.
- O conteúdo final das células sai junto com o texto da 4.7.

### Tabela 4.5 instrumentos (antiga 4.3; sua imagem)
- Cabeçalhos por pilar.
- Coluna nova "Appendix" (A a X).
- **Ordem pela primeira citação:**
  - Governance: CCDM, MRL, POT, RACI, DTRM, TRE, SCR;
  - Risk Management: SRR, SLCT, SCML, SART, CSST;
  - Operational Controls: IMP, IMC, SIRR, IQL, PSEAR, SIFSL, PFVR, ICDL;
  - Performance Oversight: PIR, FUCR, CAPA, PIDLR.
- O FUCR fica em Performance Oversight.
- O TRE tem um nome só em toda a tese: Training Record Evaluation and Release.

### Fig. 4.3 granularidade (sua imagem)
- **Legenda:** volta para "Operational Controls appears as three groups (surgery and device, enrollment, follow-up), and the safety stream appears as a row of its own". SART, SCML e CSST são de Risk Management.
- **Linha "Surgery and device":** hoje tem IMP, IMC, SIRR e IQL, que são verificação e imagem. Reagrupar ou renomear a linha.
- O FUCR passa para Performance Oversight.
- **Rodapé:** "An evidence record never depends on a synthesis or decision document existing first" é falso para o TRE. Trocar por "The evidence record is created at the event; decisions return as the requirement it is checked against".

### Fig. 4.4 instrumentos × domínios (sua imagem)
- **Regra:** marcador cheio só onde o controle do domínio é executado.
- **Domínio 11:** tirar os marcadores cheios do MRL, do PIR e do PIDLR. Pôr cheio no ICDL, no PFVR e no PSEAR.
- Rever os marcadores cheios do MRL e do PIDLR nos outros domínios.
- **PIR:** marcador no domínio 6, porque o SP-01 responde aos domínios 5 e 6.
- O FUCR fica no grupo Performance Oversight.

### Tabela 4.6 DR × componente (antiga 4.4). Eu refaço, como em 24/10.
- **Colunas novas:** instrumento(s) e fase(s).
- **DR4:** "nine review checks" → ten, com o IMP e o IMC.
- **DR6:**
  - sai "4.6.2 phase 4";
  - entram o IQL e a 4.4.2;
  - instrumentos: ICDL, SLCT, SCML, IQL.
- **DR7:** "4.5.1" → 4.4.3. Entra a qualificação de avaliadores (DTRM, TRE) junto com o SIRR, o IQL e o PSEAR.
- **DR3:** o SCR passa a apoio. O SLCT é o instrumento direto.
- **DR9:** "carries leverage" → "has most effect". Vira propriedade do conjunto ("all instruments, each assigned to its phase"), com o MRL como registro.
- **DR10:** CCDM e RACI, mais DTRM e TRE.
- **DR11:** sai "4.4.3". Fica 4.4.4 e 4.8.
- **DR12:** "three site contexts" → os três níveis da Tabela 3.3.

## 4. Pendências antigas (capítulo 3 e 4.2; suas imagens)

- **Tabela 3.1:**
  - referências do Gap 3 → [71, 72];
  - Gap 5 → ISO 14155:2026 (a obrigação de CAPA do PI) no lugar do MDR.
- **Tabela 3.2:**
  - "UDI" no domínio 4 (avaliar "batch, serial or unique device code");
  - conferir a menção a delegação no domínio 6 e o mascaramento do avaliador no domínio 8.
- **Tabela 3.4:**
  - "architecture" → framework;
  - "carries leverage" → "has most effect" (DR9);
  - rótulos das condições (depois da D3);
  - grafia americana (centre, standardised, afterwards).
- **Tabela 4.1 (funções):** "PROM workflows" → "PROM administration"; "Data QA" → "Data QA function".
