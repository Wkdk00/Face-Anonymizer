# Face Anonymizer

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat&logo=python)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.95%2B-009688?style=flat&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?style=flat&logo=docker)](https://www.docker.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-UI-FF4B4B?style=flat&logo=streamlit)](https://streamlit.io/)
[![Grafana](https://img.shields.io/badge/Grafana-Dashboards-181818?style=flat&logo=grafana)](https://grafana.com/)


[English](#-face-anonymizer-english) | [Русский](#-face-anonymizer-russian)

---

<a name="-face-anonymizer-english"></a>
## Face Anonymizer (English)
A service for face anonymization in photos: the user uploads an image and videos, the system detects faces and returns a version with blurred regions.  
Built with Python, uses MediaPipe for detection, and runs through a web interface.  
Everything is containerized with Docker, and includes monitoring via Prometheus + Grafana.

---

## What it looks like

| Upload & result | Statistics |
|----------------------|------------|
| ![UI](docs/ui.jpg)   | ![Metrics](docs/metrics.jpg) |

---

## What's inside

- **Backend** — FastAPI + OpenCV + MediaPipe (detects and blurs faces)
- **Frontend** — Streamlit (simple web UI)
- **Monitoring** — Prometheus collects metrics, Grafana visualizes them in real-time dashboards
- **Containerization** — Everything is packaged in Docker and starts with a single command

---

- **Anonymization modes**
  - `blur` — average blur filter
  - `black` — fully hides the face with a black rectangle
  - `pixel` — pixelization effect

- **Video support** — the system can process both images and videos

- **Download results** — processed files can be downloaded directly from the interface using the button below the preview

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
4. Open in your browser:
   - Main interface: http://localhost:8501
   - Grafana dashboard: http://localhost:3000/grafana (login: `admin` / `admin`)

Done! You can now upload images and see how they’re processed.

---
## Monitoring
The system automatically collects metrics:
- How many images have been processed?
- How fast does it run?
- Does it stay stable under load?

Metrics are available in two places:
1. **Statistics tab** in the Streamlit interface (basic overview)
2. **Grafana dashboard** at http://localhost:3000/grafana (detailed real-time analytics)

Under the hood — HTTP metrics from *prometheus-fastapi-instrumentator* and system metrics from the backend.

---
## Project structure

- **backend/** — FastAPI backend with MediaPipe
- **frontend/** — Streamlit web interface
- **monitoring/** — Prometheus config and Grafana dashboard definitions
- **docker-compose.yml** — builds and runs all components

---

*Created by [Wkdk00](https://github.com/Wkdk00) — January 2026*

---
<a name="-face-anonymizer-russian"></a>
## Face Anonymizer (Русский)

Сервис для анонимизации лиц на фото и видео: Пользователь загружает фото, система обнаруживает лица и возвращает изображение с размытыми областями.  
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
- **Режимы анонимизации**
  - `blur` — размытие фильтром среднего
  - `black` — полное затемнение области
  - `pixel` — пикселизация

- **Поддержка видео** — система умеет обрабатывать не только изображения, но и видео

- **Скачивание результата** — обработанный файл можно скачать кнопкой под предпросмотром

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
4. Открой в браузере:
   - Основной интерфейс: http://localhost:8501
   - Дашборд Grafana: http://localhost:3000/grafana (логин: `admin` / `admin`)

Готово! Можно грузить фото и смотреть, как оно обрабатывается.

---
## Мониторинг
Система автоматически собирает метрики:
- Сколько всего изображений обработано?
- Насколько быстро работает?
- Не падает ли под нагрузкой?

Метрики доступны в двух местах:
1. **Вкладка Statistics** в интерфейсе Streamlit (базовый обзор)
2. **Дашборд Grafana** по адресу http://localhost:3000/grafana (детальная аналитика в реальном времени)

Под капотом — HTTP-метрики от *prometheus-fastapi-instrumentator* и системные метрики бэкенда.

---
## Структура

- **backend/** — бэкенд на FastAPI с MediaPipe
- **frontend/** — веб-интерфейс на Streamlit
- **docker-compose.yml** — сборка и запуск всех компонентов
- **prometheus.yml** — настройки мониторинга

---

*Автор [Wkdk00](https://github.com/Wkdk00) — Январь 2026*

