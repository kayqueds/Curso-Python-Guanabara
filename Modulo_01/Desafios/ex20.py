# sotear a ordem de 4 alunos e mostrar ordem sorteada
import random, time

print('Qual será a ordem de apresentações? 🤔')
print('-' * 30)
a1 = input('Digite o nome do 1° aluno: ').title()
a2 = input('Digite o nome do 2° aluno: ').title()
a3 = input('Digite o nome do 3° aluno: ').title()
a4 = input('Digite o nome do 4° aluno: ').title()

lista = [a1, a2, a3, a4]
# modulo para embaralhar
random.shuffle(lista)

print('A ordem das aprestações será...')
time.sleep(1.5)
print(lista)
