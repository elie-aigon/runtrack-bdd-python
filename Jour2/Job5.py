import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="laplateforme",
)

cursor = conn.cursor()
cursor.execute("SELECT *FROM etage")
results = cursor.fetchall()
superficie_tot = 0
for liste in results:
    superficie_tot += liste [3]
print("La superficie totale de la plateforme est de " +  str(superficie_tot) + "m²." )
conn.close()