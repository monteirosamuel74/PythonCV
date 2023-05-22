num1=int(input('Digite o primeiro número: '))
num2=int(input('Digite o segundo número: '))
sair=False

while sair==False:
    
    print('[1] para somar')
    print('[2] para multiplicar')
    print('[3] para saber qual é o maior')
    print('[4] para informar novos números')
    print('[5] para sair')
    escolha=int(input('Escolha uma das opções acima:'))
    if escolha == 1:
        print('Resultado da soma é {}.'.format(num1+num2))
    elif escolha == 2:
        print('Resultado da multiplicação é {}.'.format(num1*num2))
    elif escolha == 3:
        if num2>num1:
            print('O número {} é o maior.'.format(num2))
        elif num1>num2:
            print('O número {} é o maior.'.format(num1))
    elif escolha==4:
        num1=int(input('Digite o primeiro número: '))
        num2=int(input('Digite o segundo número: '))
    elif escolha >5 or escolha<1:
        print('Escolha uma opção válida.')
    elif escolha==5:
        sair=True
        print('Encerrando.')
        break
