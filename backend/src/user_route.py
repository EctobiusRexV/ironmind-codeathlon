import mariadb
from fastapi import APIRouter
from .security import *
from .item import UserItem, ReturnModel

router = APIRouter()
sql_connection = mariadb.connect(host='db', port=3306, user="username", password="password", database="database")


@router.get("/users/{userName}")
def get_items(userName : str):
    with sql_connection.cursor() as cursor:
        query = f"SELECT {userName} FROM Utilisateurs"
        cursor.execute(query)
        results = cursor.fetchall()
        return [UserItem(name=results[0], password=results[1]) for result in results]

@router.post("/users/signup", response_model =ReturnModel)
async def registerUser(newUser : UserItem):
    if verifyGender(newUser.gender, newUser.firstName):
        with sql_connection.cursor() as cursor:
            newPswd = encryptPassword(newUser.password)
            query = f"INSERT INTO Utilisateurs(lastname,sexId,programid) VALUES ({newUser.lastname},{newUser.gender},{newUser.programid})"

    else:
        return ReturnModel.construct(status=401, data="invalid Gender")

    if verifyEmail(newUser.email):
        with sql_connection.cursor() as cursor:
            newPswd = encryptPassword(newUser.password)
            query = f"INSERT INTO Utilisateurs(lastname,sexId,programid) VALUES ({newUser.lastname},{newUser.gender},{newUser.programid})"

    else:
        return ReturnModel.construct(status=401, data="invalid Email")

@router.post("/sexe")
def add_user(user: UserItem):
    with sql_connection.cursor() as cursor:
        sql = "INSERT INTO Utilisateurs VALUES (%s)"
        cursor.execute(sql, user.name, user.password)
        sql_connection.commit()