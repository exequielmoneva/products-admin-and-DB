import pika

params = pika.URLParameters('amqps://rinseenq:iZkfHfgARAZ5YlARbX6yKDS0yYhxcn-X@beaver.rmq.cloudamqp.com/rinseenq')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')


def callback(ch, method, properties, body):
    print('Received in admin')
    print(body)


channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print('Started consuming')

channel.start_consuming()

channel.close()
