# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar
# ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

'''from datetime import date
ano_atual = date.today().year
nascimento = int(input('Ano de nascimento: '))
idade = ano_atual - nascimento
maioridade = nascimento + 18
if nascimento > ano_atual:
    print(f'Data Inválida. o ano atual é {ano_atual}.')
elif nascimento < 0:
    print('Data de nascimento invalida.')
elif idade == 18:
    print(f'Quem nasceu em {nascimento}, tem {idade} anos em {ano_atual}.')
    print('Voce deve se alistar IMEDIATAMENTE. ')
elif 0 < idade > 18:
    saldo = idade - 18
    print(f'Quem nasceu em {nascimento}, tem {idade} anos em {ano_atual}')
    print(f'Voce passou do prazo do alistamento militar. que foi em {maioridade}, á {saldo} anos atrás.')
elif 0 < idade < 18:
    saldo = 18 - idade
    print(f'Quem nasceu em {nascimento}, tem {idade} anos em {ano_atual}. ')
    print(f'Vocè poderá se alistar daqui a {saldo} anos. no ano de {maioridade}')'''

# mesmo código com alguns ajustes


from datetime import date

# Obter o ano atual
ano_atual = date.today().year

# Loop para garantir que o usuário insira um ano de nascimento válido
while True: # O while True cria um loop infinito.
    # Isso significa que o código dentro desse loop continuará a ser executado indefinidamente
    # até que uma condição de parada seja alcançada. Neste caso, a condição de parada é o comando break.

    try: # é uma estrutura de controle de fluxo em Python que permite que você teste um bloco
        # de código para possíveis exceções (erros em tempo de execução).
        # Se uma exceção ocorrer dentro do bloco try,
        # o controle é transferido para o bloco except correspondente,
        # onde você pode lidar com o erro de maneira apropriada.
        # Isso é fundamental para criar programas robustos que não falham inesperadamente
        # devido a erros previsíveis.
        nascimento = int(input('Ano de nascimento: '))

        # Verificação de ano de nascimento
        if nascimento > ano_atual:
            print(f'Data Inválida. O ano atual é {ano_atual}.')
        elif nascimento < 0:
            print('Data de nascimento inválida.')
        else:
            break  # Saia do loop se o ano de nascimento for válido.
            # O comando break é utilizado para sair do loop.
            # Se o código dentro do bloco try for executado sem erros, o break será alcançado
            # e o loop while será interrompido,
            # passando o controle para o código que vem após o loop.

    except ValueError: # O bloco except é utilizado para capturar e tratar exceções
        # que podem ocorrer no bloco try.
        # Neste caso, ele está especificamente preparado para capturar uma ValueError,
        # que é uma exceção que ocorre quando uma operação ou função recebe um argumento
        # com o tipo correto, mas um valor inapropriado,
        # como tentar converter uma string não numérica em um inteiro.
        print('Por favor, insira um número válido.')

# Cálculo da idade e do ano de alistamento
idade = ano_atual - nascimento
maioridade = nascimento + 18

if idade == 18:
    print(f'Quem nasceu em {nascimento}, tem {idade} anos em {ano_atual}.')
    print('Você deve se alistar IMEDIATAMENTE.')
elif idade > 18:
    saldo = idade - 18
    print(f'Quem nasceu em {nascimento}, tem {idade} anos em {ano_atual}.')
    print(f'Você passou do prazo do alistamento militar, que foi em {maioridade}, há {saldo} anos.')
elif 0 < idade < 18:
    saldo = 18 - idade
    print(f'Quem nasceu em {nascimento}, tem {idade} anos em {ano_atual}.')
    print(f'Você poderá se alistar daqui a {saldo} anos, no ano de {maioridade}.')












