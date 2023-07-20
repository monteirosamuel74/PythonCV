def texto(msg):
    tam=(len(msg)+4)
    print('-='*tam)
    print(f'    {msg}')
    print('-='*tam)


msg=str(input('Escreva sua mensagem: '))
texto(msg)