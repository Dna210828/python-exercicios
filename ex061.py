# Refaça o ex051, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

# Solicita o primeiro termo e a razão da PA
primeiro_termo = float(input('Digite o primeiro termo da PA: '))
razao = float(input('Digite a razão da PA: '))

# Inicializa o contador e o termo atual
contador = 0
termo_atual = primeiro_termo

# Loop para calcular e mostrar os 10 primeiros termos
while contador < 10:
    print(f'Termo {contador + 1}: {termo_atual}')  # Exibe o termo atual
    termo_atual += razao  # Calcula o próximo termo
    contador += 1  # Incrementa o contador

print('Fim da PA.')
