import json
import uuid
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# FIX: Add durable=True
channel.queue_declare(queue='orders', durable=True)

prevMessage = None
for i in range(1, 6):
    message = json.dumps({
        "event_id": str(uuid.uuid4()),
        "order_id": f"ORD-{i}",
        "item_id": f"ITEM-{i}",
        "quantity": i
    })
    if(i==3):
        message = prevMessage
    prevMessage = message

    
    channel.basic_publish(
        exchange='', 
        routing_key='orders', 
        body=message,
        properties=pika.BasicProperties(delivery_mode=2) # 2 means persistent
    )
    print(f"Sent: {message}")

connection.close()