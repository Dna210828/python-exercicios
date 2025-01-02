# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

cidade = input('Em que cidade voce nasceu? ').strip() # remove os espaços em branco no inicio e fim
print(cidade[:5].upper() == 'SANTO')

# cidade[:5]: Esta parte pega os primeiros 5 caracteres da string cidade. O fatiamento [:5] significa "do início até o quinto caractere", ou seja, os caracteres de índice 0 a 4.
# .upper(): Converte esses 5 caracteres para maiúsculas. Isso garante que a comparação não seja sensível a maiúsculas ou minúsculas.





