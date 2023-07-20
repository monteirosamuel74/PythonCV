def notas():
    base=dict()
    média=cont=maiorNota=menorNota=somaNota=aprovado=reprovado=0
    print('Digite [-1] para encerrar e ver o resultado da base.')
    while True:
        while True:
            notaAluno=float(input(f'Nota do aluno {cont+1}: '))
            if notaAluno>=0 and notaAluno<=10 or notaAluno==-1:
                break
            else:
                print('\033[0;31mERRO! Nota entre 0 e 10.\033[m')
                
        if notaAluno<7:
            reprovado+=1
        else:
            aprovado+=1
        cont+=1
        somaNota+=notaAluno
        if notaAluno>maiorNota or cont==1:
            maiorNota=notaAluno
        
        if notaAluno==-1:
            break
        elif notaAluno<menorNota or cont==1:
            menorNota=notaAluno

    média=somaNota/cont
    base["Qtde notas"]=cont-1
    base["Maior nota"]=maiorNota
    base["Menor nota"]=menorNota
    base["Média da turma"]=média
    base["Qtde aprovados"]=aprovado
    base["Qtde reprovados"]=reprovado-1
    return base


print(notas())