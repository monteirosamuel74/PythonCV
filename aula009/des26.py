# Analise
frase = input('Digite uma frase: ').upper().strip()
print('A' in frase)
print('Aparece a letra A {}'.format(frase.count('A')), 'vezes.')
print('A primeira letra A está no caracter {}'.format(frase.find('A')+1), '.')
print('A última letra A está no caracter {}'.format(frase.rfind('A')), '.')
