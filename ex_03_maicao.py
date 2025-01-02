# 3. O custo ao consumidor de um carro novo é a soma do preço de fábrica
# com o percentual de lucro do distribuidor e dos impostos aplicados ao preço de fábrica.
# Faça um programa que receba o preço de fábrica de um veículo,
# o percentual de lucro do distribuidor e o percentual de impostos,
# calcule e mostre:

# a) o valor correspondente ao lucro do distribuidor;
# b) o valor correspondente aos impostos;
# c) o preço final do veículo.

# Entrada de dados
preco_fabrica = float(input("Digite o preço de fábrica do veículo: R$ "))
percentual_lucro = float(input("Digite o percentual de lucro do distribuidor (%): "))
percentual_impostos = float(input("Digite o percentual de impostos (%): "))

# Cálculo do lucro do distribuidor
lucro_distribuidor = preco_fabrica * (percentual_lucro / 100)

# Cálculo dos impostos
impostos = preco_fabrica * (percentual_impostos / 100)

# Cálculo do preço final do veículo
preco_final = preco_fabrica + lucro_distribuidor + impostos

# Exibição dos resultados
print(f"\nLucro do distribuidor: R$ {lucro_distribuidor:.2f}")
print(f"Valor dos impostos: R$ {impostos:.2f}")
print(f"Preço final do veículo: R$ {preco_final:.2f}")

