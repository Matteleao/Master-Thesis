# Guia de estilo da revisão

A regra principal da revisão é a **skill do autor**, `thesis-writing`: `.claude/skills/thesis-writing/SKILL.md`. O Felipe escreveu essa skill a partir do workshop CBM, e ela tem três partes: prosa científica, estrutura do argumento, evidência e entrega.

Este guia não repete a skill. Ele guarda só o que é **específico desta tese**:
1. a ordem de precedência entre as regras;
2. os conflitos entre a skill e as outras skills, já resolvidos;
3. a terminologia fixa;
4. os padrões que encontrei no texto, ligados à regra correspondente;
5. os códigos usados para marcar cada mudança.

---

## 1. Precedência

Segue a seção *Rule precedence* da skill:

1. Exigências da Universidade de Lisboa, da faculdade e do mestrado.
2. O manual de estilo escolhido para as referências (Vancouver, se for o padrão do curso).
3. **`thesis-writing`, a skill do autor.**
4. Workshop CBM (`original/Roche_workshop-CBM_script_removed.pdf`), que é a fonte da skill. Uso onde a skill não fala.
5. Skills genéricas: `orwells-rules`, `plain-language`, `humanizer` e as auditorias de prosa do `apodictic`. Servem **só como lentes de detecção**. Uma regra delas nunca se sobrepõe às dos níveis 1–4.
6. Onde ainda sobrarem duas opções válidas, escolho uma e mantenho igual na tese inteira.

## 2. Conflitos resolvidos

Estes pontos do meu guia v1 e das skills genéricas batem de frente com a skill do autor. A skill do autor vence.

| Regra conflitante | De onde vinha | O que vale |
|---|---|---|
| Teto de 30 palavras por frase; média-alvo de 18–20 | meu guia v1 | **Sem teto e sem média.** A frase tem o tamanho que a ideia pede. O que se mede é a **dispersão** (desvio-padrão, frase mais longa), e só como diagnóstico. Frase longa só é defeito quando obriga a reler. |
| Frases com até 25 palavras; Flesch ≥ 60 | `plain-language` | Descartado pelo mesmo motivo. |
| *therefore* como palavra-muleta (60×) | meu guia v1 | *therefore* é conector de consequência legítimo. A skill **pede** que cadeias de consequência sejam ligadas e fechem com um conector. O defeito é outro: o mesmo conector abrir dois parágrafos na mesma seção, ou um conector que não marca consequência nenhuma. |
| Falar com o leitor por "you" | `plain-language` | Proibida a segunda pessoa. |
| Passiva abaixo de 10% das frases | `orwells-rules` | Passiva permitida onde a ação ou o objeto importam mais que o agente (Métodos). Nunca alternar a voz para o mesmo agente em frases vizinhas. |
| "we" em todos os capítulos | meu guia v1 | **Introdução em terceira pessoa impessoal**, sem "we". **Da Metodologia em diante**, primeira pessoa do plural. |
| Ponto e vírgula entre orações independentes ligadas | meu guia v1 | Ponto e vírgula **só** dentro de parênteses de citação ou em itens de lista complexos. No resto, ponto final. |
| Trocar travessão por dois-pontos ou parênteses | `humanizer` | Dois-pontos no meio da frase só antes de lista, exemplo ou definição genuínos, depois de uma afirmação completa. Na prática, ponto ou vírgula. |
| Abrir com uma frase que gera curiosidade | `scott-adams` | Fora: o parágrafo começa pela substância. |
| Trocar palavra técnica por palavra simples | `orwells-rules`, `plain-language` | Termo definido, regulatório ou técnico fica **exato**, mesmo quando existe palavra mais simples ("one object, one name"). A simplificação vale para o vocabulário de ligação e de descrição ao redor. |
| Retirar a frase *"We have not recalculated the median…"* (P4) | meu diagnóstico v1 | É a aplicação deliberada da regra de honestidade da skill (o *worked case* dela). Fica a decisão: **calcular** a mediana a partir dos seus dados do registro, o que é o melhor, ou reescrever a frase sem o tom de nota de trabalho. Inventar um número nunca é opção. |

## 3. Terminologia fixa da tese

A regra da skill é *"One object, one name"*. Os itens ⚠️ ainda esperam a sua decisão; os ✔ já estão decididos pela skill.

