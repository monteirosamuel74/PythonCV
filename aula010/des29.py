velocidade = float(input('Informe a velocidade do veículo(km/h): '))
if velocidade > 80:
    multa = (velocidade-80)*7
    print('Você ultrapassor o limite de velocidade.')
    print('Sua multa será de R${:.0f},00.'.format(multa))
else:
    print('Você está dentro do limite permitido. Siga com segurança!')
