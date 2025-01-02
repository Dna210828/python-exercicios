# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
# e mostre sua categoria, de acordo com a idade:
# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JÚNIOR
# Até 25 anos: SÊNIOR
# Acima de 25 anos: MASTER

from _datetime import date
atual_ano = date.today().year
ano_nascimento = int(input('Ano de nascimento do Atleta: '))
idade_atleta = atual_ano - ano_nascimento
print(f'Atleta de: {ano_nascimento}')
print(f'Idade: {idade_atleta}')
if idade_atleta <= 9:
    Categoria = 'MIRIM'
elif idade_atleta <= 14:
    Categoria = 'INFANTIL'
elif idade_atleta <= 19:
    Categoria = 'JÚNIOR'
elif idade_atleta <=  25:
    Categoria = 'SÉNIOR'
else:
    Categoria = 'MASTER'
print(f'Atleta da categoria {Categoria}.')



