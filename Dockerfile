FROM python:3.11

WORKDIR /app

COPY main.py /app

CMD ["python", "main.py"]