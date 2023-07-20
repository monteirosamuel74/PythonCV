mat=[[0,0,0],[0,0,0],[0,0,0]]
for l in range(0,3):
    for c in range(0,3):
        mat[l][c]=int(input(f'Informe o número da casa [{l}/{c}]: '))
for l in range(0,3):
    for c in range(0,3):
        print(f'[{mat[l][c]:^5}]',end='')
    print()
