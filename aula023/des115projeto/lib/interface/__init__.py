def leiaInt(msg):
    while True:
        try:
            numero=int(input(msg))
        except (ValueError,TypeError):
            print('\033[0;31mERRO! Digite um número válido\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[0;31mSaiu do sistema.\033[m')
            return 0
        else:
            return numero


def linha(tam=42):
    return '-'*tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('Menu principal')
    c=1
    for item in lista:
        print(f'{c} - {item}')
        c+=1
    print(linha())
    opc=leiaInt('Sua opção: ')
    return opc


