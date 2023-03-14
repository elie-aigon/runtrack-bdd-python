import mysql.connector

class Zoo:
    def __init__(self, host, user, password, database):
        self.database = mysql.connector.connect(
            host=str(host),
            user=str(user),
            password=str(password),
            database=str(database),
        )
        self.cursor = self.database.cursor()

    def load_table(self, table):
        self.cursor.execute("SELECT *FROM "+ str(table))
        return self.cursor.fetchall()

    def print_database(self, data):
        for liste in data:
            print(liste)

    def afficher_cage(self):
        self

    def delete(self, table, nom):
        sql = "DELETE FROM "+ str(table)+ " WHERE nom = %s ;"
        self.cursor.execute(sql, (nom,))
        self.database.commit()

    def new_animal(self, nom, race, cage, date, pays):
        sql = "INSERT animal (id, nom, race, id_cage, date_de_naissance, pays_origine) VALUES (NULL, %s, %s, %s, %s, %s);"
        values = (nom, race, cage, date, pays)
        self.cursor.execute(sql, values)
        self.database.commit()
    
    def modif(self, table, id, parametre, new_value):
        sql = "UPDATE " + str(table) + " SET" + str(parametre) + " = %s WHERE race = %s;"
        self.cursor.execute(sql, (new_value, id,))
        self.database.commit()

    def close_connection(self):
        self.database.close()

zoo = Zoo("localhost", "root", "root", "zoo")
zoo.print_database(zoo.load_table("animal"))
print('#########################################')
# zoo.new_animal("elie", "bouffon", 2, "20/10/2001", "France")
# zoo.new_animal("elie", "bouffon", 2, "20/10/2001", "France")
# zoo.new_animal("elie", "bouffon", 2, "20/10/2001", "France")
# zoo.new_animal("elie", "bouffon", 2, "20/10/2001", "France")
zoo.print_database(zoo.load_table("animal"))
print('#########################################')
zoo.delete("animal", "elie")
zoo.print_database(zoo.load_table("animal"))
print('#########################################')
zoo.modif("animal", "bouffon", "nom", "Bonjour")
zoo.print_database(zoo.load_table("animal"))
print('#########################################')