import pika

connection = pika.BlockingConnection(
            pika.URLParameters("amqp://guest:guest@rabbit:5672")) 
channel = connection.channel()
channel.queue_declare(queue='hello')
connection.close()


inp = input()
while inp != "exit":
    connection = pika.BlockingConnection(
            pika.URLParameters("amqp://guest:guest@rabbit:5672")) 
    channel = connection.channel()
    channel.basic_publish(exchange='', 
                          routing_key='hello', 
                          body=inp.encode())
    connection.close()
    inp = input()
