print('Conheça a tabuada do número desejado.')
num = int(input('Informe o número: '))
for c in range(1, 11):
    print('{} x {} = {}'.format(num, c, num * c))
