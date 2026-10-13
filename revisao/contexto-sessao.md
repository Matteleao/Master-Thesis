# Contexto para continuar a revisão numa sessão nova

Última atualização: 11/10/2026. Este arquivo existe para que uma sessão nova do Claude retome o trabalho sem a conversa anterior. **Leia-o inteiro antes de responder ao autor.**

## 1. Como trabalhar com o autor

- O autor é **Felipe Gregorio Lima**. Ele escreve em português e chama o Claude de "claudinho". As respostas são **em português**, e o texto acadêmico é entregue **em inglês**.
- A tese é *Translating ICH E6(R3) into Practice: A Site-Centered Operational Quality Management Framework for Shoulder Medical Device Clinical Investigations* (MSc Pharmaceutical Engineering, Universidade de Lisboa).
- **Fase atual: coedição parágrafo a parágrafo.** O autor cola um trecho e pede explicação, conferência com a fonte ou reestruturação. Ele escreve as versões finais. Não aplicar nada em `tese/*.md` sem a aprovação dele.
- O autor não usa o GitHub. Todo o trabalho vai para o branch **`claude/claudinho-status-check-8tzmxz`**. Não abrir PR sem pedido.
- Ele lê mal arquivos `.md`. Para relatórios, gerar HTML e mostrar na barra lateral, como foi feito com `revisao/reescrita/*.html`.
- Ele quer respostas honestas: discordar quando for o caso e não concordar só para agradar.

### Regras fixas

1. A skill **`thesis-writing`** (`.claude/skills/thesis-writing/SKILL.md`) é a regra principal e prevalece sobre qualquer outra skill de escrita. Não usar `humanize-kit:humanize`.
2. **Nunca** apresentar o orientador ou o coorientador como origem do problema da tese. O problema é reconhecido na literatura e na prática, e a leitura das diretrizes o delimitou. Nenhuma pessoa é nomeada.
3. **Nunca** inventar números, citações ou fatos sobre o que o autor fez. Quando faltar informação, perguntar ou pôr entre colchetes.
4. Citação literal só com as palavras exatas da fonte. Toda afirmação tirada de uma fonte leva o número da referência, mesmo que a fonte já tenha sido citada antes.
5. Não usar agentes nem workflows (custo de créditos).
6. **Não** subir o PDF da ISO 14155:2026 para o repositório (licença "NOT FOR COMMERCIAL USE OR REPRODUCTION").
7. A estimativa de "10–15 min" nunca aparece na tese.
8. Estilo:
   - sem *rather than* e disfarces, sem frases de abertura que anunciam e sem caudas que comentam a própria frase;
   - grafia americana e sem contrações;
   - Introdução impessoal e "we" a partir do Cap. 2;
   - *framework*, nunca *architecture*;
   - sigla definida na primeira ocorrência e não redefinida depois (MDR, CtQ e QbD já estão definidos no Cap. 1).
9. Vancouver: as referências são numeradas por ordem de primeira citação. Mover uma primeira citação obriga a renumerar.
10. Commits terminam com:
    ```
    Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
    Claude-Session: https://claude.ai/code/session_018xC7Cok8TcW2K2Q15D36dt
    ```

## 2. Onde está cada coisa no GitHub

Repositório: **`Matteleao/Master-Thesis`**.
- **Branch de trabalho:** `claude/claudinho-status-check-8tzmxz`. Tudo o que está abaixo fica nele.
- **Branch `main`:** só tem o `README.md` e o PDF do MDR (`Regulation on medical devices.pdf`, versão consolidada de 10/01/2025, 233 páginas), que o autor subiu.

