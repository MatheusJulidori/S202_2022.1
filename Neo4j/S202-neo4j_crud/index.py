from pprintpp import pprint as pp
from db.database import Graph

class Person(object):
    def __init__(self):
        self.db = Graph(uri='bolt://3.82.248.202:7687',user='neo4j',password='swabs-solids-children')

    def create(self, name, password):
        return self.db.execute_query('CREATE (n:Person {name:$name, password:$password}) return n',
                                     {'name': name, 'password': password})


p = Person()
p.create('Matheus','1234')
