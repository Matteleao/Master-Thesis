# Contexto de consulta do Codex

Registro em 24/10/2026. Fonte: arquivos presentes nas pontas dos quatro branches remotos, histórico recente e instruções desta conversa. Este arquivo pertence ao branch do Codex. Não substitui a tese do autor nem resolve divergências entre versões.

## Instrução atual do usuário

Usar os outros branches como fontes de consulta quando necessário, salvo orientação contrária. Nunca modificar, mover ou alterar seu conteúdo. Trabalhar somente em `codex/thesis-work`.

O usuário quer que a leitura forneça contexto sobre o assunto, referências, gostos, preferências e modo de trabalhar. Não pediu uma revisão nova da tese nem a aplicação das propostas anteriores.

## Projeto

Autor identificado nos documentos: Felipe Gregorio Lima. Mestrado em Engenharia Farmacêutica, Universidade de Lisboa, Faculdade de Farmácia / Instituto Superior Técnico, 2025/2026.

Título registrado: *Translating ICH E6(R3) into Practice: A Site-Centered Operational Quality Management Framework for Shoulder Medical Device Clinical Investigations*.

A tese propõe um framework operacional de qualidade que o centro de investigação usa e cujos registros mantém. A proposta complementa o sistema do patrocinador e procura controlar riscos locais, incluindo dados gerados no ponto de cuidado. O recorte é a investigação de dispositivos cirúrgicos de ombro, especialmente a operação em centros privados com recursos limitados.

O desenho usa DSRM de Peffers et al. Relata identificação do problema, objetivos da solução, desenho/desenvolvimento e comunicação. Demonstração e avaliação não foram realizadas. Não confundir coerência interna e rastreabilidade do desenho com validação, viabilidade ou efeitos demonstrados.

Contagens recorrentes do desenho: 5 lacunas, 12 domínios CtQ, 12 design requirements, 4 pilares, 24 instrumentos, 7 fases e 3 contextos de implementação. São contagens das versões consultadas, não impedimento para uma mudança futura expressamente decidida pelo autor.

Os pilares são Governance, Risk Management, Operational Controls e Performance Oversight. O conjunto tem 7, 5, 9 e 3 instrumentos por pilar, respectivamente. As fases são feasibility, start-up, enrollment, surgery, follow-up, close-out e continuous improvement. A vigilância de segurança atravessa as fases de condução.

## Preferências documentadas

Fontes principais: `.claude/skills/thesis-writing/SKILL.md`, `revisao/guia-de-estilo.md`, `revisao/projeto/style-rules.md`, `revisao/fase-0/ditados-transcricao.md`, `revisao/fase-0/perfil-de-voz.md` e as duas versões de `revisao/contexto-sessao.md`.

