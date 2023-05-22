#Jogo de adivinhação
import random
adv = random.randint(0, 5)
num = int(input('Digite um número de 0 a 5: '))
if num == adv:
    print('Você adivinhou!')
else:
    print('Você errou.')


