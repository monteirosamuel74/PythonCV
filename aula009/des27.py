nome = input('Digite seu nome completo: ').strip()
nome = nome.split()
print('Seu primeiro nome é {}'.format(nome[0]), '.')
print('E seu último nome é {}'.format(nome[len(nome)-1]), '.')
