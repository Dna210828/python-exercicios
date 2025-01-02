
# O que são Listas?

# - Definição: Em Python, uma lista é uma coleção ordenada e mutável de elementos.
#    Você pode armazenar diferentes tipos de dados em uma lista,
#    incluindo números, strings e até outras listas.

# - Sintaxe: As listas são definidas utilizando colchetes `[]`,
#       com os elementos separados por vírgulas.
#
# Criando Listas
#
# ```python
# # Lista vazia
# minha_lista = []
#
# # Lista com elementos
# numeros = [1, 2, 3, 4, 5]
# frutas = ['maçã', 'banana', 'laranja']
# misturado = [1, 'maçã', 3.14, True]
# ```
#
# ### Acessando Elementos
#
# - Indexação: Você pode acessar os elementos de uma lista usando índices, que começam em 0.
#
# ```python
# print(numeros[0])  # Saída: 1
# print(frutas[1])   # Saída: banana
# ```
#
# - Indexação Negativa: Você também pode usar índices negativos para acessar elementos
#         a partir do final da lista.
#
# ```python
# print(frutas[-1])  # Saída: laranja
# ```
#
# ### Modificando Listas
#
# - **Adicionar Elementos**:
#   - `append()`: Adiciona um item ao final da lista.
#
#     ```python
#     frutas.append('uva')
#     ```
#
#   - `insert()`: Insere um item em uma posição específica.
#
#     ```python
#     frutas.insert(1, 'kiwi')  # Insere 'kiwi' na segunda posição
#     ```
#
#   - `extend()`: Adiciona elementos de outra lista.
#
#     ```python
#     frutas.extend(['pera', 'manga'])
#     ```
#
# - **Remover Elementos**:
#   - `remove()`: Remove o primeiro item com o valor especificado.
#
#     ```python
#     frutas.remove('banana')
#     ```
#
#   - `pop()`: Remove e retorna o último item da lista ou o item na posição especificada.
#
#     ```python
#     ultima_fruta = frutas.pop()  # Remove e retorna a última fruta
#     ```
#
#   - `clear()`: Remove todos os itens da lista.
#
#     ```python
#     frutas.clear()
#     ```
#
# ### Características das Listas
#
# - Mutabilidade: As listas podem ser alteradas após a criação.
#       Você pode adicionar, remover ou modificar elementos.

# - Ordenação: A ordem dos elementos é mantida. Se você adicionar um item,
#       ele aparecerá no final da lista (ou na posição especificada, se usar `insert()`).

# - Elementos Duplicados: Listas podem conter elementos duplicados.
#
# ### Métodos Comuns de Listas
#
# Aqui estão alguns métodos úteis para manipular listas:
#
# - `len(lista)`: Retorna o número de elementos na lista.
# - `sort()`: Ordena os elementos da lista em ordem crescente.
#
#   ```python
#   numeros.sort()  # Ordena a lista de números
#   ```
#
# - `reverse()`: Inverte a ordem dos elementos na lista.
#
#   ```python
#   frutas.reverse()  # Inverte a lista de frutas
#   ```
#
# - `count()`: Conta quantas vezes um elemento aparece na lista.
#
#   ```python
#   count_maçã = frutas.count('maçã')
#   ```
#
# ### Fatiamento de Listas (Slicing)
#
# Você pode acessar uma parte da lista usando fatiamento.
#
# ```python
# sub_lista = numeros[1:4]  # Obtém os elementos do índice 1 ao 3
# ```
#
# ### Exemplos Práticos
#
# #### 1. Criando e Manipulando uma Lista
#
# ```python
# # Criando uma lista de números
# numeros = [10, 20, 30, 40]
#
# # Adicionando um número
# numeros.append(50)
#
# # Removendo um número
# numeros.remove(20)
#
# # Imprimindo a lista
# print(numeros)  # Saída: [10, 30, 40, 50]
# ```
#
# #### 2. Usando Loop para Iterar sobre uma Lista
#
# ```python
# for fruta in frutas:
#     print(fruta)
# ```
#
# ### Conclusão
#
# As listas em Python são uma estrutura de dados poderosa e flexível,
# permitindo armazenar e manipular coleções de itens de maneira eficiente.
# Compreender como usar listas é fundamental para programar em Python,
# pois elas são amplamente utilizadas em diversas aplicações.