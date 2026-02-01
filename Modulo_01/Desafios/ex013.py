# salário de funcionário
print('Salário de um funcionário com aumento!')
print('='*30)

salario = float(input('Digite o seu salário: R$ '))
#salario_total = salario + (salario * 0.15)
# aumento de 15%
aumento = salario * 0.15
salario_total = salario + aumento
print(f'O seu salario de R$ {salario} após o aumento de 15% passará por: R$ {salario_total:.2f}')