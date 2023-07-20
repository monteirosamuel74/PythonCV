dados=[]
while True:
    aluno={'nome':'','média':0.0,'sit':''}
    aluno["nome"]=str(input('Nome: '))
    aluno['média']=float(input('Média: '))
    if aluno['média']<0 or aluno['média']>10:
        print('Média inválida (0 a 10). Dados apagados.')
        aluno['média']=float(input('Média: '))
    elif aluno['média']>=7:
        aluno['sit']="APROVADO"
    else:
        aluno['sit']="REPROVADO"
    dados.append(aluno.copy())
    aluno.clear()
    resp=str(input('Deseja inserir mais? [S/N] '))
    if 'N' in resp:
        break
for i in dados:
    print(i)
