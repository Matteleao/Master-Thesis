# Guia de estilo da revisão

Estas são as regras que uso para revisar a tese. Elas vêm de três fontes:

1. **Workshop CBM**: *Writing a clear scientific message*, da Dra. Carolina Borges Merjane (`original/Roche_workshop-CBM_script_removed.pdf`).
2. **Skills de escrita instaladas**: `writing-skills:orwells-rules` e `writing-skills:plain-language` para clareza; `apodictic` (*AI-prose calibration*) e `ghost-writer:consistency-check` para padrões de texto de IA e coerência entre capítulos.
3. **O que a própria tese já faz bem**: onde o texto já tem uma convenção estável, eu sigo a convenção e não invento outra.

A regra que está acima de todas é a do workshop: *"Can a knowledgeable reader understand exactly what I mean on the first reading, with no ambiguity?"* Quando uma regra deixa o texto mais rígido ou menos preciso, a clareza ganha (é a "regra 6" de Orwell).

---

## Parte A: gramática (workshop CBM)

### A1. Voz ativa
- Prefira a voz ativa com sujeito explícito: *"We compared…"*, *"ISO 14155:2026 assigns…"*, *"Table 3.1 lists…"*.
- A passiva é aceitável nos Métodos quando o agente é óbvio ou irrelevante (*"Facility names were normalized"*).
- Evite a passiva que esconde quem interpreta: *"It is suggested that…"* → *"We suggest that…"* ou *"Our results suggest…"*.
- Tabelas e figuras são sujeito no presente: *"Table 4.1 maps…"*, e não *"…is mapped in Table 4.1"*.

### A2. Tempos verbais (pela função da frase)
| Função | Tempo | Exemplo na tese |
|---|---|---|
| O que fizemos ou encontramos | passado simples | *"We searched…"*, *"The analysis identified five gaps"* |
| Conhecimento estabelecido, o que as normas dizem | presente simples | *"ISO 14155:2026 places clinical quality management in Clause 9"* |
| Interpretação dos resultados (Discussão) | presente simples | *"These findings indicate…"* |
| Estudos anteriores com relevância atual | *present perfect* | *"Several studies have described site-level quality management as reactive"* |
| Sequência de eventos passados | *past perfect* | *"…after the research for this thesis had started"* |
| Referência a tabela ou figura | presente simples | *"Figure 4.1 shows…"* |

Também é preciso evitar trocar de tempo dentro da mesma frase, como em *"sites would find problems … and then corrected them"*.

### A3. Menos preposições
- Troque nominalizações por verbos: *"performed an analysis of"* → *"analyzed"*.
- Quebre cadeias de *of*: *"the analysis of the effect of the treatment on the growth of…"*.
- Use o adjetivo ou substantivo atributivo quando ficar claro: *"the cells in the liver"* → *"liver cells"*, sem empilhar mais de três substantivos.

### A4. Menos modificadores
- Corte intensificadores vazios: *genuinely*, *substantially*, *materially*, *exactly*, *directly*, *clearly*, *particularly*.
- Troque o modificador pelo dado quando ele existir (*"a substantial registry base"* → *"996 records"*).
- Não empilhe modificadores.

### A5. Pontuação
- Vírgula serial (de Oxford) **sempre**: *"temperature, pH, and cell density"*.
- Ponto e vírgula só entre orações independentes muito ligadas. Na dúvida, use ponto final.
- Travessão (—): evitar no corpo do texto.
- Hífen em modificadores compostos **antes** do substantivo (*"a site-level framework"*, *"day-to-day operations"*) e sem hífen depois dele (*"at site level"*).
- Prefixos sem hífen, salvo vogal dupla ou ambiguidade: *nonhospital*, *nonacademic*, *interobserver*, *preclinical*, mas *re-consent*, *anti-inflammatory*.
- Sem contrações e sem ponto de exclamação.

## Parte B: estilo (workshop CBM)

### B1. Fio narrativo
Pergunta → métodos → resultados → conclusões. Cada parágrafo tem uma função e começa por ela. Cada seção diz o que entrega e entrega isso, sem repetir o que outra seção já entregou.

### B2. Frases
- Uma ideia por frase. **Teto suave de 30 palavras**; acima de 35, a frase deve ser dividida, a não ser que seja uma lista.
- Concordância: *data are*, *criteria are*, *the team was*, *a total of 46 investigations were*.
- Nada de particípio solto (*dangling participle*): *"Using the registry, 235 organizations were identified"* → *"Using the registry, we identified 235 organizations"*.
- *Respectively* só para pareamento em ordem, no fim da oração.

