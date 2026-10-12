# Relatório da reescrita (10/10/2026)

## O que foi entregue

- `entrega/tese-revisada.docx`: a tese inteira reescrita. O texto está justificado, com recuo de 720 twips na primeira linha, sem linha em branco entre parágrafos, e os títulos usam Heading 1/2/3.
- `tese/*.md`: os mesmos capítulos em texto. É a cópia de trabalho; o `git diff` mostra cada mudança.
- `revisao/reescrita/alteracoes-tabelas-figuras.md`: o que só você pode mudar nas imagens.

## Tamanho

| Capítulo | Antes | Depois | Diferença |
|---|---|---|---|
| 1 Introduction | 3.128 | 3.106 | −22 |
| 2 Methodology | 3.868 | 3.680 | −188 |
| 3 Gaps and requirements | 4.793 | 4.582 | −211 |
| 4 Results | 11.718 | 11.457 | −261 |
| 5 Discussion | 8.774 | 7.286 | −1.488 |
| 6 Conclusion | 768 | 662 | −106 |
| **Corpo** | **33.049** | **30.773** | **−2.276** |
| Tese inteira (com referências e listas) | ~38.050 | ~35.770 | |

Resumo: 298 palavras. Abstract: 282. Os dois ficam abaixo de 300.

## Decisões suas, como foram aplicadas

| # | Decisão | Onde entrou |
|---|---|---|
| P1 | O framework organiza deveres que já existem e acrescenta um elemento (a curva de aprendizagem); a rastreabilidade mostra coerência, não necessidade | 2.5, 3.5, 5.1, 6. A frase *"nothing in the framework is invented"* saiu. |
| P2 | Lacuna 3 estreita: observação, caso a caso, da proficiência de cada operador | 3.2.1, 3.4.2, 4.2.3, 5.1 e a Tabela 3.1 (lista de imagens). A Cláusula 10.6 virou dever de pessoal. |
| P3 | O centro é a parte presente quando o dado nasce; a deteção mais cedo é hipótese; a posse se justifica pela continuidade e pela capacidade de mostrar o próprio controle | 4.3, 4.3.1, 5.3, 5.4, 6 |
| P4 | Sai o *"probably unrealistic"*; a Conclusão não aceita a via híbrida; sai a *"same regulatory surface"* | 5.5: o patrocinador aparece só como apoio opcional (modelos e treino), com o centro operando e guardando os registros. A Conclusão não menciona a via híbrida. |
| P5 | O Tipo B é o centro-alvo; o Tipo C são os centros menores, com os mesmos problemas agravados | 1.3, 3.4.5 (reescrita inteira, com as três características), 4.1, 4.7.1, legenda da Tabela 4.2, 5.5, 6, Resumo e Abstract. Os tipos A, B e C ficam como categorias de desenho, não derivadas do registro. |
| P6 | Sai a remissão à definição na 2.4.2 | 3.4.4 (continua *"publicly identifiable"*) |
| P7 | Contexto europeu; dados dos EUA por disponibilidade | 3.4.4 e 5.7. A nota *"has to state"* saiu, e a 5.3 deixou de afirmar o que a 3.4.4 não dizia. A frase diz *"the supervising team has its regulatory experience there"*, sem tratar isso como origem do problema. |
| P8 | Ignorar; tirar os *"five complexity strata"* | 5.6 e 6. A 4.3.2 fala em critérios definidos pelo centro antes do primeiro caso, sem número de estratos. |
| P9 | DR10: substituto nomeado | 3.4.5, 4.2.2 (RACI com *backup*) e as Tabelas 3.4 e 4.1 (lista de imagens) |
| P10 | Decisão externa quando o PI é o cirurgião avaliado | 5.5 |
| P11 | Nenhuma alegação de reprodutibilidade | 2.6: admite que um só pesquisador fez as etapas qualitativas |
| P12 | Descartado | A frase *"Organizational size was analyzed separately"* saiu da 2.4.2, porque essa análise nunca é reportada |
| P13 | **Não aplicado**: fica para a sua ideia | (pergunta no fim) |
| P14 | Decidido por mim | Saiu o marcador de ética da 2.4.1. Saiu o MDIC das *"queries older than sixty days"* (4.4.1, 4.5.6); fica só o EMA [1]. O cartão de implante saiu da 3.3, da 3.4.1 e da 5.3, para não afirmar o que eu não consigo conferir na norma. |

