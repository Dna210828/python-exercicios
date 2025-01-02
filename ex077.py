# Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS',
            'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')

for p in palavras:  # Itera sobre cada palavra na tupla
    print(f'\nNa palavra {p.upper()} temos ', end='')  # Exibe a palavra em maiúsculas
    for letra in p:  # Itera sobre cada letra da palavra
        if letra.lower() in 'aeiou':  # Verifica se a letra é uma vogal
            print(letra, end=' ')  # Se for vogal, imprime a letra













