FROM python:3.11-bookworm

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    python3-dev \
    libpq-dev && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY history_service.py .
RUN pip install --no-cache-dir flask==3.0.2 psycopg2-binary==2.9.9

CMD ["python", "history_service.py"]