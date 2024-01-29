FROM python:3.8

RUN mkdir /app

WORKDIR /app

COPY . /app

ENV PYTHONUNBUFFERED 1

CMD ["python", "main.py"]
