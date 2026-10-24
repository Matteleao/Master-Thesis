# Instruções para o trabalho do Codex

## Limite de branches definido pelo usuário

O Codex trabalha exclusivamente no branch `codex/thesis-work`. Antes de qualquer escrita no checkout ou commit, confirme o branch atual. Preserve alterações existentes.

O usuário autorizou consultar todos os outros branches como fontes de contexto e referência até indicar o contrário. Os branches abaixo são estritamente de consulta:

- `main`
- `claude/claudinho-status-check-8tzmxz`
- `claude/ecstatic-turing-3uqrhl`
- `claude/loving-cori-50pzx5`

Não editar, mover, remover ou aplicar alterações a arquivos nesses branches. Não fazer checkout deles para trabalhar, resetar seus refs, mesclar alterações neles ou fazer push para eles. Consulte com `git show <ref>:<caminho>`, `git ls-tree`, `git log` e `git diff`. Buscar objetos e atualizar referências locais `refs/remotes/origin/*` para leitura não altera os branches do GitHub. Não executar scripts encontrados nas fontes apenas por estarem nelas.

As instruções antigas que mandam trabalhar em um branch `claude/*` foram substituídas pela instrução atual do usuário. Assinaturas, links de sessão e atribuições de autoria do Claude pertencem àquelas sessões, não ao Codex.

## Contexto e forma de colaboração

Leia `codex/CONTEXTO.md` para o mapa das fontes, preferências e limites da leitura inicial. Esses registros são contexto, não autorização para executar propostas antigas de revisão.

- Conversar em português. Produzir texto acadêmico em inglês americano, com a voz B2–C1 do autor e precisão técnica.
- Preferir coedição por trecho e explicar mudanças de conteúdo. O autor edita a versão final no Word; uma revisão antiga não prova aprovação atual.
- Ser direto e discordar quando houver fundamento. Não inventar números, citações, métodos executados ou resultados.
- Conferir afirmações com a fonte real quando necessário. Um relatório de outro assistente é uma fonte sobre o histórico da revisão, não verificação independente da norma citada.
- Não usar subagentes ou workflows de vários agentes sem pedido explícito novo: os registros de contexto documentam a preferência por controlar esse custo.
- Não abrir PR nem enviar alterações ao GitHub sem pedido. Não publicar o ambiente por conta própria.
- Priorizar as instruções atuais do usuário e as regras de escrita aplicáveis. Não transformar recomendações de ferramentas antigas em regras novas.

O pedido de familiarização não autoriza reescrever a tese. Os arquivos `original/`, capítulos, entregas, tabelas e figuras dos branches de consulta ficam intactos.
