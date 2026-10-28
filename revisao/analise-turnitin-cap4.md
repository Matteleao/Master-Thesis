# Análise dos relatórios do Turnitin (cap. 4, 28/10)

## Números
| Trecho | Original (relatório do cap. 4 inteiro) | Versão enxuta (enviada separada) |
|---|---:|---:|
| 4.1 e 4.2 | 26,3% das palavras marcadas | 42,7% |
| 4.3 e 4.4 | 47,2% | 46,3% |

As duas rodadas do texto original (versão final e versão de revisão 2) dão exatamente os mesmos números nesses trechos.

## Conclusões
1. **A alta na 4.1 e na 4.2 é real.** Ela não vem de o trecho ter sido enviado separado: a 4.3 e a 4.4, enviadas do mesmo jeito, ficaram iguais (47 → 46%).
2. **A alta vem da minha reescrita.** Na 4.1 e na 4.2 eu reescrevi 107 de 126 frases. Na 4.3 e na 4.4, em que só cortei, ficaram 114 frases idênticas e o percentual não mudou.
3. **O Turnitin julga trechos, não frases.** Frases idênticas mudam de estado quando o vizinho muda:
   - na 4.3 e na 4.4, das 114 frases idênticas, 18 passaram a ser marcadas e 13 deixaram de ser;
   - na 4.1 e na 4.2, as frases que eu não toquei subiram de 32% para 53% marcadas, puxadas pelas reescritas ao lado.
4. **As medidas de superfície quase não mudaram entre o original e a reescrita da 4.1 e da 4.2:**
   - tamanho médio da frase (26 e 28 palavras);
   - desvio;
   - frequência de "and", "so" e "because";
   - vírgulas.
   
   O que mudou foi a escolha de palavras. As minhas versões são mais "lisas" e previsíveis que as suas. Exemplos:
   - "to whom a study procedure is delegated" virou "given a study procedure";
   - "makes the decision to authorize" virou "decides whether".
5. **Correlações nos 291 trechos do cap. 4 original** (são fracas e não são regra):
   - **Menos marcados:** trechos com remissão a cláusula, seção, DR ou gap; trechos com modais (may, can, has to); trechos com dados concretos de estudos; frases um pouco mais longas, com mais vírgulas.
   - **Mais marcados:** descrição de procedimento em sequência ("Each risk…", "Each case…", "The site…"), com coordenação por "and" e listas de substantivos.

## Limite
O detector é um classificador estatístico de trechos e responde ao contexto. Não existe uma regra de frase que garanta o resultado: a mesma frase passa ou é marcada conforme o que está em volta.
