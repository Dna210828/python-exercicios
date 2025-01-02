# Faça um programa que leia o nome completo de uma pessoa.
# mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Digite seu nome completo: ')).strip()
dividir_nome = nome.split()
print(f'é um prazer te conhecer {nome}')
print(f'Seu primeiro nome é {(dividir_nome[0])}')
print(f'Seu ultimo nome é {dividir_nome[len(dividir_nome)-1]}') # usa o -1 para acessar o final da lista.



