print('Vença a máquina no Jokenpo!')
import random
jkp = random.randint(0, 2)
jkp = jkp + 1
num = int(input('Digite 1 para Pedra, 2 para Papel e 3 para Tesoura: '))
escolha = ''
maquina = ''
if num == 1:
    escolha = 'Pedra'
elif num == 2:
    escolha = 'Papel'
elif num == 3:
    escolha = 'Tesoura'
else:
    print('Opção inválida.')
if jkp == 1:
    maquina = 'Pedra'
elif jkp == 2:
    maquina = 'Papel'
elif jkp == 3:
    maquina = 'Tesoura'
print('Você escolheu {} e a máquina escolheu {}.'.format(escolha, maquina))
if num == jkp:
    print('EMPATOU!')
elif num == 1 and jkp == 3 or num == 2 and jkp == 1 or num == 3 and jkp == 2:
    print('Você venceu!!!')
else:
    print('Você perdeu.')
