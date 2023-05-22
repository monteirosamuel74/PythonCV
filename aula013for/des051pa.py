a1 = int(input('Informe o primeiro número da PA: '))
razao = int(input('Informe a razão da PA: '))
decimo = a1+(10-1)*razao
listaPA = []
for c in range(a1, decimo+razao,razao):
    listaPA.append(a1)
    a1 = a1 + razao
    print('{} '.format(c), end='-> ')
print('FIM!')
print(listaPA)
