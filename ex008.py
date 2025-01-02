# 3 Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.


metros = int(input('Uma distância em metros: '))
centimetros = metros * 100
milimetros = metros * 1000
print(f'A medida de {metros:.1f}M em centimetros é {centimetros} CM')
print(f'A medida de {metros:.1f}M em milimetros é {milimetros} MM')


