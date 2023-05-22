lanche = ('hamburguer', 'Suco', 'pizza', 'batata')

for comida in lanche:
    print(f'Eu vou comer {comida}.')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} da posição {cont}.')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} da posição {pos}.')

print('Comi demais!!!')
