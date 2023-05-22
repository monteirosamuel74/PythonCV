from datetime import date

hoje = date.today().year
total = 0
for c in range(1, 8):
    ano = int(input(f'Informe o ano de nascimento da {c}ª pessoa: '))
    idade = hoje - ano
    if idade < 18:
        total += 1
print('O total de {} pessoas não atingiram a maioridade.'.format(total))
