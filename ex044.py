#  Elabore um programa que calcule o valor a ser pago por um produto,
#  considerando o seu preço normal e condição de pagamento:
# à vista dinheiro/cheque: 10% de desconto
# à vista no cartão: 5% de desconto
# em até 2x no cartão: preço formal
# 3x ou mais no cartão: 20% de juros

print('{:=^40}'.format(' Lojinha '))
preco = float(input('Preço das compras: R$ '))
print('''FORMAS DE PAGAMENTO:
[ 1 ] À vista dinheiro com 10% de desconto
[ 2 ] Á vista cartão 5% de desconto
[ 3 ] Cheque 10% de desconto
[ 4 ] Cartão de crédito em até 10x acréscimo de 20% ''')
print(f'O preço da compra foi de R${preco:.2f}.')
while True:
    opcao = int(input('Qual a forma de pagamento: '))
    if opcao == 1:
        print(f'Com desconto à vista o valor fica R${preco * 0.90:.2f}.')
        break
    elif opcao == 2:
        print(f'Com desconto do cartão o valor fica R${preco * 0.95:.2f}.')
        break
    elif opcao == 3:
        print(f'Com desconto no cheque a vista o valor fica R${preco * 0.90:.2f}.')
        break
    elif opcao == 4:
        parcelas = int(input('Quantas parcelas? '))
        print(f'Sua compra será parcelada em {parcelas}x de R${preco / parcelas * 1.20:.2f} COM JUROS. ')
        print(f'Sua compra de R${preco:.2f} vai custar R${preco * 1.20:.2f} no final.')
        break
    else:
         print('Forma de pagamento Inválida. TENTE NOVAMENTE.')




















