from random import randint

print(20 * '#')
print(3 * ' ', 'PAR OU ÍMPAR')
print(20 * '#')
playerChoice = player = cont = 0

while True:
    computer = randint(0, 9)

    playerChoice = str(input('Você escolhe PAR ou ÍMPAR? ')).upper().strip()
    player = int(input('Escolha um número: '))
    res = (player + computer)
    cont += 1
    if res % 2 == 0 and playerChoice == 'PAR' or res % 2 != 0 and playerChoice == 'IMPAR':
        print('Você venceu!', end='')
        print('DEU PAR!!' if res % 2 == 0 else 'DEU ÍMPAR!!!')
        print(f'Você escolheu {player} e a máquina {computer}, deu {res}.')
    else:
        print('Você perdeu!!', end='')
        print('DEU PAR!!' if res % 2 == 0 else 'DEU ÍMPAR!!!')
        print(f'Você escolheu {player} e a máquina {computer}, .')
        break

print(f'Você jogou {cont} vez ' if cont == 1 else f'Você jogou {cont} vezes ', 'e perdeu.')
