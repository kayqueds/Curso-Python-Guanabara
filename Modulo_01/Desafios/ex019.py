'''
criar programa que faça um sorteio de
4 alunos e escreva quem vai limpar o qadro
'''
import random, time
print('Quem vai limpar o quadro? 🤔')
print('-'*30)
a1 = input('Digite o nome do 1° aluno: ').title()
a2 = input('Digite o nome do 2° aluno: ').title()
a3 = input('Digite o nome do 3° aluno: ').title()
a4 = input('Digite o nome do 4° aluno: ').title()

lista = [a1, a2, a3, a4]
sorteio = random.choice(lista)


print('E o azarado da vez será...')
time.sleep(1.5)
print(f'{sorteio}, você que vai limpar o quadro!')
