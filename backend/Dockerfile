FROM python:3.11.9-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        libglib2.0-0 \
        libsm6 \
        libxext6 \
        libxrender-dev \
        libgomp1 \
        libxcb1 \
        libxcb-shm0 \
        libxcb-xfixes0 \
        libxcb-render0 \
        libfontconfig1 \
        libx11-6 \
        libgl1 \
        libgdk-pixbuf-2.0-0 && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "-m", "main"]