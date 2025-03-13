FROM python:3.11-slim

RUN sed -i 's/deb.debian.org/archive.debian.org/g' /etc/apt/sources.list && \
    apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY auth_service.py .
RUN pip install --no-cache-dir flask==3.0.2

CMD ["python", "auth_service.py"]