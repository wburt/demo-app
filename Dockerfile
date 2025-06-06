FROM python:3.12-slim-bullseye

WORKDIR /app

COPY app.py .

CMD ["python", "app.py"]