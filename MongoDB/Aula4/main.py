from unicodedata import name
from db.database import Database
from helper.WriteAJson import writeAJson

# db = Database("db","pessoas")

# db.create("Matheus",6)

# pessoas = db.read()
# writeAJson(pessoas,"pessoas")

# db.update("Matheus",21)

# db.delete("Matheus")


#Exercicios

db = Database("InatelDB","Livros")

'''
Schema 

{
  $jsonSchema: {
    bsonType: 'object',
    required: [
      'titulo',
      'autor',
      'ano',
      'preco'
    ],
    properties: {
      nome: {
        bsonType: 'string',
        description: 'String com o nome do livro, obrigatório'
      },
      autor:{
        bsonType: 'string',
        description: 'String com o nome do autor, obrigatório'
      }
      ano: {
        bsonType: 'int',
        description: 'Int com o ano de publicação do livro, obrigatório'
      },
      preco{
        bsonType: 'double',
        description: 'Double com o preço do livro, obrigatório'
      }
    }
  }
}
'''

'''
    Funções do DB (Estão no arquivo database.py)



    def create(self, nome, autor,ano,preco):
        return self.collection.insert_one({"nome": nome, "autor": autor,"ano": ano,"preco": preco})

    def read(self):
        return self.collection.find({})

    def update(self, nome, preco):
        return self.collection.update_one(
            {"nome": nome},
            {
                "$set": {"preco": preco},
                "$currentDate": {"lastModified": True}
            }
        )

    def delete(self, nome):
        return self.collection.delete_one({"nome": nome})

'''

db.create("O Senhor dos Anéis: O Retorno do Rei","J. R. R. Tolkien",1955,33.9)
db.create("O Senhor dos Anéis: As duas torres","J. R. R. Tolkien",1954,42.9)
db.create("O Senhor dos Anéis: A Sociedade do Anel","J. R. R. Tolkien",1954,37.9)

db.collection.createIndex( { ano: 1 } )

