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

## Inventário: 15 HTMLs, 11 instrumentos

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
| [PSEAR_Participant_Screening_and_Eligibility_Assessment_Record_v0.92_blank_editable.html](PSEAR_Participant_Screening_and_Eligibility_Assessment_Record_v0.92_blank_editable.html) | Primeira alternativa: HTML local v0.91. |
| [PSEAR_Participant_Screening_and_Eligibility_Assessment_Record_v0.93_blank_editable.html](PSEAR_Participant_Screening_and_Eligibility_Assessment_Record_v0.93_blank_editable.html) | Reaplicação: HTML legado v0.7, versão do PDF original da raiz. |
| [SIFSL_Subject_Identification_and_Failure_Screening_Log_v0.4_blank_editable.html](SIFSL_Subject_Identification_and_Failure_Screening_Log_v0.4_blank_editable.html) | Construção independente da especificação; original v0.2 conferido. |
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
