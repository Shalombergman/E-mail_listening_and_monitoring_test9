FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY emails_producer.py .
CMD ["python", "emails_producer.py"]