# Diagnóstico da 4.6 a 4.8 (lifecycle, escalabilidade, conjunto de instrumentos), 26/10

Base: o docx do autor de 26/10 (24279554-Revisao_manual_tese_alteracoes_19-10.docx), os capítulos 1 a 3 como lei, a Tabela 3.4 (DR9 e DR12), os modelos dos instrumentos e os dois HTML do quality lifecycle.

## 0. Sincronização com a versão do autor (antes de tudo)

O docx do autor tem a 4.5.3 a 4.5.7 aplicadas e as trocas 1 e 2 da varredura de split brain. Há sete pontos a corrigir ou confirmar:

1. 4.2.1 (Oversight meetings): voltou "the multidisciplinary review of risk recommended in the EMA reflection paper". O texto da EMA não tem "multidisciplinary" e não recomenda isso (conferido no texto da reflection paper). Voltar para "the periodic risk review described in the EMA reflection paper [1]".
2. Referência [77] (Vale et al.): no docx do autor está 2023;16:2353–65. Segundo o PubMed (PMID 37881165, doi:10.2147/RMHP.S426411), as páginas são 2187–2196. Voltar para 2187–96.
3. Pontos duplos: "set its scope.." (4.4.1, 2º parágrafo) e "(Appendix P).." (4.4.2).
4. 4.4.1: a verificação nova ainda está na versão antiga ("In a sample of records, … their source …"). Falta "recorded first outside the CRF" (troca 7), e o 5º parágrafo ainda diz "across all nine checks". A 4.5.6 também está na versão antiga da quarta medida (troca 13).
5. Lista de tabelas: as entradas da Tabela 3.3 e da 3.4 mostram "Erro! Indicador não definido." Refazer o campo (F9) depois de corrigir as legendas.
6. 4.2.4 (último parágrafo): agora diz "the CCDM carries the resulting authorization into the delegation record". Em 25/10 o autor decidiu que o CCDM só define a criticalidade e que quem está com cada tarefa é o RACI, e o modelo do RACI diz "the RACI is the site's delegation log". Confirmar qual vale.
7. 4.8: "nine in Operational Controls, and three in Performance Oversight". Depois de o FUCR passar para Performance Oversight (25/10), são oito em Operational Controls e quatro em Performance Oversight (PIR, FUCR, CAPA, PIDLR). A Figura 4.2 precisa mudar também.

## 1. O que a lei (cap. 1 a 3) pede desta parte

- DR9: "each instrument must be assigned to the phase of the investigation where it has most effect, because a control that is technically correct but mistimed does not do its job". A 4.1 repete a promessa: "A lifecycle assigns every instrument to the phase of the investigation where it acts".
- DR12: a profundidade de implementação escala com os recursos do centro e com o risco da investigação, e a completude e a coerência da trilha documental ficam iguais em qualquer profundidade.
- 3.4.5: o centro-alvo é uma organização nonhospital. "These conditions define the minimum implementation level used in the scalability model." "Organizations with established research departments can place the same functions within their existing systems and use deeper controls."
- 3.4.4: as categorias da Tabela 3.3 dizem que tipo de organização é o site e não quanto ele está preparado ("the readiness of each site … remains unknown").
- 3.3: os domínios foram agrupados "by the area of the site where the work happens and by the phase of the investigation".

## 2. 4.6 Lifecycle

### O que funciona
- A tese central (um controle certo na hora errada não funciona) e os três exemplos.
- Segurança como corrente transversal, e a melhoria contínua como fase de fechamento.
- A 4.6.2 trata a organização por fases como hipótese de desenho, com [22] e [24]. É honesto e bom.

