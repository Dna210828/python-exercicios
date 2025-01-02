# O Pedro comprou um saco de ração com peso em quilos.
# Ele possui dois cães, para os quais fornece a quantidade de ração em gramas.
# A quantidade diária de ração fornecida para cada cão é sempre a mesma.
# Faça um programa que receba o peso do saco de ração
# e a quantidade de ração fornecida para cada cão,
# calcule e mostre o quanto restará de ração no saco após cinco dias.


peso_saco = float(input("Digite o peso do saco de ração em quilos: "))
racao_por_cao = float(input("Digite a quantidade de ração fornecida para cada cão em gramas: "))

# Convertendo o peso do saco de quilos para gramas
peso_saco_gramas = peso_saco * 1000

# Calculando a quantidade total de ração fornecida em cinco dias
quantidade_total_racao = racao_por_cao * 2 * 5  # 2 cães e 5 dias

# Calculando a quantidade de ração que restará no saco
racao_restante = peso_saco_gramas - quantidade_total_racao

print(f"A quantidade de ração que restará no saco após cinco dias é: {racao_restante:.2f} gramas")



