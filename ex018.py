# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import sin, cos, tan, radians

angulo = int(input('Digite o ângulo que deseja: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print(f'O ângulo de {angulo:.1f} tem o seno de {seno:.2f}')
print(f'O ângulo de {angulo:.1f} tem o cosseno de {cosseno:.2f}')
print(f'O ângulo de {angulo:.1f} tem a tangente de {tangente:.2f}')

