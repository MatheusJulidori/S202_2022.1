from db.database import Database
from helper.WriteAJson import writeAJson

db = Database(database="pokedex", collection="pokemons")
db.resetDatabase()

#Exercicios

#1 Fracos contra fogo e gelo com evolução
weaknesses = ["Fire", "Ice"]
pokemons = db.executeQuery({"weaknesses": {"$all": weaknesses},"next_evolution": {"$exists": True}})

writeAJson(pokemons,"Query1")


#2 Psiquicos que tem duas fraquesas
typeP = ["Psychic"]
pokemons = db.executeQuery({"weaknesses": {"$size": 2},"type": {"$all": typeP}})

writeAJson(pokemons,"Query2")

# Fogos e gelo com spawn chance menor que 0.2
types = ["Fire", "Ice"]
pokemons = db.executeQuery({"type": {"$all": types},"spawn_chance": {"$lt":0.2}})

writeAJson(pokemons,"Query3")

#Pokemons com duas fraquezas
pokemons = db.executeQuery({"weaknesses": {"$size": 2}})

writeAJson(pokemons,"Query4")

#Fracos contra grama e veneno ou com chance de spawn maior que 0.5
weaknesses = ["Grass", "Poison"]
pokemons = db.executeQuery({"$or": [{"spawn_chance": {"$gt":0.5}},{"weaknesses": {"$all":weaknesses}}]})

writeAJson(pokemons,"Query5")

