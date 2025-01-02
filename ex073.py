# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro
# na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.
from operator import index

times = ('Santos', 'Mirassol', 'Sport', 'Ceará', 'Novorizontino', 'Goiás', 'Operário',
         'América-MG', 'Vila nova', 'Avaí', 'Amazonas', 'Coritiba', 'Paysandu', 'BotafogoSP',
         'Chapecoense', 'CRB', 'Ponte Preta', 'Ituano', 'Brusque', 'Guarani')
print('Os 5 primeiros colocados são:')
print(times[0:5])
print()
print('Os  4 últimos colocados são:')
print(times[-4:])
print()
print('A ordem alfabética é:', sorted(times))
print()
print(f'O time da chapecoense está na {times.index("Chapecoense")}° Posição.')

















