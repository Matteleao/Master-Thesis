# Passagem de contexto para nova sessão (2026-11-13)

## 1. O projeto

- **Tese de mestrado** (ULisboa) de Felipe Gregorio Lima: *Translating ICH E6(R3) into Practice: A Site-Centered Operational Quality Management Framework for Shoulder Medical Device Clinical Investigations*.
- **Coorientador:** Dr. Nuno Moura (pode ser citado pelo nome).
- **Repositório:** `matteleao/master-thesis`. **Branch de trabalho:** `claude/claudinho-status-check-8tzmxz`. Fazer commit e push nesse branch. **Nunca** abrir PR sem pedido.
- **Método:** DSRM adaptado (Peffers). A tese reporta as atividades 1 a 3 e a comunicação. Não há implementação, e isso já estava previsto no método.

## 2. Arquivos (pasta `revisao/`)

| Arquivo | Estado |
|---|---|
| `Tese_Versao_final_corrigida.docx` | **Versão final atual** (183 pp). Já contém: cap. 1 novo; correções pontuais do cap. 3; remissões internas removidas em toda a tese (ficaram só referências a normas, tabelas, figuras e apêndices, e o mapa do DSRM na metodologia). Ainda contém o cap. 5 **antigo**. |
| `Cap5_Discussion_reescrito_2026-11-12.docx` / `.txt` | Cap. 5 reescrito com as decisões do autor. **Ainda não juntado** à tese. O 5.1 continua em aberto (ver §5). |
| `Revisao_critica_cap5_2026-11-11.md` | Parecer de arguente sobre o cap. 5 (itens A–G). As decisões do autor sobre ele estão no §4. |
| `Revisao_referencias_2026-11-12.md` | Auditoria das referências: ordem e numeração corretas; lista de correções de colocação, de fontes em falta e de completude. **Nada aplicado ainda.** |
| `Cap3_correcoes_pontuais_2026-11-10.*` | Versão do cap. 3 que foi juntada à tese. |
| `Cap3_Gaps_reescrito_2026-11-10.*` | Reescrita longa do cap. 3. **Rejeitada** pelo autor (acrescentava pouco). Só serve para aproveitar frases. |
| `Cap1_Introduction_reescrito_2026-11-08.*` | Cap. 1 novo, já juntado à tese. |

**Material que o autor carregou e não está no repositório:**
- Planilha `Derivacao_Site_level_CTQ_domains.xlsx`: matriz de 251 entradas e 43 temas, com os filtros, os domínios e as lacunas.
- Planilha `Analise_centros_clinical_trials.xlsx`: o registro.
- PDF licenciado da ISO 14155:2026. **Não fazer commit dele.**

Se forem necessários, pedir que o autor os envie de novo. **Nunca alterar as planilhas do autor.**

## 3. Preferências do autor

**Comunicação:**
- Responder em **português**. O texto acadêmico vai em **inglês americano**.
- Ser direto e honesto. Dizer quando uma mudança acrescenta pouco.
- Gastar poucos tokens.

**Forma de trabalhar:**
- **Propor antes de aplicar.** Mostrar o texto no chat para ele conferir.
- Não acrescentar nada que ele não decidiu.
- Gerar capítulos como **documento separado** antes de juntar à tese.

**Escrita:** seguir a skill `.claude/skills/thesis-writing` (as regras dele, com precedência sobre qualquer outra). O que ele mais cobra:
- **Repetição:** nenhuma, nem dentro do capítulo nem entre capítulos. Isso vale também para a mesma ideia dita por outras palavras em parágrafos seguidos. É a queixa nº 1.
- **Enchimento:** nada de frases vagas ou com floreio. Exemplos que ele rejeitou: "final responsibility stays where the regulations place it"; "the site, which produces part of the same evidence, has no requirement to hold one". Ser direto.
- **Coesão:** nada de frase solta, desconectada do parágrafo.
- **Remissões internas:** não remeter a capítulos ou seções da própria tese. Exceções: referências a cláusulas e seções de normas (rotular o instrumento, por exemplo "(ICH E6(R3), Section 2.3.3)"), referências a tabelas e figuras, e a apêndices.
- **Construções proibidas:**
  - "rather than", "not X but Y" e qualquer disfarce;
  - travessões;
  - listas de três por cadência;
  - frase de abertura que só anuncia;
  - aforismos;
  - afirmações desproporcionais à evidência;
  - excesso de "explicit" (poucas vezes, só onde importa).
- **Voz:** ele quer a **voz dele**: direta, frases afirmativas, sujeito no início, verbos práticos. Ainda não há um perfil de voz bem construído; pedir dois ou três parágrafos que ele escreveu sozinho. Ele testou vozes (Gawande, Orwell etc.) e não fechou nenhuma. As vozes de palco (Jobs, King, Obama) ficam só para a defesa oral.

## 4. Decisões de conteúdo já tomadas

**Propósito e centro-alvo:**
- **Propósito principal:** controle da qualidade durante a condução. Continuidade (quando muda a equipe) e reaproveitamento entre investigações são benefícios adicionais.
- **Baixo recurso:** orienta o desenho mas não remove funções essenciais. A adoção parcial não equivale ao nível mínimo. Um centro que não sustenta o mínimo precisa de apoio.
- **Centro-alvo:** pequena clínica independente. É mais estreito que a categoria "nonhospital" do registro, que inclui hospitais ortopédicos de cirurgiões. A classificação do registro não muda.
- **O argumento da 5.1 fica:** o registro mostra quase um terço de centros fora de hospitais, então o framework tem de funcionar primeiro onde pode supor menos apoio institucional.
- **Categoria e nível:** a categoria organizacional dá uma *estimativa* do nível de implementação. Estimar não é garantir.

