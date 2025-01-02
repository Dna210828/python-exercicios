# Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
from time import  sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''Suas Opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA ''')
jogador = int(input('Escolha sua Opção: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 11)
print(f'computador jogou {itens[computador]}')
print(f'Jogador jogou {itens[jogador]}')
print('-=' * 11)
if computador == 0: # computador jogou pedra
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('Jogador vence')
    elif jogador == 2 :
        print('computador vence')
    else:
        print('Jogada Inválida!')
elif computador == 1: # computador jogou papel
    if jogador == 0:
        print('computador vence')
    elif jogador == 1:
        print('empate')
    elif jogador == 2:
        print('jogador vence')
    else:
        print('Jogada Inválida!')
elif computador == 2: # computador jogou tesoura
    if jogador == 0:
        print('jogador vence')
    elif jogador == 1:
        print('computador vence')
    elif jogador == 2:
        print('empate')
    else:
        print('jogada invalida')





