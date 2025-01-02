#Crie um programa que leia dois valores e mostre um menu na tela:
#[1] somar
#[2] multiplicar
#[3] maior
#[4] novos números
#[5] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
while True:
    print('''Escolha uma Opção 
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR''')
    opcao = int(input('Opção: '))
    if opcao == 1:
        print(f'{n1} + {n2} = {n1 + n2}.')
        print('-' * 20)
    elif opcao == 2:
        print(f'{n1} x {n2} = {n1 * n2}')
        print('-' * 20)
    elif opcao == 3:
        if n1 == n2:
            print('Os valores são iguais.')
            print('-' * 20)
        elif n1 > n2:
            maior = n1
            print(f'Entre os números {n1} e {n2}, o maior é {maior}.')
            print('-' * 20)
        elif n2 > n1:
            maior = n2
            print(f'Entre os números {n1} e {n2}, o maior é {maior}.')
            print('-' * 20)
    elif opcao == 4:
        print('Digite novos números ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
        continue
    elif opcao == 5:
        print('Finalizando...')
        break
    else:
        print('Opção inválida! Tente novamente.')
    sleep(2)
print('Fim do programa.')


































