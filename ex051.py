# Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
if razao == 0:
    print('A razão não pode ser 0. ')
else:
    decimo = primeiro + (10 - 1) * razao
    for c in range(primeiro, decimo + razao, razao):
        print(f'{c}')
        







