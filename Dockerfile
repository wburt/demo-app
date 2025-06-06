FROM python:3.12-slim-bullseye

WORKDIR /app

COPY app.py .

EXPOSE 8080

CMD ["python", "app.py"]