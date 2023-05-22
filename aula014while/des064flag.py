number=0
cont=0
soma=0
while number!=999:
    number=int(input('Insira um número: '))
    cont+=1
    if number!=999:
        soma+=number
    else:
        break
print(cont)
print(soma)
