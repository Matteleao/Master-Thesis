# Instrumentos concluídos

Versões consideradas concluídas pelo autor, organizadas no branch `codex/thesis-work`. Os arquivos de trabalho e as versões anteriores permanecem preservados.

Cada instrumento tem quatro arquivos: HTML em branco, HTML preenchido com exemplo fictício e os dois PDFs correspondentes. `filled` significa preenchimento simulado, sem dados reais.

```text
instrumentos-concluidos/
├── HTML/
│   ├── blank/
│   └── filled/
└── PDF/
    ├── blank/
    └── filled/
```

## Arquivos

| Instrumento | Versão | HTML blank | HTML filled | PDF blank | PDF filled |
|---|---|---|---|---|---|
| **CCDM** — Criticality-Coded Delegation Matrix | v0.2 | [blank](HTML/blank/CCDM_v0.2_blank.html) | [filled](HTML/filled/CCDM_v0.2_filled.html) | [blank](PDF/blank/CCDM_v0.2_blank.pdf) | [filled](PDF/filled/CCDM_v0.2_filled.pdf) |
| **DTRM** — Device and Study Training Requirements Matrix | v0.2 | [blank](HTML/blank/DTRM_v0.2_blank.html) | [filled](HTML/filled/DTRM_v0.2_filled.html) | [blank](PDF/blank/DTRM_v0.2_blank.pdf) | [filled](PDF/filled/DTRM_v0.2_filled.pdf) |
| **TRE** — Training Record Evaluation and Release | v0.4 | [blank](HTML/blank/TRE_v0.4_blank.html) | [filled](HTML/filled/TRE_v0.4_filled.html) | [blank](PDF/blank/TRE_v0.4_blank.pdf) | [filled](PDF/filled/TRE_v0.4_filled.pdf) |
| **RACI** — Responsibility Assignment Matrix | v0.3 | [blank](HTML/blank/RACI_v0.3_blank.html) | [filled](HTML/filled/RACI_v0.3_filled.html) | [blank](PDF/blank/RACI_v0.3_blank.pdf) | [filled](PDF/filled/RACI_v0.3_filled.pdf) |
| **SCR** — Surgical Credentialing Record | v0.5 | [blank](HTML/blank/SCR_v0.5_blank.html) | [filled](HTML/filled/SCR_v0.5_filled.html) | [blank](PDF/blank/SCR_v0.5_blank.pdf) | [filled](PDF/filled/SCR_v0.5_filled.pdf) |
| **SCML** — Site Complication Monitoring Log | v0.7 | [blank](HTML/blank/SCML_v0.7_blank.html) | [filled](HTML/filled/SCML_v0.7_filled.html) | [blank](PDF/blank/SCML_v0.7_blank.pdf) | [filled](PDF/filled/SCML_v0.7_filled.pdf) |

| **SLCT** — Surgeon Learning Curve Tracking Log | v0.4 | [blank](HTML/blank/SLCT_v0.4_blank.html) | [filled](HTML/filled/SLCT_v0.4_filled.html) | [blank](PDF/blank/SLCT_v0.4_blank.pdf) | [filled](PDF/filled/SLCT_v0.4_filled.pdf) |

## Pendências que não entram nesta pasta

- **POT v0.9:** o autor pediu nova conferência antes de confirmar a conclusão. Não foi incluído nos arquivos finais.
- **MRL:** suspenso, sem aprovação final.
- **SRR:** encaminhado à montagem externa, sem aprovação final do HTML nesta conversa.

## Critério de inclusão e manutenção

Só adicionar um instrumento quando o autor disser que está concluído. Uma versão mais recente, relatório favorável, correção técnica ou pedido para passar ao próximo não substitui essa declaração. Para cada versão aprovada, manter o par blank/filled em HTML e gerar o par PDF correspondente. Se faltar o preenchido, criar um exemplo fictício antes da exportação.

CCDM v0.2, DTRM v0.2, TRE v0.4, RACI v0.3 e SCR v0.5 foram aceitos no histórico recebido. SCML v0.7 foi confirmado pelo autor em 30/10/2026. SLCT v0.4 teve a inclusão como concluído confirmada explicitamente pelo autor em 30/10/2026. O preenchido SLCT foi criado para esta organização, conforme solicitado; os demais preenchidos já existiam. As versões em branco foram copiadas sem reescrever seu conteúdo.

## Exportação e rastreabilidade

Os PDFs usam paginação A4 do HTML, incluindo páginas em paisagem, cores e texto selecionável. Fontes Arial e Comic Sans MS, já previstas nos modelos, são incorporadas aos PDFs; assinaturas com fallback cursivo usam Z003. Os arquivos de fonte não são redistribuídos nesta pasta. Os HTMLs preservam suas próprias listas de fontes e recursos de edição existentes.

O [manifesto](manifesto.json) registra fontes, hashes e correspondência HTML/PDF. A conferência de exportação é registrada em `VERIFICACAO.md`.

Atualizado em 30/10/2026.
