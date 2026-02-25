import mysql.connector

def get_connection():
    try:
        connection=mysql.connector.connect(
            host='localhost',
            user='root',
            password='MotDePasseFort',
            database='gestion_bibliotheque'
        )
        return connection
    except Exception as e:
        print('erreur de connexion a la base de donnee: ',e)


    