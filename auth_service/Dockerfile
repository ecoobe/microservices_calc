# Используем лёгкий базовый образ Python
FROM python:3.9-slim

# Устанавливаем зависимости
RUN pip install flask

# Копируем код сервиса
COPY auth_service.py .

# Запускаем сервис
CMD ["python", "auth_service.py"]