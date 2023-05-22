print('Simulação de financiamento habitacional')
valorCasa = float(input('Qual o valor do imóvel a financiar? '))
renda = float(input('Qual é o valor da sua renda bruta?'))
tempo = int(input('Em quantos anos deseja financiar? (Mínimo são 15 anos e máximo 35.'))

valorCasa = valorCasa * 1.82
valorParcela = valorCasa / (tempo * 12)
limiteParcela = renda * .3

if tempo <= 15 or tempo > 35:
    print('Não é possível realizar financiamento no período indicado.')
    print('Reajuste o tempo e tente novamente.')
elif valorParcela <= limiteParcela:
    print('Parabéns! Seu financiamento foi aprovado.')
    print('Sua parcela ficou no valor de {} Reais/mês para financiamento em {} anos.'.format(valorParcela, tempo))
else:
    print('Não é possível realizar o financiamento.')
    print('O valor da sua parcela ultrapassa 30% da sua renda.')
print('O valor total do financiamento ficou R${}.'.format(valorCasa))
print('O valor da parcela ficou R${}.'.format(valorParcela))
print('O seu limite de parcela é R${}.'.format(limiteParcela))
