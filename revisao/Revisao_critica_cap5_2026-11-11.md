# Revisão crítica do Capítulo 5 (Discussion)

Leitura como arguente. Referências de localização: secção e ordem do parágrafo (ex.: 5.1 §3 = terceiro parágrafo da 5.1). Citações do texto em inglês, entre aspas.

## Avaliação global

O capítulo tem boas passagens de discussão verdadeira: 5.3.3 (onde a implementação falha), 5.3.5 (documentação melhora a condução?), 5.4.1 (custos do nível mínimo), 5.5.2 §4 (alinhamento com o sponsor) e 5.6.1 (tipo de avaliação feita). Nelas o texto põe o trabalho contra algo externo e é honesto sobre o que não mostrou.

Os problemas estão em quatro frentes, por ordem de gravidade:

1. **Duas secções repetem capítulos anteriores em vez de discutir.** A 5.2 recontra os estudos do cap. 1 quase palavra por palavra. A 5.3.1 e a 5.3.2 recontam o cap. 4.
2. **Há conflitos internos latentes com os caps. 3 e 4.** Um arguente atento pega pelo menos cinco (secção B).
3. **Pontos cegos operacionais.** O texto ignora atores e estruturas que existem nos ensaios de dispositivos ortopédicos e que um arguente da indústria vai levantar (secção C).
4. **Escrita:** a densidade de siglas na 5.3, tiques de conector e repetição de ideias dentro do próprio capítulo.

---

## A. Estrutura do capítulo

**A1. A 5.2 repete o cap. 1.** Quase todos os estudos da 5.2 já foram descritos no 1.4, muitas vezes com a mesma frase:
- unidades de ensaio académicas (frase praticamente idêntica);
- os 83% de 1.111 centros com monitorização central;
- CTAIM;
- ISO 9001 em Itália;
- os 19,6% de centros portugueses;
- inquérito RBQM;
- desafios do SQA;
- o "primer" do centro privado;
- autoavaliação do CT-SPM.

Numa discussão, o leitor já conhece estes trabalhos. A secção deveria dizer só o que o framework faz de diferente face a cada grupo, em uma ou duas frases por tema, apoiando-se na Tabela 5.1. Hoje cerca de metade de cada parágrafo é descrição repetida.

**A2. A 5.3.1 e a 5.3.2 recontam o cap. 4.** O percurso pelo ciclo de vida e o ciclo de revisão já estão no cap. 4, e várias frases são quase idênticas:
- "A signal tied to a surgeon goes to the learning curve review…";
- "The review may confirm stable execution or lead to closer observation…";
- a abertura do SRR antes do primeiro participante;
- "Fifteen of the twenty-four instruments…".

Pela regra que você mesmo adotou, uma secção de discussão que só explica o trabalho de novo é defeito. Há duas opções:
- (a) mover o percurso para o cap. 4, como síntese operacional;
- (b) reduzi-lo a um parágrafo e manter na 5.3 só o que é discussão: 5.3.3, 5.3.4 e 5.3.5.

O cap. 4 vai ser reescrito, por isso vale decidir isto agora.

**A3. A 5.1 mistura quatro funções:**
- contribuição (§1–2);
- elementos que surgiram durante o desenho (§3);
- autocrítica (§4);
- classificação de Gregor e Hevner (§5–6).

O §4 ("delivered less than we hoped… In hindsight, the order of the work…") é uma limitação e pertence à 5.6.2. Do jeito que está, a abertura da discussão termina com o autor a desvalorizar a parte mais original antes de a posicionar.

**A4. As ressalvas estão espalhadas e repetidas.**
- **"Não houve implementação":** 5.1 §1, 5.3.3 §1, 5.3.4, 5.3.5 §4, 5.4.1 §1, 5.5.1 §3, 5.5.2 §3 e 5.6.2 §1.
- **"Registro pesa para os EUA" e "a análise regulatória não depende do registro":** 5.4.4 §1 e 5.6.2 §5.
- **Mapear para a 21 CFR 812:** 5.4.4 §2 e 5.6.3 §5.

Uma ressalva dita uma vez, no lugar certo, pesa mais do que oito vezes de passagem.

