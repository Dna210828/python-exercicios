# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.


dinheiro = float(input('Quanto de dinheiro você tem na carteira? R$'))
dolar = dinheiro / 6.19
euro = dinheiro / 6.46
print(f'Com R${dinheiro:.2f}, você pode comprar US${dolar:.2f} dólares')
print(f'Com R${dinheiro:.2f}, você pode comprar E{euro:.2f} Euros')




