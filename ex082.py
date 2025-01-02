# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras
# que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.
#--------------------------------------------------------------------------------------------------
# Inicializa três listas vazias: impares para armazenar números ímpares,
# pares para números pares
# e numeros para armazenar todos os números digitados pelo usuário.
impares = list()
pares = list()
numeros = list()
while True: # Inicia um loop infinito que continuará até que um break seja encontrado.
    numeros.append(int(input('Digite um número: ')))
    resposta = input('Quer continuar? [S/N]: ')
    if resposta in 'Nn': # Verifica se a resposta do usuário é 'Nn'.
        # Se for, o bloco de código dentro do if será executado.
        break # break entra em ação após o usuario digitar 'Nn' após, o comando break interrompe o loop.
for i, v in enumerate(numeros): # A função enumerate() é usada para adicionar um contador (ou índice)
    # a um iterável (como uma lista).
#Quando você passa a lista numeros para enumerate(), ela retorna um objeto enumerado que gera pares de índice
    # e valor. Por exemplo,
    # se numeros contiver [10, 15, 20], enumerate(numeros) gerará:
    #(0, 10)
    #(1, 15)
    #(2, 20)
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print('-=' * 20)
print(f'A lista completa é {numeros}.')
print(f'A lista de pares é {pares}.')
print(f'A lista de impares é {impares}.')



