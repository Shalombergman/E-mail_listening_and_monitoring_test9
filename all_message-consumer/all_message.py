from kafka import KafkaConsumer
import json
from main_service.database import save_to_mongo


# Kafka consumer setup
consumer = KafkaConsumer(
    'messages.all',
    bootstrap_servers=['kafka:9092'],
    auto_offset_reset='earliest',
    group_id='messages_all_group',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

for message in consumer:
    message = message.value
    save_to_mongo(message)
    print(f"insertion to message into collection message.all : {message}")