# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.


while True:
    numero = int(input('Digite um numero para ver sua tabuada: '))
    print('-'* 15)
    if numero < 0:
        break
    for c in range(1,11):
        print(f'{numero} x {c} = {numero * c}')
    print('-' * 15)
print('fim do programa')





