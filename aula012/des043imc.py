print('Veja qual é seu IMC.\nInforme as suas medidas abaixo.')
h = float(input('Sua altura em m: '))
p = float(input('Seu peso em kg: '))
imc = p / (h * h)
print('Seu IMC é {:.2f} e está classificado como '.format(imc), end='')
if imc <= 0 or h <= 0 or p <= 0:
    print('Dados inválidos. Tente novamente.')
elif imc <= 18.5:
    print('ABAIXO DO PESO.')
elif imc <= 25:
    print('PESO IDEAL.')
elif imc <= 30:
    print('SOBREPESO.')
elif imc <= 40:
    print('OBESIDADE.')
else:
    print('OBESIDADE MÓRBIDA.')