| Caminho | O que é | Estado |
|---|---|---|
| `tese/01-introduction.md` | Cap. 1 | **Versão final do autor** (commit 21f4d9e). Ainda tem os problemas listados na Seção 4. |
| `tese/02-methodology.md` | Cap. 2 | **Desatualizado.** Ainda contém a reescrita do Claude. A versão em discussão está em `revisao/reescrita/cap2-2.1-2.2-proposta.md`. |
| `tese/03-…`, `04-…`, `05-…`, `06-conclusion.md` | Caps. 3 a 6 | Reescrita do Claude (commit 4dcac8b), ainda não revista pelo autor |
| `tese/00-elementos-pre-textuais.md` | Resumo, Abstract e listas | Reescrita do Claude |
| `tese/07-references.md` | 90 referências Vancouver | [5] = ICH E8(R1), [6] = ICH E6(R3), [8] = ISO 14155:2026, [10] = MDR |
| `tese/08-appendices.md` | Apêndices | |
| `tese/figuras/` | Tabelas e figuras em imagem | Não editáveis pelo Claude |
| `entrega/tese-revisada.docx` | .docx gerado da reescrita | **Desatualizado** (anterior ao Cap. 1 final) |
| `original/` | .docx original da tese e PDF do workshop CBM | Não editar |
| `.claude/skills/thesis-writing/SKILL.md` | A skill do autor | Regra principal |
| `revisao/reescrita/cap2-2.1-2.2-proposta.md` | **Proposta atual das Seções 2.1 e 2.2** | Em discussão, com pendências entre colchetes |
| `revisao/reescrita/mudancas-cap2-2.1-2.2.html` | Relatório palavra a palavra: texto do autor × proposta, com o motivo de cada mudança | Não inclui a versão refeita do último parágrafo, que está só na proposta |
| `revisao/reescrita/relatorio-reescrita.md` / `.html` | Relatório da reescrita completa (decisões P1–P14, correções F1–F25) | |
| `revisao/reescrita/alteracoes-tabelas-figuras.md` | O que o autor precisa mudar nas imagens das tabelas e figuras | Precisa de atualização (ver Seção 4) |
| `revisao/analise-v2/registro-consolidado.md` | Registro consolidado da análise (C, A, R, F) | |
| `revisao/analise-v2/onda-1/` | Os relatórios de cada lente da análise | |
| `revisao/projeto/style-rules.md`, `contrato-apodictic.md` | Regras e contrato do projeto | R26 e o contrato precisam de ajuste (ver Seção 4) |
| `revisao/guia-de-estilo.md`, `diagnostico.md`, `workflow.md`, `fase-0/` | Material das fases anteriores | Referência |

### Fontes primárias fora do repositório

- **ICH E8(R1):** https://database.ich.org/sites/default/files/E8-R1_Guideline_Step4_2021_1006.pdf
- **ICH E6(R3):** https://database.ich.org/sites/default/files/ICH_E6%28R3%29_Step4_FinalGuideline_2025_0106.pdf
- **ISO 14155:2026:** só existe como upload do autor numa sessão anterior. Numa sessão nova, **peça ao autor para enviá-la de novo** se precisar conferir uma cláusula.
- **MDR:** no `main`, `Regulation on medical devices.pdf`. Para ler: `git fetch origin main && git show "origin/main:Regulation on medical devices.pdf" > mdr.pdf`.

## 3. O que já foi verificado nas fontes (não refazer)

- **"CtQ", "QbD", "critical to quality" e "quality by design":** zero ocorrências na ISO 14155:2026 e no MDR. Os dois usam a ideia sem o nome:
  - ISO 6.7 e 9.2.3(c): "critical data points and endpoints";
  - ISO 7.4.2, Note 1 e MDR Art. 80(1)(a): eventos adversos "critical to the evaluation of the results";
  - ISO Annex D.5: "critical features of the clinical investigation".
  - Nenhum dos dois define criticidade nem dá critério.
- **"proficiency", "operator performance", "credential", "proctor" e "surgical skill":** zero no MDR e na ISO, o que confirma a frase da 3.2 para esses dois textos.
- **ICH E8(R1):**
  - 3.2 traz a definição de CtQ, a proporcionalidade, o "not cluttered with minor issues" e "Knowledge of the drug … will continually inform the identification of CtQ factors and control processes";
  - 3.3 (3.3.1 a 3.3.5) diz como identificar os fatores;
  - **a Section 7 tem exatamente 18 considerações.**
- **ICH E6(R3):**
  - 3.10 define CtQ de forma curta e remete à E8(R1);
  - Principle 4.2 trata do estado do conhecimento; Principle 7 e 7.1, da proporcionalidade;
  - 2.3.2: pessoal delegado "appropriately qualified";
  - 3.2: recursos; 3.3: alocação de papéis; 3.4: qualificação; 3.7.1: o investigador demonstra recursos adequados;
  - 3.10.1.3: *quality tolerance limits*; 3.10.1.5: "emerging knowledge and experience".
- **MDR Art. 61(4):** investigação clínica obrigatória para implantáveis e classe III, com as exceções de dispositivo modificado e equivalente. Confirmado.
- **ISO 14155:2026:**
  - 10.1: o PI responde pela condução diária e pela integridade dos dados;
  - 9.1: princípios de gestão da qualidade, mas procedimentos escritos só do patrocinador;
  - 10.6(a–r): deveres do PI como lista de resultados, sendo 10.6(h) equipe e instalações adequadas, 10.6(i) manutenção e calibração documentadas, e 10.6(o) causa e CAPA para não conformidade significativa;
  - cartão de implante: 9.2.2(e) e 10.7(g);
  - "learning curve": só no Annex A.

