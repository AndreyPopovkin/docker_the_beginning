import psycopg2

try:
    conn = psycopg2.connect("dbname='data_' user='postgres' host='localhost' password='postgres'")
    cur = conn.cursor()
    cur.execute("""INSERT INTO Messages VALUES (%s)""", (input(),))
except:
    print ("I am unable to connect to the database")