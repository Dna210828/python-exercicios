# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa,
# o salário do comprador
# e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
from time import sleep

imovel = float(input('Valor do imóvel: R$'))
salario = float(input('Seu salário: R$'))
anos_a_pagar = int(input('Em quantos anos deseja pagar o imóvel? '))
prazo = anos_a_pagar * 12
prestacao = imovel / prazo
print(f'Para pagar um imóvel de R${imovel:.2f} Reais, em {anos_a_pagar} anos, a prestacao sera de R${prestacao:.2f}.')
limite = salario * 30/100
print(f'AGUARDE, Analisando seus dados...')
sleep(2)
if prestacao > limite:
    print(f'Baseado nos dados informados, a prestação não corresponde com o minimo exigido.')
    print('EMPRÉSTIMO NEGADO. seu salario nao corresponde com a prestação mensal.')
else:
    print(f'Baseado nos dados informados, a prestação corresponde com o minimo exigido.')
    print('EMPRÉSTIMO CONCEDIDO, salario compátivel com a prestação.')











