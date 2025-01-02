# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
# No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves

nome = list()
peso = list()
while True:
    nome.append(str(input('Nome: ')))
    peso.append(float(input('Peso: ')))
    resposta = input('Quer continuar? [S/N]: ')
    if resposta in 'Nn':
        break
print(f'Ao todo você cadastrou {}')



