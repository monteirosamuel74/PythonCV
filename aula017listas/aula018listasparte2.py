pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32]]
print(pessoas[0][0])
print(pessoas[1][1])
print(pessoas[2][0])
print(pessoas[1])

galera = [['Miguel', 7], ['Davi', 9], ['Marco', 39], ['Rosangela', 67]]
for indiv in galera:
    print(f'{indiv[0]} tem {indiv[1]} anos de idade.')
galera.clear()
dado = list()
totmai = totmen = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append((int(input('Idade: '))))
    galera.append(dado[:])#O formato em cópia para não entrar no princípio de igualdade
    dado.clear()

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores de idade.')
