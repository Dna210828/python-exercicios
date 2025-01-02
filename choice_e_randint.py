from random import choice, randint

nomes = ['Alice', 'Bob', 'Carlos', 'Diana']
indice = randint(0, len(nomes) - 1)  # Gera um índice aleatório. o -1 é porque na contagem do randint,
#o indice vai de 0 a 3. o numero 0 é (alice), o 1 é (bob), 2 e 3. (carlos e diana). o - 1 ta excluindo o indice 4
# pois o randint é diferente da variavel 'nomes'. que tem 4 nomes. o randint inicia no indice 0 e vai até o fim.
# diferente do range. que vai de range(1,11). nesse caso o range nao conta o 11. indo de 1 até 10.

aluno_escolhido = nomes[indice]  # Escolhe o aluno na lista

print(f'O aluno escolhido foi: {aluno_escolhido}')


# para o python a tradução de randint é ( aleatorio inteiro) ou seja, vai sortear um numero inteiro aleatório.
# random (aleatório)

