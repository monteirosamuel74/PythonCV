lista=[]
par=[]
impar=[]
while True:
    numero=int(input('Informe um número: '))
    lista.append(numero)
    
    continuar=str(input('Deseja continuar? [S/N] ')).upper().strip()
    if continuar=='N':
        print('Acabou.')
        break
    if numero%2==0:
        par.append(numero)
    else:
        impar.append(numero)
print(lista)
print(par)
print(impar)
