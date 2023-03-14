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
capacite_tot = 0
for liste in results:
    capacite_tot += liste [3]
print(capacite_tot) 
conn.close()