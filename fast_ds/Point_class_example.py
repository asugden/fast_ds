import sqlite3
from dataclasses import dataclass

# This is a class, so the file and class name are capitalized


class Point:
    def __init__(self, x: int = None, y: int = None):
        # __init__ is always the first function run, and it's run
        # automatically
        self.x = x
        self.y = y


# This is a decorator, and it's secretly just a function that modifies
# whatever comes after

# A dataclass makes it so that you don't have to define all of the
# variables in init
@dataclass
class Person:
    firstname: str
    lastname: str
    age: int
    job: str
    height: float
    weight: float

    def bmi(self):
        return self.height*100/self.weight


arthur = Person(firstname='arthur', lastname='sugden', height=6, weight=195)
print(arthur.bmi())
print(arthur.lastname)


class DBConnection():
    def __init__(self, path: str):
        self.path = path
        self.db = None

    def connect(self):
        self.db = sqlite3.connect(self.path)

    def cursor(self):
        return self.db.cursor()


db1 = DBConnection()
db2 = DBConnection()
db1.connect()

db1.db != db2.db

print(db2.db)