**A5. Siglas.** Só a 5.3.1 usa 18 siglas de instrumentos: SRR, SLCT, ICDL, PSEAR, IQL, SART, SCML, PFVR, CCDM, POT, MRL, RACI, DTRM, TRE, SCR, CSST, FUCR e PIDLR. Um leitor da discussão não as retém, e um arguente lê a discussão antes do cap. 4. Fora das passagens técnicas, use o nome descritivo ("the risk register", "the intraoperative record"). A sigla só se justifica onde o leitor precisa identificar o instrumento.

**A6. O mesmo objeto aparece com dois nomes.**
- "SLCT" e "learning curve log" (5.1 §6, 5.3.1 item 5, 5.3.2 §3 e 5.4.1 §3) são o mesmo instrumento.
- "SRR" e "risk register" também.
- "complication review" corresponde a CSST, a SCML ou a ambos, e o texto não diz qual.

Um nome por objeto.

---

## B. Conflitos internos e saltos lógicos

**B1. Registro e centro-alvo: o cap. 5 volta a fazer o salto que corrigimos no 3.4.5.**
- **5.1 §3:** "The registry analysis then showed that nonhospital organizations hosted almost a third of the site records, so the framework had to work first where it could assume the least support". É a mesma inferência causal registro → desenho que foi corrigida no cap. 3.
- **5.2 §5:** "A nonhospital organization has none of this". O registro não mede recursos, e a categoria inclui hospitais ortopédicos de cirurgiões.
- **Conflito mais fundo, com o cap. 4:** o 3.4.4 diz que as categorias "say little about how it is prepared for research". O modelo de escalabilidade usa a categoria como primeira estimativa do nível (5.3.1 item 1: "The organizational category of the site gives a first estimate of its implementation level"; e "the MRL at the academic level"). Um arguente pergunta: se a categoria pouco diz sobre preparação, por que ela define o nível? A resposta existe (é só ponto de partida, conferido contra a equipa real), mas precisa estar escrita onde o modelo é apresentado. Isso afeta o cap. 4.

**B2. "None of these elements was among the objectives" (5.1 §3).** O ciclo de vida e o modelo de escalabilidade respondem ao DR9 e ao DR12 (cap. 4, abertura), e esses requisitos vêm do cap. 3. Se não estavam nos objetivos e surgiram durante o desenho, o arguente pergunta se os DR9 e DR12 foram escritos depois do desenho. Reformule: os dois elementos surgiram como a forma de cumprir o DR9 e o DR12, e o que não estava previsto foi a forma, não a necessidade.

**B3. "Testable propositions" com a condição de refutação em aberto (5.3.4 §1).** A Tabela 5.3 chama os efeitos de "testable propositions", e o texto diz logo a seguir que "The conditions for refuting them are left open on purpose… each site should decide". Uma proposição sem condição de refutação não é testável. Além disso, o próprio framework exige que "Every rule is fixed before any data exist" (5.3.1 item 5). Há duas saídas:
- dar a cada proposição um horizonte mínimo, por exemplo "after N review periods";
- chamá-las de "expected effects", sem o adjetivo.

**B4. Superfície regulatória (5.5.3 §3, 5.4.1 §1 e 5.5.1 §3).**
- A 5.4.1 §1 diz que a premissa de que a inspeção avalia completude e consistência dos registros "we could not source".
- A 5.5.3 §3 afirma categoricamente que "an inspection under the MDR would not treat their absence as a noncompliance" e que os dois centros "present the same regulatory surface".
- A 5.5.1 §3 diz que "a finding the site raised against itself is still a finding", ou seja, os registros do centro aumentam o que um inspetor pode ler.

As três passagens não conversam. A superfície não é a mesma: o centro com o framework expõe mais. Esse é um argumento honesto e importante, e hoje ele se contradiz. Sugestão: buscar fonte para a premissa (procedimentos de inspeção de BPC da EMA ou do FDA) e reescrever a 5.5.3 §3 reconhecendo a exposição.

**B5. O ganho principal do centro (5.5.1 §1).** "For the site, the main gain is an account of its own conduct that survives changes of people." Isto contradiz a decisão que tomamos para o cap. 3: o propósito principal é o controlo da qualidade durante a condução, e a continuidade é benefício adicional. Contradiz também a 5.1 §1–2, que põe o controlo no centro. Ajuste para controlo como ganho principal e continuidade como ganho adicional.

**B6. "The derivation is unaffected" (5.4.4 §1).** É verdade só para a parte regulatória. O DR10 a DR12 vêm das condições operacionais, que se apoiam no registro, com peso nos EUA, e em literatura de ensaios de medicamentos. Restrinja a frase: "The regulatory derivation is unaffected…".

