lanche = ['x-burger', 'suco', 'pizza', 'pudim']
print(lanche)
lanche[3] = 'picolé'
lanche.append('cookie')
print(lanche)
lanche.insert(3, 'hotdog')
del lanche[4]  # lanche.pop(4) e lanche.remove('pizza') também serve para remover
if 'pudim' in lanche:
    lanche.remove('pudim')
print(lanche)
valores = list(range(4, 21, 3))
print(valores)
valores.sort()
print(valores)
valores.sort(reverse=True)
print(valores)
print(f'O vetor lanche possui {len(lanche)} elementos.')
print(f'O vetor valores possui {len(valores)} elementos.')

num = []
for cont in range(0, 5):
    num.append(int(input('Informe um valor: ')))
for c, n in enumerate(num):
    print(f'Na posição {c} está o número {n}.')
print('Fim da lista.')

a = [2, 3, 4, 5]
b = a[:]  # se não colocar os colchetes, a igualdade linkará a e b
b[2] = 8
print(f'O conteúdo de a = {a}')
print(f'O conteúdo de b = {b}')
