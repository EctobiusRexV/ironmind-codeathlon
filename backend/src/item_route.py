import mariadb
from fastapi import APIRouter

from .item import Item, ProgramItem, SexeItem

router = APIRouter()
sql_connection = mariadb.connect(host='db', port=3306, user="username", password="password", database="database")


@router.get("/")
def index():
    return {"message": "Hello, World!"}


@router.get("/items")
def get_item():
    with sql_connection.cursor() as cursor:
        query = "SELECT name,description,price FROM items"
        cursor.execute(query)
        results = cursor.fetchall()
        return [Item(name=result[0], description=result[1], price=result[2]) for result in results]


@router.post("/item")
def add_item(item: Item):
    with sql_connection.cursor() as cursor:
        sql = "INSERT INTO items (name, description, price) VALUES (%s, %s, %s)"
        cursor.execute(sql, (item.name, item.description, item.price))
        sql_connection.commit()
