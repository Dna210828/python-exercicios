# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

from math import sqrt
numero = int(input('Digite um número: '))
raiz = sqrt(numero)
print(f'O dobro de {numero} vale {numero * 2}')
print(f'O triplo de {numero} vale {numero * 3}')
print(f'A raiz quadrada de {numero} vale {raiz:.2f}')

