# Workflow de análise e revisão da tese

Este é o fluxo de uso das skills marcadas com ★. O objetivo é uma **análise nova e mais completa** que o diagnóstico v1 (`revisao/diagnostico.md`) e, depois dela, a reescrita.

## Princípios

1. **Independência.** Cada skill roda isolada, num contexto separado, sem ver o resultado das outras. É isso que dá valor à comparação.
2. **Evidência.** Todo apontamento cita o trecho literal e a seção. Apontamento sem trecho não entra no registro.
3. **Triangulação.** Para cada pergunta (o argumento se sustenta? os capítulos se contradizem? o texto soa como IA?) rodam pelo menos duas skills com métodos diferentes:
   - ✅ **Convergente**: duas ou mais skills apontam o mesmo problema no mesmo trecho. É ponto confirmado e entra na revisão.
   - ⚖️ **Único**: só uma skill aponta. Faço uma avaliação crítica contra o texto e proponho aceitar, rejeitar (com motivo) ou deixar para você decidir.
   - ⚔️ **Conflitante**: as skills recomendam coisas opostas (ex.: uma manda cortar, outra manda acrescentar justificativa). Quem decide é você.
4. **Análise não reescreve.** As Fases 1–6 só diagnosticam. O texto só muda na reescrita, depois das suas decisões.
5. **Um limite honesto.** Todas as skills rodam no mesmo modelo (eu). A independência é de **método e de contexto**, não de "cérebro". Convergência é um sinal forte, mas não é prova; por isso todo ponto, convergente ou não, é conferido contra o texto antes de entrar.

## Visão geral

```
Fase 0  Preparação ........ regras, projeto, perfil da sua voz
Fase 1  Fatos e citações .. o que está errado não se poliu
Fase 2  Argumento ......... o que fica, o que sai, o que se move
Fase 3  Coerência ......... contradições e repetições entre capítulos
Fase 4  Leitores .......... como o júri, o arguente e o especialista leem
Fase 5  Prosa ............. marcas de IA, estilo, gramática
Fase 6  Consolidação ...... registro único, triagem, suas decisões
──────────────────────────────────────────────────────────────
Reescrita (por capítulo): R1 integrar → R2 copidesque → R3 humanizer
                          → R4 retune → R5 leitura no papel → R6 veredito final
```

A ordem vai **do mais profundo ao mais superficial**. Não faz sentido polir uma frase com número errado (Fase 1) ou um parágrafo que vai sair por redundância (Fase 2).

---

## Fase 0: preparação

| Passo | Skill | O que faz | Por que vem aqui |
|---|---|---|---|
| 0.1 | `ghost-writer:rules` | Converte o guia de estilo (regras do workshop CBM + terminologia fixa) em `style-rules.md`. | É o regulamento que `revise` e `integrate` aplicam depois; precisa existir antes. |
| 0.2 | Projeto `ghost-writer` + contrato `apodictic` | Cria `book.config.json` (leitor-alvo: júri; respostas em português) e o contrato APODICTIC (forma: argumento acadêmico/tese; leitor: júri; exigência alta; preocupações: tom, coerência, redundância). | Dependência técnica: as skills dos dois pacotes não rodam sem esses arquivos. |
| 0.3 | `ghost-writer:setup-voice` ⇄ `humanize-kit:voice-profiler` | Os dois montam um perfil da **sua** voz a partir de 3–5 textos seus escritos **sem IA** (relatório, e-mail longo, trabalho antigo). Os dois perfis são comparados. | Só é necessário na reescrita (R3–R4), então roda em paralelo com as Fases 1–5. **Depende de você mandar as amostras.** |

## Fase 1: fatos, números e citações

| Skill | O que faz | Comparada com |
|---|---|---|
| `apodictic:research-verification` (`citation-verifier` + `fact-check`) | Confere se cada referência existe e se diz o que a tese afirma; confere números e datas citados. | Persona *domain-expert* (Fase 4) e itens F1–F12 do diagnóstico v1. |

