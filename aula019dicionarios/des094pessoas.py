pessoa=dict()
cadastro=[]
soma=media=mulher=0
while True:
    pessoa.clear()
    pessoa["Nome"]=str(input('Nome: '))
    while True:
        pessoa["Sexo"]=str(input('Sexo[M/F]: ')).upper()[0]
        if pessoa['Sexo'] in 'MF':
            break
        print('ERRO! Informe apenas M ou F.')
    pessoa["Idade"]=int(input("Idade: "))
    soma+=pessoa['Idade']
    cadastro.append(pessoa.copy())
    cont=str(input('Deseja continuar?[S/N]: ')).upper()
    if cont == 'N':
        print('COMPUTANDO...')
        break

print(cadastro)
print('-='*30)
print(f'Foram cadastradas {len(cadastro)} pessoas.')
media = soma/len(cadastro)
print(f'A média de idades é {media}.')

for pos in cadastro:
    if pos['Sexo'] in 'Ff':
        mulher+=1
print(f'Foram cadastradas {mulher} mulheres.')
print('Elas são ', end='')
for p in cadastro:
    if p['Sexo'] in 'Ff':
        print(f'{p["Nome"]}, ', end='')
for p in cadastro:
    if p['Idade']>=media:
        print(' ', end='')
        for k,v in p.items():
            print(f'    {k} tem {v} anos de idade.')
