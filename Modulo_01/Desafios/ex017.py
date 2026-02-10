from math import sqrt, pow
print('Hipotenusa, Teorema de Pitágoras')
print('-'*35)
cateto_op = float(input('Digite o comprimento do cateto oposto: '))
cateto_adj = float(input('Digite o comprimento do cateto adjacente: '))

hipotenusa = sqrt(pow(cateto_op, 2) + pow(cateto_adj, 2) )
print(f'O comprimento da hipotenusa de {cateto_op} e {cateto_adj} equivale a {hipotenusa:.2f}m²')