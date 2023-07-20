def contador(i,f,p):
    """
    -> Faz uma contagem e mostra na tela:
    *i
    *f
    *p
    """
    c=i
    while c<=f:
        print(f'{c}',end='..')
        c+=p
    print('FIM!!')


contador(2,10,2)

help(contador)