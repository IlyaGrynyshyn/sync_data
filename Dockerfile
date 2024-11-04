FROM python:3.10.9-slim-buster
LABEL authors="Ilya Hrynyshyn"

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
