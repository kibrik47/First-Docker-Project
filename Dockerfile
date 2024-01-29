FROM python:3.8

WORKDIR C:\Users\POTTER-2.0\Desktop

COPY . /app

ENV PYTHONUNBUFFERED 1

CMD ["python", "main.py"]
