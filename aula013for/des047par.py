print('Saiba quais são os números pares entre o intervalo desejado.')
inicio = int(input('Informe o início do intervalo: '))
fim = int(input('Informe o fim do intervalo: '))
pares = []
impares = []
for c in range(inicio, fim):
    if (c % 2) == 0:
        pares.append(c)
    else:
        impares.append(c)
print('Os números pares são: {}.'.format(pares))
print('E os ímpares são: {}.'.format(impares))
