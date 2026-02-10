# ler numero qualquer e mostrando sua porção inteira
from math import trunc
# trunc ignora a virgula
num = float(input('Digite um número: '))
inteiro = trunc(num)
print(f'O número {num} tem a parte inteira {inteiro}')

