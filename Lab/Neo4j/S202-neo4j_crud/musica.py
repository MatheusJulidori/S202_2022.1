from pprintpp import pprint as pp
from db.database import Graph


class Musica(object):
    def __init__(self):
        self.db = Graph(uri='bolt://3.82.248.202:7687',user='neo4j',password='swabs-solids-children')

    def create(self, nome,genero,banda):
        return self.db.execute_query('CREATE (n:Musica {nome:$nome, genero:$genero,banda:$banda}) return n',
                                     {'nome': nome, 'genero': genero,'banda':banda})

    def read_by_name(self, nome):
        return self.db.execute_query('MATCH (n:Musica {nome:$nome}) RETURN n',
                                     {'nome': nome})
    
    def read_all_nodes(self):
        return self.db.execute_query('MATCH (n) RETURN n')

    def update_genero(self, nome,genero):
        return self.db.execute_query('MATCH (n:Musica {nome:$nome}) SET n.genero = $genero RETURN n',
                                     {'nome':nome, 'genero': genero})

    def delete(self, nome):
        return self.db.execute_query('MATCH (n:Musica {nome:$nome}) DELETE n',
                                     {'nome': nome})

    def delete_all_nodes(self):
        return self.db.execute_query('MATCH (n) DETACH DELETE n')

    def create_relation(self, musica1, musica2, relation):
        return self.db.execute_query('MATCH (n:Musica {nome:$nome1}), (m:Musica {nome:$nome2}) CREATE (n)-[r:RELATES{relation: $relation}]->(m) RETURN n, r, m',
                                     {'nome1': musica1['nome'], 'name2': musica2['nome'], 'relation': relation})

    def read_relation(self, musica1, musica2):
        return self.db.execute_query('MATCH (n:Person {name:$name1})-[r]->(m:Person {name:$name2}) RETURN n, r, m',
                                     {'nome1': musica1['nome'], 'name2': musica2['nome']})

def divider():
    print('\n' + '-' * 80 + '\n')

m = Musica()

while 1:    
    option = input('1. Create\n2. Read\n3. Update\n4. Delete\n')

    if option == '1':
        nome = input('  Nome: ')
        genero = input('   Genero: ')
        banda = input('   Banda: ')
        aux = m.create(nome,genero,banda)
        divider()

    elif option == '2':
        aux = m.read_all_nodes()
        pp(aux)
        divider()

    elif option == '3':
        nome = input('  Nome: ')
        genero = input('   Genero: ')
        
        aux = m.update_genero(nome,genero)
        divider()

    elif option == '4':
        nome = input('  Nome: ')

        
        aux = m.delete(nome)
        divider()

    else:
        break

m.db.close()