nome = ''
totalidade = 0
maisvelho = 0
mulher = 0
menos20 = 0
erro = False
for c in range(1, 5):
    nomepessoa = input('Informe o nome da {}ª pessoa: '.format(c))
    idade = int(input('Informe a idade da {}ª pessoa: '.format(c)))
    sexo = int(input('Digite 1 para Homem e 2 para Mulher: '))
    totalidade += idade
    if sexo > 2 or sexo < 1:
        print('Informe a opção correta. Apuração encerrada.')
        erro = True
        break
    elif idade > maisvelho and sexo == 1:
        maisvelho = idade
        nome = nomepessoa
    elif sexo == 2:
        mulher += 1
        if idade < 20:
            menos20 += 1
if erro == False:
    print('A média de idade do grupo é de {} anos.'.format(totalidade / 4))
    print('O homem mais velho é {}.'.format(nome))
    if menos20 > 0:
        print('E esse tem {} mulher(es) menor(es) de 20 anos.'.format(menos20))
    else:
        print('Esse grupo não tem mulher menor de 20 anos.')
