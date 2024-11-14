FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY all_message.py .
CMD ["python", "all_message.py"]
