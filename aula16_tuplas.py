'''lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
for comida in lanche:
    print(f'eu vou comer {comida}')
print(f'comi bastante')


O que são Tuplas?
As tuplas são uma estrutura de dados em Python que permitem armazenar uma coleção de itens.
 Elas são semelhantes às listas, mas possuem algumas diferenças importantes:

Imutabilidade: Uma vez criada, uma tupla não pode ser modificada.
Isso significa que você não pode adicionar, remover ou alterar os elementos de uma tupla.

Definição: Tuplas são definidas usando parênteses () e os elementos são separados por vírgulas.

Criando Tuplas

Você pode criar uma tupla de várias maneiras:

Tupla vazia:

tupla_vazia = ()

Tupla com elementos:
tupla_com_elementos = (1, 2, 3, 4)
Tupla com diferentes tipos de dados:
tupla_mista = (1, "texto", 3.14, True)
Tupla de um único elemento:
Para criar uma tupla com um único elemento, você deve incluir uma vírgula após o elemento:
tupla_unico = (5,)

Acessando Elementos
Os elementos de uma tupla podem ser acessados utilizando índices, assim como em listas.
 Os índices começam em 0.
tupla = (10, 20, 30, 40)

print(tupla[0])  # Saída: 10

print(tupla[2])  # Saída: 30

Slicing (Fatiamento)

Você pode usar o slicing para obter uma sub-tupla:

tupla = (1, 2, 3, 4, 5)
sub_tupla = tupla[1:4]  # Saída: (2, 3, 4)
Métodos de Tuplas
As tuplas têm alguns métodos embutidos, mas são limitados devido à sua imutabilidade:

count(): Conta quantas vezes um elemento aparece na tupla.
index(): mostra em que posição está um elemento

Exemplo:
tupla = (1, 2, 3, 1, 2)
print(tupla.count(1))  # Saída: 2 ( porque apareceu o numero 1, duas vezes)
print(tupla.index(2))  # Saída: 1 ( o numero 2 esta na posiçao 1 da tupla)

Comparação com Listas

Característica	Tuplas	            Listas

Sintaxe:    	 ()	                  []

Imutabilidade:	 Sim	              Não
Performance:  Mais rápidas	       Mais lentas
Métodos disponíveis: Menos métodos / Mais métodos


Quando Usar Tuplas?
Dados Imutáveis: Quando você precisa garantir que os dados não serão alterados,
como coordenadas geográficas ou valores constantes.

Desempenho: Tuplas são mais leves em termos de memória
e podem ser mais rápidas para acessar do que listas, devido à sua imutabilidade.

Chaves de Dicionário: Tuplas podem ser usadas como chaves em dicionários,
enquanto listas não podem (porque são mutáveis).

Exemplos de Uso
Armazenar coordenadas:

coordenadas = (10.0, 20.0)
Retornar múltiplos valores de uma função:

def funcao():
    return (1, 2, 3)

resultado = funcao()
Agrupamento de dados:

aluno = ("João", 20, "Engenharia")


Conclusão
As tuplas são uma parte fundamental da linguagem Python,
oferecendo uma maneira eficiente e segura de agrupar dados.
Sua imutabilidade e simplicidade fazem delas uma escolha ideal para várias situações,
especialmente quando a integridade dos dados é uma preocupação.'''








