# salário de funcionário
print('Salário de um funcionário com aumento!')
print('='*30)

salario = float(input('Digite o seu salário: R$ '))
#salario_total = salario + (salario * 0.15)
# aumento de 15%
aumento = salario + (salario*15/100)
print(f'O seu salario de R$ {salario} após o aumento de 15% passará por: R$ {aumento:.2f}')