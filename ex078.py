# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final,
# mostre qual foi o maior e o menor valor digitado
# e as suas respectivas posições na lista.


numeros = []  # Cria uma lista vazia para armazenar os números

for c in range(0, 5):  # Loop que irá iterar 5 vezes (de 0 a 4)
    numeros.append(int(input(f'Digite um numero para a posição {c}: ')))
    # Solicita um número ao usuário e o adiciona à lista

print(f'Você digitou os valores {numeros}.')  # Exibe todos os números digitados
print(f'O maior valor digitado foi {max(numeros)} ')  # Encontra e exibe o maior número da lista
print(f'O menor valor digitado foi {min(numeros)}, ')  # Encontra e exibe o menor número da lista
print('-'*40)  # Imprime uma linha de separação














