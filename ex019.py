# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.


from random import choice #  Para usar a função choice(), você precisa importar o módulo random:

# Coletando os nomes dos alunos
aluno1 = input('Nome do aluno: ')
aluno2 = input('Nome do aluno: ')
aluno3 = input('Nome do aluno: ')
aluno4 = input('Nome do aluno: ')

lista = [aluno1, aluno2, aluno3, aluno4] #  Armazenando os nomes em uma lista

escolhido = choice(lista) ## Sorteando um aluno
#A função choice() é uma maneira simples e eficaz de selecionar um item aleatório de uma sequência em Python,
# tornando-a útil em diversas situações, como sorteios, jogos, e qualquer aplicação que requeira aleatoriedade.

print(f'O aluno escolhido foi {escolhido}') # Imprimindo o aluno escolhido











