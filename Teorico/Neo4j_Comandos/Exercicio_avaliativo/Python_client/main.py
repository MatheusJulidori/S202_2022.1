from helper.write_a_json import write_a_json
from db.database import Graph


db = Graph("bolt://44.201.19.132:7687", "neo4j", "damping-bomb-debit")

def quemECrianca():
    return db.execute_query("match (n:Criança) return n")
    
def desdeQuandoECasado(nomeP):
    return db.execute_query("match (n:Person)-[cc:CASADO_COM]->(n1:Person) WHERE n.name=$nomeP return n1.name,cc.desde,n.name",{'nomeP':nomeP})

def qualAIdadeDaPessoa(nomeP):
    return db.execute_query("Match (p:Person) WHERE p.name = $nomeP RETURN p.age",{'nomeP':nomeP})

aux = quemECrianca()
write_a_json(aux,'criancas')


aux = desdeQuandoECasado('Carlos Julidori')
write_a_json(aux,'casado')


aux = qualAIdadeDaPessoa('Tina Julidori')
write_a_json(aux,'idade')
