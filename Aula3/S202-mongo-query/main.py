from db.database import Database
from helper.WriteAJson import writeAJson

db = Database(database="pokedex", collection="pokemons")
#db.resetDatabase()

tipos = ['Grass','Poison']

pokemons = db.collection.find(
    db.executeQuery({'type':{'$in':tipos},"next_evolution":{"exists":True}}),
    {'type':1}
)

writeAJson(pokemons,"pokemons")

