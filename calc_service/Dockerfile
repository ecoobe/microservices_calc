FROM python:3.9-slim

# Устанавливаем зависимости (включая requests)
RUN pip install flask requests

COPY calc_service.py .

CMD ["python", "calc_service.py"]