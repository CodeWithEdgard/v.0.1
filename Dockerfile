# Usa uma imagem leve do Python 3.11
FROM python:3.11-slim

# Define a pasta de trabalho dentro do container
WORKDIR /app

# Copia só o requirements primeiro (melhor cache do Docker)
COPY requirements.txt .

# Instala as dependências sem guardar arquivos temporários
RUN pip install --no-cache-dir -r requirements.txt

# Copia TODO o código do projeto para dentro do container
COPY . .

# Comando que roda quando o container inicia
# uvicorn = servidor, main:app = arquivo main.py e variável app dentro dele
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]