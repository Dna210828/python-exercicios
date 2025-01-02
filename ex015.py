# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dias = int(input('Quantos dias alugados? '))
km = float(input('KM percorrido: '))
diaria = dias * 60
km_rodado = km * 0.15
total = diaria + km_rodado
print(f'O carro foi alugado por {dias} dias, as diarias ficam no total de R${diaria:.2f}')
print(f'O veiculo andou por {km:.2f}km, totalizando R${km_rodado:.2f}')
print(f'O valor das diaria e do KM percorrido é de R${total:.2f}')



