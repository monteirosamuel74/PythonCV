num1 = int(input('Informe um valor inteiro de 0 a 10: '))
num2 = int(input('Informe outro valor inteiro de 0 a 10: '))
num3 = int(input('Informe o último valor inteiro de 0 a 10: '))

if num1 > num2 and num1 > num3:
    print('O maior valor é {}.'.format(num1))
else:
    if num2 > num1 and num2 > num3:
        print('O maior valor é {}.'.format(num2))
    else:
        print('O maior valor é {}.'.format(num3))

if num1 < num2 and num1 < num3:
    print('O menor valor é {}.'.format(num1))
else:
    if num2 < num1 and num2 < num3:
        print('O menor valor é {}.'.format(num2))
    else:
        print('O menor valor é {}.'.format(num3))

