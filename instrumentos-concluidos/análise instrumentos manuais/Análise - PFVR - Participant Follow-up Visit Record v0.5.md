# Análise crítica — PFVR: Participant Follow-up Visit Record v0.5

**Status:** análise manual para orientar a próxima reconstrução do instrumento. O HTML v0.5 não foi alterado nesta etapa.

## 1. Veredito executivo

O PFVR v0.5 tem o instrumento certo e a unidade de análise certa: **uma pessoa, em uma visita de follow-up**. Ele também preserva a distinção essencial entre:

- a visita ter acontecido dentro ou fora da janela; e
- cada componente exigido ter sido realizado, completado, documentado e, quando aplicável, considerado utilizável.

Essa distinção é necessária. Uma visita pode ocorrer no prazo e ainda assim ter um componente ausente, parcial, realizado fora da janela ou sem evidência suficiente. O PFVR deve tornar essa diferença reconstruível para que o FUCR consiga agregar os resultados sem reinterpretar o caso.

A versão v0.5 está funcionalmente próxima do desenho correto, mas ainda está carregada demais para um registro preenchido no momento clínico. O principal problema não é ausência de conteúdo; é a distribuição do conteúdo entre as seções. Há risco de a pessoa preencher a mesma questão em D, E, I e J, ou de não saber qual seção contém a decisão principal.

**Recomendação geral:** manter o PFVR, a identidade visual e a maior parte das seções, mas fazer uma revisão focal de fluxo e fronteiras. Não transformar o documento em FUCR, não eliminar E, e não criar um segundo log de compliance em J.

---

## 2. Decisão que o PFVR deve suportar

Depois de preencher o formulário, o responsável deve conseguir decidir:

> **For this participant and scheduled visit, did the visit occur within the applicable window, were all required components completed by the specified method and with sufficient evidence, and is the visit usable, usable with a documented limitation, or subject to an exception requiring follow-up or escalation?**

Essa é uma decisão individual de visita. Não é uma decisão de tendência do site, não é uma taxa e não é uma avaliação populacional.

### Unidade de análise

Uma unidade é composta por:

```text
one participant + one nominal visit + one visit-level record
```

Se um componente for concluído posteriormente, o PFVR não deve exigir a abertura de um segundo PFVR para a mesma visita. Deve permitir atualizar ou anexar uma continuação controlada ao mesmo registro, preservando a data real do componente, a relação com a visita original e o impacto sobre a utilizabilidade.

---

## 3. O que está correto no v0.5

### 3.1. Identidade e escopo

O cabeçalho e o Purpose and Use deixam claro que o PFVR é um registro individual e que não substitui o FUCR. Essa fronteira deve ser preservada.

### 3.2. D como registro primário de componentes

A seção D é o núcleo mais importante do documento. Ela já contém a lógica correta: uma linha por componente requerido, com planned date/window, actual date, completion status, within window e evidence/observation/linked record.

D deve continuar sendo a fonte primária para responder:

- quais componentes eram exigidos;
- quais foram realizados;
- em que data;
- dentro ou fora da janela individual do componente;
- com que status;
- onde está a evidência;
- se existe impacto ou necessidade de ação.

### 3.3. E não é redundante com D

A seção E deve ser mantida. Ela não faz a mesma pergunta que D.

- **D:** o componente aconteceu e está completo/documentado?
- **E:** o resultado de imagem ou teste objetivo é utilizável, interpretável e adequado para a finalidade prevista?

Uma imagem pode ter sido adquirida na data correta e ainda ser não utilizável. Um teste pode estar disponível, mas exigir revisão, repetição ou interpretação clínica. E deve continuar como revisão de qualidade/utilizabilidade, ligada à linha correspondente de D, sem repetir o status de presença ou completude.

### 3.4. F e G têm uma função clínica legítima

F registra mudança relatada pelo participante, sem exigir que a pessoa copie uma narrativa clínica inteira. G registra a avaliação clínica/física e sua comparação com a visita anterior. As duas seções devem continuar, desde que os campos permaneçam sintéticos e apontem para a fonte clínica quando a narrativa completa estiver em outro local.

### 3.5. J como rota de resposta

A ideia de J é correta quando usada apenas para questões que exigem resposta, escalonamento ou acompanhamento. Ela não deve ser outro lugar para registrar se cada componente foi feito. Esse registro já pertence a D.

---

## 4. Problemas críticos identificados

### 4.1. C aparece como um gate antes da evidência necessária

A seção C, intitulada `Visit Timing and Attendance Gate`, aparece antes de D. O problema é lógico: o responsável não consegue concluir corretamente o gate de uma visita sem primeiro saber quais componentes foram realizados e em que datas.

A presença física ou a data da visita pode ser registrada em C, mas a decisão de que a visita é utilizável não deve ser tomada ali.

