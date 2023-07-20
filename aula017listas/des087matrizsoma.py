mat=[[0,0,0],[0,0,0],[0,0,0]]
par=num=terceira=maior=0
for l in range(0,3):
    for c in range(0,3):
        num=int(input(f'Informe o número da casa [{l},{c}]: '))
        mat[l][c]=(num)
        if num%2==0:
            par+=num
        if c==2:
            terceira+=num
        if l==1 and maior<=num:
                maior=num
for l in range(0,3):
    for c in range(0,3):
        print(f'[{mat[l][c]:^5}]',end='')
    print()
print(f'A soma dos números pares é {par}.')
print(f'A soma dos números da 3ª coluna é {terceira}')
print(f'O maior valor da segunda linha é {maior}.')