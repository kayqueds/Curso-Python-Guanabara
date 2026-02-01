# Operações Aritiméticas

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1+n2
m = n1*n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('A soma vale: {},\n o produto vale {}\n e a divisão vale: {:.2f}\n'.format(s, m, d))
print('Divisão inteira: {} e potência vale: {}'.format(di, e))