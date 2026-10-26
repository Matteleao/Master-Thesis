# Flags: instrumentos x texto (cap. 4) e cap. 2-3
Gerado a partir dos PDFs e HTML enviados em 25/10. Falta só o IMP (Internal Monitoring Plan).

## Conflito com cap. 2-3 (lei)
- SRR v0.1, seção C: lista própria de 12 "CtQ domains" diferente da Tabela 3.2 (nomes, número e conteúdo). Não tem "site capability" (dom. 1); cria "PI oversight" e "Delegation and training"; separa "Surgical technique" e "Learning curve"; numeração toda diferente. Substituir pela Tabela 3.2.
- SRR v0.1: cada entrada liga a um CtQ domain; pela 3.3 (lei) o site identifica os CtQ factors dentro de cada domínio no início, e o risco deveria ligar ao fator (com o domínio). Acrescentar campo "CtQ factor".
- IMC v1.3: usa "Operational Control Domain" (e "domains" em todo o documento) para outra coisa; colide com os 12 CtQ domains (um objeto, um nome). Trocar por "operational control area" ou similar.
- CAPA v0.10: campo "CTQ / operational domain"; alinhar aos 12 domínios da Tabela 3.2.
- CSST v1.0: cita "ISO 14155:2020"; a tese usa ISO 14155:2026.
- Grafia britânica nos modelos (authorised x16, prioritise, catalogue, summarise, materialised, localised, specialised); a tese usa inglês americano.
- RACI v0.3: campo "Site type (scalability model) Type A/B/C"; depende da revisão da 4.7.1 (conflito já registrado com a 3.4.5).

## Instrumento x texto do cap. 4 (decidir qual se ajusta)
- MRL v0.2 tem 13 marcos (M0 a M12); a 4.2.1 diz que o PI revisa em quatro pontos (implementação do procedimento, pós-operatório imediato, aproximação da avaliação de endpoint e close-out).
- MRL v0.2 rodapé "Pillar 1 - Principal Investigator Oversight"; o pilar se chama Governance.
- MRL v0.2 M5 "after first 3-5 cases per surgeon": é momento de revisão, não limiar de proficiência, mas a 4.3.2 diz que o framework não adota contagem fixa; conferir a redação.
- [RESOLVIDO NO TEXTO 25/10] SCR v0.5 + TRE v0.4: o SCR vem antes e é pré-requisito da liberação no TRE (seção B); a liberação específica do dispositivo fica no TRE. O texto (4.2.3 e 4.2.4) diz o contrário: a liberação no treinamento do dispositivo alimenta a decisão do SCR.
- [RESOLVIDO NO TEXTO 25/10] RACI v0.3: "Read with the CCDM, the RACI is the site's delegation log" e o RACI é quem recebe o resultado do SCR/TRE. A 4.2.4 diz que "the CCDM carries the resulting authorization into the delegation record".
- RACI v0.3 seção C: sete funções (inclui operating surgeon); a Tabela 4.1 tem seis.
- RACI v0.3: PI sem backup para decisões C1; a 4.2.2 diz que cada função tem backup nomeado.
- CCDM v0.2: arquivo substituído no GitHub em 25/10 pela versão correta (sem CDTR; atribuição de pessoas fica no RACI). Resolvido.
- CCDM v0.2 (novo): coluna "CtQ domain" por tarefa deve usar os 12 domínios da Tabela 3.2.
- DTRM v0.2 organiza o treinamento por módulos e perfis; a 4.2.3 fala em cinco training areas. Os módulos podem seguir as cinco áreas.
- SRR v0.1 classifica impacto em quatro dimensões (safety, procedure, device accountability, data reliability) + probabilidade + detectabilidade -> prioridade Low/Moderate/High/Critical; a 2.5.2 fala em probability, detectability e impact (compatível).

## Regra do autor (25/10)
O texto é a referência: os modelos se ajustam ao texto, salvo quando o modelo estiver mais correto (caso SCR antes do TRE, aceito pelo autor).

