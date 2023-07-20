from time import sleep
from operator import itemgetter
from random import randint
jogos={'jogador 1': randint(1,6),
       'jogador 2': randint(1,6),
       'jogador 3': randint(1,6),
       'jogador 4': randint(1,6)}
ranking=dict()
for jogador,lance in jogos.items():
    print(f'O jogador {jogador} tirou {lance}.')
    sleep(1.5)
ranking=sorted(jogos.items(), key=itemgetter(1), reverse=True) #itemgetter serve para ordenar pela chave
print('=-'*30)
print('RANKING')
for indice,valor in enumerate(ranking):
    print(f'    {indice+1}º lugar: {valor[0]} com {valor[1]}.')