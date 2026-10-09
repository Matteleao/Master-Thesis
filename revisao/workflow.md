# Workflow de análise e revisão da tese

Este é o fluxo de uso das skills marcadas com ★, com a skill do autor (`thesis-writing`) como regra principal. O objetivo é uma **análise nova e mais completa** que o diagnóstico v1 (`revisao/diagnostico.md`) e, depois dela, a reescrita.

## Princípios

1. **A regra principal é a skill do autor.** `.claude/skills/thesis-writing/SKILL.md` está acima de todas as skills genéricas. Precedência: exigências da universidade → manual de estilo → `thesis-writing` → workshop CBM → skills genéricas (ver `revisao/guia-de-estilo.md`, seção 1). Um apontamento de skill genérica que contradiz a skill do autor é descartado automaticamente.
2. **Independência.** Cada skill roda isolada, num contexto separado, sem ver o resultado das outras. É isso que dá valor à comparação.
3. **Evidência.** Todo apontamento cita o trecho literal e a seção. Apontamento sem trecho não entra no registro. Número sem fonte nunca entra; é a regra de honestidade da skill.
4. **Triangulação.** Para cada pergunta rodam pelo menos duas lentes com métodos diferentes:
   - ✅ **Convergente**: duas ou mais lentes apontam o mesmo problema no mesmo trecho. É ponto confirmado e entra na revisão.
   - ⚖️ **Único**: só uma lente aponta. Faço uma avaliação crítica contra o texto e proponho aceitar, rejeitar (com motivo) ou deixar para você decidir.
   - ⚔️ **Conflitante**: as lentes recomendam coisas opostas. Quem decide é você.
5. **Análise não reescreve.** As Fases 1–6 só diagnosticam. O texto só muda na reescrita, depois das suas decisões.
6. **Um limite honesto.** Todas as skills rodam no mesmo modelo (eu). A independência é de **método e de contexto**, não de "cérebro". Convergência é sinal forte, não prova; por isso todo ponto é conferido contra o texto antes de entrar.

## Visão geral

```
Fase 0  Preparação ........ regras do projeto, contrato, perfil da sua voz
Fase 1  Fatos e citações .. o que está errado não se poliu
Fase 2  Argumento ......... o que fica, o que sai, o que se move
Fase 3  Coerência ......... contradições e repetições entre capítulos
Fase 4  Leitores .......... como o júri, o arguente e o especialista leem
Fase 5  Prosa ............. registro, construções proibidas, marcas de IA
Fase 6  Consolidação ...... registro único, triagem, suas decisões
         ▲
         └── Lente do autor (thesis-writing): uma auditoria completa que
             alimenta as Fases 1, 2, 3 e 5
──────────────────────────────────────────────────────────────
Reescrita (por capítulo): R1 integrar → R2 copidesque → R3 humanizer
            → R4 checklist da skill (portão) → R5 retune → R6 leitura no papel
            → R7 veredito final
```

A ordem vai **do mais profundo ao mais superficial**. Não faz sentido polir uma frase com número errado (Fase 1) ou um parágrafo que vai sair por redundância (Fase 2).

---

## Lente do autor: `thesis-writing`

Uma execução independente aplica à tese inteira a parte **Before delivering** da skill, os 25 itens, mais as seções de argumento e evidência. Os achados são distribuídos assim:

| Parte da skill | Vai para a fase |
|---|---|
| *Honesty rules*, *Verb strength*, números rastreáveis (itens 22–23) | 1, Fatos |
| *Proportionality of the claim*, *Vary the development path* (mapa de uma frase por seção), *The opposition construction* (itens 2, 3, 5) | 2, Argumento |
| Siglas, deriva de termos, remissões, um parágrafo por função (itens 17, 21, 23, 24) | 3, Coerência |
| *Cohesion*, frases curtas, trios, caudas autocomentadas, aberturas que anunciam, vocabulário previsível, registro, convenções (itens 1, 4, 6–16, 18–20, 25) | 5, Prosa |

