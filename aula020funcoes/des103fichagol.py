def ficha(jogador='<desconhecido>',gol=0):
    print(f'O jogador {jogador} fez o total de {gol} gol(s) na partida.')


jogador=str(input('Qual o nome do jogador? '))
gol=str(input('Quantos gols ele fez na partida? '))
if gol.isnumeric():
    gol=int(gol)
else:
    gol=0

if jogador.strip()=='':
    ficha(gol=gol)
else:
    ficha(jogador,gol)
#print(ficha(jogador,gol))