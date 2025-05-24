import pika, json
from app.meter_logic import process_meter_data

def callback(ch, method, properties, body):
    data = json.loads(body)
    print("📥 New data received from queue")
    process_meter_data(data)

def start_consumer():
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    channel = connection.channel()
    channel.queue_declare(queue="meter_readings")
    channel.basic_consume(queue="meter_readings", on_message_callback=callback, auto_ack=True)
    print("🎧 Waiting for messages...")
    channel.start_consuming()
