from random import randint


def sorteia(lista):
    for cont in range(0,5):
        aleat=randint(0,100)
        lista.append(aleat)
        print(f'{aleat} >>',end='',flush=True)
    print('FIM!!')



def somaPar(lista):
    soma=0
    for valor in lista:
        if valor%2==0:
            soma+=valor
    print(f'Soma total dos pares é {soma}.')



números=list()
sorteia(números)
somaPar(números)