sexo=str(input('Informe o sexo (M/F): ')).upper()
if sexo == 'M' or sexo == 'F':
    print('Dados computados. Aguarde...')
else:
    while sexo != 'M' or sexo != 'F':
        sexo = input('Dado incorreto. Digite novamente (M/F): ').upper()
        if sexo == 'M' or sexo == 'F':
            print('Dado computado corretamente.')
            break
if sexo == 'M':
    print('Sexo masculino.')
elif sexo == 'F':
    print('Sexo feminino.')
    