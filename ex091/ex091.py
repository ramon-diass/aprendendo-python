from random import randint
from time import sleep
from operator import itemgetter

jogadores = {'jogador 1': randint(1, 6), 'jogador 2': randint(1, 6),
             'jogador 3': randint(1, 6), 'jogador 4': randint(1, 6)}
ranking = list()
print(f'{"Valores sorteados:":^30}')
for k, v in jogadores.items():
    sleep(1)
    print(f'O {k} tirou o número {v}.')
sleep(1)
print('==' * 18)
print(f'{"Ranking dos jogadores:":^30}')
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1}° lugar: {v[0]} com o número {v[1]}')
    sleep(1)