## 4. Pendências

### Cap. 2 (em andamento)

0. **Cap. 2 reestruturado por atividade do DSRM** em `revisao/reescrita/cap2-reestruturado.md` (e `.docx`), a pedido do autor: 2.1 desenho; 2.2 identificação do problema (normas, leitura e comparação fundidas, literatura, frameworks existentes, registro); 2.3 objetivos (critérios CtQ, domínios, requisitos); 2.4 desenho e desenvolvimento; 2.5 limitações. Metodologia expositiva: o quê e como, sem porquês desnecessários. O Cap. 3 **não** deve ser reordenado; só as remissões precisam de ajuste (ver relatório da sessão).

1. **MDR:** a leitura foi só do Annex XV, ou incluiu também o Art. 27, o Annex VI e o Cap. VI? A 2.2.3 usa atributos de UDI, que não estão no Annex XV.
2. **Os 18 itens da E8(R1):** entraram na matriz como atributos ou serviram só como checagem de cobertura?
3. **Regra de entrada no último parágrafo da 2.2.2:** o critério que o autor de fato usou corresponde ao descrito? E o consentimento informado está na matriz, para servir de exemplo?
4. **[39]:** "finds" descreve bem o estudo?
5. **Fazer na sequência:**
   - aplicar a proposta em `tese/02-methodology.md`;
   - na 2.2.3 e na 3.3, trocar "the four criteria drawn from ICH E8(R1)" por "the four criteria of Section 2.2.2";
   - levar para a 3.2 o parágrafo da ISO (10.1, 9.1 e 10.6) e o das *quality tolerance limits*, que saíram da 2.1.1 e da 2.2.2.
6. O autor ainda vai rever 2.2.3, 2.3, 2.4, 2.5 e 2.6.

### Cap. 1 (problemas apontados, sem aprovação do autor)

1. "Delphi process with 21 stakeholders" → 71.
2. A [38] não é mais citada no Cap. 1: a primeira citação passa para a 5.2 e a ordem Vancouver quebra.
3. A [40] saiu do Cap. 1, mas continua citada na 5.2. Falta decidir o destino.
4. "It also requires investigators to maintain appropriate site processes…" não está na E6(R3). Sugestão: "It also asks investigators to have an adequate number of qualified staff and adequate facilities for the conduct of the trial [6]."
5. "between … from" → "between … and".
6. "the edition that it's still referenced" → "that is still referenced".
7. "weight,." → "weight.".
8. "beyond the record … it also requested to explain why": falta sujeito.
9. "[10, 8]" → "[8, 10]".
10. "it  [29]": espaço duplo.
11. A sigla API não é mais definida (a 2.4.1 usa "API v2"), e a busca de 996 registros saiu do Cap. 1.
12. Os números novos de Florez (119 patrocinadores, 32 práticas, 60 de 119, 39%, 68%) não foram conferidos.

### Remissões entre capítulos

- A 3.4.1 diz "Section 1.3 introduced five conditions" e deveria ser 1.2.
- A 5.6 diz "Section 1.3 gives the reason for narrowing" e deveria ser 1.5.
- A 5.2 diz "Section 1.4 described four bodies of work" e precisa ser conferida com o Cap. 1 final.

### Correções sugeridas pela ISO (ainda não aplicadas)

- **Lacuna 5:** na Tabela 3.1 (lista de imagens) e na 4.5.7, citar a ISO 10.6(o) em vez da ICH E6(R3) 3.12.2 ou do MDR.
- **5.5:** a frase "no clause describes the record" sobre calibração está errada, porque a 10.6(i) existe.
- **4.4.2:** pode citar a 10.6(i).
- **Cartão de implante:** restaurar na 3.3, 3.4.1 e 5.3 com as cláusulas 9.2.2(e) e 10.7(g).
- **Precisão das remissões:** onde se fala em equipe adequada, "Clause 10.6" → "Clause 10.6(h)".

### Outros

- Atualizar a R26 em `revisao/projeto/style-rules.md` e o `contrato-apodictic.md` com a nuance da origem do problema (regra 2 da Seção 1).
- P13: ideia do autor sobre por que a ICH E6 importa para centros de dispositivos.
- Figura 4.5: o que significa o marcador tracejado.
- Confirmar as datas de fundação: TransCelerate (2012), CTTI (2007, FDA e Duke), MDIC (2012).
- Regerar o `.docx` de entrega quando os capítulos estiverem fechados. O comando é pandoc `-f markdown-auto_identifiers-implicit_figures`, com pós-processamento em python-docx: texto justificado, recuo de 720 twips na primeira linha e sem linhas em branco entre parágrafos.
