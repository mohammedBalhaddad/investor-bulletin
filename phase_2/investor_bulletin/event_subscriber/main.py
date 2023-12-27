from pika import BlockingConnection,ConnectionParameters
# Create a connection object to start consuming events

def init_subscriber():
  return BlockingConnection(ConnectionParameters(host='localhost',port=5672))

def on_event(ch, method, properties, body):
      print(f"Received new message {body}")


if __name__ == "__main__":
    subscriber = init_subscriber()
    channel = subscriber.channel()
    channel.queue_declare(queue='prices')
    channel.basic_consume(queue='prices', auto_ack=True ,on_message_callback=on_event)
    print("Start Consuming")
    channel.start_consuming()
