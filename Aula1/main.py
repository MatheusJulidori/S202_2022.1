from leao import Leao
from pato import Pato

leao = Leao(nome="Simba", selvagem=True, idade=15, genero="neutro")
pato = Pato(nome="Patolino", corDoBico="Rosa", idade=5, genero="M")

print(leao.toString())
print(pato.toString())

animais = [leao, pato]

print
