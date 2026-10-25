# Flags: instrumentos x texto (cap. 4) e cap. 2-3
Gerado a partir dos PDFs em main/upload de 25/10. Faltam: POT, SART, IMP, SIFSL, FUCR, PIR.

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
