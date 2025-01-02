# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

produto = float(input('Qual é o preço do produto? R$'))
desconto = produto * 0.95
print(f'O preço do produto é R${produto:.2f}, com desconto de 5% passa a ser R${desconto:.2f}')