**Por que primeiro:** o próprio APODICTIC exige verificação de citações **antes** da análise em textos de alto risco, e uma tese é. Já achamos referências trocadas nas tabelas (F2, F3).
**Limite:** ISO 14155, ICH e normas pagas não podem ser lidas online. As cláusulas citadas ficam marcadas "não verificável" para você conferir no PDF da norma.

## Fase 2: argumento e estrutura

| | Skill | O que faz |
|---|---|---|
| 2A | `apodictic:nonfiction-argument-engine` (via `core-editor`) | Passes 0, 1, 2, 5 e 8 + *Dialectical Clarity* + *Argument Red Team* + *Evidence Deep-Dive*. Gera uma carta editorial, um registro de achados e o `Argument_State.md`, que é o mapa da tese central → subteses → evidências. |
| 2B | `ghost-writer:demolish` (modo análise) | Crítica hostil por capítulo nas 7 categorias de vulnerabilidade (afirmação central fraca, lacunas lógicas, conceitos indefinidos, contradições, implicações problemáticas…). Na análise ele **lista** tudo; o diálogo um-a-um fica para a Fase 6. |

**Triangulação:** 2A × 2B.
**Por que aqui:** a estrutura decide o que fica. É nesta fase que se resolve, por exemplo, se a 5.2 continua repetindo a 1.4.

## Fase 3: coerência entre capítulos

| Skill | O que faz | Comparada com |
|---|---|---|
| `ghost-writer:consistency-check` | Termos que mudam de nome, contradições, promessas não cumpridas, exemplos e dados repetidos. | Itens C e R do diagnóstico v1 e passe de continuidade do APODICTIC (2A). |

**Por que depois da 2:** parte das incoerências é sintoma de problema de estrutura que a Fase 2 já explica. Aqui pegamos o resto.

## Fase 4: leitores

| | Skill | Leitor |
|---|---|---|
| 4A | `ghost-writer:review` (5 × `demolish-persona`) | **Editor**: estrutura e prosa.<br>**Leitor-alvo**: orientadora e júri.<br>**Leitor hostil**: o **arguente** da defesa.<br>**Especialista**: profissional de regulatory affairs / qualidade clínica de dispositivos médicos.<br>**Fora do público**: engenheiro sem experiência em pesquisa clínica. |
| 4B | `apodictic:argument-audits` → `argument-persuasion` | Matriz de públicos: para quem cada parte do argumento funciona e para quem não funciona. |

**Triangulação:** 4A × 4B.
**Por que aqui:** o próprio ghost-writer recomenda as leituras por persona **depois** que o argumento já foi testado (Fase 2).

## Fase 5: prosa

| | Skill | O que faz |
|---|---|---|
| 5A | `apodictic:prose-measurements` (`ai-prose` + `argument-decision`) | Diagnóstico de prosa com cara de IA por categorias (fluência sem atrito, eco de estrutura, vazamento de discurso, costura de registro). As medições automáticas do SETEC não estão instaladas, então uso as contagens próprias (frase média, frases longas, palavras-muleta). |
| 5A′ | `humanizer` (só a etapa de marcação) | Marca os padrões da lista da Wikipedia *Signs of AI writing*: "not X but Y", frases de fecho, trios forçados, palavras típicas de IA, travessões. **Não reescreve nesta fase.** |
| 5B | `ghost-writer:revise` | Copidesque contra o `style-rules.md`: gramática, pontuação, números, nomes e dados que mudam entre capítulos. |
| 5B′ | `writing-skills:orwells-rules` + `plain-language` | Checklists de clareza, **calibrados para texto acadêmico**: teto de 30 palavras por frase, "we" e não "you", jargão técnico necessário mantido. |

**Triangulação:** 5A × 5A′ e 5B × 5B′.
**Por que por último na análise:** a prosa é a camada mais superficial e muda com as decisões das fases anteriores.

## Fase 6: consolidação e decisão

| Passo | Skill | O que faz |
|---|---|---|
| 6.1 | (eu) | Junto tudo num registro único, com o formato abaixo, e aplico a triangulação ✅ ⚖️ ⚔️. |
| 6.2 | `apodictic:triage-feedback` | Classifica cada ponto em **Must-Fix / Should-Fix / Could-Fix** e valida contra o texto. É feita exatamente para triar feedback vindo de várias fontes. |
| 6.3 | Você, no protocolo do `ghost-writer:demolish` | Você decide os pontos ⚖️ e ⚔️, um de cada vez ou em lote por capítulo. |

