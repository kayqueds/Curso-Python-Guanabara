print("Tabuada")
print('-'*10)
def tab(num):
    for i in range(1,11):
        print(f"{num} x {i} = {num * i}")

n1 = int(input('Digite um número: '))
tab(n1)