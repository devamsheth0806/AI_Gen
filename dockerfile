FROM python:3.12-slim

RUN apt-get update && apt-get install -y build-essential libsqlite3-dev sqlite3

WORKDIR /app

COPY . /app

ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH="/app"

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python", "run.py"]
