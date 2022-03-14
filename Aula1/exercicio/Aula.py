class Aula():
    def __init__(self, prof, alunos, materia):
        self.prof = prof
        self.alunos = alunos
        self.materia = materia

    def getListaPresenca(self):
        lista = f"Aula de {self.materia} \n" \
                f"Professor: {self.prof.nome} \n" \
                f"Alunos Presentes: "
        for aluno in self.alunos:
            lista += aluno.toString()

        return lista
