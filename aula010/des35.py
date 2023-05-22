lado1 = float(input('Informe a medida de um lado do triângulo: '))
lado2 = float(input('Informe a medida de outro lado do triângulo: '))
lado3 = float(input('Informe a medida do último lado do triângulo: '))

if (lado2-lado3)<lado1 and lado1<(lado2+lado3) and (lado1-lado3)<lado2 and lado2<(lado1+lado3) and (lado1-lado2)<lado3 and lado3<(lado2+lado1):
    print('Essas medidas FORMAM um triângulo.')
else:
    print('Essas medidas NÃO FORMAM um triângulo.')

