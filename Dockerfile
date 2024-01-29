FROM python:3.8

WORKDIR /app

COPY . /app

ENV PYTHONUNBUFFERED 1

CMD ["python", "main.py"]
