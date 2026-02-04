print("Tabuada")
print('-'*10)
def tab(num):
    for i in range(1,11):
        print(f"{num} x {i} = {num * i}")

n1 = int(input('Digite um número: '))
tab(n1)
# jeito antigo, não viável
"""
n2 = int(input('Digite um número: '))
print('{} x {} = {}'.format(n2,1,n2*1))
print('{} x {} = {}'.format(n2,2,n2*2))
print('{} x {} = {}'.format(n2,3,n2*3))
print('{} x {} = {}'.format(n2,4,n2*4))
print('{} x {} = {}'.format(n2,5,n2*5))
print('{} x {} = {}'.format(n2,6,n2*6))
print('{} x {} = {}'.format(n2,7,n2*7))
print('{} x {} = {}'.format(n2,8,n2*8))
print('{} x {} = {}'.format(n2,9,n2*9))
print('{} x {} = {}'.format(n2,10,n2*10))
"""
