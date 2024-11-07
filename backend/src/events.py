import mariadb
from fastapi import APIRouter
from .item import ReturnModel


eventsRouter = APIRouter()

sql_connection = mariadb.connect(host='db', port=3306, user="username", password="password", database="database")

@eventsRouter.get("/events/list", response_model=ReturnModel)
def retreiveEventList():
    with sql_connection.cursor(dictionnary=True) as cursor:
        sql = "SELECT * FROM Evenements"
        cursor.execute(sql)
        print(cursor.fetchall())
        return cursor.fetchall()
