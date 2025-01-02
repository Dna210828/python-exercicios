# Desenvolva um programa que leia seis números inteiros
# e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.

soma = 0
contador = 0
for c in range(1,7):
    numero = int(input(f'Digite o {c}° valor: '))
    if numero % 2 == 0:
        soma = soma + numero
        contador = contador + 1
print(f'Você informou {contador} números Pares, e a soma foi {soma}')









