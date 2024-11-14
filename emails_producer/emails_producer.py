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
        'emails.explosive',
        value=email_data
    )
    producer.flush()

def hostage_email(email_data):
    producer = KafkaProducer(
        bootstrap_servers=['kafka:9092'],
        value_serializer=lambda v: json.dumps(v).encode('utf-8'),
    )
    producer.send(
        'emails.hostages',
        value=email_data
    )
    producer.flush()