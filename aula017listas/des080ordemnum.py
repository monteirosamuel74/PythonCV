lista=[]
maior=menor=cont=0
while cont<5:
    cont+=1
    num=int(input('Digite um valor: '))
    
    if cont==1 or num>lista[-1]:
        print(f'O número {num} foi adicionado ao final da fila.')
        lista.append(num)
    else:
        pos =0
        while pos<len(lista):
            if num <= lista[pos]:
                lista.insert(pos,num)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos+=1
print(f'A lista na ordem inversa: {lista}')