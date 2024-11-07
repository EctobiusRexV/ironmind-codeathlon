import mariadb
from fastapi import APIRouter

from .item import ProgramItem

router = APIRouter()
sql_connection = mariadb.connect(host='db', port=3306, user="username", password="password", database="database")

@router.get("/programs")
def get_item():
    with sql_connection.cursor() as cursor:
        query = "SELECT name FROM Programmes"
        cursor.execute(query)
        results = cursor.fetchall()
        return [ProgramItem(program=results[0]) for result in results]


@router.post("/program")
def add_program(program: ProgramItem):
    with sql_connection.cursor() as cursor:
        sql = "INSERT INTO Programmes (program) VALUES (%s)"
        cursor.execute(sql, program.program)
        sql_connection.commit()