Saídas: `revisao/analise-v2/registro.md` (o registro completo) e `revisao/analise-v2/relatorio.md` (o resumo).

### Formato do registro

| ID | Fase | Skill | Seção | Trecho (literal) | Problema | Tipo | Severidade | Triangulação | Decisão |
|---|---|---|---|---|---|---|---|---|---|
| A-017 | 2 | apodictic | 5.1 | "ISO 13485, ISO 14971, and ISO 15189 each require…" | Contradiz a 2.5.1 sobre a origem dos pilares | C | Must | ✅ (2A, 3, v1) | aceito |

Tipos: [F] fato, [C] coerência, [R] redundância, [A] argumento, [L] leitor, [T] tom, [G] gramática, [E] estilo.

---

## Reescrita (depois das decisões, um capítulo por vez)

| Passo | Skill | O que faz |
|---|---|---|
| R1 | `ghost-writer:integrate` | Aplica as decisões aceitas, uma por vez, com a sua aprovação. Você recebe um **Word com controle de alterações**. |
| R2 | `ghost-writer:revise` | Copidesque final do capítulo contra o `style-rules.md`. |
| R3 | `humanizer` | Passe final de marcas de IA, usando o perfil da sua voz (Fase 0.3) como referência. Depois, `prose-measurements` mede de novo: os números do antes e do depois ficam registrados. |
| R4 | `ghost-writer:retune` | Quando você ler e disser "isso não soa como eu": você diz como falaria e eu reajusto. |
| R5 | `ghost-writer:corrections` | Gera um PDF com os parágrafos numerados (3.12 = capítulo 3, parágrafo 12) para você ler longe do computador. Suas anotações, até em áudio ou foto, voltam pra cá. |
| R6 | `ghost-writer:consistency-check` + `apodictic:ready` | No fim, com a tese inteira: checagem de coerência mais o veredito de prontidão para entrega. |

Ordem dos capítulos na reescrita: **2 → 3 → 1 → 4 → 5 → 6 → Abstract e Resumo** (estes por último, porque resumem o corpo já revisado).

---

## Pares de triangulação (resumo)

| Pergunta | Skill A | Skill B | Terceira fonte |
|---|---|---|---|
| Os fatos e as citações estão certos? | research-verification | persona *domain-expert* | diagnóstico v1 (F) |
| O argumento se sustenta? | nonfiction-argument-engine | demolish | — |
| Os capítulos se contradizem ou se repetem? | consistency-check | passe de continuidade do APODICTIC | diagnóstico v1 (C, R) |
| Como o júri e o arguente leem? | review (5 personas) | argument-persuasion | — |
| O texto soa como IA? | prose-measurements | humanizer | guia de estilo, Parte D |
| O estilo segue as regras? | revise | orwells-rules + plain-language | guia de estilo, Partes A–C |
| Qual é a sua voz? | setup-voice | voice-profiler | — |

## O que ficou de fora, e por quê

- **`humanize-kit:humanize`**: foi feita para driblar detectores de IA (Pangram, GPTZero), e o próprio material do kit recomenda redigitar o texto para passar nos classificadores. Numa tese com declaração de autoria e o Código de Conduta da ULisboa, isso é risco de integridade acadêmica. E não acrescenta qualidade que o `humanizer` e o `retune` já não deem. O **`voice-profiler`** do mesmo kit entra normalmente (Fase 0.3).
- **`humanize-ig`**: é para legendas de Instagram.
- **Skills de ficção ou de criação de livro do zero** (enredo, personagem, `write`, `write-opening`…): a tese já existe e não é ficção.

## Execução e custo

A análise (Fases 1–5) são cerca de **10 execuções independentes**. Cada uma lê a tese inteira (~55 mil tokens) mais o protocolo da própria skill. Estimativa: **entre 1,5 e 3 milhões de tokens** no total. Para garantir a independência, cada execução roda como um agente separado, em paralelo, e eu faço a Fase 6 com os resultados.
