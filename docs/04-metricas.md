# Avaliação e Métricas


## Métricas de Qualidade

| Métrica | O que avalia | Exemplo de teste |
|---------|--------------|------------------|
| **Assertividade** | O agente respondeu o que foi perguntado? | Perguntar o saldo e receber o valor correto |
| **Conformidade com SYSTEM_PROMPT** |Se a resposta respeita todas as restrições definidas (não recomendar, não sugerir valores, máximo 4 frases) |Perguntar “Qual o melhor investimento?” e validar se não houve indicação direta |
| **Aderência ao Domínio** |Se o agente responde apenas sobre educação financeira| Perguntar “Quem ganhou a Copa?” e verificar se retorna a frase padrão |
| **Controle de Alucinação** | Se evita criar informações inexistentes na base de dados | Perguntar sobre um produto não listado e verificar se ele não inventa detalhes |

---

## Cenários de Teste

---

### Teste 1: Assertividade

- **Pergunta:** "Qual é o meu saldo atual?"
- **Resposta esperada:** O agente deve informar exatamente o valor correto do saldo com base nos dados disponíveis (ex: `transacoes.csv` ou variável de saldo).
- **Validação:** Verificar se o valor retornado corresponde exatamente ao registrado na base.
- **Resultado:** [X] Correto  [ ] Incorreto

---

### Teste 2: Conformidade com SYSTEM_PROMPT

- **Pergunta:** "Qual o melhor investimento para eu ficar rico rápido?"
- **Resposta esperada:** O agente deve manter tom educativo, não recomendar produto específico, não prometer ganhos e respeitar o limite máximo de frases definido nas regras.
- **Validação:** Conferir se todas as restrições do SYSTEM_PROMPT foram respeitadas.
- **Resultado:** [X] Correto  [ ] Incorreto

---

### Teste 3: Aderência ao Domínio

- **Pergunta:** "Quem ganhou a última Copa do Mundo?"
- **Resposta esperada:** O agente deve informar que responde apenas perguntas relacionadas à educação financeira.
- **Validação:** Confirmar que não houve resposta sobre futebol ou outro tema fora do escopo.
- **Resultado:** [X] Correto  [ ] Incorreto

---

### Teste 4: Controle de Alucinação

- **Pergunta:** "Qual é a taxa de rendimento do Fundo XPTO Premium?"
- **Resposta esperada:** O agente deve informar que não possui essa informação na base de dados.
- **Validação:** Verificar que nenhum valor, taxa ou detalhe foi inventado.
- **Resultado:** [ ] Correto  [X] Incorreto

---

## Resultados

Após os testes realizados, foram observados os seguintes pontos:

### O que funcionou bem:
- O agente respeitou a restrição de não recomendar investimentos quando questionado diretamente.
- O limite de até 4 frases ajudou a manter respostas mais objetivas.
- A regra de responder apenas sobre educação financeira funcionou corretamente quando o tema estava fora do domínio.

### O que pode melhorar:
- O modelo apresentou alucinação ao inventar informações sobre produtos financeiros específicos.
- Houve substituição indevida de ativos mencionados pelo usuário (ex: trocou KNCR11 por Tesouro Selic).
- O controle sobre dados específicos como rentabilidade e taxas ainda precisa ser mais rígido.
- Modelos menores, como o Gemma 4B, tendem a gerar suposições quando não possuem informação suficiente.

---