- Respostas em português; texto acadêmico em inglês. Registro de inglês B2–C1, simples e preciso, preservando a voz de um autor não nativo competente.
- Termos técnicos, números de cláusula e nomes de instrumentos exatos. Simplificar a linguagem de ligação sem trocar o termo definido por um sinônimo elegante.
- O raciocínio costuma partir do contexto e seguir mecanismo e consequência. Ligar as frases que formam uma cadeia causal. Evitar prosa picada e frases de efeito.
- Comprimento de frases e parágrafos determinado pelo conteúdo. Sem teto arbitrário de palavras ou média-alvo.
- `itself` é um traço documentado da voz do autor, associado ao português “próprio”. Retirar somente quando funcionar como ênfase vazia. `therefore` é um conector de consequência permitido; não removê-lo por uma contagem mecânica.
- Evitar `rather than` e disfarces de oposição, caudas que comentam a própria frase, aberturas que só anunciam, aforismos e séries montadas por cadência. Preservar distinções conceituais necessárias com parcimônia.
- Introdução impessoal; primeira pessoa do plural a partir da Metodologia. Grafia americana, sem contrações e sem travessões na prosa acadêmica.
- Um objeto, um nome: `framework` para o artefato; `Risk Management` para o pilar; `RBQM` para a abordagem; `PROM` para o instrumento de resultado relatado pelo paciente.
- Referências Vancouver em ordem de primeira citação. Alterar a posição da primeira citação pode exigir renumeração. Há divergência histórica sobre subscrito versus citação na linha, que não deve ser resolvida silenciosamente.
- Relatórios legíveis em HTML e entregas em Word são preferidos a relatórios extensos em Markdown. Para capítulos: texto justificado, primeira linha com 720 twips, sem linha vazia entre parágrafos e estilos de título do Word.
- Coedição parágrafo a parágrafo; o autor escreve as versões finais no Word. Explicar o que mudou e por quê. Não aplicar uma proposta antiga por ela existir no repositório.
- Honestidade e discordância fundamentada. Não atribuir ao autor uma ação metodológica que não esteja documentada. Citação literal exige palavras exatas da fonte.
- Não atribuir o problema da tese ao orientador ou coorientador. O enquadramento acadêmico o situa na literatura, na prática e na leitura das diretrizes.
- Não inserir a estimativa verbal de 10–15 minutos como resultado da tese.
- As notas posteriores pedem não usar agentes ou workflows por custo. Um workflow antigo descreve execução paralela; isso é histórico, não autorização atual.
- O limite registrado é 40.000 palavras, com Resumo e Abstract de até aproximadamente 300 palavras. O prazo histórico registrado é o fim de outubro de 2026; não foi reconfirmado nesta conversa.

## Decisões e cautelas sobre o conteúdo

As instruções recentes distinguem os domínios CtQ do centro dos fatores CtQ de cada investigação. A tese organiza domínios; o centro identifica os fatores específicos do ensaio usando o protocolo e as informações do patrocinador. A proposta de 19/10 coloca essa tradução no Site Risk Register, mas não se deve tratar todas as alterações controladas como aceitas.

ICH E8(R1) é referência conceitual/de desenho e de checagem de cobertura. A instrução de 17/10 exclui a E8 da matriz de comparação. A matriz compara ICH E6(R3), ISO 14155:2026 e MDR. Não afirmar que a E6 cria por si só a mesma obrigação jurídica para dispositivos que o MDR.

A origem dos quatro pilares nas versões posteriores é uma síntese estrutural a partir de ISO 13485:2016, ISO 14971:2019 e ISO 15189:2022. Documentos anteriores contam essa origem de outras formas. Não harmonizar versões automaticamente.

Separar: obrigação regulatória, escolha do desenho, benefício esperado e efeito demonstrado. O aprendizado cirúrgico é um ponto central, particularmente a observação da trajetória do operador durante a condução. A afirmação deve manter o escopo do corpus e não apagar deveres contínuos de qualificação já existentes.

Os números do registro aparecem como 46 investigações e 235 organizações em várias versões. Depois foi adotada a unidade de registro centro–investigação, com uma organização contribuindo uma observação por estudo. Uma alteração de 22/10 no Word com alterações controladas adiciona exclusões. Não reutilizar distribuições e denominadores antigos sem conferir a versão e os dados.

O registro de 19/10 diz que a menção a `permanent clinical trial infrastructure` deve ser retirada após recontagem; capítulos e tabelas anteriores ainda usam essa variável. Não converter ausência de informação pública em prova de ausência de recursos ou qualidade.

A planilha de derivação disponível em `loving-cori` tem 211 candidatos e 45 temas, com 40 mecanismos separados. As três listas de candidatos têm 77 entradas E6, 57 MDR e 77 ISO. Naquela versão, os 45 temas se distribuem em 7 fortemente harmonizados, 23 parcialmente e 15 sem obrigação no centro; 31 passam no filtro e geram 11 grupos, com imagem e avaliação de desfechos juntas no G8. São resultados daquela execução, cujos juízos ainda pedem revisão pelo autor. O relatório de 19/10 menciona outra planilha, v5, com 251 trechos e 43 temas. Essa v5 não aparece no inventário dos arquivos presentes nas pontas consultadas. Não misturar as contagens ou dizer que a v5 foi lida.