É a lente de referência: nas comparações, ela conta como uma fonte, e quando entra em conflito com uma skill genérica, ela vence.

## Fase 0: preparação

| Passo | Skill | O que faz | Por que vem aqui |
|---|---|---|---|
| 0.1 | `ghost-writer:rules` | Converte a skill `thesis-writing` e a terminologia fixa do guia em `style-rules.md`. | É o regulamento que `revise` e `integrate` aplicam depois; precisa existir antes. |
| 0.2 | Projeto `ghost-writer` + contrato `apodictic` | Cria `book.config.json` (leitor-alvo: júri; respostas em português) e o contrato APODICTIC (forma: argumento acadêmico/tese; leitor: júri; exigência alta; preocupações: tom, coerência, redundância). | Dependência técnica: as skills dos dois pacotes não rodam sem esses arquivos. |
| 0.3 | `ghost-writer:setup-voice` ⇄ `humanize-kit:voice-profiler` | Os dois montam um perfil da **sua** voz a partir de 3–5 textos seus escritos **sem IA**. Os perfis são comparados entre si e com a *governing instruction* da skill (prosa B2–C1, plana e precisa). | Só é necessário na reescrita, então roda em paralelo com as Fases 1–5. **Depende de você mandar as amostras.** |

## Fase 1: fatos, números e citações

| Lente | O que faz |
|---|---|
| `apodictic:research-verification` (`citation-verifier` + `fact-check`) | Confere se cada referência existe e se diz o que a tese afirma; confere números e datas. |
| `thesis-writing` (honestidade, força dos verbos) | Confere se cada número é rastreável e se o verbo combina com a força da evidência (*demonstrates* × *suggests* × *is consistent with*). Separa o que o trabalho demonstrou do que foi feito para permitir e do que é só benefício esperado. |

Comparadas também com a persona *domain-expert* (Fase 4) e com os itens F1–F12 do diagnóstico v1.
**Por que primeiro:** o APODICTIC exige verificação de citações **antes** da análise em textos de alto risco, e já achamos referências trocadas nas tabelas (F2, F3).
**Limite:** ISO 14155, ICH e normas pagas não podem ser lidas online. As cláusulas citadas ficam marcadas "não verificável" para você conferir no PDF da norma.

## Fase 2: argumento e estrutura

| | Lente | O que faz |
|---|---|---|
| 2A | `apodictic:nonfiction-argument-engine` (via `core-editor`) | Passes 0, 1, 2, 5 e 8 + *Dialectical Clarity* + *Argument Red Team* + *Evidence Deep-Dive*, e também a *Argument Persuasion* usada na Fase 4. Gera a carta editorial, o registro de achados e o `Argument_State.md` (tese central → subteses → evidências). |
| 2B | `ghost-writer:demolish` (modo análise) | Crítica hostil por capítulo nas 7 categorias de vulnerabilidade. Na análise ele **lista**; o diálogo um-a-um fica para a Fase 6. |
| 2C | `thesis-writing` (parte argumento) | Proporcionalidade das afirmações, quantificadores absolutos sem escopo, construções de oposição, e o mapa do caminho de desenvolvimento de cada seção (duas seções vizinhas com o mesmo caminho = uma é reescrita). |

**Triangulação:** 2A × 2B × 2C.
**Por que aqui:** a estrutura decide o que fica. É nesta fase que se resolve, por exemplo, se a 5.2 continua repetindo a 1.4.

## Fase 3: coerência entre capítulos

| Lente | O que faz |
|---|---|
| `ghost-writer:consistency-check` | Termos que mudam de nome, contradições, promessas não cumpridas, exemplos e dados repetidos. |
| `thesis-writing` (terminologia e remissões) | *One object, one name*, siglas nunca voltando à forma por extenso, toda remissão apontando para algo que existe na numeração atual. |

Comparadas também com os itens C e R do diagnóstico v1 e com o passe de continuidade do APODICTIC (2A).
**Por que depois da 2:** parte das incoerências é sintoma de problema de estrutura que a Fase 2 já explica.

