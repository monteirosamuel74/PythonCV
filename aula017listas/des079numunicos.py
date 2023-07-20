lista =[]
c=0
while True:
    n =int(input('Informe um número: '))
    
    if n not in lista:
        lista.append(n)
    c+=1
    if c==5:
        break
print(sorted(lista))
