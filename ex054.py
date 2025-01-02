#  Crie um programa que leia o ano de nascimento de sete pessoas. No final,
#  mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date
atual = date.today().year
maior = 0
menor = 0
for pessoas in range(1,8):
    nascimento = int(input(f'Ano de nascimento da {pessoas}° pessoa: '))
    idade = atual - nascimento
    if idade >= 18:
        maior = maior + 1
    else:
        menor = menor + 1
print(f'Ao todo temos {maior} pessoas maiores de idade.')
print(f'E {menor} pessoas menores de idade.')






































