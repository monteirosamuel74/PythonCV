from time import sleep
from random import randint
jogo=int(input('Quantos jogos da LOTOFACIL você deseja? '))
cont=0
aposta=[]
todosJogos=list()
while True:
    while len(aposta)<15:
        num=randint(1,25)
        if num not in aposta:
            aposta.append(num)
    aposta.sort()
    todosJogos.append(aposta[:])
    aposta.clear()
    cont+=1
    if cont == (jogo):
        break
for i, l in enumerate(todosJogos):
    print(f'Aposta {i+1}: {l}')
    sleep(1)
print('BOA SORTE!!')