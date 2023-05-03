# Usa un'immagine di Python come base
FROM python:3.9-slim-buster

# Imposta la directory di lavoro nell'immagine
WORKDIR /app

# Copia i file dell'applicazione all'interno dell'immagine
COPY . /app

# Installa le dipendenze dell'applicazione
RUN pip install --no-cache-dir -r requirements.txt

# Esposizione della porta di default per Flask
EXPOSE 5000

# Avvia l'applicazione Flask
CMD ["python", "main.py"]