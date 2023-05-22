print('=-' * 15)
print('Descubra se o número é primo.')
print('=-' * 15)
divisores = []
num = int(input('Informe o número: '))
if num == 0:
    print('O número 0 não pode ser dividido.')
else:
    for c in range(1, num + 1):
        if num % c == 0:
            divisores.append(c)
if divisores.__len__() == 2:
    print('O número {} É PRIMO.'.format(num))
else:
    print('O número {} NÃO É PRIMO, '.format(num), end='')
    print('pois ele é divisível por: {}.'.format(divisores))
