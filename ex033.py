# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
c = int(input('Digite mais um número: '))
#verificando o maior
maior = a # já considerou o 'a' maior. eliminando assim, um if.
if b > c and b > a:
    maior = b
if c > a and c > b:
    maior = c
#verificando o menor
menor = a # já considerou o 'a' menor eliminando assim, um if.
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print(f'O maior valor digitado é {maior}. ')
print(f'O menor valor digitado é {menor}. ')





