FROM python:3.9-slim

RUN pip install flask psycopg2-binary  # Добавили psycopg2

COPY history_service.py .

CMD ["python", "history_service.py"]