numero = int(input('Quantos termos você quer mostrar? '))
fibonacci = []
cont = 3
first = 0
second = 1
fibonacci.append(first)
fibonacci.append(second)
while cont <= numero:
    fibo = first + second
    fibonacci.append(fibo)
    first = second
    second = fibo
    cont += 1
if numero == 0:
    print('Não se aplica. Informe um número maior que 0.')
elif numero == 1:
    print(f'Sequência de Fibonacci com {numero} posição: [0]')
elif numero == 2:
    print(f'Sequência de Fibonacci com {numero} posições: [0, 1]')
else:
    print(f'Sequência de Fibonacci com {numero} posições: {fibonacci}')
