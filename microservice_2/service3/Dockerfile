# Base image olarak Python 3.9 kullan
FROM python:3.9

# Gerekli paketleri yükle
RUN pip install flask

# Uygulama dosyalarını kopyala
COPY app.py /app.py
COPY templates /templates

# Uygulamayı çalıştır
CMD ["python", "/app.py"]