### Problemas
1. O DR9 não é demonstrado. A Figura 4.1 lista ações, não os 24 instrumentos, e o texto não diz em que fase cada instrumento abre, roda e fecha. A promessa da 4.1 e do DR9 fica sem resposta (já apontado na análise anterior, A-041).
2. Inícios contraditórios. A 4.6.2 diz que o learning curve log é iniciado na fase 2, e a 4.3.1 diz que o SRR abre antes do primeiro participante. Mas a Figura 4.1 não traz o SRR, o SLCT, o IMP, as regras do PIR nem o SIRR em nenhuma fase.
3. As fases não estão ligadas aos domínios, apesar de a 3.3 ter derivado os domínios por área e por fase. A ligação existe e é forte: fase 1 → domínio 1; fase 2 → 6 (e a preparação de 4 e 9); fase 3 → 2 e 3; fase 4 → 4 e 5; fase 5 → 7, 8 e 9; segurança → 10; transversais → 11 e 12.
4. Erro de fonte: "causality assessment follows the three risk streams of ISO 14155:2026 Section 6.2". A 6.2 trata das fontes de risco para a gestão de risco do sponsor, não da avaliação de causalidade (que segue o Anexo F). A frase sobre "patient factors … fourth risk stream" depende desse erro.
5. Cláusulas repetidas: ICH E8(R1) 3.3.2 aparece duas vezes, e a E6(R3) 3.10.1.3 é a seção das QTL, não da alocação de recursos (a mesma confusão já corrigida na 4.5).
6. Fase 6, "Final safety report for the whole study period": o relatório final é do sponsor. O site contribui com dados e reconciliação.
7. Estilo: "Two design decisions shape the structure, and neither of them is obvious…", "Three examples make the claim concrete", "In each case the instrument is correct and the timing makes it useless" (frase de efeito); "Section 5.4 presents this as an expected benefit that no measurement has yet confirmed as an inverse proportional relationship" está confuso.
8. Nova casa do PIDLR (decisão de 26/10): a fase 7.

### O achado mais importante: o MRL já é o lifecycle
O modelo do MRL tem os marcos M0 a M12: viabilidade (M0), iniciação e qualificação (M1), primeiro consentimento e triagem (M2), primeiro participante incluído (M3), primeira cirurgia (M4), série inicial e curva de aprendizagem (M5), revisão periódica (M6), sinal de segurança (M7), mudança substancial (M8), prontidão do seguimento (M9), revisão de dados (M10), pré-encerramento (M11), encerramento (M12). Isso é o checklist macro de fase que o HTML tentava ser, e é a pendência D2 (13 marcos no modelo contra quatro na 4.2.1).

Proposta: o MRL vira o registro do lifecycle. Cada passagem de fase é confirmada numa revisão registrada no MRL contra a condição de saída da fase, e os quatro pontos de concentração de risco da 4.2.1 continuam como revisões de marco dentro das fases. Assim o DR9 ganha um instrumento, a D2 se resolve, e a ideia do HTML ganha uma casa.

## 3. O HTML do quality lifecycle (Apêndice Y)

- As fases são diferentes das da tese: no HTML, Safety é a fase 6 e não há melhoria contínua; na tese, segurança é transversal, close-out é a 6 e melhoria contínua é a 7.
- Muitas ações são do sponsor ou da rotina clínica e saíram pelos filtros de responsabilidade e de escopo da 3.3: "Develop recruitment strategy", "DSMB collaboration", "Regulatory reporting", "Prepare regulatory reports", "Participant result communication", "Infection control", "Intraoperative sample collection", "Design intraoperative CRF".
- Os "CtQ" do HTML são rótulos livres ("Institutional Capacity", "Proactive Monitoring") e não os 12 domínios da Tabela 3.2.
- Nenhuma ação aponta para um instrumento.

Conclusão: o HTML é anterior ao framework e hoje contradiz a tese. Ou ele é refeito a partir do mapa instrumento × fase (e passa a ser o próprio checklist do MRL), ou o Apêndice Y sai. A tese também diz que foi gerado com ajuda de IA e que não é validado, o que enfraquece o apêndice.

## 4. 4.7 Escalabilidade

### O conflito com a lei
- 3.4.5 diz que o centro-alvo (nonhospital) define o nível mínimo. A 4.7.1 diz que o alvo é o Type B (clínicas privadas médias e hospitais), com implementação completa, e cria um Type C abaixo dele com um "essential core". Isso põe um nível abaixo do mínimo que a lei definiu.
- Os Types A/B/C são definidos por tipo de organização (hospital acadêmico, clínica média, centro pequeno), mas a 3.4.4 diz que tipo de organização não informa preparo. As categorias da Tabela 3.3 (academic, nonacademic hospital, nonhospital) também não batem com A/B/C.
- Proposta: níveis definidos por capacidade e não por tipo de organização, coerentes com a 3.4.5.
  - Nível base (as condições do centro-alvo): sem unidade de pesquisa nem função de qualidade dedicadas, funções acumuladas, papel ou sistema existente. Todas as funções do framework em forma enxuta. É o mínimo.
  - Nível integrado: o centro com unidade de pesquisa ou sistema de qualidade institucional põe as mesmas funções dentro do que já tem, separa papéis e aprofunda os controles.
  - O risco da investigação (4.7.3) ajusta a profundidade dentro de cada nível (cadência, amostra, segunda revisão).
  - O núcleo reduzido abaixo do mínimo sai. Um centro com pouca atividade reduz cadência e amostra pelo risco, não troca de categoria.
