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