**B7. A classificação da observação do cirurgião (5.1 §6 contra 5.2 §3).** A 5.1 classifica-a como "improvement" (solução nova para problema conhecido). Mas a 5.2 §3 mostra que a solução já existe: as recomendações IDEAL já propunham controlo estatístico de processo para curvas de aprendizagem. O que é novo é quem a usa (o centro, durante a condução). Pelas suas próprias definições, isso é "exaptation". Ou reclassifica, ou explica por que a revisão clínica estruturada por complexidade é uma solução diferente do SPC. Além disso, "delivered less than we hoped" (5.1 §4) soa estranho para um desenho que não foi testado. O que entregou menos? A derivação.

**B8. Apoio do CT-SPM (5.2 §4).** "its four domains match four of our six indicators although the two sets were built independently, which gives modest support to our domain analysis". Há dois problemas:
- Não foram construídos independentemente: o CT-SPM foi lido e citado no cap. 1 antes do desenho.
- Compara domínios de uma medida com indicadores da outra, que são categorias diferentes.

Retire o "independently" e o apoio, ou formule como convergência descritiva.

**B9. Da evidência externa ao sinal interno (5.2 §4).** A evidência mostra que sinais vindos de fora (monitorização central, ranking do sponsor) melhoram os centros. A conclusão de que um sinal gerado no próprio centro e mais cedo terá valor é uma extrapolação plausível, mas não decorre da evidência. Formule como hipótese, ligando-a à proposição correspondente da Tabela 5.3.

**B10. Revisão externa: está ou não no desenho?** A 5.3.3 §2 diz que revisão por par externo ou entre centros "None of these options is part of the current design". A 5.5.4 §2 diz que "the framework can therefore pass the decision to that substitute or to a party outside the site… on a route fixed before the first case". Decida e diga o mesmo nos dois lugares.

**B11. Orçamento (5.4.2 §2 contra 5.5.1 §2).**
- A 5.4.2 diz que "Site compensation is also calculated per procedure and per participant" (sem fonte) e que "What has no budget line is setting up the structure".
- A 5.5.1 diz que "The preparation of a trial is therefore already a negotiated budget item".

Lidas juntas, parecem contraditórias, e taxas de ativação ("start-up fees") são prática corrente. Distinga o custo de preparar a investigação, que é pago, do custo de montar uma estrutura que serve a várias investigações, que não tem linha. E cite fonte para a remuneração por procedimento, ou suavize.

**B12. Registro valioso mesmo sem mudar a condução (5.3.5 §2 contra §4).** O §2 diz que o registro completo já seria melhor do que nada. O §4 diz que um framework que nada mudasse teria consumido o recurso mais escasso. As duas coisas podem ser verdade ao mesmo tempo, mas o texto não as reconcilia, e o leitor fica com duas conclusões opostas. Uma frase de ligação resolve: o registro tem valor, mas não necessariamente valor que cubra o custo.

**B13. A premissa central não tem âncora (5.1 §1).** "A party that shares responsibility for quality has to be able to show how it carries its share." O argumento todo da tese repousa nisto, e a frase é afirmada sem apoio. Ancore nos deveres de registro do investigador (E6(R3) e ISO 14155:2026, 10.x), ou apresente como posição da tese.

**B14. Afirmações acima da evidência:**
- **5.2 §5:** "so that the instruments carry the quality function that an academic hospital receives from its trial unit". Instrumentos não substituem uma equipa; "part of the quality function" seria proporcional.
- **5.4.1 §3:** "only the sponsor can ask for the reasoning behind it". A comissão de ética e o inspetor também podem.
- **5.1 §2:** "The site is the only party that sees these risks as they arise". Ver C1.
- **5.5.3 §2:** "A standard of this kind… would also solve the fragmentation". "Could reduce" seria proporcional.

**B15. Frase obscura (5.6.2 §1).** "the design already limits its consequence by keeping the regulatory analysis and the derivation independent of any expected effect". Não se entende como isso limita a consequência da falta de implementação. Explique em uma frase (por exemplo: a falta de teste não invalida as lacunas nem os requisitos, só os efeitos esperados) ou corte.

---

## C. Pontos cegos operacionais

