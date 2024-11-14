from kafka import KafkaConsumer
import json
from pymongo import MongoClient

# MongoDB setup


# Kafka consumer setup
consumer = KafkaConsumer(
    'emails.explosive',
    bootstrap_servers=['kafka:9092'],
    auto_offset_reset='earliest',
    group_id='emails_explosive_group',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

for message in consumer:
    sentences = message.value
    collection.insert_one(sentences)
    print(f"emails explosive: {sentences}")