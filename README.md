# Master-Thesis — revisão da tese

**Tese:** *Translating ICH E6(R3) into Practice: A Site-Centered Operational Quality Management Framework for Shoulder Medical Device Clinical Investigations*
Felipe Gregorio Lima — Mestrado em Engenharia Farmacêutica, Universidade de Lisboa (2025/2026)

Este repositório guarda a tese e o trabalho de revisão de escrita: tom, coerência interna, redundâncias, uniformidade e aplicação das regras de escrita científica. As regras vêm da skill do próprio autor (`thesis-writing`), construída a partir do workshop da Dra. Carolina Borges Merjane (CBM Science).

## Estrutura

| Pasta / arquivo | Conteúdo |
|---|---|
| `original/` | Arquivos exatamente como foram recebidos (a tese em `.docx` e o PDF do workshop). Não são editados. |
| `tese/` | A tese convertida para texto (Markdown), um arquivo por capítulo. É a cópia de trabalho: cada revisão vira um commit, então dá para ver o antes e o depois de cada frase. |
| `tese/figuras/` | Tabelas e figuras extraídas do `.docx` (no Word elas estão como imagem). |
| `.claude/skills/thesis-writing/SKILL.md` | **A skill de escrita do autor** (prosa científica, estrutura do argumento, evidência e entrega). É a regra principal da revisão e é carregada automaticamente por qualquer sessão do Claude neste repositório. |
| `revisao/guia-de-estilo.md` | A camada específica desta tese: precedência entre regras, conflitos resolvidos entre a skill do autor e as skills genéricas, terminologia fixa e padrões encontrados no texto. |
| `revisao/workflow.md` | A ordem de uso das skills na análise e na reescrita, com os pares de triangulação. |
| `revisao/fase-0/` | Preparação: definição do projeto, ditados do autor (amostra de voz) e perfil de voz. |
| `revisao/diagnostico.md` | O diagnóstico da versão original: incoerências, erros factuais, redundâncias, tom e estilo, com a localização de cada problema. |

## Observações sobre a conversão para texto

- As citações aparecem como `[n]` em texto normal. No `.docx` elas estão em **subscrito** (ver diagnóstico).
- O sumário (Index) foi omitido porque só tem números de página.
- A Figura 4.1 está inserida **duas vezes** no `.docx`. No texto ficou uma só.
- A ordem das imagens perto da Tabela 4.4 e das Figuras 4.2–4.4 foi ajustada para seguir a leitura.
