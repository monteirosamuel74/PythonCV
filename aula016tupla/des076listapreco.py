tupla = ('Caneta', 1.50, 'Cerveja', 3.50, 'Pão', 1, 'Muçarela', 52.99)
print('=' * 40, f'\n{"LISTA DE PREÇOS":^40}\n', '=' * 40)
for pos in range(0, len(tupla)):
    if pos % 2 == 0:
        print(f'{tupla[pos]:.<30}', end='')
    else:
        print(f'R${tupla[pos]:>7.2f}')
