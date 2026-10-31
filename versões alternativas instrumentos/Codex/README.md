# Versões alternativas de instrumentos · Codex

Esta pasta reúne as alternativas HTML produzidas pelo Codex para comparação e revisão pelo autor. As primeiras versões e as reaplicações aos primários coexistem, com seus nomes e números preservados.

Branch de trabalho: `codex/thesis-work`.

## Fluxo definido pelo autor em 31/10/2026

- Acrescentar aqui cada novo HTML gerado neste fluxo de revisão de instrumentos.
- Preservar todas as versões anteriores; uma nova alternativa recebe um nome/versionamento próprio.
- Manter aqui tanto as alternativas produzidas a partir de uma base intermediária quanto as reaplicadas ao primário.
- Usar a análise correspondente em `instrumentos-concluidos/análise instrumentos manuais/` e conferir o template primário. Os originais do branch `claude/claudinho-status-check-8tzmxz` são fontes de consulta.
- Distinguir arquivos antigos da raiz dos HTMLs já reconstruídos em `revisao/instrumentos` e das versões concluídas copiadas para o branch Codex. Editor e componentes visuais comuns podem ser reutilizados.
- Conferir editor, preenchimento/salvamento e paginação antes de acrescentar uma entrega.
- Gerar PDFs e demonstrações preenchidas quando solicitados; preservar a identificação blank/filled no nome.

## Inventário: 19 HTMLs, 15 instrumentos

| HTML | Base / origem |
|---|---|
| [CAPA_Corrective_and_Preventive_Action_Log_v0.11_blank_editable.html](CAPA_Corrective_and_Preventive_Action_Log_v0.11_blank_editable.html) | HTML v0.10 editado pelo autor, com simulação removida. |
| [CSST_Complication_Signal_Surveillance_Template_v0.2_blank_editable.html](CSST_Complication_Signal_Surveillance_Template_v0.2_blank_editable.html) | Construção independente a partir da análise de reconcepção. |
| [FUCR_Follow-up_Compliance_Review_v0.5_blank_editable.html](FUCR_Follow-up_Compliance_Review_v0.5_blank_editable.html) | Primeira alternativa: base local v0.4, com cinco páginas. |
| [FUCR_Follow-up_Compliance_Review_v0.6_blank_editable.html](FUCR_Follow-up_Compliance_Review_v0.6_blank_editable.html) | Reaplicação: HTML v0.4 (2) original da raiz do branch Claude. |
| [ICDL_Intraoperative_Checklist_and_Device_Log_v0.14_blank_editable.html](ICDL_Intraoperative_Checklist_and_Device_Log_v0.14_blank_editable.html) | HTML legado v0.12 indicado na análise. |
| [IMC_Internal_Monitoring_Checklist_v1.5_blank_editable.html](IMC_Internal_Monitoring_Checklist_v1.5_blank_editable.html) | Primeira alternativa: HTML local v1.4. |
| [IMC_Internal_Monitoring_Checklist_v1.6_blank_editable.html](IMC_Internal_Monitoring_Checklist_v1.6_blank_editable.html) | Reaplicação: HTML legado v1.3, versão do PDF original da raiz. |
| [IMP_Internal_Monitoring_Plan_v0.2_blank_editable.html](IMP_Internal_Monitoring_Plan_v0.2_blank_editable.html) | Construção do zero a partir da análise, sem usar o IMP v0.1. |
| [IQL_Imaging_Quality_Log_v0.6_blank_editable.html](IQL_Imaging_Quality_Log_v0.6_blank_editable.html) | Primeira alternativa: evolução local dos rascunhos v0.4/v0.5, inicialmente derivados do v0.3. |
| [IQL_Imaging_Quality_Log_v0.7_blank_editable.html](IQL_Imaging_Quality_Log_v0.7_blank_editable.html) | Reaplicação direta ao HTML legado v0.3, sem ler o corpo dos IQLs revisados. |
| [MRL_Milestone_Review_Log_v0.4_blank_editable.html](MRL_Milestone_Review_Log_v0.4_blank_editable.html) | Aplicação da análise ao primário legado v0.2, conferido contra o PDF da raiz do Claude. Não usa o MRL v0.3 já reformulado. |
| [PFVR_Participant_Follow-up_Visit_Record_v0.6_blank_editable.html](PFVR_Participant_Follow-up_Visit_Record_v0.6_blank_editable.html) | Aplicação da análise v0.5 ao HTML primário v0.3, correspondente ao PDF da raiz do Claude. |
| [PIDLR_Post_Investigation_Debrief_and_Lessons_Record_v0.3_blank_editable.html](PIDLR_Post_Investigation_Debrief_and_Lessons_Record_v0.3_blank_editable.html) | Aplicação da análise ao PIDLR v0.2 primário editado pelo autor, preservando a estrutura de sete páginas. |
| [PIR_Performance_Indicator_Record_v0.11_blank_editable.html](PIR_Performance_Indicator_Record_v0.11_blank_editable.html) | Revisão do primário v0.8 citado na análise; v0.10 da raiz conferido como referência de comparação. |
| [PSEAR_Participant_Screening_and_Eligibility_Assessment_Record_v0.92_blank_editable.html](PSEAR_Participant_Screening_and_Eligibility_Assessment_Record_v0.92_blank_editable.html) | Primeira alternativa: HTML local v0.91. |
| [PSEAR_Participant_Screening_and_Eligibility_Assessment_Record_v0.93_blank_editable.html](PSEAR_Participant_Screening_and_Eligibility_Assessment_Record_v0.93_blank_editable.html) | Reaplicação: HTML legado v0.7, versão do PDF original da raiz. |
| [SIFSL_Subject_Identification_and_Failure_Screening_Log_v0.4_blank_editable.html](SIFSL_Subject_Identification_and_Failure_Screening_Log_v0.4_blank_editable.html) | Construção independente da especificação; original v0.2 conferido. |
| [SIRR_Site_Imaging_Readiness_Record_v0.5_blank_editable.html](SIRR_Site_Imaging_Readiness_Record_v0.5_blank_editable.html) | Revisão do HTML primário v0.4, correspondente à referência PDF da raiz do Claude. |
| [SRR_Site_Risk_Register_v0.92_blank_editable.html](SRR_Site_Risk_Register_v0.92_blank_editable.html) | Aplicação da análise ao HTML primário v0.1, correspondente ao PDF da raiz do Claude; sem usar o SRR v0.9/v1.0 já reformulado. |