## Fase 4: leitores

| | Lente | Leitor |
|---|---|---|
| 4A | `ghost-writer:review` (5 × `demolish-persona`) | **Editor**: estrutura e prosa.<br>**Leitor-alvo**: orientadora e júri.<br>**Leitor hostil**: o **arguente** da defesa.<br>**Especialista**: regulatory affairs / qualidade clínica de dispositivos médicos.<br>**Fora do público**: engenheiro sem experiência em pesquisa clínica. |
| 4B | `apodictic:argument-audits` → `argument-persuasion` (na mesma execução da 2A) | Matriz de públicos: para quem cada parte do argumento funciona e para quem não funciona. |

**Triangulação:** 4A × 4B.
**Por que aqui:** o ghost-writer recomenda as leituras por persona **depois** que o argumento já foi testado.

## Fase 5: prosa

| | Lente | O que faz |
|---|---|---|
| 5A | `thesis-writing` (parte prosa) | A lente de referência. Coesão e cadeias de consequência primeiro; depois as construções proibidas (oposições, caudas autocomentadas, aberturas que anunciam, aforismos, clefts, particípios antepostos), trios, frases curtas, vocabulário previsível, registro B2–C1 e convenções. Mede a **dispersão** do tamanho das frases e dos parágrafos, nunca a média. |
| 5B | `apodictic:prose-measurements` (`ai-prose` + `argument-decision`) | Diagnóstico de prosa com cara de IA por categorias. As medições automáticas do SETEC não estão instaladas, então uso as contagens próprias. |
| 5C | `humanizer` (só a etapa de marcação) | Marca os padrões da lista *Signs of AI writing*. **Não reescreve nesta fase.** |
| 5D | `ghost-writer:revise` | Copidesque contra o `style-rules.md`: gramática, pontuação, números, nomes e dados que mudam entre capítulos. |
| 5E | `writing-skills:orwells-rules` + `plain-language` | Checklists de clareza. **Subordinados à skill do autor:** não valem teto de palavras, "you", meta de passiva nem troca de termo técnico. Só contam como fonte de convergência; sozinhos, nunca geram mudança. |

**Triangulação:** 5A × 5B × 5C (registro e marcas de IA) e 5A × 5D × 5E (gramática e estilo).
**Por que por último na análise:** a prosa é a camada mais superficial e muda com as decisões das fases anteriores.

## Fase 6: consolidação e decisão

| Passo | Skill | O que faz |
|---|---|---|
| 6.1 | (eu) | Junto tudo num registro único e aplico a triangulação ✅ ⚖️ ⚔️. |
| 6.2 | `apodictic:triage-feedback` | Classifica cada ponto em **Must-Fix / Should-Fix / Could-Fix** e valida contra o texto. |
| 6.3 | Você, no protocolo do `ghost-writer:demolish` | Você decide os pontos ⚖️ e ⚔️, um de cada vez ou em lote por capítulo. |

Saídas: `revisao/analise-v2/registro.md` (o registro completo) e `revisao/analise-v2/relatorio.md` (o resumo). O relatório fecha com um resumo numerado das ações e as perguntas em sequência, como pede a skill.

### Formato do registro

| ID | Fase | Lente | Seção | Trecho (literal) | Problema | Tipo | Severidade | Triangulação | Decisão |
|---|---|---|---|---|---|---|---|---|---|
| A-017 | 2 | apodictic | 5.1 | "ISO 13485, ISO 14971, and ISO 15189 each require…" | Contradiz a 2.5.1 sobre a origem dos pilares | C | Must | ✅ (2A, 3, v1) | aceito |

Tipos: [F] fato, [C] coerência, [R] redundância, [A] argumento, [L] leitor, [T] tom, [G] gramática, [E] estilo.

---

## Reescrita (depois das decisões, um capítulo por vez)

