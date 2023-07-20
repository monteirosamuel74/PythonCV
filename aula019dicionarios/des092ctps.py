from datetime import datetime
cadastro=dict()
cadastro['Nome']=str(input('Nome: '))
anoNasc=int(input('Ano de nascimento: '))
cadastro['CTPS']=int(input('Nº da CTPS: '))
cadastro['Idade']=datetime.now().year-anoNasc

if cadastro['CTPS']!=0:
    cadastro['Admissão']=datetime.now().year
    cadastro['Salário']=float(input('Salário: '))
    cadastro['Aposentadoria prevista']=(datetime.now().year)-anoNasc+35

print(cadastro)