import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="laplateforme",
)

cursor = conn.cursor()
cursor.execute("SELECT *FROM etudiants")
results = cursor.fetchall()
print(results)
conn.close()