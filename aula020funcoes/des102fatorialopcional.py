def fatorial(num=1, show=False):
    f=1
    for c in range(num,0,-1):
        f*=c
        if show==True:
            if c==1:
                print(f'{c} = ',end='')
            else:
                print(f'{c} x ', end='')
    return f
    


show=False
while True:
    ask=int(input('Deseja ver a solução? [1:Sim/0:Não] '))
    if ask == 1:
        show=True
        break
    else:
        print(f'Resposta é: ', end='')
        break
f1= 5

print(fatorial(f1,show))