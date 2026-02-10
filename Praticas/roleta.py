# importando biblioteca
import random, time
ti = time.time()
colega1 = input('Digite o nome do 1° colega: ').title()
colega2 = input('Digite o nome do 2° colega: ').title()
colega3 = input('Digite o nome do 3° colega: ').title()

# vetor fixo
lista_tarefas = ['Documentar código', 'Limpar o café','Corrigir bug chato']

lista_colegas = [colega1, colega2, colega3]

# método para embaralhar vetor
random.shuffle(lista_colegas)

# laço de repetição
for i in range(3):
    print(f'Sorteando responsável pela tarefa {lista_tarefas[i]}...')
    time.sleep(2)
    print(f'Colega: {lista_colegas[i]}')
    print('-'*30)
tf = time.time()
tempo =tf-ti
print(f'O sorteio durou {tempo:.2f} segundos')
