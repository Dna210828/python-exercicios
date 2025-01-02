# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A",
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.


frase = str(input('Digite uma frase: ')).strip().upper()
print(f'A letra A, apareceu {frase.count('A')} vezes na frase.')
print(f'A primeira vez que aparece a letra A, é na posição {frase.find('A')+1}')
print(f'A ultima posição que aparece a letra A, é na posição {frase.rfind('A')+1}.')





