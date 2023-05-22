cLegalAge = cMale = cWMinor20 = 0
while True:
    age = int(input('Qual a sua idade? '))
    gender = str(input('Qual o seu sexo? [M/F] ')).upper().strip()
    while gender not in 'MF':
        gender = str(input('Qual o seu sexo? [M/F] ')).upper().strip()
    if age >= 18:
        cLegalAge += 1
    if gender == 'M':
        cMale += 1
    if age <= 20 and gender == 'F':
        cWMinor20 += 1
    continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()
    if continuar == 'N':
        break
print(f'Foram informados {cLegalAge} maiores de idade.')
print(f'Foram informados {cMale} homens.')
print(f'Foram informados {cWMinor20} mulheres menores de 20 anos.')
