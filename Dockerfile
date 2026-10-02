# Image de base VOLONTAIREMENT ancienne (Debian 10 "buster", fin de vie) - pour le TP
FROM python:3.12-slim-bookworm
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000
CMD ["python", "app.py"]
