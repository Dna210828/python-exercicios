# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Seu Salario: R$'))
novo_salario = salario * 1.15
print(f'O seu salario era de R${salario:.2f}, com aumento de 15% passa a ser R${novo_salario:.2f}')
