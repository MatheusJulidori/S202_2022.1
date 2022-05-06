from helper.write_a_json import write_a_json
from db.database import Graph


db = Graph("bolt://3.82.187.238:7687", "neo4j", "laughs-worry-radars")

data = db.execute_query("match (n) return n")
write_a_json(data, "all_data")


#exercicio 1

def createProfessor(nomeP,idadeP,areaP):
    db.execute_query("create (n:Professor {nome: nomeP,idade: idadeP,area: areaP}) return n")
    
def createMateria(assuntoM,horarioM):
    db.execute_query("create (n:Materia {assunto:assuntoM,horario:horarioM}) return n")

def creteLeciona(nomeP,assuntoM):
    db.execute_query("match ((p:Professor),(m:Materia)) WHERE assunto(m) = assuntoM and nome(p) = nomeP CREATE (p)-[l:LECIONA]->(m) RETURN type(l)")


createProfessor('Matheus Julidori','22','Computacao')
createProfessor('Gabriel Pivoto','22','Computacao')
createProfessor('Davi Restani','20','Computacao')
createProfessor('Fabio','23','Computacao')

createMateria('POO','22h')
createMateria('BD','20h')

createLeciona('Matheus Julidori','BD')
createLeciona('Davi Restani','BD')
createLeciona('Gabriel Pivoto','POO')
createLeciona('Favio','POO')