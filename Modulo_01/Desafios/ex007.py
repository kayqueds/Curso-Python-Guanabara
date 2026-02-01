from time import sleep
print('Média do Aluno')
print("-"*20)
nota1 = float(input('Digite a sua primeira nota: '))
nota2 = float(input('Digite a sua segunda nota: '))
media = (nota1+nota2)/2
print('Calculando média do aluno...')
sleep(1.5)
print(f'A média do aluno foi: {media}')