# importando uma biblioteca (conteudo adicional)
#import math # importa tudo de match
from math import sqrt, floor # importa apenas esses 2 módulos

print('Biblioteca de operações Matemática')
num = int(input('Digite um número: '))
raiz = sqrt(num)

print(f'Raíz quadrada de {num} é: {floor(raiz)}')