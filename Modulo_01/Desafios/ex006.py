print('Dobro, Triplo e Raíz Quadrada')
print('-'*30)
numero = int(input('Digite um número: '))
dobro = numero * 2
triplo = numero * 3
raiz_quadrada = numero ** (1/2)
# :.2f formta para 2 casas decimais
print(f'Você digitou: {numero}\no seu dobro é: {dobro},\nseu triplo é: {triplo}\nsua raíz quadrada é: {raiz_quadrada:.2f}')
