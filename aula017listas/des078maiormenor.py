lista=[]
c=0
for c in range(0,5):
    lista.append(int(input('Informe um número: ')))

print(f'O maior valor digitado é: {max(lista)} e está na posição ')
print(f'O menor valor digitado é: {min(lista)}')
print(f'Essa é a lista: {lista}')
