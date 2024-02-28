FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

WORKDIR /app/drf_api

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
