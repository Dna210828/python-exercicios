# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.


from random import randint

print('Sou seu computador, e vou pensar em um número entre 0 e 5. tente adivinhar')
print('-=' * 30)
computador = randint(0,6)
jogador = int(input('Eu pensei no número: '))
print('-=' * 15)
if jogador == computador:
    print(f'PARABÉNS. VOCE ACERTOU. eu também pensei no número {computador}.')
else:
    print(f'Poxa. voce errou. eu tinha pensado no número {computador} e nao no {jogador}')


