# Crie um programa que leia uma frase qualquer
# e diga se ela é um palíndromo, desconsiderando os espaços.

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
juntos = ''.join(palavras)
inverso = ''
for letra in range(len(juntos) -1, -1, -1):
    inverso += juntos[letra]
print(f'O inverso de {juntos} é {inverso}.')
if inverso == juntos:
    print('Temos um PALÍNDROMO!')
else:
    print('A frase digitada não é um palíndromo.')







