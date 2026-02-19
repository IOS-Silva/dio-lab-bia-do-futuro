# 🎓 ISA IA — Assistente de Educação Financeira com IA

A **ISA IA** é uma assistente virtual de educação financeira desenvolvida como projeto do laboratório da DIO.  
Ela utiliza um modelo de linguagem (LLM) executado localmente via Ollama para responder perguntas financeiras com base em dados estruturados do cliente.

O foco da ISA IA é **educação financeira**, não recomendação de investimentos.

---

## 🎯 Objetivo do Projeto

Construir um agente de IA capaz de:

- Interpretar perguntas financeiras em linguagem natural
- Utilizar dados reais do cliente (JSON e CSV)
- Manter contexto completo da conversa
- Respeitar restrições rígidas de compliance
- Evitar recomendações diretas de produtos financeiros

O projeto demonstra integração entre:
- Interface web
- Base de conhecimento estruturada
- Modelo de linguagem
- Engenharia de prompt
- Controle de respostas

---

## 🧠 Como a ISA IA Funciona

A aplicação:

1. Carrega dados estruturados:
   - Perfil do investidor (`perfil_investidor.json`)
   - Transações (`transacoes.csv`)
   - Histórico de atendimento (`historico_atendimento.csv`)
   - Produtos financeiros disponíveis (`produtos_financeiros.json`)

2. Monta um contexto completo do cliente

3. Injeta um **SYSTEM_PROMPT restritivo**

4. Envia tudo para o modelo `gemma3:4b` via Ollama

5. Exibe a resposta na interface Streamlit

---

## 📁 Estrutura do Projeto

```
dio-lab-bia-do-futuro/
│
├── data/
│   ├── perfil_investidor.json
│   ├── transacoes.csv
│   ├── historico_atendimento.csv
│   └── produtos_financeiros.json
│
├── src/
│   ├── app.py
│   └── README.mb
│   
└── README.mb
```

---

## ⚙️ Tecnologias Utilizadas

- Python
- Streamlit
- Pandas
- Requests
- Ollama
- Modelo Gemma 3 (4B)



---

## 🔒 Regras da ISA IA (Compliance)

A ISA IA:

✔ Pode explicar produtos financeiros  
✔ Pode falar sobre educação financeira  
✔ Pode usar dados do cliente  

🚫 Não pode recomendar produtos  
🚫 Não pode sugerir valores para investir  
🚫 Não pode direcionar decisões  
🚫 Não pode usar frases como:
- "invista em"
- "a melhor opção é"
- "você pode começar com"

Se o usuário pedir recomendação direta, ela responde explicando que a decisão depende do perfil e objetivos.

Se a pergunta não for sobre finanças, ela responde exatamente:

> "Eu só posso falar sobre educação financeira. Como posso te ajudar com seu dinheiro?"

Respostas devem:
- Ter no máximo 4 frases
- Não sugerir produtos
- Terminar com uma pergunta simples

---

## ▶️ Como Instalar

Clone o repositório:

```bash
git clone https://github.com/IOS-Silva/dio-lab-bia-do-futuro.git
cd dio-lab-bia-do-futuro
```

Instale as dependências:

```bash
pip install requests pandas streamlit
```

Instale o Ollama e baixe o modelo:

```bash
ollama pull gemma3:4b
```

---

## 🚀 Como Rodar

```bash
streamlit run app.py
```

A aplicação abrirá no navegador.

---

## 💬 Exemplos de Perguntas

- "Qual é o meu perfil de investidor?"
- "Explique o que é CDB"
- "Como funciona renda fixa?"
- "Quanto eu gastei no último mês?"

---

## 📊 Arquitetura Simplificada

Usuário → Streamlit → Construção do Prompt  
Prompt → Ollama (Gemma 3)  
Modelo → Resposta controlada pelo SYSTEM_PROMPT  
Resposta → Interface Web  

---

## ⚠️ Limitações

- O modelo pode apresentar alucinações.
- Não substitui consultoria financeira profissional.
- Não executa investimentos reais.
- Depende totalmente da qualidade do prompt e do modelo local.

---

## 📚 Aprendizados Técnicos

Durante o desenvolvimento foram aplicados conceitos como:

- Engenharia de Prompt
- Controle de comportamento via SYSTEM_PROMPT
- Injeção de contexto estruturado
- Persistência de histórico de conversa
- Integração LLM local com interface web
- Implementação de restrições de compliance

---

## 👩‍💻 Desenvolvido para

Projeto educacional do laboratório da DIO — criação de um agente de IA aplicado a finanças pessoais com controle de comportamento e restrições técnicas.

---



