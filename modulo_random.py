''' O módulo random em Python é uma biblioteca padrão que fornece várias funções para gerar números aleatórios
 e realizar operações relacionadas a aleatoriedade.

Aqui estão algumas das principais funcionalidades e como elas podem ser usadas:

                   1. Importando o Módulo
Para usar o módulo random, você precisa importá-lo no seu código:

import random
    2. Funções Comuns do Módulo random

random.random(): Gera um número de ponto flutuante aleatório entre 0.0 e 1.0.
numero = random.random()
print(numero)  # Exemplo de saída: 0.37444887175646646

random.randint(1, 10): Gera um número inteiro aleatório entre 1 e 10.
numero_inteiro = random.randint(1, 10)
print(numero_inteiro)  # Exemplo de saída: 7


random.choice(seq): Escolhe um elemento aleatório de uma sequência (como uma lista ou tupla).

lista = ['maçã', 'banana', 'laranja']
fruta = random.choice(lista)
print(fruta)  # Exemplo de saída: 'banana'


random.shuffle(x): Embaralha a lista x in-place, ou seja, modifica a lista original.

lista = [1, 2, 3, 4, 5]
random.shuffle(lista)
print(lista)  # Exemplo de saída: [3, 1, 4, 5, 2]

o termo "in-place" refere-se a operações que modificam diretamente o objeto original,
sem criar uma cópia dele. Isso significa que a alteração é feita no próprio local da memória
onde o objeto está armazenado.


random.sample(population, k): Retorna uma lista de
k
k elementos únicos escolhidos aleatoriamente da population.

amostra = random.sample(range(100), 10)  # 10 números únicos de 0 a 99
print(amostra)


3. Aplicações Práticas
Jogos: Usado para gerar resultados aleatórios, como em jogos de dados ou sorteios.

Simulações: Útil em simulações estatísticas onde a aleatoriedade é necessária.

Teste de Algoritmos: Para testar algoritmos com entradas aleatórias e verificar seu comportamento.

4. Considerações sobre Aleatoriedade
Embora o módulo random seja adequado para muitas aplicações, ele não é adequado para criptografia
ou situações que exigem segurança, pois os números gerados não são verdadeiramente aleatórios
 (são pseudoaleatórios). Para essas situações, você pode usar o módulo secrets,
que é projetado para gerar números aleatórios de forma mais segura.'''