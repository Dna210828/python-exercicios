# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.

import random

# Gera um número aleatório entre 0 e 10
computador = random.randint(0, 10)
palpites = 0

print('Estou pensando em um número de 0 a 10, tente adivinhar:')

# Loop para o jogador tentar adivinhar
while True:
    palpite = int(input('Qual o seu palpite? '))
    palpites += 1  # Contador de palpites

    if palpite < 0 or palpite > 10:
        print('Por favor, insira um número entre 0 e 10.')
        continue  # Pede novo palpite se o número estiver fora do intervalo

    if palpite == computador:
        print(f'Parabéns! Você acertou o número {computador} em {palpites} palpites.')
        break  # Sai do loop se o jogador acertar
    else:
        print('Errou. Tente novamente!')


