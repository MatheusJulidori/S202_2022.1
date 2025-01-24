from Pessoa import Pessoa


class Professor(Pessoa):
    def __init__(self, nome, especialidade):
        self.nome = nome
        self.especialidade = especialidade

    def toString(self):
        return f'''
        Nome do professor: {self.nome}
        Especialidade do professor: {self.especialidade}
        '''
