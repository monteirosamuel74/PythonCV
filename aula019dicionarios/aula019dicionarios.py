pessoas={'nome':'samuel','sexo':'Masculino','idade':41}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos de idade.')
print()
print(pessoas.keys())
print()
print(pessoas.items())
print()
print(pessoas.values())
print()
for k, v in pessoas.items():
    print(f'{k} = {v}')
pessoas['nome']='Miguel' #Não precisa do append
pessoas['idade']=7
print()
print(pessoas)
print()
for k, v in pessoas.items():
    print(f'{k} = {v}')