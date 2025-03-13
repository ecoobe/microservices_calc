FROM python:3.11

# Универсальное решение для всех версий Debian
RUN set -ex; \
    { \
        echo "deb http://deb.debian.org/debian/ bullseye main"; \
        echo "deb http://security.debian.org/debian-security bullseye-security main"; \
        echo "deb http://deb.debian.org/debian/ bullseye-updates main"; \
    } > /etc/apt/sources.list; \
    rm -rf /etc/apt/sources.list.d/*; \
    apt-get update; \
    apt-get install -y --no-install-recommends \
    gcc \
    python3-dev; \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY auth_service.py .
RUN pip install --no-cache-dir flask==3.0.2

CMD ["python", "auth_service.py"]