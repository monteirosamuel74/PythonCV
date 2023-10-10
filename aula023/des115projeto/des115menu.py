from time import sleep
from lib.arquivo import *
from lib.interface import *

arq='cadastro.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta=menu(['Consulta cadastro','Add cadastro','Exit'])
    if resposta==1:
        lerArquivo(arq)
    elif resposta==2:
        cabeçalho('NOVO CADASTRO:')
        nome = str(input('Nome: '))
        idade=leiaInt('Idade: ')
        cadastrar(arq,nome,idade)
    elif resposta==3:
        cabeçalho('Exiting...')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida...\033[m')
    sleep(1.5)