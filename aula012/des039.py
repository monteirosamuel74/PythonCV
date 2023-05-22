from datetime import date
atual = date.today().year
nasc = int(input('Informe seu ano de nascimento: '))
idade = atual-nasc
sexo = int(input('Digite 1 para Masculino e 2 para Feminino: '))
if sexo == 2:
    print('Você não precisa se alistar.')
elif sexo < 1 or sexo > 2:
    print('Opção inválida.')
elif idade ==18:
    print('Você está no ano de alistamento. Verifique se perdeu o prazo.')
elif idade > 18:
    print('Você perdeu o prazo para alistamento. Poderá ser penalizado.')
elif idade <18:
    print('Você ainda não está no ano de alistamento.')