| Passo | Skill | O que faz |
|---|---|---|
| R1 | `ghost-writer:integrate` | Aplica as decisões aceitas, uma por vez, com a sua aprovação, seguindo a skill do autor. |
| R2 | `ghost-writer:revise` | Copidesque do capítulo contra o `style-rules.md`. |
| R3 | `humanizer` | Passe de marcas de IA, usando o perfil da sua voz (Fase 0.3) como referência. Nunca acrescenta fato, número ou fonte. |
| R4 | `thesis-writing`, **portão** | Os 25 itens do *Before delivering*, coesão primeiro. O capítulo só é entregue se passar. Os números do antes e do depois (dispersão de frases, oposições, trios, caudas) ficam registrados, mas não são apresentados como conquista. |
| R5 | `ghost-writer:retune` | Quando você ler e disser "isso não soa como eu": você diz como falaria e eu reajusto. |
| R6 | `ghost-writer:corrections` | PDF com os parágrafos numerados para você ler longe do computador; suas anotações, até em áudio ou foto, voltam pra cá. |
| R7 | `ghost-writer:consistency-check` + `apodictic:ready` | No fim, com a tese inteira: checagem de coerência e o veredito de prontidão para entrega. |

**Entrega:** `.docx` justificado, recuo de primeira linha de 720 twips, sem linha em branco entre parágrafos, estilos Heading 1 e Heading 2, com controle de alterações.
**Ordem dos capítulos:** 2 → 3 → 1 → 4 → 5 → 6 → Abstract e Resumo (estes por último, porque resumem o corpo já revisado).

---

## Lentes por pergunta (resumo)

| Pergunta | Lente do autor | Lente A | Lente B | Outra fonte |
|---|---|---|---|---|
| Os fatos e as citações estão certos? | honestidade, força dos verbos | research-verification | persona *domain-expert* | diagnóstico v1 (F) |
| O argumento se sustenta? | proporcionalidade, oposições, caminhos | nonfiction-argument-engine | demolish | — |
| Os capítulos se contradizem ou se repetem? | terminologia, siglas, remissões | consistency-check | continuidade do APODICTIC | diagnóstico v1 (C, R) |
| Como o júri e o arguente leem? | — | review (5 personas) | argument-persuasion | — |
| O texto soa como IA ou como ensaio? | prosa, coesão, trios, caudas | prose-measurements | humanizer | — |
| A gramática e as convenções estão certas? | gramática, mecânica, convenções | revise | orwells-rules + plain-language | — |
| Qual é a sua voz? | *governing instruction* | setup-voice | voice-profiler | — |

## O que ficou de fora, e por quê

- **`humanize-kit:humanize`**: foi feita para driblar detectores de IA, e o próprio material do kit recomenda redigitar o texto para passar nos classificadores. Numa tese com declaração de autoria e o Código de Conduta da ULisboa, isso é risco de integridade acadêmica, e a skill do autor, o `humanizer` e o `retune` já cobrem a qualidade e a voz. O **`voice-profiler`** do mesmo kit entra normalmente.
- **`humanize-ig`**: é para legendas de Instagram.
- **`scott-adams`**: ganchos de abertura contradizem a regra da skill de abrir pela substância.
- **Skills de ficção ou de criação de livro do zero** (enredo, personagem, `write`, `write-opening`…): a tese já existe e não é ficção.

## Execução e custo

A análise são **10 execuções independentes**, cada uma lendo a tese inteira (~55 mil tokens) mais o protocolo da skill:

1. `research-verification`
2. `apodictic` (motor de argumento + `argument-persuasion`)
3. `demolish`
4. `consistency-check`
5. `review` (as 5 personas)
6. `prose-measurements`
7. `humanizer` (marcação)
8. `revise`
9. `orwells-rules` + `plain-language`
10. `thesis-writing` (lente do autor)

Cada execução roda como um agente separado, em paralelo, e eu faço a Fase 6 com os resultados. Custo estimado, ondas e esforço por lente: ver `revisao/fase-0-preparacao.md`, seção D (análise completa em torno de US$ 30–60).