**C1. Representantes do fabricante no bloco operatório.** Nos ensaios de próteses ortopédicas, o especialista clínico do fabricante costuma estar presente na cirurgia, apoia a técnica e muitas vezes recolhe as etiquetas dos implantes. Isso derruba "the site is the only party that sees these risks as they arise" (5.1 §2) e toca a rastreabilidade e o ICDL. A tese não menciona esta figura uma única vez. Um arguente da indústria vai perguntar como o framework convive com ela: quem regista, o conflito de interesse e o que acontece quando o representante corrige a técnica em tempo real.

**C2. Laboratórios centrais de imagem.** A 5.5.2 §6 diz que os sistemas dos CROs "cannot establish whether an image was acquired as the charter required". Os laboratórios centrais de imagem (core labs) fazem exatamente isso: verificam a conformidade com o protocolo de imagem e emitem queries ou rejeitam a imagem. O argumento certo é de tempo. O core lab deteta depois, quando a janela de visita pode já ter fechado, e o IQL deteta no momento da aquisição. Reescreva assim; hoje a frase está factualmente fraca.

**C3. SMOs e redes de centros.** Nos EUA, onde estão 63 das 68 organizações nonhospital do registro, as organizações de gestão de centros (SMOs) e as redes de centros existem justamente para dar a consultórios independentes SOPs, coordenadores e qualidade. A tese não as menciona. É a alternativa óbvia ao framework para o centro-alvo, e a discussão precisa dizer por que o framework continua necessário: por exemplo, o conteúdo CtQ do dispositivo, ou o facto de o centro na Europa raramente ter SMO. Verificar a literatura antes de afirmar.

**C4. Precedentes de acreditação de centros (5.5.3 §2).** "Whether sites should one day be accredited in this way is beyond what this thesis can answer." Existem esquemas que acreditam ou registam centros de investigação: acreditação de unidades de fase I no Reino Unido, acreditação de programas de proteção de participantes (AAHRPP) e registo obrigatório de instituições de ensaios em algumas jurisdições. Verifique e cite os relevantes, ou retire a sugestão de que a ideia é inédita. Sem isso, a frase parece ignorar o campo.

**C5. Ética da informação sobre o cirurgião (5.5.4).**
- "keep every action… within the scope of the investigation": se a revisão mostra que um cirurgião opera mal, o centro pode guardar essa informação dentro do ensaio enquanto o cirurgião opera doentes fora dele? Há um dever de governação clínica que a tese não discute.
- A codificação do cirurgião com a chave guardada pelo PI não protege nada num centro com um ou dois cirurgiões, nem quando o PI é o próprio cirurgião, caso que o texto descreve no parágrafo seguinte.

**C6. Dupla documentação.** O ICDL, o registro operatório do hospital e o CRF registam os mesmos dados. A 5.5.2 §4 trata o ICDL como possível fonte, mas o texto não discute o risco de três registros do mesmo dado divergirem (princípios de dado-fonte, ALCOA+). Isso é o que um monitor vai perguntar primeiro.

**C7. Método da Tabela 5.2.** "This is our own assessment, made without data from a site" (5.3.3 §1). Um terceiro não consegue refazer a tabela, porque o método não está descrito. Diga como os modos de falha foram identificados (percurso fase a fase pelo ciclo de vida, por exemplo) ou apresente a tabela como ilustrativa.

---

## D. Repetições

**Dentro do cap. 5:**

| Ideia | Onde aparece |
|---|---|
| 1 de 247 ensaios analisou aprendizagem | 5.2 §3 e 5.5.2 §5 |
| Cláusula 6.8 (qualificação do centro) | 5.3.1 item 1 e 5.5.2 §3 |
| Revisor que é empregado do cirurgião | 5.3.3 §2 e 5.5.4 §2 |
| 15 de 24 instrumentos atuam no arranque | 5.3.1 item 6 e 5.4.2 §2 |
| Os cinco registros do momento clínico | 5.3.1 item 7, 5.4.1 §1 e 5.5.1 §3 |
| Comissão de eventos clínicos (CEC) | 5.4.4 §3, 5.5.2 §4 e 5.5.3 §1 |
| Analogia fabricante / laboratório (ISO 13485, ISO 15189) | 5.1 §5 e 5.5.3 §2; no total aparece cinco vezes na tese (caps. 2, 3, 4 e 5) |

**Cap. 5 contra cap. 1:** ver A1, e ainda EN ISO 14155:2020+A11 (5.4.4 §3) e os "2 of 12 randomized trials" (5.6.3 §3).

