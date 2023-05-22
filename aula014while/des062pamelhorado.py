a1 = int(input('Informe o primeiro número da PA: '))
razao = int(input('Informe a razão da PA: '))
listaPAW=[]
listaPAW.append(a1)
cont=0
limite=10
res=a1

print('Deseja incluir mais casas?')
confirmacao=str(input('(S/N): ')).upper()
while confirmacao=='S' or confirmacao!='N':
    if confirmacao=='S':
        casas=int(input('Mais quantas casas? '))
        limite+=casas
        print('Deseja incluir mais casas?')
        confirmacao=str(input('(S/N): ')).upper()
    elif confirmacao!='N':
        print('Dados incorretos.')
        confirmacao=str(input('(S/N): ')).upper()
    else:
        print('Segue a PA solicitada.')
while cont!=limite:
    cont+=1
    
    res=res+razao
    listaPAW.append(res)
print(listaPAW)
