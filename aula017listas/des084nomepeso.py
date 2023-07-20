pessoas=[]
leves=[]
pesadas=[]
cadastro=pesado=leve=0
while True:
    individuo=[]
    nome=str(input('Qual o seu nome? '))
    individuo.append(nome)
    seupeso=float(input('Qual o seu peso? '))
    individuo.append(seupeso)
    pessoas.append(individuo[:])
    cadastro+=1
    if seupeso>=50:
        pesado+=1
        pesadas.append(nome)
    else:
        leve+=1
        leves.append(nome)
    individuo.clear()
    cont=str(input('Deseja inserir mais uma pessoa? [S/N]')).upper()
    if cont=='N':
        print('Seguem as informações: ')
        break
    else:
        individuo.clear()
print(f'O total de pessoas cadastradas foi {cadastro}.')
print(f'A lista de pessoas com mais de 50kg: {pesadas}.')
print(f'A lista de pessoas com menos de 50kg: {leves}.')
print(pessoas)