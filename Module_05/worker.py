import json
import sys
import pika

SIMULATE_CRASH = False

processed_events = set()

def callback(ch, method, properties, body):
    data = json.loads(body)
    event_id = data["event_id"]
    order_id = data["order_id"]

    if event_id in processed_events:
        print(f"\tDuplicate key detected ({event_id}), skipping exec.")
        ch.basic_ack(delivery_tag=method.delivery_tag)
        return

    print(f"Processing order {order_id}...")

    if SIMULATE_CRASH:
        sys.exit(1)

    processed_events.add(event_id)

    ch.basic_ack(delivery_tag=method.delivery_tag)
    print(f"\tAcknowledged order {order_id}")

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='orders', durable=True)

channel.basic_consume(queue='orders', on_message_callback=callback)
print("Worker waiting")
channel.start_consuming()