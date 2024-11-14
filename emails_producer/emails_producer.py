import json
import os

from kafka import KafkaProducer



def all_email(email_data):
    producer = KafkaProducer(
        bootstrap_servers=['kafka:9092'],
        value_serializer=lambda v: json.dumps(v).encode('utf-8'),
    )
    producer.send(
        'messages.all',
        value=email_data
    )
    producer.flush()

def explosive_email(email_data):
    producer = KafkaProducer(
        bootstrap_servers=os.environ['kafka:9092'],
        value_serializer=lambda v: json.dumps(v).encode('utf-8'),
    )
    producer.send(
        os.environ['TOPIC_MESSAGES_EXPLOSIVE_NAME'],
        value=email_data
    )
    producer.flush()

def hostage_email(email_data):
    producer = KafkaProducer(
        bootstrap_servers=['kafka:9092'],
        value_serializer=lambda v: json.dumps(v).encode('utf-8'),
    )
    producer.send(
        os.environ['TOPIC_MESSAGES_HOSTAGE_NAME'],
        value=email_data
    )
    producer.flush()