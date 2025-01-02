#  Crie um programa onde o usuário possa digitar cinco valores numéricos
#  e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
#  No final, mostre a lista ordenada na tela.

# Cria uma lista vazia chamada 'numeros'
numeros = list()

# Loop que irá iterar 5 vezes, permitindo a entrada de 5 números
for c in range(0, 5):
    # Solicita ao usuário que digite um valor e converte para inteiro
    n = int(input('Digite um valor: '))

    # Verifica se é a primeira iteração ou se o número é maior que o último da lista
    if c == 0 or n > numeros[-1]:
        # Adiciona o número ao final da lista
        numeros.append(n)
        # Informa que o número foi adicionado ao final
        print('Adicionado ao final da lista')
    else:
        # Inicializa a variável 'posicao' para encontrar o local correto de inserção
        posicao = 0
        # Loop para encontrar a posição correta na lista
        while posicao < len(numeros):
            # Verifica se o número 'n' é menor ou igual ao elemento na posição 'posicao'
            if n <= numeros[posicao]:
                # Insere o número 'n' na posição correta
                numeros.insert(posicao, n)
                # Informa que o número foi adicionado na posição específica
                print(f'Adicionado na posição {posicao} da lista...')
                # Interrompe o loop após a inserção
                break
            # Incrementa a posição para verificar o próximo elemento
            posicao = posicao + 1

# Imprime uma linha de separação para melhor legibilidade
print('-=' * 30)
# Exibe a lista final de números em ordem
print(f'Os valores digitados em ordem foram {numeros}.')