### B3. Ortografia: inglês americano
O corpo da tese já é americano (*center*, *orthopedic*, *standardized*, *enrollment*, *analyze*). Ficam como estão:
- nomes próprios: *International Council for **Harmonisation***, *ROMIO (**Randomised** Oesophagectomy…)*;
- títulos de referências, que mantêm a grafia publicada.

O que precisa ser uniformizado: *orthopaedic* (2×) e as **tabelas e figuras em imagem**, que usam grafia britânica (*centre*, *standardised*, *programme*, *authorisation*, *enrolment*, *recognise*, *theatre*, *afterwards*).

### B4. Números
- Algarismos para medidas, dados e estatística (*46 investigations*, *27.7%*, *p = 0.03*).
- Por extenso de um a nove no texto corrido (*five gaps*, *seven phases*, *four pillars*).
- **Algarismos de 10 para cima** (*12 domains*, *24 instruments*, *12 design requirements*). Hoje a tese alterna entre *twenty-four* e *24*.
- Nunca começar frase com algarismo (*"Sixty of the 65…"*).
- O mesmo formato para valores comparáveis na mesma frase.
- Ponto decimal (27.7%) e vírgula de milhar (1,111).

### B5. Maiúsculas
- Com maiúscula quando numerado: *Section 3.2*, *Table 4.1*, *Figure 4.1*, *Chapter 3*, *Appendix A*, *Phase 2*, *Clause 10.3*.
- Pilares e instrumentos com maiúscula, porque são nomes próprios do framework: *Governance*, *Risk Management*, *Site Risk Register*.
- Métodos e conceitos comuns em minúscula: *failure mode and effects analysis*, *risk-based monitoring*.
- **Títulos de seção:** um só padrão. Proponho *sentence case* (*"1.1 Historical overview and recent updates"*), que já é a maioria nos níveis 2 e 3.

### B6. Abreviaturas
- Definir na primeira ocorrência do corpo do texto (o Abstract conta à parte) e **depois usar sempre a sigla**.
- Não redefinir: ISO e MDR estão definidas duas ou três vezes.
- Não alternar: *CtQ* aparece 43× e *Critical-to-Quality* por extenso 8×; *PI* e *principal investigator*; *CAPA* e *corrective and preventive action*; *CIP*, *CRO*, *RBM* e *AE*, todos nas duas formas.
- Siglas dos 24 instrumentos: no texto corrido, use o nome do instrumento (*the Site Risk Register*). As siglas ficam nas tabelas e figuras, como pede o workshop: *"Readers should not need a glossary to follow your paper"*.

## Parte C: terminologia fixa da tese

Esta é a tabela que trava a consistência. As decisões marcadas com ⚠️ precisam do seu OK.

| Conceito | Forma única | Hoje aparece também como |
|---|---|---|
| O artefato inteiro | **framework** | *architecture*, *model*, *quality architecture* (Abstract e Resumo falam em "architecture"/"arquitetura"; o título diz "Framework") ⚠️ |
| Pilar 2 | **Risk Management** | *RBQM* (Abstract, Seção 2.5.1, Resumo) |
| As cinco condições estruturais (Seções 1.3, 3.4.1 e 5.3) | ⚠️ *irreversibility*, *operator dependence*, *unit-level traceability*, *follow-up burden*, *measurement reliability* | *persistent traceability*, *the operational weight of follow-up*, *limited classification reliability* |
| Instrumento de curva de aprendizagem | **Surgeon Learning Curve Tracking Log** | *Surgical Learning Curve Tracking*, *learning curve log*, *learning-curve log* |
| Instrumento de supervisão do PI | **PI Oversight Template** | *PI Oversight Plan* (Tabela 4.1), *oversight plan* |
| Instrumento de treinamento | **Training Record Evaluation and Release** | *…and Training Release* (Figura 4.2) |
| Resultado relatado pelo paciente | ⚠️ **PROM** (*patient-reported outcome measure*) | *PRO*, *PROs*, *PROMs* |
| Partes de normas | ISO → *Clause*; ICH → *Section*; MDR → *Article* / *Annex XV, Chapter II, Section 3.x* | *ISO 14155:2026 Section 6.2*, *Section 9.1(b)*, *ISO 13485 Sections 8.5.2* |
| Formato de subcláusula | *Clause 9.2.4.5(p)* | *9.2.4.5 p)* |
| Brochura | **Investigator's Brochure** | *Investigator Brochure* |
| Citação de autores | *Peffers et al.* | *Diani and colleagues*, *Adams and colleagues* |
| Citações | **[1, 2]** em texto normal | subscrito no .docx, e algumas sem subscrito ([1], [76]) |
| Centro | *site* (genérico); *target center* (o centro-alvo) | *centre* nas tabelas |
| Prefixos | *nonhospital*, *nonacademic*, *interobserver* ⚠️ | *non-hospital*, *non hospital*, *non-academic*, *inter-observer* |

