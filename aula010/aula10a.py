nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota1+nota2)/2
print('Sua nota final é {}.'.format(media))
print('Parabéns! APROVADO' if media >=7 else 'REPROVADO')
