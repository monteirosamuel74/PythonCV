número = int(input('Digite um número entre 0 e 9999: '))
u=número//1%10
d=número//10%10
c=número//100%10
m=número//1000%10
print('Analisando o número: {}'.format(número))
print('Unidade: {}'.format(u))
print('Unidade: {}'.format(d))
print('Unidade: {}'.format(c))
print('Unidade: {}'.format(m))


