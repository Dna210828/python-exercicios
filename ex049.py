# Refaça o DESAFIO ex009 mostrando a tabuada de um número que o usuário escolher,
# só que agora utilizando um laço for.

while True:
    try:
        numero = int(input('Digite um numero para ver sua tabuada: '))
        break    # Sai do loop se a entrada for válida
    except ValueError:
        print('Digite um número válido')
for c in range(1,11):
    print(f'{numero} x {c} = {numero * c}')










