'''
faça um programa que leia um angulo qualquer e mostre
na tela o valor do seno, cosseno e tangente desse angulo
'''
import math
angulo = int(input('Digite o angulo: '))
# convertendo angulo para radiano
radial = math.radians(angulo)

coseno = math.cos(radial)
tangente = math.tan(radial)
seno = math.sin(radial)

# saida
print(f'{angulo}°')
print(f'Seu cosseno é: {coseno:.2f}')
print(f'Seu seno é: {seno:.2f}°')
print(f'Seu tangente é: {tangente:.2f}°')