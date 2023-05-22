numero = 0
while True:
    numero = int(input('Digite um número de 0 a 20: '))
    if 0 <= numero <= 20:
        break
    print('Esse número não é válido. ', end='')
tupla = (
    'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis',
    'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
    'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
print(tupla[numero])