Para IMC, IQL e PSEAR, os PDFs antigos locais foram identificados por Git blob como idênticos aos originais da raiz do branch Claude; os HTMLs legados locais da mesma versão serviram como contrapartes editáveis. O hash do PDF não afirma equivalência binária entre PDF e HTML.

As versões preexistentes nas outras pastas do repositório são preservadas. Este índice mantém a origem de cada alternativa explícita para a comparação do autor.

## MRL v0.4: origem e revisão

- Primário editável: `HTML/Desatualizados/MRL_Milestone_Review_Log.html` local, Git blob `b57736619cbb3eceb645656b36fe68348d636c6a`.
- Referência do branch Claude: `MRL v0.2 Blank.pdf`, Git blob `eed948fd89c9bfb52a35009675f61baef4f9e368`; o PDF local tem o mesmo hash e seu conteúdo foi conferido contra o HTML legado.
- Análise aplicada: `Análise - MRL - Milestone Review Log v0.3.md`, Git blob `5c5853432ba41a24f97995727b5b90a2d083e592`.
- Escopo: decisão formal de gate, com unidade/denominador, configuração prospectiva, evidência, suficiência, escopo permitido/bloqueado, condições e re-review. Rotinas do POT e registros especializados conservam suas avaliações próprias.
- Entrega blank em sete páginas, sem dados simulados nem opções selecionadas. Editor e paginação testados, incluindo salvar/reabrir o HTML.

## SRR v0.92: origem e revisão

