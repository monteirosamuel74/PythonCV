print('=-' * 18)
print('Descubra se a frase é um Palíndromo.')
print('=-' * 18)
frase = input('Digite a frase desejada: ')
frase = frase.replace(' ', '')
print(frase)
if frase == frase[::-1]:
    print('Yes!')
else:
    print('No!!')
