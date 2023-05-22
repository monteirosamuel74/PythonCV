maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input(f'Informe o peso da {c}ª pessoa: '))
    if peso < float(menor) or menor == 0:
        menor = peso
    if peso > float(maior):
        maior = peso
print('O maior peso registrado foi: {}kg.'.format(maior))
print('O menor peso registrado foi: {}kg.'.format(menor))
