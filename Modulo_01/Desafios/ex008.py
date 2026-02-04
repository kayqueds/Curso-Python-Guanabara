print('Coversão de metros, centimetros e milimetros')
print("-"*30)

metros = int(input('Digite um valor em metros: '))
centimetros = metros * 100
milimetros = metros * 1000
decametros = metros / 10
hectometros = metros / 100
kilometros = metros / 1000

print(f'{metros}m equivalem a:')
print(f'{centimetros}cm')
print(f'{milimetros}mm')
print(f'{decametros}dm')
print(f'{hectometros}hm')
print(f'{kilometros}km')