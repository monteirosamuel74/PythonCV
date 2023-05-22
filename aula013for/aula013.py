for c in range(0, 2):
    print('Hello, world!!')

for i in range(1, 8, -1):
    print(i)
s = 0
for contador in range(0, 8):
    n = int(input('Digite um valor: '))
    s += n
    print('A soma parcial é {}.'.format(s))

print('A soma total é {}.'.format(s))
