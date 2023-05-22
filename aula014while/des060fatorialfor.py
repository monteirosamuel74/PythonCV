print('Encontre o Fatorial de um número.')
numero=int(input('Informe um número: '))
fatorial=numero
resultado=1
print('Calculando {}! '.format(numero))

for c in range(numero, 0,-1):
    print('{} '.format(fatorial), end='')
    print('x ' if fatorial >1 else '= ', end='')
    resultado*=fatorial
    fatorial-=1
print('{}'.format(resultado))
