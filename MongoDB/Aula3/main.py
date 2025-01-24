from db.database import Database
from helper.WriteAJson import writeAJson
from dataset.produto_database import dataset

compras = Database(database="database", collection="produtos", dataset=dataset)
compras.resetDatabase()

result1 = compras.collection.aggregate([
    {"$group": {"_id": "$cliente_id", "total": {"$sum": "$total"} } }, # formata os documentos
    {"$sort": {"total": -1} } # ordena os documentos -1 é ao contrario

    # percebam que não utilizamos o sifrão '$' no campo 'total' do Stage $sort
    # porque o campo 'total' é dos documentos formatados pelo Stage $group

		# Conceito de 'field paths' em pipeline expressions (DOCS)
])

writeAJson(result1,"resultado")

result2 = compras.collection.aggregate([
    {"$match": {"total": {"$gt": 9}}}, # filtro  gt=greather than
    {"$project": {"produto": 1, "_id": 0} }, # escolhe os campos que irão aparecer
])

writeAJson(result2,"resultado2")

exercicio = compras.collection.aggregate([
    {"$lookup":
        {
            "from": "pessoas",  # Olho na tabela cliente
            "localField": "cliente_id",  # chave estrangeira
            "foreignField": "_id",  # id da outra colecao
            "as": "cliente"  # jogos as informações como cliente no json
        }
    } ,{"$group":
        {"_id": "$cliente", "total": {"$sum": "$total"}# aqui eu agrupo tornando o campo _id do JSON as informações da variavel cliente
            #depois do group, só os campos _id e total são mantidos
        }
    } ,{"$sort":{"total":-1}# ordeno pelo campo total, -1 para ser decrescente
    },{"$set": { # cria um novo campo
        "nome": "$_id.nome"}# nome do novo campo
     }, {"$unwind": '$_id' #remove do array
    },{"$project":
        {"nome":1,"_id":0,"total":1,"desconto": 
            {
                "$cond": {"if": {"$gte": ["$total", 10]}, "then": True, "else": False}
            }
        }
    },{"$unwind": '$nome' #remove do array
    }

      
])

writeAJson(exercicio,"exercicio")



