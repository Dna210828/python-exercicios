'''

1. Métodos Básicos para Manipulação de Strings

a. upper()
Converte todos os caracteres da string para maiúsculas.
texto = "olá, mundo!"
texto_maiusculo = texto.upper()  # "OLÁ, MUNDO!"


b. lower()
Converte todos os caracteres da string para minúsculas.
texto = "OLÁ, MUNDO!"
texto_minusculo = texto.lower()  # "olá, mundo!"


c. capitalize()
Converte o primeiro caractere da string para maiúsculo e os demais para minúsculos.
texto = "olá, mundo!"
texto_capitalizado = texto.capitalize()  # "Olà, mundo!"



d. title()
Converte o primeiro caractere de cada palavra para maiúsculo.
texto = "olá, mundo!"
texto_titulo = texto.title()  # "Olà, Mundo!"



e. strip()
Remove espaços em branco do início e do fim da string.
texto = "   olá, mundo!   "
texto_sem_espacos = texto.strip()  # "olá, mundo!"



2. Busca e Substituição
a. find(substring)
Retorna o índice da primeira ocorrência de uma substring. Retorna -1 se não encontrar.
texto = "olá, mundo!"
indice = texto.find("mundo")  # 5



b. replace(old, new)
Substitui todas as ocorrências de uma substring por outra.
texto = "olá, mundo!"
novo_texto = texto.replace("mundo", "universo")  # "olá, universo!"



3. Divisão e Junção
a. split(sep)
Divide a string em uma lista de substrings, usando o separador especificado.
texto = "olá, mundo!"
lista = texto.split(", ")  # ['olá', 'mundo!']

b. join(iterable)
Une uma lista de strings em uma única string, usando a string que chama o método como separador.
lista = ['olá', 'mundo!']
texto_unido = " ".join(lista)  # "olá mundo!"



5. Outros Métodos Úteis
a. len()
Retorna o comprimento da string.
texto = "olá"
comprimento = len(texto)  # 3


b. count(substring)
Conta quantas vezes uma substring aparece na string.
texto = "olá, mundo! olá!"
contagem = texto.count("olá")  # 2'''



