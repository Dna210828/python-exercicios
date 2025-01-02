# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = input('Informe seu Sexo:[M/F]: ').strip().upper()[0]
while sexo not in ['M', 'F']:
    sexo = str(input('Dados Inválidos. Digite seu sexo [M/F]: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso.')























