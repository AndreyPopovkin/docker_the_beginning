import pika
import psycopg2
import time

def callback(ch, method, properties, body):
    recieved = (body.decode())
    print (recieved)
    try:
        conn = psycopg2.connect("dbname='data_' user='postgres' host='postgres' password='postgres'")
        conn.autocommit = True
        cur = conn.cursor()
        cur.execute("""INSERT INTO Messages VALUES (%s)""", (recieved,))
    except:
        print ("I am unable to connect to the database")

while True:
    print ("wait")
    try:
        connection = pika.BlockingConnection(
            pika.URLParameters("amqp://guest:guest@rabbit:5672")) 
        break
    except:
        print ('cant connect')
        time.sleep(5)
print ("done")

connection = pika.BlockingConnection(
            pika.URLParameters("amqp://guest:guest@rabbit:5672"))
channel = connection.channel()
channel.queue_declare(queue='hello')

channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

print ("start")

channel.start_consuming()
