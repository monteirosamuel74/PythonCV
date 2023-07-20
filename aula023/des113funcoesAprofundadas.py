def leiaInt(msg):
    while True:
        try:
            n=int(input(msg))
        except (ValueError,TypeError):
            print(f'Se não digitar nada, não podemos seguir.')
            continue
        except UnboundLocalError:
            print(f'Não digitou nada. Vai levar 0.')
            return 0
        return n


def leiaFloat(dec):
    while True:
        try:
            d=int(input(dec))
        except(ValueError,TypeError):
            print(f'Se não digitar nada, não podemos seguir.')
            continue
        except UnboundLocalError:
            print(f'Não digitou nada. É 0.')
            return 0
        return d
    
    
numero=leiaInt('Digite um número: ')
dec=leiaFloat('Digite um número decimal: ')
print(f'Você digitou o número {numero} e {dec}.')