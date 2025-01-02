# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas e minúsculas.
# Quantas letras ao todo e sem considerar espaços
# Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome completo: ')).strip() # strip(): Remove espaços em branco no início e no final da string digitada.
print('Analisando seu nome...')
print(f'Seu nome em letras maiúsculas é {nome.upper()} ') # nome.upper(): Converte todas as letras da variável nome para maiúsculas.
print(f'Em minúsculas é {nome.lower()}') # nome.lower(): Converte todas as letras da variável nome para minúsculas.
print(f'Ao todo sem considerar espaços seu nome tem {len(nome) - nome.count(" ")} letras')
# len(nome): Conta o número total de caracteres na string nome.
# nome.count(" "): Conta quantos espaços existem na string nome.
# len(nome) - nome.count(" "): Calcula o total de letras, subtraindo o número de espaços do total de caracteres.

#print(f'E seu primeiro nome tem {nome.find(' ')} letras.')
separa = nome.split() # nome.split(): Divide a string nome em uma lista de palavras, usando o espaço como delimitador. O primeiro nome estará na posição 0 da lista.
print(f'Seu primeiro nome é {separa[0]}, e ele tem {len(separa[0])} letras')
# separa[0]: Acessa o primeiro elemento da lista separa, que é o primeiro nome.
# len(separa[0]): Conta o número de letras no primeiro nome.
# Exibe o primeiro nome e o número de letras que ele contém.



















