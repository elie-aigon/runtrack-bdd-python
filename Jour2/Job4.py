import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="laplateforme",
)

cursor = conn.cursor()
cursor.execute("SELECT *FROM salles")
results = cursor.fetchall()
for liste in results:
    print(liste[1], liste[3])
conn.close()