#Jogo de adivinhação melhorado
import random
adv = random.randint(0, 100)
num = -1
tentativa=0
print('Jogo da adivinhação. Tente adivinhar o número!!')
while num != adv:
    num=int(input('Digite um número de 0 a 100: '))
    tentativa+=1
    if num == adv:
        print('Você adivinhou!')
        print('A máquina também escolheu {}.'.format(adv))
        print('Você precisou de {} tentativa(s).'.format(tentativa))
    else:
        print('Você errou. Tente novamente.')


