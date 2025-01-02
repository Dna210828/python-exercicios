#  Crie um programa onde o usuário possa digitar vários valores numéricos
#  e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado.
#  No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

numeros = list()  # Cria uma lista vazia para armazenar os números

while True:  # Inicia um loop infinito
    n = int(input('Digite um valor: '))  # Solicita ao usuário um valor inteiro

    # Verifica se o número não está na lista
    if n not in numeros:
        numeros.append(n)  # Adiciona o número à lista
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado. Não vou adicionar...')  # Informa que o número já existe

    r = input('Quer continuar? [S/N] ')  # Pergunta se o usuário deseja continuar
    if r in 'Nn':  # Se a resposta for 'N' ou 'n', o loop é encerrado
        break

print('-=' * 30)  # Imprime uma linha de separação
numeros.sort()  # Ordena a lista de números em ordem crescente
print(f'Você digitou os valores {numeros}.')  # Exibe os números digitados
