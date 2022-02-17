from Aula1.animal import Animal


class Leao(Animal):
    def __init__(self, nome, selvagem, idade, genero):
        self.nome = nome
        self.selvagem = selvagem
        self.idade = idade
        self.genero = genero

    def correr(self):
        return f"O leão {self.nome} está correndo!"

    def toString(self):
        f'''Nome:{self.nome}
                {self.selvagem}
        '''