- O autor já disse que os nomes Type A/B/C vão mudar.

### Outros problemas
1. 4.7.2 é uma lista de cláusulas (MDR 72(5), ISO 9.1(b), 10.5, 10.2, 10.3, 7.9, 8.3(a)(4), 9.2.4.5(p), A.6.4, 8.6, Anexo E, 7.5.3; MDR Anexo XV vários; E6(R3) 2.3.2, 2.3.3, 2.5.3, 2.12.2, Apêndice C). Contraria a regra de referências, e boa parte não foi conferida na edição de 2026. A ideia (o que não escala é a evidência ligada às obrigações) é boa e é a segunda metade do DR12. Reescrever sem a lista, com [6, 8, 10].
2. 4.7.1, Type A: as referências [88], [89], [90], [30], [22] sustentam frases soltas ("room for improvement", "units vary", "self-assessment correlational", "surgeons stabilize at different volumes") que não levam a uma decisão de desenho.
3. Tabela 4.2: depende da decisão acima. Hoje tem "quality function", "imaging liaison", "multidisciplinary reviews", "Role architecture" e grafia britânica (specialised, centre, authorisation, programme). "Imaging liaison" não é uma das seis funções da Tabela 4.1.
4. 4.7 intro: "would fail to achieve any significance" e "We aim that every site … is able to use it to the full extent" (inglês travado).

## 5. 4.8 Conjunto de instrumentos

### Para que serve a 4.8 agora
Depois que a 4.2 a 4.5 nomeiam cada instrumento com o apêndice, a 4.8 não precisa reapresentar instrumentos. Ela tem três trabalhos que nenhuma outra seção faz:
1. mostrar o conjunto de uma vez (Tabela 4.3);
2. mostrar como os instrumentos se ligam: registro fino → síntese → decisão, e a decisão voltando como exigência de verificação (Figura 4.3). É também onde a regra da 4.4.4 aparece no conjunto (os registros finos apontam para a fonte);
3. verificar a cobertura: todo domínio tem um controle primário (Figura 4.4) e todo DR tem resposta (Tabela 4.4).

### Problemas
1. Redundância de figuras: a Figura 4.2 (por pilar) repete o agrupamento da Tabela 4.3, e a Figura 4.5 (instrumento × DR) repete a Tabela 4.4 (DR → componente → seção). Proposta: tirar a Figura 4.2 e escolher entre a Figura 4.5 e a Tabela 4.4.
2. A legenda da Figura 4.5 fala em "inherited from a combined or earlier instrument" e "extension added to the original set". O leitor não sabe qual é o "original set": é a história do desenvolvimento, que a tese não conta.
3. Contagem por pilar errada (ver 0.7).
4. Repete a 4.1: "paper-compatible … None requires software … DR11". Abertura que anuncia: "We list them in one place for two reasons".
5. Falta a coluna de fase (DR9). Se o mapa instrumento × fase ficar na 4.6, a Tabela 4.3 ou a 4.4 pode carregar a fase de cada instrumento.
6. O parágrafo sobre adaptar os modelos a outra especialidade é bom e fica.

## 6. Decisões para o autor

1. Escalabilidade: níveis por capacidade, com o mínimo igual ao centro-alvo, e sem núcleo reduzido abaixo dele? (recomendado)
2. MRL como registro do lifecycle (passagens de fase + os quatro marcos da 4.2.1), resolvendo a D2? (recomendado)
3. Apêndice Y: refazer a partir do mapa instrumento × fase, ou tirar? (recomendo tirar agora e, se sobrar tempo, refazer)
4. 4.8: tirar a Figura 4.2 e ficar com a Tabela 4.4 ou com a Figura 4.5? (recomendo tirar a 4.2 e a 4.5 e pôr uma coluna de instrumentos e de fase na Tabela 4.4)
5. 4.2.4: CCDM ou RACI como quem leva a autorização para o delegation record?

## 7. Ordem de trabalho proposta
1. Corrigir a sincronização (seção 0).
2. Decidir os pontos da seção 6.
3. Montar o mapa instrumento × fase (24 linhas: abre, roda, fecha), que vira a espinha da 4.6.
4. Reescrever 4.6 (intro, 4.6.1, 4.6.2), com o PIDLR na fase 7 e o MRL como registro.
5. Reescrever 4.7 a partir da decisão 1, com a Tabela 4.2 nova.
6. Reescrever 4.8 a partir da decisão 4.
7. Listar as mudanças de imagem (Figura 4.1, Tabela 4.2, Figuras 4.2 a 4.5, Tabela 4.4).
