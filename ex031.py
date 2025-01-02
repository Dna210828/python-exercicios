# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km
# e R$0,45 parta viagens mais longas.

distancia = float(input('Distancia da viagem em KM: '))
preco_1 = 0.50 * distancia
preco_2 = 0.45 * distancia
if distancia <= 200:
    print(f'A distancia da viagem é {distancia:.0f} km, o valor da passagem é R${preco_1:.2f}')
else:
    print(f'A distancia da viagem é {distancia:.0f} km, o valor da passagem é R${preco_2:.2f}.')