**Cap. 5 contra cap. 4:** ver A2, e ainda as três frentes de risco da Cláusula 6.2 (5.5.3 §1 repete 17 palavras seguidas do cap. 4) e "The indicator does not rank surgeons" (5.5.4 §1).

---

## E. Escrita

**E1. Tiques de conector.** Em ~8.300 palavras:

| Palavra | Ocorrências |
|---|---|
| "while" | 25 |
| "only" | 24 |
| "together with" | 10 |

"Together with" virou a forma padrão de desmontar tríades e agora é ela própria um padrão audível. Muitas frases seguem o molde "X, and Y, while Z".

**E2. Aberturas e fechos que anunciam ou fazem efeito:**
- **5.2 §1:** "…and the text below discusses those that shaped the design" anuncia.
- **5.3 §1:** "The route below assumes…" também.
- **5.1 §3:** fecha com "they are what turns a list of instruments into something a site can run", frase de efeito.
- **5.4.3:** "The claim stops at…" é a forma curta assertiva da sua lista de padrões a evitar.

**E3. Mudança de registro em 5.5.2 §1–2.** Estes dois parágrafos foram escritos noutra voz:
- passiva administrativa ("Signals requiring sponsor notification… are communicated");
- verbos formais ("establish", "initiate", "complements");
- apóstrofo curvo ("sponsor’s"), quando o resto usa o reto.

Parecem colados junto com a Figura 5.1. Harmonize com o resto.

**E4. Defeito introduzido por mim na limpeza das remissões.** Na 5.6.2 §2 ficou "the position of this work in the literature rests only on the works we found and read, a position that a systematic search can test", com "position" repetido. Proposta: "…rests only on the works we found and read, which a systematic search can test."

**E5. Parágrafo-toco.** A 5.6.2 §6 ficou com duas frases ("Some choices… are delimitations… They set the scope of the claims."). Junte-a ao §5 ou desenvolva-a.

**E6. Títulos.**
- O 5.1 ("What the thesis set out to do and what it delivered") promete os objetivos, e a secção não volta a eles.
- O 5.3.5 é o único título em forma de pergunta na tese.

---

## F. Apresentação visual

**F1. Tabela 5.1.** Pela largura da imagem, a letra fica em cerca de 5 pt impressa. É ilegível em papel. Há duas soluções: página em paisagem com letra maior, ou menos texto por célula.

**F2. Tabela 5.4.** Só tem siglas, 24 em monoespaçado. Sem os nomes, não informa nada a quem não decorou o cap. 4. Junte os nomes ou uma legenda.

**F3. Figura 5.1.**
- A linguagem visual é outra: fluxograma em tons pastel e outra fonte, diferente das tabelas em Plex.
- É estreita, e o texto interno fica pequeno.
- É citada na 5.3.2 §2 e só aparece na 5.5.2, sete páginas depois.

Alinhe o estilo com as tabelas e aproxime a figura da primeira citação, ou cite-a só na 5.5.2.

**F4. Tabelas 5.2 e 5.3.** São densas e com letra pequena. Ficam legíveis, mas no limite.

---

## G. Prioridades sugeridas

1. **Conflitos:** resolver B1–B5. São os que um arguente usa contra a tese.
2. **Pontos cegos:** acrescentar C1 a C3, uma frase ou um parágrafo cada. C2 corrige uma afirmação fraca.
3. **Repetição:** cortar a 5.2 para o que é posicionamento (A1) e decidir o destino da 5.3.1–5.3.2 (A2) junto com a reescrita do cap. 4.
4. **Ressalvas:** concentrar na 5.6.2 (A3, A4).
5. **Siglas e nomes:** reduzir na 5.3 (A5) e unificar nomes (A6).
6. **Visual:** Tabela 5.1 legível, Tabela 5.4 com nomes, Figura 5.1 no estilo da tese.
7. **Escrita miúda:** E1–E6.

## Perguntas para você

1. Na A2: o percurso da 5.3.1–5.3.2 vai para o cap. 4 ou fica reduzido na 5.3?
2. Na B3: prefere dar um horizonte mínimo a cada proposição ou tirar "testable" da Tabela 5.3?
3. Na C1 e C3: confirma que, na sua experiência, o representante do fabricante está no bloco nos ensaios de ombro, e que SMOs são relevantes para o centro-alvo europeu? Isso define o tamanho da resposta no texto.
4. Quer que eu aplique já as correções pequenas e seguras (E4, E5, B6, B14, A6) e deixe as estruturais para depois do cap. 4?
