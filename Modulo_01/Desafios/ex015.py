print('Aluguel de Carro 🚗')
print('='*30)
qtd_dias_alugado = int(input('Quantos dias o carro foi alugado? '))
km_rodado = float(input('Quantos KM rodados? '))

preco_pagar = (qtd_dias_alugado * 60) + (km_rodado * 0.15)
print("O total a pagar é de R${:.2f}".format(preco_pagar))