A planilha antiga chama atenção para ISO 14155:2026, Clause 10.6(o), CAPA atribuída ao PI; Clause 10.6(i), manutenção/calibração documentada atribuída ao PI; e Annex A.7(g), roll-in como item do CIP. Esses trechos estão transcritos na planilha e afetam afirmações antigas de ausência absoluta de obrigação. A lista de mecanismos e a lista de atributos são distintas. A planilha também identifica decisões ainda abertas, como a exclusão de confidencialidade por escopo. Não aplicar suas sugestões automaticamente.

A referência ISO 15189:2022 foi inserida como [54] nas versões posteriores; referências antes numeradas 54–90 passaram a 55–91. Nos arquivos antigos, [54] é CTTI. Números de citação exigem versão identificada.

Há 24 títulos de templates nos Apêndices A–X e um Apêndice Y para o modelo interativo, mas o Markdown consultado ainda tem marcadores de conteúdo pendente. Não afirmar que os templates estão disponíveis só porque um capítulo diz que foram fornecidos.

Não subir o PDF da ISO 14155:2026 ao repositório. O texto completo não está entre os arquivos presentes nas pontas consultadas. A planilha inclui trechos de cláusulas; não é equivalente à norma completa. A nota sobre ISO 15189:2022 foi feita a partir de uma amostra pública, não do texto integral das cláusulas.

## Mapa dos branches consultados

| Branch | Commit consultado | Conteúdo e cautela |
|---|---|---|
| `main` | `969c46ca5e92481bc7528edcad1fc5164079b7b6` | README curto e MDR consolidado em 10/01/2025, com 233 páginas. |
| `claude/claudinho-status-check-8tzmxz` | `cbb1781a86698ef67596f180b011fda7c736048a` | Tese manual recebida em outubro, capítulos Markdown, regras, ditados, análises, Word de entrega e revisão de 19/10 com alterações controladas. Último commit em 22/10 altera somente o Word com alterações controladas. |
| `claude/loving-cori-50pzx5` | `332ebc39bd498b0955ac06e71a652a21994d717f` | Parte do material de revisão compartilhado, versões anteriores dos capítulos, planilha de derivação CtQ, guia HTML e buscas CTIS/EUDAMED. Último commit em 14/10. |
| `claude/ecstatic-turing-3uqrhl` | `786d3ff692f73db231bc756aa992938f75f9f1e5` | Revisão específica do Capítulo 4 em quatro HTMLs, Word corrigido com comentários e tabela das seis funções. Commits de 22 a 24/10. Não contém uma tese inteira atualizada. |

`original/` contém versões recebidas do autor. `entrega/tese-revisada.docx` é uma reescrita anterior e é descrita nas notas como desatualizada. O estado dos arquivos e o histórico têm prioridade sobre tabelas de estado antigas que não foram atualizadas. Versão posterior não implica aprovação pelo autor.

## Referências e materiais de apoio

Fontes recorrentes: ICH E8(R1), ICH E6(R2/R3), ISO 14155, MDR, ISO 13485, ISO 14971 e ISO 15189; reflexão EMA/269011/2013; CTTI QbD; suplemento MDIC de 2016; TransCelerate; SQA-Onc./ROMIO; Clinical Trial Site Performance Measure; Vale et al. sobre centros portugueses; estudos de curva de aprendizagem, clustering, imagem, follow-up e instrumentos do ombro.

O workshop de escrita é de Dra. Carolina Borges Merjane (CBM Science), com 50 páginas. É a base declarada das regras autorais, que resolvem conflitos com conselhos genéricos.

A busca CTIS registrada em 14/10 encontrou 64 ensaios distintos, dos quais 19 envolvem ombro e oito contexto cirúrgico, sem dispositivo como produto em investigação segundo o registro. A busca EUDAMED registrada no mesmo dia explora fichas de dispositivos, SSCPs e cruzamentos com ClinicalTrials.gov, não uma lista pública completa de centros do módulo de investigações. Esses são resultados relatados nos arquivos, não buscas refeitas nesta sessão.

