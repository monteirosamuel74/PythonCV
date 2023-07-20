from time import sleep


def contador(i,f,p):
    if p == 0:
        print('ERRO! Contagem impossível.')
    if p<0:
        p*= -1
    
    print(f'Contagem de {i} até {f} com razão {p}.')
    sleep(2.5)
   
    if i>0:
        cont=i
        while cont<=f:
            print(f'{cont} >> ', end='', flush=True)
            sleep(.5)
            cont+=p
        print('FIM!')
    else:
        cont=i
        while cont>=f:
            print(f'{cont} >> ', end='', flush=True)
            sleep(.5)
            cont-=p
        print('FIM!')
        


contador(1,10,1)
contador(10,0,2)

inicio=int(input('Informe o início: '))
fim=int(input('Informe o fim: '))
passo=int(input('Informe a razão: '))
contador(inicio,fim,passo)