def leiaInt(msg):
    ok=False
    valor=0
    while True:
        numero=str(input(msg))
        if numero.isnumeric():
            valor=int(numero)
            ok=True
        else:
            print('\033[0;31mERRO! Digite um número válido\033[m')
        if ok:
            break
    return valor


numero=leiaInt('Digite um número: ')
print(f'Você digitou o número {numero}.')