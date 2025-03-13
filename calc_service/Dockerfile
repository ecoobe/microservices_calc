FROM python:3.11

# Добавлена обработка security-репозиториев
RUN set -ex; \
    for file in /etc/apt/sources.list /etc/apt/sources.list.d/*.list; do \
        [ -f "$file" ] && sed -i 's/deb.debian.org/archive.debian.org/g' "$file"; \
    done; \
    apt-get update; \
    apt-get install -y --no-install-recommends \
    gcc \
    python3-dev; \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY calc_service.py .
RUN pip install --no-cache-dir flask==3.0.2 requests==2.31.0

CMD ["python", "calc_service.py"]