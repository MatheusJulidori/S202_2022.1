from unicodedata import name
from db.database import Database
from helper.WriteAJson import writeAJson

db = Database("db","pessoas")

db.create("Matheus",6)

pessoas = db.read()
writeAJson(pessoas,"pessoas")

db.update("Matheus",21)

db.delete("Matheus")

