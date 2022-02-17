from Aluno import Aluno
from Aula import Aula
from Professor import Professor

aluno1 = Aluno("Matheus Henrique Julidori", "66", "GES", 5)

aluno2 = Aluno("Arthur Ferreira Silva", "1698", "GEC", 5)

aluno3 = Aluno("Amanda Silva Guimarães", "1643", "GEC", 5)

alunos = [aluno1, aluno2, aluno3]

prof = Professor("Bruno Monteiro", "Circuitos Digitais")

aula = Aula(prof, alunos, "Digital II")

lista = aula.getListaPresenca()

print(lista)
