# Melhore o ex061, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.

# Solicita o primeiro termo e a razão da PA
primeiro_termo = float(input('Digite o primeiro termo da PA: '))
razao = float(input('Digite a razão da PA: '))

# Inicializa o contador e o termo atual
contador = 0
termo_atual = primeiro_termo

# Loop principal para mostrar os termos da PA
while True:
    # Mostra os 10 primeiros termos
    for _ in range(10):
        print(f'Termo {contador + 1}: {termo_atual}')  # Exibe o termo atual
        termo_atual += razao  # Calcula o próximo termo
        contador += 1  # Incrementa o contador

    # Pergunta ao usuário se deseja mostrar mais termos
    mais_termos = int(input('Quantos termos você quer mostrar a mais? (Digite 0 para encerrar): '))

    if mais_termos == 0:
        break  # Encerra o loop se o usuário digitar 0

    # Atualiza o contador para mostrar mais termos
    for _ in range(mais_termos):
        print(f'Termo {contador + 1}: {termo_atual}')  # Exibe o termo atual
        termo_atual += razao  # Calcula o próximo termo
        contador += 1  # Incrementa o contador

print('Fim da PA.')
