import json
import pandas as pd
import requests
import streamlit as st


# ============ CONFIGURAÇÃO ============
OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "gemma3:4b"

# ========== CARREGAR DADOS ==========
perfil = json.load(open('./data/perfil_investidor.json'))
transacoes = pd.read_csv('./data/transacoes.csv')
historico = pd.read_csv('./data/historico_atendimento.csv') 
produtos = json.load(open('./data/produtos_financeiros.json'))

# ========== MONTAR CONTEXTO ==========
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

# ========== SYSTEM PROMPT ==========
SYSTEM_PROMPT = """
Você é ISA IA.

Você fala APENAS sobre educação financeira.

Se a pergunta NÃO for sobre finanças, responda exatamente:
"Eu só posso falar sobre educação financeira. Como posso te ajudar com seu dinheiro?"

Responda sempre:
- Curto
- Máximo 4 frases
- Sem recomendar produtos
- Termine com uma pergunta simples.
"""

# ============ CHAMAR OLLAMA ============
def perguntar(msg):
    prompt = f"""
    {SYSTEM_PROMPT}

    CONTEXTO DO CLIENTE:
    {contexto}

    Pergunta: {msg}"""

    r = requests.post(OLLAMA_URL, json={"model": MODELO, "prompt": prompt, "stream": False})
    return r.json()['response']

# ============ INTERFACE ============
st.set_page_config(page_title="Isa IA", page_icon="🎓")

st.title("🎓 Isa IA - Sua Ajudante Financeira Pessoal")

# Botão limpar conversa
if st.sidebar.button("Limpar Conversa"):
    st.session_state.messages = [
        {"role": "assistant", "content": "Olá! Eu sou a Isa IA. Como posso te ajudar com suas finanças hoje?"}
    ]
    st.rerun()

# Inicializa histórico
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Olá! Eu sou a Isa IA. Como posso te ajudar hoje?"}
    ]

# Exibe mensagens antigas
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Campo de entrada
if user_input := st.chat_input("Digite sua dúvida financeira..."):

    # Adiciona mensagem do usuário
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    # Monta histórico formatado
    historico_formatado = ""
    for msg in st.session_state.messages:
        historico_formatado += f"{msg['role'].upper()}: {msg['content']}\n"

    # Mostra "digitando..."
    with st.chat_message("assistant"):
        with st.spinner("Isa está pensando..."):
            resposta = perguntar(historico_formatado)
            st.markdown(resposta)

    # Salva resposta
    st.session_state.messages.append({"role": "assistant", "content": resposta})
