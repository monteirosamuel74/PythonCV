n = tabuada = cont = 0
while True:
    n = int(input('Digite um número: '))
    if n <= -1:
        break
    while tabuada < 10:
        tabuada += 1
        print(f'{n} x {tabuada} = {n * tabuada}')
    cont += 1
    tabuada = 0
print(f'Fim.')