## SLCT v0.3 (conferido em 25/10, revisão da 4.3.2)
- Disposição "Adapt controls" manda "Update TRE, SCR or CCDM". O CCDM só define criticalidade; mudança de escopo de uma pessoa vai para o SCR (decisão) e o RACI (atribuição). Trocar CCDM por RACI.
- Estratos de complexidade: o SLCT define três contextos (lower, standard, higher), definidos pelo site. A 4.8 diz "five complexity strata used in the learning curve log" (ver lembretes M5).
- MRL M5 "after first 3-5 cases" e SLCT revisão "Cases 1-5, 6-10": alinhar os dois. São pontos de revisão, não limiar de proficiência (a 4.3.2 diz que o framework não adota contagem fixa).

## SCML v0.3 e CSST v1.0 (conferido em 25/10, revisão da 4.3.3)
- CSST seção C traz limiares "Suggested: 5%" (categoria ligada ao dispositivo), "10%" (intraoperatório total) e "5%" (luxação precoce em rTSA), sem fonte. O texto diz que o site define os limiares antes; os números sugeridos precisam de fonte ou devem sair do modelo.
- CSST: rodapé "Page 3 of 2" (tem 3 páginas).
- CSST: "ISO 14155:2020, Cl. 10.8(b)" (já registrado acima): usar ISO 14155:2026.
- SART: PDF não está no repositório; a 4.3.3 usa só a descrição da Tabela 4.3.
- MRL v0.2 M7 (safety / complication signal review): "Monthly, quarterly, or immediately". A 4.3.3 e a Figura 4.1 fixam revisão de tendência de segurança pelo menos mensal; tirar "quarterly" ou deixar como intervalo máximo mensal.

## FUCR, PIR, POT, SIFSL, SART (HTML, conferidos em 25/10)
- FUCR v0.4 e PIR v0.10 chamam o log de imagem de "ICQL"; o instrumento é IQL (Imaging Quality Log). Unificar.
- POT v0.9 diz que imprime "eight framework triggers" de escalonamento; a 4.2.1 não fala em oito gatilhos. Conferir na revisão da 4.8 ou ajustar o texto.
- POT v0.9: campo "Site type (scalability model) Type A/B/C" (depende da 4.7.1) e "meeting architecture" (trocar architecture).
- PIR v0.10: limiares (FC-01 95%/90%; DC-01 98%/95%, mediana de query 7/14 dias; ST-01 janela de 24 h; PD-01 3 desvios menores) a conferir contra a 4.5 quando revisarmos.
- PIR v0.10: domínios CtQ dos indicadores batem com a Tabela 3.2 (EQ-01 2, PD-01 12, FC-01 7, ST-01 10, SP-01 5 e 6, DC-01 11). OK.
- SIFSL v0.2: fica em Operational Controls; não precisa virar um instrumento de agregação como o FUCR (inclusão gera pouco volume; o PIR EQ-01 calcula direto do PSEAR e do SIFSL). Sugestão: na seção E, manter só a contagem de motivos (desfecho, motivo, contagem, etapa) e tirar as colunas de interpretação e ação, que ficam no PIR.
- FUCR v0.4: passa para Performance Oversight (decisão do autor, 25/10).

## IMC v1.3 (conferido em 25/10, revisão da 4.4.1)
- Verificação "Early complication pattern review": no texto passa a confirmar que a vigilância de complicações (SCML/CSST) rodou no prazo e que os sinais foram tratados; a análise do padrão fica no CSST. Ajustar o domínio do IMC para não refazer a análise.
- IMC funciona como a autoinspeção periódica do DR5 (texto da 4.4.1); conferir se a 4.5.7 e o CAPA log tratam a mesma autoinspeção sem criar um segundo cronograma.

## SIRR v0.4 e IQL v0.3 (conferidos em 25/10, revisão da 4.4.2)
- SIRR organiza a prontidão em quatro elementos (aquisição; exibição, transferência e arquivo; revisão local; tempo e manutenção). O texto da 4.4.2 usa quatro elementos diferentes (definir a aquisição; qualificar e treinar pessoas, com calibração; revisão local; momento da imagem). Alinhar o SIRR ao texto (qualificação e treino como elemento próprio; transferência e arquivo dentro do registro de cada imagem, no IQL).
- IQL v0.3: "authorised" (grafia britânica); e o nome do instrumento aparece como ICQL no FUCR e no PIR (já registrado).
- PIR v0.10, PD-01: usa "domain" para as áreas de desvio (consent/eligibility, procedure/device, imaging, follow-up, safety, documentation); a 4.5.2 usa "area" para não confundir com os 12 domínios CtQ. Trocar no PIR. O texto também diz que os critérios de "important" vêm do sponsor (E6(R3) 3.9.3) e que o PI classifica no site; conferir se o PIR e o CCDM refletem isso.

