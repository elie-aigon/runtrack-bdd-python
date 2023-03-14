import mysql.connector


class Crud:
    def __init__(self, host, user, password, database):
        self.database = mysql.connector.connect(
            host=str(host),
            user=str(user),
            password=str(password),
            database=str(database),
        )
        self.cursor = self.database.cursor()
        self.load_database()

    def load_database(self):
        self.cursor.execute("SELECT *FROM employes")
        self.results = self.cursor.fetchall()
        self.print_database(self.results)

    def print_database(self, data):
        for liste in data:
            print(liste)

    def change_salaire(self, id, new_salaire):
        sql = "UPDATE employes SET salaire= %s WHERE id=%s"
        values = (new_salaire, id)
        self.cursor.execute(sql, values)
        self.load_database()

    def close_connection(self):
        self.database.close()
database1= Crud("localhost", "root", "root", "apple")
print('################################')
database1.change_salaire(2, 3500)
database1.close_connection()