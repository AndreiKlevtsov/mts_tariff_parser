FROM python:3.11-alpine
WORKDIR /app

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

COPY requirements.txt /app
RUN pip install --upgrade pip

COPY requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir

COPY src /app

CMD ["gunicorn", "config.wsgi:application", "--bind", "0:8000" ]