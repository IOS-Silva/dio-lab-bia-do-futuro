# Passo a Passo de Execução - Isa IA

## Setup do Ollama
```bash
# Instalar o Ollama:
Acesse https://ollama.com e instale no seu sistema

# Baixar o modelo usado no projeto:
ollama pull gemma3:4b

# Testar se o modelo está funcionando:
ollama run gemma3:4b
```
## Código Completo
```
Todo o código-fonte esta localizado no arquivo 'app.py'.
```
## Como Rodar

```bash
# 1 Instalar as dependências do projeto
pip install streamlit pandas requests

# 2️ Iniciar o servidor do Ollama
# (Certifique-se de que o Ollama está instalado)
ollama serve

# 3️ Em outro terminal, garantir que o modelo esteja disponível
ollama pull gemma3:4b

# 4️ Executar a aplicação Streamlit
streamlit  run .\src\app.py
```

## Evidência de Execução
<img width="1627" height="868" alt="image" src="https://github.com/user-attachments/assets/8349367b-dc8f-4f46-8d5d-e9fa9fc2e261" />



