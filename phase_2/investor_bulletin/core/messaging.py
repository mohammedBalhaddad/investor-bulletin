from amqpstorm import Connection
from amqpstorm import Message

if __name__ == "__main__":
    # Create a connection object to publish events
    broker = Connection("localhost", "guest", "guest")

    # Create a Channel
    channel = broker.channel()

    # Declare the Queue, 'simple_queue'.
    channel.queue.declare('prices')

    # Message Properties.
    properties = { 'content_type': 'text/plain' }

    # Create the message.
    message = Message.create(channel, 'THRESHOLD_ALERT', properties)
    message.publish("prices")
    broker.close()