- Primário: HTML legado `HTML/Desatualizados/SRR_Site_Risk_Register.html`, Git blob `08a3a9b5627ed85b9f69d6dbac79b7b350d7f66e`.
- PDF de referência: `SRR v0.1 Blank.pdf`, Git blob `3d73db9639aee27b19341e0e499136d9c8c3843c`; as cópias locais têm o mesmo hash.
- Análise: `Análise - SRR - Site Risk Register v0.91.md`, Git blob `1283248480814900f9864316474c6a68ce9541e2`.
- Revisão: fator CtQ específico e sua fonte; prioridade atual/residual pelo maior score aplicável, sem média/produto; N/A e Critical explícitos; controles implementados separados de ações planejadas; risco e estado da ação independentes; revisão com evidência de efetividade; ponte urgente para Risk ID e rota competente; aceitação/fechamento com justificativa.
- A referência de domínios foi atualizada para o catálogo de 12 domínios, considerando o item X-list do requisito SRR. O perfil separado de fatores CtQ proposto em X-CtQ não foi tornado obrigatório.
- Seis páginas. Registros de trabalho em branco; ilustração de preenchimento confinada à orientação E, sem estudo, datas, participantes ou Risk IDs simulados. Editor e paginação testados, incluindo salvar/reabrir.

## PIDLR v0.3: origem e revisão

- Primário: `PIDLR_Post_Investigation_Debrief_and_Lessons_Record_v0_2_edited_2026-09-29_13-02-59.html`, Git blob `1480c522f785f586e95eabd3247167271a22ad39`, indicado na análise. O HTML legado v0.2 não editado também foi conferido (`64695fcacc44a4cf8e15a9a868c5b3f621221055`).
- Referência da raiz do Claude: `PIDLR v0.2 Blank.pdf`, Git blob `a99a8b9d6821cdbacfaf7113b9b022e4fc3de6be`; as cópias locais correspondem a esse hash. Nenhum PIDLR já reconstruído foi usado como base.
- Análise aplicada: `Análise - PIDLR - Post-Investigation Debrief and Lessons Record v0.2.md`, Git blob `b0be77e0f111f87b6facb7522779a4f0f9cf38cc`.
- Revisão conservadora em sete páginas A–I: fontes aplicáveis e limitações; revisão seletiva das sete fases e segurança transversal; síntese com contribuintes sustentados por evidência; seis tipos de lição; transferência com escopo, destino e dono; limitações residuais; transferência, implementação e efetividade diferenciadas; fechamento com itens controlados fora do debrief e arquivo recuperável.
- Registros de trabalho em branco e nenhuma opção pré-selecionada. Cabeçalho em todas as páginas. Editor testado (texto, formatação, linhas, colunas, caixas, opções, desfazer/refazer e salvar/reabrir); sete páginas inspecionadas, sem overflow, com distância mínima ao rodapé de 29 px.

## PIR v0.11: origem e revisão

- Primário da análise: `Performance_Indicator_Record_v0.8.html` local, Git blob `5bd168384f5b8c3ff4fc5a0cf7ad3211e7ddb5e4`. Seu conteúdo e o v0.8 preenchido descrito na análise orientaram a revisão, sem importar dados simulados para o blank.
- Referência da raiz de `claude/claudinho-status-check-8tzmxz`: `Performance_Indicator_Record_v0.10.html`, Git blob `7dd00dbc153b5c674a7cdaa5fb8fd41acfa777a9`, idêntico à cópia local conferida. Não foi usado um PIR reconstruído das pastas de revisão.
- Análise aplicada: `Análise - PIR - Performance Indicator Record v0.8.md`, Git blob `5ee74a66110da052d55e0b8242422d64a945f4fc`.
- Sete páginas: escopo; catálogo/configuração; reconciliação e resultado com interpretação integrada; duas folhas de detalhes dos seis indicadores; ações/efetividade; conclusão e revisão. Os IDs EQ-01, PD-01, FC-01, ST-01, SP-01 e DC-01 permanecem consistentes. Bases de cálculo distinguem decisões, visitas, procedimentos, casos, campos, queries e entradas amostradas.
- Regras configuradas prospectivamente, com versão/data, condições de decisão e referência controlada. Sem valores universais impostos para intervalos CIP, notas operatórias ou percentuais. Mantidas as quatro medidas de follow-up e de dados críticos; resultados e interpretações limitados ao período/fontes. Ações têm rota, destino, dono, prazo e verificação separada da conclusão da ação.
- Blank sem valores simulados ou opções selecionadas. Catálogo em paisagem e demais folhas em retrato. Sete páginas renderizadas/inspecionadas, sem overflow e com folga mínima de 28 px até o rodapé. Editor testado, incluindo salvar/reabrir com texto, formatação e opções preservados.

