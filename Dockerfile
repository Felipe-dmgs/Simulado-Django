# Usa a imagem oficial do Python
FROM python:3.11-slim

# Define variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Instala dependências do sistema se necessário
RUN apt-get update && apt-get install -y libpq-dev gcc && rm -rf /var/lib/apt/lists/*

# Instala as dependências do Python
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copia o projeto para dentro do container
COPY . /app/

# Expõe a porta padrão do Django
EXPOSE 8000

# Comando para rodar as migrações e iniciar o servidor de desenvolvimento
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
