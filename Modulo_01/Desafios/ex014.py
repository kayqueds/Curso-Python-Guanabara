from time import sleep
print('Conversor de Célcius para Fahrenheit')
c = float(input('Informe a temperatura em °C: '))
f = c * (9/5) + 32
print("Convertendo temperatura...")
sleep(1.5)
print(f"A temperatura de {c:.1f}°C corresponde a {f:.1f}°F!")