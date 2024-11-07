from enum import Enum

from pydantic import BaseModel
from typing import Any
#from item import ProgramItem, SexeItem


class Sexe(Enum):
    h: str
    f: str
    a: str


class UserItem(BaseModel):
    firstName: str
    lastName: str
    email: str
    gender: bool # 1 H / 0 F
    birthDate : str
    programme : str
    password: str


class Item(BaseModel):
    name: str
    description: str
    price: float


class ProgramItem(BaseModel):
    name: str
    description: str


class SexeItem(BaseModel):
    sexe: Sexe

class ReturnModel(BaseModel):
    status : int = 200
    data : Any = None
    message : str = None
