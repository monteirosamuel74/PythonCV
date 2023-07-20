listaNotas=[]
while True:
    dados=list()
    aluno=str(input('Nome do aluno: '))
    dados.append(aluno)
    nota1=float(input('Primeira nota: '))
    dados.append(nota1)
    nota2=float(input('Segunda nota: '))
    dados.append(nota2)
    media=(nota1+nota2)/2
    dados.append(media)
    listaNotas.append(dados[:])
    dados.clear()
    novo=str(input('Deseja inserir mais um aluno? [S/N] ')).upper().strip()
    if novo in 'Nn':
        break
for i,a in enumerate(listaNotas):
    print(f'[{i:<4}{a[0]:<10}{a[3]:>8.1f}]')
while True:
    opc=int(input('Deseja ver qual aluno? (999 para interromper): '))
    if opc==999:
        break
    if opc <= len(listaNotas)-1:
        print(f'Aluno {listaNotas[0]}: N1: {listaNotas[1]} // N2: {listaNotas[2]}')
