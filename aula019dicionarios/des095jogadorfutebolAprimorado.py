time = list()
jogador=dict()
partidas=list()

while True:
    jogador.clear()
    jogador['Nome']=str(input('Nome do jogador: '))
    totalPartidas=int(input(f'Quantas partidas o {jogador["Nome"]} jogou? '))
    for contador in range(1,totalPartidas+1):
        partidas.append(int(input(f'    Quantas gols na partida {contador}? ')))
    jogador['Gols']=partidas[:]
    jogador['Total de gols']=sum(partidas)
    time.append(jogador.copy())
    while True:
        confirm=str(input('Quer continuar? [S/N] '))
        if confirm in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if confirm=='N':
        break

print('-='*30)
print('cod  ', end='')
for índice in jogador.keys():
    print(f'{índice:<15}',end='')
print()
print('-='*30)

for chave, valor in enumerate(time):
    print(f'{chave:>2} ', end='')
    for dados in valor.values():
        print(f'{str(dados):<15}',end='')
    print()
print('-='*30)
while True:
    busca=int(input('Informe o cód do jogador para ver os dados: [negativo para encerrar] '))
    if busca<0:
        break
    if busca>= len(time):
        print(f'ERRO!! Não há cód {busca}.')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["Nome"]}: ')
        for indice, gols in enumerate(time[busca]['Gols']):
            print(f'    No jogo {indice+1} fez {gols} gols.')
    print('-'*30)
print('<<VOLTE SEMPRE>>')