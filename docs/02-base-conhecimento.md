# Base de Conhecimento

## Dados Utilizados

A ISA IA utiliza arquivos estruturados da pasta `data/` como base de conhecimento para contextualizar as respostas do modelo.

| Arquivo | Formato | Utilização no Agente |
|----------|----------|----------------------|
| historico_atendimento.csv | CSV | Contextualizar interações anteriores do cliente |
| perfil_investidor.json | JSON | Informar perfil, idade, patrimônio e objetivo |
| produtos_financeiros.json | JSON | Explicar como produtos financeiros funcionam (sem recomendar) |
| transacoes.csv | CSV | Exibir transações recentes e analisar movimentações |

---

## 🔄 Adaptações nos Dados

Os dados utilizados são mockados para fins educacionais.

Foram estruturados para simular um cliente real contendo:

- Perfil de investidor
- Patrimônio total
- Reserva de emergência
- Histórico de atendimentos
- Lista de produtos financeiros disponíveis
- Registro de transações

Os arquivos foram organizados para permitir fácil leitura via `pandas` e `json`, facilitando a injeção no contexto do modelo.

Não foram utilizados datasets externos.  
Os dados são simulados para atender ao escopo do desafio.

---

## Estratégia de Integração

### Como os dados são carregados?

Os arquivos JSON e CSV são carregados no início da aplicação:

```python
perfil = json.load(open('./data/perfil_investidor.json'))
transacoes = pd.read_csv('./data/transacoes.csv')
historico = pd.read_csv('./data/historico_atendimento.csv')
produtos = json.load(open('./data/produtos_financeiros.json'))
```

Os dados são convertidos em texto estruturado e incluídos dentro do contexto enviado ao modelo.

---

### Como os dados são usados no prompt?

Os dados NÃO substituem o SYSTEM_PROMPT.

A estrutura é:

1. SYSTEM_PROMPT (regras rígidas de comportamento)
2. CONTEXTO DO CLIENTE (dados estruturados)
3. Pergunta do usuário

Os dados são injetados diretamente no prompt como texto formatado:

```python
contexto = f"""
CLIENTE: {perfil['nome']}, {perfil['idade']} anos, perfil {perfil['perfil_investidor']}
OBJETIVO: {perfil['objetivo_principal']}
PATRIMÔNIO: R$ {perfil['patrimonio_total']} | RESERVA: R$ {perfil['reserva_emergencia_atual']}

TRANSAÇÕES RECENTES:
{transacoes.to_string(index=False)}

ATENDIMENTOS ANTERIORES:
{historico.to_string(index=False)}

PRODUTOS DISPONÍVEIS:
{json.dumps(produtos, indent=2, ensure_ascii=False)}
"""
```

Isso permite que o modelo tenha acesso completo aos dados antes de gerar a resposta.

---

## 🧾 Exemplo de Contexto Montado

Exemplo simplificado enviado ao modelo:

Dados do Cliente:
- Nome: João Oliveira
- Idade: 25 anos
- Perfil: Moderado
- Objetivo: Construir reserva de emergência
- Patrimônio: R$ 15.000
- Reserva de emergência: R$ 10.000

Transações recentes:
- 01/11: Supermercado - R$ 450
- 03/11: Streaming - R$ 55
- 05/11: Restaurante - R$ 120

Atendimentos anteriores:
- Dúvida sobre renda fixa
- Pergunta sobre reserva de emergência

Produtos disponíveis:
- CDB
- Tesouro Direto
- Fundos de Investimento

---

## ⚠️ Observação Técnica

A base de conhecimento é estática e é injetada integralmente no prompt a cada pergunta.

Isso significa que:

- Não há busca semântica
- Não há banco vetorial
- Não há recuperação dinâmica (RAG)
- O contexto completo é reenviado ao modelo em cada interação

Essa abordagem é suficiente para fins educacionais, mas pode não escalar para grandes volumes de dados.

---