## Parte D: padrões de "texto de IA" a evitar

A tese é tecnicamente sólida, mas tem marcas típicas de texto gerado ou polido por modelo de linguagem. O protocolo *AI-prose calibration* do `apodictic` chama isso de **fluência sem atrito**: frases corretas que qualquer paráfrase substituiria sem perda. Estes são os padrões que achei e o que fazer com cada um.

| # | Padrão | Exemplos na tese | Tratamento |
|---|---|---|---|
| D1 | **Molde "X is harder than…"** | *"Turning that principle into a workable schedule is harder than it sounds"*, *"Doing this well is harder than listing…"*, *"Building that evidence is harder than…"*, *"Executing that review well is harder than scheduling it"*, *"Closing that interval is harder than…"*, *"The harder question is…"*, *"The harder task is…"* (7×, quase todos no Cap. 4) | Dizer qual é a dificuldade, sem o molde. No máximo uma vez na tese. |
| D2 | **Correctio ("não é X, é Y")** | *"What is missing is not a rule. It is a layer"*; *"These five gaps are not defects…"*; *"Paper is the floor of the design, not its endpoint"* | Afirmar Y diretamente. Guardar a forma para um ou dois momentos que realmente precisam dela. |
| D3 | **Aforismo de fecho de parágrafo** | *"Verification comes too late."*; *"A control that the site never executes protects no one…"*; *"What the protocol cannot standardize, the site has to govern."* | No máximo um por seção. Os outros viram afirmação comum ou saem. |
| D4 | **Palavras-muleta** | *therefore* (60×), *itself* (36×), *", which is"* (27×), *genuine/genuinely* (6×), *the one…* | Cortar onde a lógica já é óbvia; variar o conector ou reestruturar a frase. |
| D5 | **Ressalva defensiva repetida** | *"This is a result limited to…, not proof that…"*, *"…is a hypothesis we did not test"*, *"Nobody has demonstrated…"* (repetido nas Seções 2.2, 3.2, 4.x, 5.x) | Juntar as ressalvas nas Seções 2.6 e 5.7 e deixar no corpo só a que muda a leitura da frase. |
| D6 | **Metacomentário de rascunho** | *"our earlier set of five indicators"* (4.5); *"an extension added to the original set"* e *"inherited from … an earlier instrument"* (Figura 4.5); *"We have not recalculated the median…"* (5.7); *"Section 3.4.4 has to state which of the two governs the argument"* (5.7) | Remover. São notas de trabalho que ficaram no texto. |
| D7 | **Abstração personificada** | *"The comparison does more than describe the gap"*; *"the operational architecture that the instruments would be glad the site has"* | Devolver o agente humano: *"We…"*, ou o documento como sujeito literal. |
| D8 | **Eco de estrutura** | Parágrafos seguidos que abrem com *"Whether…"*, *"Nobody…"*, *"A site that…"*; listas sempre em trios | Variar a abertura e usar o número de itens que existe, sem forçar o trio. |
| D9 | **Frases longas encadeadas** | Caps. 4 e 5: média de 22–24 palavras por frase e ~100 frases com mais de 35 palavras | Dividir. Mirar a média em 18–20, com variação natural de tamanho. |
| D10 | **Costura de registro** (*register seam*) | O Cap. 2 tem frases informais ou quebradas (*"Although very important their main focus is still mainly drug investigational products, so we needed to go after…"*), e os Caps. 4 e 5 têm prosa lisa e longa | Levar tudo para o mesmo registro: acadêmico, direto, com "we", sem coloquialismo e sem floreio. |

O que torna o texto mais humano, nesta tese:
- **Tomar posição** com o dado na mão. A tese já faz isso bem na comparação com a *Clinical Trial Site Performance Measure*: *"A reader who asks which set is better evidenced should prefer the validated one"*.
- **Ser concreto**: um número, uma cláusula, um exemplo do ombro, no lugar da formulação geral.
- **Variar o ritmo**: frases curtas ao lado de médias, e nem todo parágrafo fechando com uma sentença de efeito.

## Parte E: como cada mudança é marcada

Toda alteração proposta leva um código:

| Código | Tipo |
|---|---|
| **[F]** | Fato, número ou referência (precisa da sua confirmação) |
| **[C]** | Coerência entre seções (contradição, remissão errada) |
| **[R]** | Redundância (texto repetido em outra seção) |
| **[T]** | Tom (padrões da Parte D, registro) |
| **[G]** | Gramática (Parte A) |
| **[E]** | Estilo e convenções (Partes B e C) |

Mudanças **[F]** nunca entram sem você confirmar. O conteúdo técnico e o argumento são seus. A revisão mexe em **como** as coisas são ditas, e quando acha um problema de conteúdo, aponta.
