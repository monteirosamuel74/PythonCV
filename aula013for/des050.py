s = 0
cont = 0
for c in range(1, 7):
    num = int(input('Informe um número: '))
    if num % 2 == 0:
        s += num
        cont += 1
if cont==1:
    print('Você informou apenas um número PAR e seu valor é {}.'.format(s))
elif cont>1:
    print('A informou {} números PARES e a soma deles é {}.'.format(cont, s))
else:
    print('Você não digitou número PAR.')