**Ajuste recomendado:**

- manter C como registro de planejamento e ocorrência da visita;
- registrar planned window, actual visit date, attendance e status administrativo;
- não fazer C emitir a decisão final de compliance/usability;
- fazer D produzir o componente-level evidence;
- fazer uma síntese posterior usar C + D para classificar a visita.

A frase de C deve ser semelhante a: **“This section records the planned and actual visit timing. Final usability depends on the component record in Section D.”**

Se a seção C continuar contendo Yes/No, essas opções devem responder apenas à ocorrência/timing da visita, não à completude total da visita.

### 4.2. B está instrutiva demais para um registro clínico

A `Applicable Visit Component Guide` é útil para explicar famílias de componentes, mas o v0.5 dedica muito espaço a exemplos de CT, MRI, PROMs, physical examination, physiotherapy e outros.

O risco é a pessoa interpretar a tabela como uma lista universal obrigatória ou marcar componentes por hábito, em vez de seguir o CIP e a configuração real da visita.

**Ajuste recomendado:**

- manter B como uma orientação curta;
- afirmar que a lista real de componentes vem do CIP/visit schedule aplicável;
- não transformar exemplos em checklist de preenchimento;
- transferir para D a única lista operacional da visita;
- reduzir a tabela de exemplos a famílias e regras de uso.

B não deve competir com D nem duplicar a tabela de componentes.

### 4.3. D precisa de uma distinção mais explícita entre status e timing

A tabela D tem as colunas certas, mas `Completion status` e `Within window?` podem ser preenchidos de forma inconsistente. Por exemplo, um componente pode ser `Complete` mas `No` em within window; pode ser `Partial` e ainda ter uma data real; ou pode ser `Not performed` sem actual date.

A versão final precisa de uma taxonomia curta e coerente:

| Dimensão | Estados recomendados |
|---|---|
| Completion status | Complete; Partial; Not performed; Not applicable |
| Timing | Within window; Outside window; Not assessable; Not applicable |
| Evidence/utilizability | Adequate; Limited; Unavailable; Not applicable |

`Not applicable` exige justificativa ou referência ao componente/visit schedule. `Not performed`, `Partial`, `Outside window` e `Unavailable` exigem explicação curta, consequência ou rota em J quando relevante.

### 4.4. D não acomoda bem um componente concluído depois

O v0.5 reconhece que a visita pode ser pontual e um componente pode ser late, mas não deixa suficientemente claro como registrar o componente feito no dia seguinte ou em uma data posterior.

Não se deve abrir outro PFVR para a mesma visita apenas porque um componente foi concluído depois. A linha de D deve permitir:

- planned date/window;
- first scheduled visit date;
- actual component date;
- outside-window status;
- reason;
- effect on data/usability;
- linked continuation or exception reference.

Se o componente for concluído após o fechamento inicial do PFVR, usar uma `record update / continuation reference`, sem apagar o estado original.

### 4.5. E pode voltar a duplicar D se não for disciplinada

A nota de E diz que a seção não repete completion status, o que é correto. Porém, os cabeçalhos e as perguntas devem tornar isso impossível ou improvável.

E deve conter somente campos como:

- component/reference from D;
- image/test record reference;
- adequacy or usability status;
- reviewer/method;
- concise finding relevant to use or eligibility/endpoint;
- linked action or clinical/safety route, when applicable.

Não repetir em E:

- planned date;
- actual date;
- generic complete/partial status;
- toda a narrativa do resultado;
- conclusão populacional de qualidade.

### 4.6. F e G precisam de orientação de fonte, não de cópia clínica

O PFVR é source-adjacent e pode ser preenchido no encontro clínico, mas não deve tornar-se uma segunda ficha clínica. F e G devem pedir a informação mínima que muda a decisão da visita:

- o que mudou desde a visita anterior;
- quando começou, se relevante;
- severidade/relevância;
- ação ou encaminhamento;
- referência ao record clínico, safety record ou SART quando aplicável.

A narrativa completa permanece na fonte clínica. O PFVR registra síntese operacional e ligação.

### 4.7. I ainda pode repetir a tabela D

A seção I, `Visit Compliance Review`, é útil apenas se for uma síntese curta baseada em C e D. Ela não deve pedir novamente, linha por linha, o que já foi registrado em D.

I deve responder a três ou quatro decisões agregadas dentro da visita:

1. visit timing acceptable;
2. all required components complete;
3. all endpoint-critical components usable;
4. any unresolved issue requiring J.

Cada resposta deve apontar para C, D ou E. I não precisa repetir datas, resultados ou explicações de cada componente.

### 4.8. J precisa ser uma rota de exceção, não um mini-log

J está conceitualmente correto como `Visit Exception and Required Response`, mas deve ter um limite operacional firme.

