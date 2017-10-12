import psycopg2

# Try to connect

connection = psycopg2.connect(dbname='db1', user='db1_user', password='qwerty')
cursor = connection.cursor()
cursor.execute("select * from users")
rows = cursor.fetchall()

for row in rows:
    print(row[1][1])