## FUCR v0.4 e PIR v0.10, FC-01 (conferidos em 25/10, revisão da 4.5.3)
- Categorias de causa diferentes: o FUCR E2 atribui como Site-controlled, Participant-driven, Protocol/design-related, Mixed ou Not assessable; o PIR FC-01 usa Participant, Site, Workflow, Protocol, Unknown. A 4.5.3 fala em participante, processo do site ou desenho do protocolo. Usar uma lista só nos dois (a do FUCR cobre o texto).
- PIR FC-01 m2 diz "every critical component"; o FUCR diz "every required component" e a 4.5.3 segue o FUCR ("every component the CIP requires"). Trocar no PIR.
- FUCR seção F (checagem de método só quando planejada ou quando omissões se repetem) bate com a 4.5.3. OK.

## PIR v0.10, ST-01 (conferido em 25/10, revisão da 4.5.4)
- ST-01 m1 fixa "(24 h)" como janela de notificação inicial. A ISO 14155:2026 pede "without unjustified delay" com o detalhe que o CIP especificar, e a 4.5.4 diz que o intervalo vem do CIP. Trocar "24 h" por "CIP interval" (o 24 h pode ficar só como exemplo).
- ST-01 é a única regra que não usa valor escolhido pelo site: o limite vem do CIP (uma notificação inicial atrasada já é ação). Bate com a 4.5.4. OK.

## PIR v0.10, DC-01 (conferido em 26/10, revisão da 4.5.6)
- DC-01 m3 fixa "Operative notes finalised inside 48 h"; a 4.5.6 diz que o site define o intervalo. Trocar por "inside the site interval" (48 h só como exemplo). "finalised" é grafia britânica.
- DC-01 regra (98%/95%, mediana de query 7/14 dias, 3 notas atrasadas, discrepância não corrigida, 2 medidas piores em 2 meses seguidos) bate com a lógica da 4.5.6, que não traz números. OK.

## IMC v1.3 (26/10, decisão D10)
- A 4.4.1 passa a ter dez verificações; a nova é "Endpoint data agreement" (amostra de registros, campos críticos de endpoint no CRF conferidos contra a fonte, discrepância corrigida com causa registrada). Acrescentar o domínio ao IMC, e o resultado alimenta a quarta medida do DC-01 no PIR (m4, source–CRF agreement in sample).

## Varredura de split brain (26/10; ver revisao/split-brain-cap4.md)
- PFVR: tem campos de resultado (ROM, força, escore funcional, PRO). Só servem como fonte se a definição de fonte do site atribuir esses dados ao PFVR. Senão, o campo vira referência ao registro que guarda o resultado. Pôr essa instrução no modelo.
- RACI: o modelo já diz "the RACI is the site's delegation log" (bate com a troca 10). Acrescentar: quando o sponsor exige o próprio delegation log, o RACI remete a ele.
- SART: o boundary do modelo já diz que não substitui fonte, CRF nem formulários do sponsor. OK; conferir se os campos de classificação são marcados como "as reported in" e não como registro próprio.
- SCML: marcar a avaliação de entrada como preliminar e prever a troca pela classificação final do investigador.
- IMC: a verificação nova vale só para os campos registrados fora do CRF (a ISO 7.8.2 diz que o CIP define o que entra direto no CRF).
- ICDL: deixar claro que é fonte só do que a definição de fonte do site atribuir a ele.

## CAPA v0.10 (conferido em 26/10, revisão da 4.5.7)
- O modelo se define como "portfolio log" que "does not replace the authorized QMS CAPA" e pede para reconciliar com o "authorised QMS CAPA register". O centro-alvo não tem QMS (Gap 1), então o CAPA log é o próprio registro de cada ação. Ajustar: o log é o registro da CAPA, e só quando a instituição já tem um sistema de CAPA ele remete a esse sistema (regra da 4.1). Hoje, para o centro-alvo, o modelo cria dois registros (Master CAPA Register e QMS CAPA).
- "authorised" (grafia britânica).
- Fechamento só com eficácia verificada ou limitação documentada: bate com a 4.5.7 e com o PIR. OK.
