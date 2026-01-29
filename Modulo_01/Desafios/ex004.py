# usuario vai digitar algo
valor = input('Digite algo: ')
# verificações desse dado (o que ele é)
tipo_dado = type(valor)
eTexto = valor.isalpha()
eNumero = valor.isnumeric()
eTextoNumero = valor.isalnum()
eTudoMaiusculo = valor.isupper()
eTudoMinusculo = valor.islower()
temEspaco = valor.isspace()

# saída
print("-" * 30)
print(f'{valor} é do tipo {tipo_dado}')
print(f'Ele é um número? {eNumero}')
print(f'Ele é um texto? {eTexto}')
print(f'Ele é um número ou texto? {eTextoNumero}')
print(f'Ele é todo em maiúsculo? {eTudoMaiusculo}')
print(f'Ele é todo em minúsculo? {eTudoMinusculo}')
print(f'Ele tem espaco? {temEspaco}')

