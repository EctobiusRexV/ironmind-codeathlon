import mariadb

connexion = mariadb.connect(host='db', port=3306, user="username", password="password", database="database")

cursor = connexion.cursor(dictionary=True)

def get_cursor():
    if not connexion.is_connected():
        connexion.connect(host='db', port=3306, user="username", password="password", database="database")
        cursor = connexion.cursor(dictionary=True)
    return cursor