**Base regulatória e registro:**
- Base regulatória europeia, com intenção internacional (EUA incluídos), que exige adaptação. Não se afirma equivalência.
- Registro: 347 registros de centros, 238 organizações, 31,1% nonhospital. 63 das 68 organizações nonhospital estão nos EUA.

**Ponto a ponto, do parecer do cap. 5 (já aplicado no cap. 5 separado):**
- **A5 e A6:** as siglas ficam. Na 1.ª menção no cap. 5, nome mais sigla.
- **A4:** "sem implementação" só onde algo não pode ser medido por isso.
- **B3:** "expected effects", e não "testable propositions". As condições de refutação são fixadas pelo centro no arranque, antes dos dados.
- **B4:** a exposição dos achados que o centro registra contra si é positiva, porque mostra um centro consciente que age. O framework também antecipa requisitos futuros.
- **B5:** ganho principal = controle da própria condução. Tem também valor económico e reputacional, e a continuidade.
- **B7:** a observação do cirurgião é "exaptation" (Gregor e Hevner, ref. 89).
- **B10:** a revisão por terceiros externos não está no desenho.
- **B11, argumento económico:**
  - o trabalho de qualidade pode ser cobrado no orçamento, dentro do valor justo de mercado;
  - justifica uma linha para um revisor de qualidade de dados;
  - dá renda mais estável, porque se perdem menos elegíveis e há menos correções, e porque melhora a reputação junto aos patrocinadores;
  - o custo de execução cai com a repetição.
- **B12:** o parágrafo "documentation has a cost" foi retirado.
- **C1:** representante do fabricante no bloco: não mencionar.
- **C2:** **CROs fora da tese.** Usar o argumento de tempo do monitoramento central.
- **C3:** mencionar SMOs. O apoio delas é genérico.
- **C4:** citar os esquemas de acreditação MHRA fase I e AAHRPP (novas refs. 94 e 95). Não fazer parecer inédito.
- **C5:** desempenho abaixo do esperado com técnica nova não é juízo sobre a prática habitual do cirurgião. A codificação protege de olhares acidentais.

## 5. Pendências (por prioridade)

1. **5.1 em aberto.** O autor acha que a 5.1 atual acrescenta pouco. A última proposta, ainda não aprovada, tinha três parágrafos:
   - achados principais amarrados aos 4 objetivos do 1.5;
   - o que significam juntos, dito uma vez só e sem repetir o achado;
   - o tipo e o nível da contribuição: exaptation, mais três lições de desenho como "nascent design theory" (Gregor e Hevner).

   As lições são: (a) o controle fica no momento em que o erro se torna irreversível; (b) um registro só mostra o problema quando lido com outros, por isso leva a revisão e decisão; (c) o framework é feito para o centro com menos apoio e cresce depois.

   Ele rejeitou a redação por repetição, frases vagas e uma frase solta. Precisa ser reescrita **na voz dele**.
2. **Juntar o cap. 5 à tese.**
   - Inserir as refs. novas 94 (MHRA Phase I Accreditation Scheme, gov.uk) e 95 (AAHRPP, aahrpp.org/about).
   - Renumerar as antigas 94→96, 95→97, 96→98. Nada acima de 93 é citado fora do cap. 5.
   - Refazer a Tabela 5.3 com o cabeçalho "Expected effect". A imagem já está pronta no cap. 5 separado.
3. **Aplicar a auditoria de referências** (`Revisao_referencias_2026-11-12.md`). Itens principais:
   - 3.4.2: "funder guidance" deve citar a ref. 68, não a 70;
   - retirar a ref. 37 de "reactive and ad hoc";
   - ref. 93 é sobre ensaios pediátricos num centro sueco;
   - ref. 1 não sustenta "over the past decade";
   - refs. 27 e 28 no 3.3;
   - normas sem citação nos caps. 3 e 5;
   - no 3.2.1, "process risks" deve ser "CIP procedure risks";
   - refs. 27 e 28 sem URL;
   - capitalização dos títulos;
   - ref. 49 a confirmar no texto completo.
4. **Cap. 4:** o autor vai reescrevê-lo com outra ferramenta (Fable). Não acrescentar nada ao cap. 4. Notas para a reescrita:
   - cerca de 15 parágrafos sem citação da norma;
   - "Existing SQA frameworks deal with it mainly at selection^31,33";
   - Clavien-Dindo com a citação depois do ponto.
5. **Pendências menores:**
   - tique de "together with" (deixado para depois);
   - Tabela 5.1 com letra de ~5 pt;
   - Tabela 5.4 só com siglas;
   - estilo diferente da Figura 5.1 (o autor adiou o visual);
   - título "3.1 … of this chapter".

## 6. Notas técnicas

**Edição do docx:**
- Editar por regex em `word/document.xml`.
- Estilos: `Ttulo1/2/3` (títulos), `Tablecaption`, `Figurecaption`, `PargrafodaLista` (numId 4).
- As citações são runs em sobrescrito (sz 18) **antes** do ponto, em Vancouver, numeradas pela 1.ª aparição. Isso inclui as citações dentro da imagem da Tabela 5.1, que contam na posição da imagem.

**Tabelas em imagem:** refazer em HTML com IBM Plex Sans e capturar com Playwright. Estilo:
- cabeçalho #1e1f1c;
- linhas alternadas #f4f3ef;
- borda com cantos arredondados.

**Ferramentas:** os scripts da sessão estavam no scratchpad, que é efêmero. Recriar quando necessário:
- extrair um capítulo com os sobrescritos;
- substituir texto atravessando runs;
- montar um capítulo separado com os estilos da tese;
- auditar a ordem das referências.

**Privacidade:** o email do autor é privado e nunca deve ser enviado para fora.