## Correções de fato (Parte 2 do registro)

- **Feitas no texto:** F1 (Delphi 71), F2 (*about one in six*), F4 ([37, 39, 41]), F5 ([41], *underdeveloped*), F7 (Anexo XV, Cap. II, 3.14 + Art. 80(2); *immediately* na 3.2), F8 (três PMIDs, quatro títulos, autores de [36], páginas de [76]), F10, F11 (MDIC 2016), F12 (Anexo ZA da edição EN ISO), F14, F15, F16 (Fair Market Value e anti-indução saíram), F17 (Diani = RBM do patrocinador), F18, F19, F20, F21 (*same assessors* saiu), F22, F23, F24 (MDCG 2020-1 saiu; não tinha número de referência), F25 (classe III, Regra 8, Art. 61(4)).
- **F9:** tirei a oração do *"funder guidance"* em vez de incluir a referência nova, porque uma referência nova obrigaria a renumerar tudo de [71] em diante. As 90 referências seguem citadas na ordem de primeira aparição (conferido por script).
- **Só na imagem:** F3, F6, F13 (lista de imagens).

## Coerência, argumento e redundância (Partes 3 e 4)

Todos os itens C1–C30, A1–A20 e R1–R8 foram aplicados no texto, com exceção dos que dependem das imagens (C8, C9, C18 só na legenda, C20 parcial), que estão na lista de imagens. Pontos que valem destacar:

- **C6:** as tabelas foram renumeradas (4.3 → 4.2, 4.4 → 4.3) no texto, nas legendas e na lista de tabelas.
- **C12:** a 5.2 agora faz a comparação componente a componente que a 2.3.3 promete (SCR × SQA, SLCT sem contraparte, SRR × [76], indicadores × CT-SPM item a item).
- **C16:** os 24 instrumentos são nomeados na prosa do Cap. 4 onde são descritos.
- **C29:** a lacuna é definida uma vez na 2.2.3 e cobre o caso da lacuna 3.
- **R1/R2:** a 5.2 e a 5.3 deixaram de recontar a 1.4 e a 3.4 (−1.488 palavras na Discussão).
- **A17:** os seis indicadores **não** viraram tabela. Preferi enxugar a prosa, para não criar uma tabela nova que mudaria de novo a numeração.

## Estilo (Parte 6), conferido por script

- *rather than* e disfarces: zero no texto. As tabelas ainda têm alguns, que estão na lista de imagens.
- *architecture*: zero. Travessões, exclamações, contrações e *Taken together*: zero. Grafia britânica: zero no texto (as imagens ainda têm alguns casos).
- Ponto e vírgula: só nos itens da lista de registros mínimos da 4.7.2, que já têm vírgulas internas.
- Siglas: as que eram usadas só uma vez (CT, ICC, QMS, DSR) saíram. Das que voltavam à forma por extenso no Cap. 5, as que o script encontrou foram corrigidas.
- Remissões internas (Seção, Tabela, Figura, Capítulo): todas apontam para algo que existe (conferido por script).
- Frases: o comprimento médio fica entre 20 e 27 palavras, com desvio-padrão em torno de 10, e a mais longa tem 53. O detector ainda acha muitas séries de três no Cap. 4, mas a maior parte são listas de cláusulas e de itens de instrumento. Eu converti as séries que eram ritmo e deixei as que são conteúdo contado.

## O que eu não consegui verificar

1. O texto da **Cláusula 10.6 da ISO 14155:2026**, que manda manter a equipe adequada. Usei a mesma formulação que já estava na 4.2.3.
2. A numeração **ICH E6(R3) Section 3.12.2** para a análise de causa raiz e o CAPA do patrocinador. Ela vem da lente de fatos; vale conferir.
3. O **Art. 61(4)** do MDR (investigação obrigatória para implantáveis e classe III, com exceções) e a **Regra 8** (próteses de ombro na classe III). Ambos estão de acordo com o texto do MDR que eu conheço, mas não foram conferidos de novo nesta sessão.
