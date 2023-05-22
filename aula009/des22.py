nome = input('Digite seu nome completo: ')
#mostrar maiúsculo:
print('Seu nome em caixa alta: ', nome.upper())

#mostrar minúsculo:
print('Seu nome em caixa baixa: ', nome.lower())

#contar letras:
print('Seu nome inteiro tem o total de ', nome.__len__(), 'caracteres.')

#contar letras do primeiro nome:
contagem = nome.split()
print('Seu primeiro nome tem o total de ', contagem[0].__len__(), 'caracteres.')
