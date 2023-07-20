todos=[[],[]]
for i in range(0,7):
    num=int(input(f'Digite o {i+1} número: '))
    if num%2==0:
        todos[0].append(num)
    else:
        todos[1].append(num)
todos[0].sort()
todos[1].sort()
print(f'PARES: {todos[0]}')
print(f'ÍMPARES: {todos[1]}')