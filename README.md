# Face Anonymizer

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat&logo=python)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.95%2B-009688?style=flat&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?style=flat&logo=docker)](https://www.docker.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-UI-FF4B4B?style=flat&logo=streamlit)](https://streamlit.io/)

[English](#-face-anonymizer-english) | [Русский](#-face-anonymizer-russian)

---

<a name="-face-anonymizer-english"></a>
## Face Anonymizer (English)
A service for face anonymization in photos: the user uploads an image, the system detects faces and returns a version with blurred regions.  
Built with Python, uses MediaPipe for detection, and runs through a web interface.  
Everything is containerized with Docker, and includes monitoring via Prometheus.

---

## What it looks like

| Upload & result | Statistics |
|----------------------|------------|
| ![UI](docs/ui.jpg)   | ![Metrics](docs/metrics.jpg) |

---

## What's inside

- **Backend** — FastAPI + OpenCV + MediaPipe (detects and blurs faces)
- **Frontend** — Streamlit (simple web UI)
- **Monitoring** — Prometheus collects metrics
- **Containerization** — Everything is packaged in Docker and starts with a single command

---

## How to run

1. Make sure you have [Docker](https://www.docker.com/) and [Docker Compose](https://docs.docker.com/compose/).
2. Clone the repository:
   ```bash
   git clone https://github.com/Wkdk00/Face-Anonymizer.git
   cd Face-Anonymizer
   ```
3. Start the services:
   ```bash
    docker-compose up --build
   ```
4. Open in your browser: http://localhost:8501

Done! You can now upload images and see how they’re processed.

---
## Monitoring
The system automatically collects metrics:
- How many images have been processed?
- How fast does it run?
- Does it stay stable under load?

All this data is available in the **Statistics** tab of the interface. Under the hood — HTTP metrics from *prometheus-fastapi-instrumentator*.

---
## Project structure

- **backend/** — FastAPI backend with MediaPipe
- **frontend/** — Streamlit web interface
- **docker-compose.yml** — builds and runs all components
- **prometheus.yml** — monitoring configuration

---

*Created by [Wkdk00](https://github.com/Wkdk00) — January 2026*

---
<a name="-face-anonymizer-russian"></a>
## Face Anonymizer (Русский)

Сервис для анонимизации лиц на фото: Пользователь загружает фото, система обнаруживает лица и возвращает изображение с размытыми областями.  
Построен на Python, использует MediaPipe для детекции и работает через веб-интерфейс.  
Всё завернуто в Docker, есть мониторинг через Prometheus.

---

## Как это выглядит

| Загрузка и результат | Статистика |
|----------------------|------------|
| ![UI](docs/ui.jpg)   | ![Metrics](docs/metrics.jpg) |

---

## Что внутри

- **Бэкенд** — FastAPI + OpenCV + MediaPipe (ищет лица и размывает)
- **Фронтенд** — Streamlit (простой веб-интерфейс)
- **Мониторинг** — Prometheus собирает метрики
- **Контейнеризация** — Всё это упаковано в Docker и поднимается одной командой

---

## Как запустить

1. Убедись, что у тебя установлены [Docker](https://www.docker.com/) и [Docker Compose](https://docs.docker.com/compose/).
2. Склонируй репозиторий:
   ```bash
   git clone https://github.com/Wkdk00/Face-Anonymizer.git
   cd Face-Anonymizer
   ```
3. Запусти:
   ```bash
    docker-compose up --build
   ```
4. Открой в браузере: http://localhost:8501

Готово! Можно грузить фото и смотреть, как оно обрабатывается.

---
## Мониторинг
Система автоматически собирает метрики:
- Сколько всего изображений обработано?
- Насколько быстро работает?
- Не падает ли под нагрузкой?

Все эти данные доступны во вкладке Statistics в интерфейсе. Под капотом — HTTP-метрики от *prometheus-fastapi-instrumentator*.

---
## Структура

- **backend/** — бэкенд на FastAPI с MediaPipe
- **frontend/** — веб-интерфейс на Streamlit
- **docker-compose.yml** — сборка и запуск всех компонентов
- **prometheus.yml** — настройки мониторинга

---

*Автор [Wkdk00](https://github.com/Wkdk00) — Январь 2026*

