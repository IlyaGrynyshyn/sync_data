FROM python:3.10.9-slim-buster
LABEL authors="Ilya Hrynyshyn"

# Встановимо необхідні пакети
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

# Виконання міграцій та запуск процесу
#CMD ["python", "main.py", "migration"] && ["python", "main.py", "process", "cnap_reports"]