FROM python:3.11-slim

# Установка системных зависимостей + очистка кеша
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Установка зависимостей Python с кешированием
COPY auth_service.py .
RUN pip install --no-cache-dir flask==3.0.2

# Запускаем сервис
CMD ["python", "auth_service.py"]