# 1. Faça um programa que receba o salário base de um funcionário,
# calcule e mostre o salário a receber,
# sabendo-se que o funcionário tem um bônus de 10% sobre o salário base
# e paga plano de saúde de 7% sobre este salário.


salario_base = float(input('Salário base do funcionário: R$'))
bonus = salario_base * 0.10
desconto_plano_saude = salario_base * 0.07
salario_a_receber = salario_base + bonus - desconto_plano_saude
print(f'Salário base é R${salario_base:.2f}')
print(f'Bônus de 10%: R${bonus:.2f}.')
print(f'Desconto plano de saúde. 7%: {desconto_plano_saude:.2f}')
print(f'Salário a receber: R${salario_a_receber:.2f}.')











