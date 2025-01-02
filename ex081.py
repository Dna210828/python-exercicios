# Crie um programa que vai ler vários números e colocar numa lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

from itertools import count
numeros = []
while True:
    numeros.append(int(input('Digite um numero: ')))
    resposta = input('Quer continuar? [S/N] ').strip().lower() # strip() remove quaisquer espaços em branco
    # no início ou no final da string.
    # lower() converte a string para letras minúsculas, facilitando a comparação.
    if resposta in 'Nn':
        break
print('-=' * 20)
print(f'Voce digitou {len(numeros)} elementos.')
numeros.sort(reverse=True) # Ordena a lista numeros em ordem decrescente.
# O parâmetro reverse=True faz com que a lista seja ordenada do maior para o menor.
print(f'Os numeros em ordem decrescente é {numeros}')
if 5 in numeros:
    print('O número 5 está na lista.')
else:
    print('Não foi encontrado o número 5 na lista')









