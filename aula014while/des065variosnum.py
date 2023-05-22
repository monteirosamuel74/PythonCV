number=0
cont=0
pare=False
number=int(input('Insira um número: '))
confirmacao=''
soma=number
media=0
contmedia=1
maior=0
menor=0
while pare==False:
    confirmacao=str(input('Deseja inserir mais? (S/N): ')).upper()
    
    if confirmacao == 'S':
        number=int(input('Insira um número: '))
        soma+=number
        contmedia+=1
        if cont == 0:
            menor=number
            if number<menor:
                menor=number
            if number>maior:
                maior=number
    elif confirmacao!='N':
        print('Dados incorretos.')
    else:
        pare=True
    media=soma/contmedia
    cont+=1
print('Número de laços é {}.'.format(cont))
print('Qtde de vezes contadas para média é {}.'.format(contmedia))
print('A soma total é {}.'.format(soma))
print('A média é {}.'.format(media))
print('O maior é {}.'.format(maior))
print('O menor é {}.'.format(menor))