Abrir J somente quando houver:

- timing issue com impacto ou necessidade de decisão;
- missing/partial component, especialmente endpoint-critical;
- unexpected finding ou participant concern que exija ação, referral ou safety route;
- evidence/unusability issue que bloqueie ou limite a utilização da visita;
- deviation ou limitação que precise de owner, prazo, escalation ou follow-up.

Não abrir J para toda linha que seja simplesmente `Complete / Within window / Adequate`. Não repetir em J a tabela D. J deve apontar para a origem do problema e registrar resposta, impacto, owner, due date, linked record e status.

### 4.9. K deve ser a classificação final da visita

K deve transformar C + D + E + I + J em um resultado curto. Recomenda-se não usar apenas `Compliant / Non-compliant`, porque a realidade pode ser parcial.

Categorias recomendadas:

- Complete and usable;
- Complete with documented observation;
- Usable with limitation;
- Incomplete — follow-up required;
- Not usable for the intended assessment;
- Missed / not completed.

A classificação deve ser explicada por uma referência curta, não por uma narrativa longa. A presença de uma exceção não determina automaticamente que a visita seja não utilizável; isso depende do componente, do endpoint e da limitação documentada.

### 4.10. L deve permanecer enxuta e controlada

A seção de revisão e sign-off é necessária. Deve conter quem registrou, quem revisou quando necessário, data e localização controlada. Não deve ganhar novos campos narrativos ou um segundo bloco de fechamento clínico.

---

## 5. Arquitetura recomendada para a próxima versão

### Página 1 — Identificação, Purpose and Use, planejamento e timing

- cabeçalho original preservado;
- A. Purpose and Use;
- B. pequena orientação sobre componentes aplicáveis;
- C. planned visit, applicable window, actual visit date, attendance/status;
- nota explícita: a decisão de completude e usabilidade depende de D/E.

### Página 2 — Landscape: Required Visit Components

- D como tabela central;
- uma linha por componente exigido;
- actual component date e timing individual;
- completion status separado de evidence/utilizability;
- linked record/reference;
- linha/folha de continuação para mais componentes;
- espaço suficiente para registrar componentes feitos posteriormente.

### Página 3 — Participant report, clinical assessment e personnel continuity

- F: mudanças e preocupações relatadas;
- G: avaliação clínica/funcional mínima e referência à fonte;
- H: personnel/continuity apenas quando a continuidade ou handover altera a interpretação ou exige accountability.

H não deve consumir espaço excessivo se nenhum problema de continuidade ocorreu.

### Página 4 — Compliance synthesis, exception route e outcome

- I: síntese derivada de C/D/E;
- J: somente exceções que exigem resposta;
- K: classificação da visita e justificativa curta;
- L: sign-off e controlled filing.

O layout deve manter o visual do v0.3/v0.5, mas reduzir blocos instrutivos que não são usados no preenchimento real.

---

## 6. Interfaces do PFVR

### PFVR → FUCR

O PFVR deve entregar, por visita:

- participant code e visit identifier;
- expected/nominal visit e window;
- actual visit date/status;
- completed within-window visit;
- required components count;
- complete components count;
- components missing, partial, late ou outside window;
- endpoint-critical component missing, quando aplicável;
- main cause category;
- data/usability impact;
- unresolved follow-up or lost-to-follow-up reference;
- PFVR/J/K status and linked records.

O FUCR pode então calcular, por período:

- visits completed within window / visits expected;
- visits with all required components / visits completed;
- visits missing endpoint-critical component / visits requiring that component;
- participants not recovered despite documented efforts / participants due.

O PFVR não deve calcular essas taxas. Ele deve fornecer o numerador classificável e o denominador/referência da visita.

### PFVR → IQL / imaging record

Quando houver imaging:

- PFVR registra que o componente foi requerido e aponta para o image-set/IQL reference;
- IQL registra qualidade, adequacy, positioning, usability e resolution;
- PFVR registra apenas a consequência operacional para a visita e a referência à decisão do IQL.

### PFVR → ICDL / procedure-related records

O PFVR não deve repetir detalhes intraoperatórios. Se o follow-up exige uma verificação de device, procedure ou complication, ele aponta para ICDL, SCML, SART ou fonte clínica conforme aplicável.

### PFVR → SART / safety route

Unexpected findings e participant concerns podem abrir ou alimentar uma rota de segurança. O PFVR deve registrar o reconhecimento, a ação e o record ID relacionado; não deve duplicar a avaliação completa do evento no SART.

### FUCR/PIR → PFVR

O FUCR ou PIR pode identificar uma tendência — por exemplo, atrasos em determinado componente ou repetição de imaging incompleto. A ação deve voltar para o processo, scheduling, treinamento, IMC, SRR ou CAPA conforme a causa. O PFVR individual não deve ser alterado retrospectivamente para acomodar uma tendência agregada, salvo correção controlada de erro real.

