# biblioteca random aleatorio
import random, time
from math import ceil

print('-----------JOGO: chegar no 10-----------')
print('Você tem 5 chances')
inicio = time.time()
cont = 5
reset = 0
while True:
    num = random.randint(1, 10)
    if num == 10:
        fim = time.time()
        total = fim - inicio
        print(f'Fim de jogo!🏆 Você chegou a {num}\ntempo de busca: {ceil(total)} segundos')
        print(f'Foi resetado: {reset} vezes')
        break
    elif cont == 0:
        print('Você perdeu, recomeçando')
        cont = 5
        reset +=1
    else:
        print(num)
        time.sleep(1)
        cont -= 1
