tupla = (int(input('Informe o primeiro número: ')),
         int(input('Informe o segundo número: ')),
         int(input('Informe o terceiro número: ')),
         int(input('Informe o quarto número: ')))
print(tupla)
print(tupla.count(9))
if 3 in tupla:
    print(f'Valor 3 apareceu na {tupla.index(3) + 1}ª posição.')
else:
    print('O valor 3 não foi digitado.')

for pos in tupla:
    if pos % 2 == 0:
        print(f'O número {pos} é PAR.')
    else:
        print(f'O número {pos} é IMPAR.')
