jogador=dict()
partidas=list()
jogador['Nome']=str(input('Nome do jogador: '))
totalPartidas=int(input(f'Quantas partidas o {jogador["Nome"]} jogou? '))
for contador in range(1,totalPartidas+1):
    partidas.append(int(input(f'    Quantas gols na partida {contador}? ')))
jogador['Gols']=partidas[:]
jogador['Total de gols']=sum(partidas)
print(jogador)
print('-='*30)
print(f'O jogador {jogador["Nome"]} jogou {partidas} partidas.')
for indice,valor in enumerate(jogador['Gols']):
    print(f'    => Na partida {1+indice}, fez {valor} gols.')
print(f'Seu desempenho foi de {jogador["Total de gols"]} gols.')