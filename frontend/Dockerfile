FROM python:3.11.9-slim

ENV POETRY_VERSION=1.8.3 \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_REQUESTS_TIMEOUT=300 \
    PIP_DEFAULT_TIMEOUT=100

WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        libglib2.0-0 libsm6 libxext6 libxrender-dev \
        libgomp1 libxcb1 libfontconfig1 libx11-6 libgl1 && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir "poetry==${POETRY_VERSION}"

COPY pyproject.toml ./

RUN poetry lock --no-update && \
    poetry install --no-root -vvv

COPY . .

CMD ["streamlit", "run", "main.py", "--server.address=0.0.0.0"]