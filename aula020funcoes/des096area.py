def area(b,a):
    area=b*a
    print(f'A área em metros de {b}x{a} = {area}m².')


base=float(input('Informe o valor da base: '))
altura=float(input('Informe o valor da altura: '))
area(base,altura)
print('Resultado ',area(base,altura)) #precisa do return para apresentar a resposta assim
