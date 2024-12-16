# Utilizăm o imagine oficială Python ca bază
FROM python:3.9-slim

# Setăm directorul de lucru în container
WORKDIR /app

# Copiem fișierele necesare în container
COPY requirements.txt ./

# Instalăm toate pachetele necesare
RUN pip install --no-cache-dir -r requirements.txt

# Copiem codul aplicației în container
COPY . .

# Expunem portul 8082 pentru a accesa aplicația
EXPOSE 8082

# Comanda de rulare a aplicației
CMD ["python", "app.py"]
