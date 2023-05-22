ano = int(input('Informe o ano para saber se é bissesto: '))
if ano % 400 == 0 and ano % 4 == 0 and ano % 100 != 0:
    print('O ano {} é bissesto.'.format(ano))
else:
    print('O ano {} não é bissesto.'.format(ano))
