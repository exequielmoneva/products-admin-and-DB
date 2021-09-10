import pika

params = pika.URLParameters('amqps://rinseenq:iZkfHfgARAZ5YlARbX6yKDS0yYhxcn-X@beaver.rmq.cloudamqp.com/rinseenq')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish():
    channel.basic_publish(exchange='', routing_key='main', body="Boca la concha de tu madre")
