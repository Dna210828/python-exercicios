# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
# Ex: Digite um número: 6.127
# O número 6.127 tem a parte Inteira 6.

from math import trunc # trunc mostra a porçao inteira, eliminando da virgula para frente.
numero = float(input('Digite um numero: '))
inteiro = trunc(numero)
print(f'O numero digitado foi {numero}, e sua porção inteira é {inteiro}.')


