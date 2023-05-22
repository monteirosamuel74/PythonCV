num1 = int(input('Informe um valor inteiro: '))
num2 = int(input('Informe outro valor inteiro: '))

if num1 > num2:
    print('O maior valor é {}.'.format(num1))
elif num2 > num1:
    print('O maior valor é {}.'.format(num2))
else:
    print('Os números são iguais.')


