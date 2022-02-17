from Aula1.animal import Animal


class Pato(Animal):
    def __init__(self, nome, corDoBico, idade, genero):
        self.nome = nome
        self.corDoBico = corDoBico
        self.idade = idade
        self.genero = genero

    def correr(self):
        return f"O pato {self.nome} está nadando!"

    def toString(self):
        f'''Nome:{self.nome}
            Cor do bico:{self.corDoBico}
        '''
