from datetime import date

# Obter o ano atual
ano_atual = date.today().year

# Loop para garantir que o usuário insira um ano de nascimento válido
while True:
    try:
        nascimento = int(input('Ano de nascimento: '))

        # Verificação de ano de nascimento
        if nascimento > ano_atual:
            print(f'Data Inválida. O ano atual é {ano_atual}.')
        elif nascimento < 0:
            print('Data de nascimento inválida.')
        else:
            break  # Saia do loop se o ano de nascimento for válido

    except ValueError:
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
