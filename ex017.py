#  Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
#  Calcule e mostre o comprimento da hipotenusa.

from math import hypot
cateto_oposto = float(input('Digite o comprimento do cateto oposto: '))
cateto_adjacente = float(input('Digite o comprimento do cateto adjacente: '))
#hipotenusa = hypot(cateto_oposto, cateto_adjacente) # calculo do python
hipotenusa = (cateto_oposto ** 2 + cateto_adjacente ** 2) ** (1/2) # calculo matematico
print(f'O comprimento da Hipotenusa é {hipotenusa:.2f}')







