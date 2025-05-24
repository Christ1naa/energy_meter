import pika, json, random
from datetime import datetime

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()
channel.queue_declare(queue="meter_readings")

def generate_data():
    return {
        "id": f"000{random.randint(1,5)}",
        "date": str(datetime.now().date()),
        "readings": {
            "day": random.randint(0, 200),
            "night": random.randint(0, 200)
        }
    }

channel.basic_publish(
    exchange='',
    routing_key='meter_readings',
    body=json.dumps(generate_data())
)

print("📤 Data sent.")
connection.close()
