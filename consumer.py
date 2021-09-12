import json
import pika
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.settings")
django.setup()

from products.models import Product

params = pika.URLParameters('amqps://rinseenq:iZkfHfgARAZ5YlARbX6yKDS0yYhxcn-X@beaver.rmq.cloudamqp.com/rinseenq')
#   params = pika.URLParameters('localhost')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')


def callback(ch, method, properties, body):
    print('Received in admin')
    _id = json.loads(body)
    print(id)
    product = Product.objects.get(id=_id)
    product.likes += 1
    product.save()


channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print('Started consuming')

channel.start_consuming()

channel.close()
