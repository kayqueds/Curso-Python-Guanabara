print('Altura e Largura de uma parede')
print("-"*30)
altura = float(input('Digite a altura em m da parede: '))
largura = float(input('Digite a largura em m da parede: '))
area = altura * largura

# 1 balde = 2m² da area da parede
balde_tinta = area / 2
print(f'A área da parede será: {area}m²')
print(f"Serão necessários: {balde_tinta}l de tinta")