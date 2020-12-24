from confluent_kafka import Producer
import socket

conf  = {
    'bootstrap.servers': "host1:9092,host2:9092",
    'client.id': socket.gethostbyname()
}

producer = Producer(conf)

def acked(err, msg):
    if err is not None:
        print("Failed to deliver message: %s: %s" % (str(msg), str(err)))
    else:
        print("Message produced: %s" % (str(msg)))

producer.produce(topic, key="key", value="value", callback=acked)

producer.poll(1)