---

## 7. O que deve ser mantido, alterado ou removido

| Elemento | Decisão | Motivo |
|---|---|---|
| PFVR como registro de uma visita | Manter | É a unidade correta e exigida pela tese. |
| Cabeçalho e identidade visual | Manter | Já são reconhecíveis e adequados. |
| Purpose and Use | Manter | Explica diferença para FUCR. |
| B detailed guide | Reduzir | Útil, mas extensa e potencialmente confundível com checklist. |
| C timing/attendance | Manter, reposicionar a lógica | Deve registrar planejamento/ocorrência, não decidir sozinho a utilizabilidade. |
| D component record | Fortalecer | É a fonte primária da decisão de completude/timing por componente. |
| E imaging/objective review | Manter | É avaliação de qualidade/utilizabilidade, não duplicação de D. |
| F participant report | Manter e compactar | Captura mudança relevante sem copiar fonte clínica. |
| G clinical assessment | Manter e compactar | Registro mínimo + source reference. |
| H personnel continuity | Manter condicional | Só é útil quando continuidade/handover altera a confiabilidade ou accountability. |
| I compliance review | Manter como síntese | Deve referenciar C/D/E, não repetir D. |
| J exception response | Manter, limitar escopo | Uma rota de resposta, não um segundo log de compliance. |
| K overall outcome | Manter e clarificar estados | Precisa traduzir a consequência operacional da visita. |
| L sign-off | Manter | Garante autoria, revisão e filing controlado. |

---

## 8. Critérios de qualidade para o HTML revisado

A próxima versão deve passar por estas perguntas:

1. Uma pessoa que preenche o PFVR pela primeira vez sabe quais componentes colocar em D?
2. Fica explícito que C registra o timing da visita, enquanto D registra timing/completude por componente?
3. É possível registrar um componente feito posteriormente sem abrir uma visita duplicada?
4. E consegue avaliar uma imagem/teste sem repetir a conclusão de D?
5. F e G pedem síntese operacional, não transcrição clínica?
6. I consegue ser preenchida referenciando C/D/E sem repetir tabelas?
7. J é aberta somente quando há resposta, owner, prazo, escalonamento ou follow-up necessário?
8. K diferencia visita completa, observação, limitação, incompletude e não utilizabilidade?
9. FUCR consegue extrair os quatro grupos de contagem e seus denominadores sem reinterpretar o caso?
10. Nenhuma tabela, caixa ou assinatura invade o rodapé?
11. O Editor v2 permite editar todas as células, caixas, opções, linhas e colunas aplicáveis?
12. A versão blank permanece realmente em branco, enquanto o worked example contínuo fica apenas na filled demonstration?

---

## 9. Conclusão

O PFVR deve ser mantido. Ele não é redundante com o FUCR: o PFVR documenta uma visita; o FUCR revisa muitas visitas ao longo de um período.

A principal correção necessária é tornar D inequivocamente a tabela central de componentes e reorganizar as outras seções ao redor dela. C deve registrar timing e ocorrência; E deve avaliar utilizabilidade de imagem/teste; I deve sintetizar; J deve responder a exceções; K deve classificar a visita. Essa divisão evita que o mesmo problema seja preenchido quatro vezes e, ao mesmo tempo, preserva a informação necessária para o FUCR.

Não recomendo uma reconstrução radical. Recomendo uma versão revisada que mantenha a identidade do v0.5, reduza a carga instrutiva de B, explicite a dependência C → D → E/I, ofereça uma continuação controlada para componentes tardios e fortaleça as interfaces com FUCR e PIR.

---

## 10. Fontes verificadas

- Tese completa (29-10), seção 4.4.3: cada follow-up visit registra janela, componentes exigidos pelo CIP, resultado de cada componente, exceção e ação; visita só é utilizável quando as avaliações CtQ foram concluídas pelo método especificado e dentro da janela.
- Tese completa (29-10), seção 4.5.3: FUCR agrega quatro medidas de follow-up compliance, cada uma com seu próprio denominador, e usa a causa registrada na visita para atribuir a falha.
- Tese completa (29-10), implementação do ciclo: PFVR é um dos cinco registros preenchidos no clinical moment; os demais instrumentos leem seus registros.
- Tese completa (29-10), Appendix T: PFVR registra one participant's one follow-up visit.
- PFVR v0.5: seções A–L, com D como Primary Completion Record, E como Imaging and Objective Assessment Review, I como Visit Compliance Review, J como Visit Exception and Required Response, K como Overall Visit Outcome e L como Review and Sign-off.
- Operational Quality Form Templates skill: separação entre revisão individual e performance agregada, regra de não duplicação, cadeia de evidência e requisitos de editor/paginação.
