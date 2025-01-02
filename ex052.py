# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

numero = int(input('Digite um número: '))
numero_primo = 0
for c in range(1, numero + 1):
    if numero % c == 0:
        print('\033[33m', end='')
        numero_primo += 1
    else:
        print('\033[31m', end='')
    print(f'{c} ', end='')
print(f'\n\33[mO número {numero} foi divisível {numero_primo} vezes.')
if numero_primo == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele não é PRIMO!')






