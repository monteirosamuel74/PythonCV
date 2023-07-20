from time import sleep


def maior(* num):
    mais=cont=0
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(.3)
        if cont==0 or valor>mais:
            mais=valor
        
        cont+=1
    print(f'Foram informados {cont} valores.')
    print(f'O maior valor informado foi {mais}.')


maior(1,2,3,4,5,6,7,8,9,14)