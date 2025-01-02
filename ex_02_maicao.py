# Faça um programa que receba o ano de nascimento de uma pessoa. o ano atual, calcule e mostre:
# A) a idade dessa pessoa
# B) Quantos anos ela terá em 2050.

from datetime import date
ano_atual = date.today().year
nascimento = int(input('Ano de nascimento: '))
idade = ano_atual - nascimento
anos_em_2050 = 2050 - nascimento
print(f'Quem nasceu em {nascimento}, tem {idade} anos em {ano_atual}')
print(f'Você terá a idade de {anos_em_2050} anos, No ano de 2050, daqui há {anos_em_2050 - idade} anos.')




