from confluent_kafka import Producer
import socket

conf  = {
    'bootstrap.servers': "localhost:9092",
    'client.id': socket.gethostname()
}

producer = Producer(conf)

def acked(err, msg):
    if err is not None:
        print("Failed to deliver message: %s: %s" % (str(msg), str(err)))
    else:
        print("Message produced: %s" % (str(msg)))

topic = "students"
producer.produce(topic, key="key", value="This is a message", callback=acked)

producer.poll(1)