## SIRR v0.5: origem e revisão

- Primário: `SIRR_Site_Imaging_Readiness_Record_v0.4_blank_editable.html` local, Git blob `97ffaa54c403b8dbfe2e70c67f7e71a361dda45a`. Nenhum SIRR reconstruído nas pastas de revisão foi usado como base.
- Referência da raiz do Claude: `SIRR v0.4 Blank.pdf`, Git blob `d5f86050a800d353a1160736f23e48afd1b07320`; as duas cópias locais conferidas têm o mesmo hash. O hash do PDF não implica identidade binária com o HTML.
- Análise aplicada: `Análise - SIRR - Site Imaging Readiness Record v0.4.md`, Git blob `d6e0e717b60fc951e80a50c42558a7c071974636`.
- Preservadas quatro páginas, com mapping em paisagem. Purpose and Use padronizado; controle de fonte/versão/vigência/recebimento; IDs de requisito estáveis por SIRR; implementação, evidência, gap e ação distinguíveis; manutenção/calibração com validade; teste de transferência/recuperação referenciado; funções com treinamento/delegação/liberação; rotas e gatilhos de reavaliação explícitos.
- Os controles de função antes repetidos na tabela técnica ficam em F, junto das evidências de qualificação e do estado de prontidão da função; G documenta a operação das rotas. E concentra infraestrutura e teste de arquivo/transferência. Cada registro de imagem permanece no IQL; o SIRR recebe somente sinais que afetam o arranjo local.
- Conclusão do site para submissão separada de review, resposta e decisão de ativação externos. A assinatura local não autoriza ativação, enrollment ou uso de imagem. Observações exigem dono, prazo, rota e impacto; gaps críticos impedem Ready.
- Blank sem nomes, datas, estudos ou opções simulados. IDs IMG-01 a IMG-06 são identificadores de linhas de requisito, vinculados ao SIRR, e podem ser continuados sem reutilização. Editor e salvar/reabrir testados; quatro páginas inspecionadas, sem overflow, com folga mínima de 28 px até o rodapé.

## PFVR v0.6: origem e revisão

- Primário: `PFVR_Participant_Follow-up_Visit_Record_v0.3.html` local, Git blob `66f90be50b682ac4b2e06f7e8246c95e31974614`. As alternativas v0.4 locais e os HTMLs já reconstruídos nas pastas de revisão não foram usados como base de conteúdo.
- Referência da raiz do Claude: `PFVR v0.3 Blank.pdf`, Git blob `4df7dbc1c956ffdc3f62c798b2339b0a53e649c7`; as duas cópias locais conferidas têm o mesmo hash. O conteúdo do HTML primário foi lido; o hash do PDF não implica identidade binária entre formatos.
- Análise aplicada: `Análise - PFVR - Participant Follow-up Visit Record v0.5.md`, Git blob `6e9e4be5c68ae1310fa1151ee490f5a4a92523b5`.
- Quatro páginas A–L, com componentes em paisagem: B reduzido a famílias; C documenta ocorrência/timing sem concluir a visita; D registra componente, método especificado/usado, CtQ, data real, completude, timing e evidência; E preserva a lente de utilizabilidade; F/G mantêm síntese clínica e fontes; H é condicional; I deriva a síntese; J limita-se à resposta necessária; K diferencia os seis outcomes; L mantém autoria e filing.
- Componente tardio permanece no mesmo PFVR/visita, com entrada inicial preservada e atualização/continuação datada e atribuída. Cinco linhas repetíveis para componentes e duas para revisão de imagem/teste. FUCR recebe identificação, contagens, causas e impacto, sem taxas agregadas no PFVR. Uma visita perdida não é automaticamente loss to follow-up.
- Blank sem dados simulados ou opções selecionadas. Editor testado (texto, fonte/cor/negrito/itálico/alinhamento, linhas, colunas, caixas, opções, undo/redo e salvar/reabrir); quatro páginas inspecionadas, sem overflow e com folga mínima ao rodapé de 28 px.
