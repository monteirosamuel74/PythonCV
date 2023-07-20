def contador():
    for c in range(1,11):
        print(f'{c} >> ', end='')
    print('-='*30)
    for d in range(10,0,-2):
        print(f'{d} >> ',end='')
    print('-='*30)
    inicio=fim=passo=0
    inicio=int(input('Informe o início: '))
    fim=int(input('Informe o fim: '))
    passo=int(input('Informe a razão: '))
    for e in range(inicio,fim,passo):
        print(f'{e} >> ',end='')


contador()