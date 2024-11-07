import mariadb
from fastapi import APIRouter

from .item import SexeItem

router = APIRouter()
sql_connection = mariadb.connect(host='db', port=3306, user="username", password="password", database="database")

@router.get("/sexes")
def get_item():
    with sql_connection.cursor() as cursor:
        query = "SELECT sexe FROM Sexes"
        cursor.execute(query)
        results = cursor.fetchall()
        return [SexeItem(sexe=results[0]) for result in results]

@router.post("/sexe")
def add_item(sexe: SexeItem):
    with sql_connection.cursor() as cursor:
        sql = "INSERT INTO Sexes VALUES (%s)"
        cursor.execute(sql, sexe.sexe)
        sql_connection.commit()