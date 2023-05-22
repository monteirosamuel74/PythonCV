lado1 = float(input('Informe a medida de um lado do triângulo: '))
lado2 = float(input('Informe a medida de outro lado do triângulo: '))
lado3 = float(input('Informe a medida do último lado do triângulo: '))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print('Essas medidas FORMAM um triângulo.')
    if lado2 == lado1 and lado1 == lado3:
        print('Esse triângulo é EQUILÁTERO.')
    elif lado2 == lado1 and lado1 != lado3 or lado1 == lado3 and lado2 != lado1 or lado3 == lado2 and lado3 != lado1:
        print('Esse triângulo é ISÓSCELES.')
    elif lado2 != lado3 and lado1 != lado2 and lado1 != lado3:
        print('Esse triângulo é ESCALENO.')
else:
    print('Essas medidas NÃO FORMAM um triângulo.')
