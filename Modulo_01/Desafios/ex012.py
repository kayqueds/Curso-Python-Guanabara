print('Desconto de um produto')
print('-'*30)
# desconto de produto
produto_preco = float(input('Digite um valor de um produto: '))
desconto = produto_preco * 0.05
# subtração produto base - desconto 5%
preco_total = produto_preco - desconto

print(f'O preço do produto é R$ {produto_preco}')
print(f'Com desconto de 5%, o preço total será: R$ {preco_total:.2f}')