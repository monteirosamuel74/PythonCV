lista=[]
contdig=0
while True:
    lista.append(int(input('Informe um número: ')))
    contdig+=1
    continuar=str(input('Deseja continuar? [S/N] ')).upper().strip()
    if continuar=='N':
        print('Acabou.')
        break
print(lista)
print(f'Foram informados {contdig} números.')
lista.sort(reverse=True)
print(lista)
if 5 in lista:
    print('O número 5 foi digitado.')
else:
    print('O número 5 não foi digitado.')