| Conceito | Forma única | Hoje aparece também como |
|---|---|---|
| O artefato inteiro | ⚠️ **framework** | *architecture*, *model*, *quality architecture* (Abstract e Resumo falam em "architecture"/"arquitetura"; o título diz "Framework") |
| Pilar 2 | ⚠️ **Risk Management** | *RBQM* (Abstract, Seção 2.5.1, Resumo) |
| As cinco condições estruturais | ⚠️ *irreversibility*, *operator dependence*, *unit-level traceability*, *follow-up burden*, *measurement reliability* | *persistent traceability*, *the operational weight of follow-up*, *limited classification reliability* |
| Resultado relatado pelo paciente | ⚠️ **PROM** | *PRO*, *PROs*, *PROMs* |
| Instrumentos | Nome exato da Tabela 4.4: *Surgeon Learning Curve Tracking Log*, *PI Oversight Template*, *Training Record Evaluation and Release* | *Surgical Learning Curve Tracking*, *learning curve log*, *PI Oversight Plan*, *…and Training Release* |
| Partes de normas | ISO → *Clause*; ICH → *Section*; MDR → *Article* / *Annex XV, Chapter II, Section 3.x*; formato *Clause 9.2.4.5(p)* | *ISO 14155:2026 Section 6.2*, *9.2.4.5 p)* |
| Brochura | *Investigator's Brochure* | *Investigator Brochure* |
| Citação de autores | *Peffers et al.* | *Diani and colleagues*, *Adams and colleagues* |
| Citações | [1, 2] em texto normal | subscrito no .docx nos Caps. 1–4 |
| ✔ Ortografia | Inglês americano; nomes próprios mantêm a grafia oficial (*International Council for Harmonisation*) | *orthopaedic* (2×), grafia britânica nas tabelas em imagem |
| ✔ Prefixos | Sem hífen: *nonhospital*, *nonacademic*, *interobserver*, *predefined*, *intraoperative*. Exceção: termos regulatórios consagrados (*post-market clinical follow-up*) | *non-hospital*, *non hospital*, *non-academic*, *inter-observer* |
| ✔ Números | Algarismos para dados e valores (*12 domains*, *24 instruments*, *89%*); por extenso de um a nove no texto corrido; nunca começar frase com algarismo | *twenty-four*, *twelve* por extenso |
| ✔ Siglas | Definir na primeira menção e nunca mais voltar à forma por extenso | *Critical-to-Quality* 8× após a definição, *principal investigator*, *CAPA*/*corrective and preventive action* etc. |

## 4. Padrões encontrados nesta tese → regra da skill

Estes exemplos saem do texto atual. A seção da skill indica qual regra cada um viola.

| Padrão nesta tese | Exemplos | Regra da skill |
|---|---|---|
| **Construção de oposição** e seus disfarces | *"What is missing is not a rule. It is a layer."*; *"Paper is the floor of the design, not its endpoint"*; *"These are general functions, not required positions"*. São 18 casos de *", not X"* e 5 de *"not X. It is Y"*. | *The opposition construction*; *`rather than` and every disguise of it* |
| **Molde de frase feita para soar bem** | *"X is harder than it sounds/than Y"* (7×, quase todos no Cap. 4) | *Two tests before delivering* ("Does any sentence exist because it sounded good?") |
| **Aforismo e fecho que repete** | *"Verification comes too late."*; *"A control that the site never executes protects no one…"*; *"What the protocol cannot standardize, the site has to govern."* | *A closing sentence that merely repeats…*; *Aphorism and epigram* |
| **Cauda autocomentada** | Candidatos: *", and this/that/it …"* (55) e *", which is the …"* (14), a maioria nos Caps. 4 e 5. É preciso conferir caso a caso: a busca dá candidatos, não veredito. | *The self-commenting tail* |
| **Trios por cadência** | Em todo o texto, com concentração no Cap. 4 (a contagem automática dá centenas de candidatos, inclusive listas legítimas de 4 ou mais itens) | *Grouping: the list of three is a default shape* |
| **Frases curtas enfáticas em sequência** | *"Verification comes too late."* (3.4.3), *"The difference matters in practice."* (1.1); 26–29 frases com menos de 8 palavras por capítulo nos Caps. 2–4 | *Short assertive sentences* (primeiro ligar, depois testar se dá para apagar) |
| **Afirmação maior que a evidência** | *"so nothing in the framework is invented"* (3.5); *"No standard tells an investigational site how to run a quality system"* (3.2.1) | *Proportionality of the claim* |
| **Metacomentário e história do rascunho** | *"our earlier set of five indicators"* (4.5); legenda da Figura 4.5 (*"earlier instrument"*, *"original set"*); *"Section 3.4.4 has to state…"* (5.7) | *Meta-commentary about the writing* |
| **Abertura que anuncia** | *"Two findings limit what this work has achieved."* (1.4.1); *"Three limitations apply to the work as a whole."* (2.6); *"Nine checks define the scope…"* (4.4.1) | *The announcing opener* |
| **"we" na Introdução** | *"Within this context, we narrowed the work…"* (1.3) | *Fixed conventions* (Introdução impessoal) |
| **Ponto e vírgula fora de citação** | 21 ocorrências (Cap. 4: 10) | *Punctuation* |
| **Costura de registro** | Cap. 2 informal e com frases quebradas; Caps. 4 e 5 lisos e longos | *The governing instruction* (prosa B2–C1, plana, precisa) |
| **Repetição do mesmo caminho de desenvolvimento** | interpretação convencional → rejeição → reformulação → consequência, em seções vizinhas dos Caps. 4 e 5 | *Vary the development path* |

Já estão em zero na versão atual: *rather than*, *instead of*, *and not*, *Taken together*, travessões, contrações.

## 5. Códigos de cada mudança

| Código | Tipo |
|---|---|
| **[F]** | Fato, número ou referência (precisa da sua confirmação) |
| **[C]** | Coerência entre seções |
| **[R]** | Redundância |
| **[A]** | Estrutura do argumento (oposição, caminho de desenvolvimento, proporcionalidade) |
| **[T]** | Tom e registro |
| **[G]** | Gramática e mecânica |
| **[E]** | Estilo e convenções |

Mudanças **[F]** nunca entram sem você confirmar. A skill é explícita: nunca inventar número, citação, fonte, ano ou precisão.

## 6. Convenções de entrega

Seguem *Document conventions for deliverables* e *How to report* da skill:
- **Arquivos:** `.docx`, justificado, recuo de primeira linha de 720 twips, sem linha em branco entre parágrafos, estilos Heading 1 e Heading 2 do Word.
- **Idioma:** respostas para você em português; texto acadêmico em inglês.
- **Fechamento de cada entrega:** resumo numerado das ações e perguntas em sequência.
- **Plano:** o plano é discutido e fechado antes de qualquer arquivo ser gerado.