Os relatórios de análise v2 registram 590 apontamentos de cinco lentes, consolidados em 104 problemas. A segunda onda não foi executada por limite de créditos. O consolidado e os relatórios de entrega registram recomendações e aplicações distintas; não confundir convergência entre assistentes com confirmação em fonte primária.

## Consulta técnica e cobertura da leitura inicial

Foram inventariadas 129 entradas nos quatro branches, correspondentes a 83 conteúdos Git distintos: 69 arquivos textuais/documentos e 14 PNGs. Todo o conteúdo textual foi extraído localmente, incluindo comentários do Word e todas as abas preenchidas das três planilhas. As 14 imagens foram inspecionadas, além das nove imagens incorporadas no Word corrigido do Capítulo 4, que são variantes das figuras e tabelas. Diretórios vazios de mídia do ZIP não são imagens.

Foram lidos os registros de contexto, guias de estilo, regras autorais, ditados, perfil de voz, preparação, configuração/contrato, workflow, panorama e consolidado das análises, relatório de mudanças de 19/10, relatórios da reescrita, capítulos da versão manual em Markdown, referências, apêndices, variantes de Word por trechos não repetidos e o corpo/comentários do Word corrigido do Capítulo 4. Também foram lidos os quatro relatórios HTML do Capítulo 4, propostas e relatórios do Capítulo 2, diagnóstico, relatórios das lentes de fatos, argumento, demolish e consistência. A lente do autor foi percorrida com todos os problemas e a narrativa do relatório; o anexo de candidatos mecânicos contém trechos já presentes na tese. Houve retornos truncados, depois relidos em partes quando identificados. Não apresentar isso como garantia de leitura literal integral de cada palavra de todos os arquivos.

Na planilha CtQ, foram lidas todas as abas, incluindo os 211 candidatos e 40 mecanismos com seus trechos literais, a matriz, filtros, critérios, cobertura e achados. Na CTIS, foram percorridos os 64 registros e suas classificações; os nomes de medicamentos e os links não foram todos relidos individualmente. Na EUDAMED, foram lidas as notas, fabricantes, investigações declaradas, SSCPs e centros. Os 957 grupos da aba Dispositivos foram processados integralmente para conferir distribuições e relação com os resumos; não houve leitura humana individual de cada identificador/link/nome de tamanho de componente.

Do workshop, foi lido o texto das 50 páginas. Do MDR, foram lidos o Anexo XV, o Anexo XIV, os Artigos 61–82, 18 e 27, além do início e dos trechos consultados na preparação. Houve uma passagem estrutural pelos demais artigos e anexos, com texto integral indexado para consulta. O restante das 233 páginas não foi lido palavra por palavra. Portanto, a leitura literal integral de todo o acervo pedido pelo usuário ainda não está concluída. Indexação não deve ser apresentada como leitura, e leitura não significa conferência independente das fontes externas.

Índice completo local desta instância:

`/workspace/scratch/master-thesis/branch-consultation-hxhvnspe/INDEX.md`

Inventário com branch, commit, caminho e OID:

`/workspace/scratch/master-thesis/branch-consultation-hxhvnspe/manifest.json`

Textos e originais extraídos ficam em `text/` e `blobs/` nesse diretório. A base `sources.sqlite3` oferece busca FTS5 nos 69 conteúdos textuais. Esses caminhos são auxiliares locais; se não existirem em uma nova instância, recupere os arquivos pelos commits, sem alterar os branches-fonte.

Exemplo de leitura sem checkout:

```bash
git show cbb1781a86698ef67596f180b011fda7c736048a:revisao/contexto-sessao.md
git show 786d3ff692f73db231bc756aa992938f75f9f1e5:revisao/cap4-turnitin/bloco-1.html
```

Antes de uma afirmação técnica ou de uma reescrita futura, abrir a versão exata da fonte e conferir o trecho pertinente. Instruções novas do usuário podem alterar estas preferências ou restringir uma fonte.
