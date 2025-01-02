# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Qual seu salário? R$ '))
if salario > 1250:
    print(f'O seu salário era R${salario:.2f} reais, com o aumento previsto em lei, passou a ser R${salario * 1.10:.2f} ')
if salario <= 1250:
    print(f'O seu salário era R${salario:.2f} reais, com o aumento previsto em lei, passou a ser R${salario * 1.15:.2f}')

