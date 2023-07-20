from random import randint

tupla = (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
print('Os valores sorteados foram: ', end='')
for n in tupla:
    print(f'{n} ', end='')
print(f'\nO maior valor foi {max(tupla)}.')
print(f'O menor valor foi {min(tupla)}.')
