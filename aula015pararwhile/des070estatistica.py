total = cont = totptous = minor = 0
cheap = ''
while True:
    product = str(input('Product name: '))
    price = float(input('Price: R$'))
    cont += 1
    total += price
    if price > 1000:
        totptous += 1
    if cont == 1 or price < minor:
        minor = price
        cheap = product
    res = ''
    while res not in 'SN':
        res = str(input('Deseja continuar? [S/N] '))
    if res == 'N':
        break
print(f'Total purchase amount: R${total}')
print(f'There is {totptous} over R$1.000,00.')
print(f"The cheapest product is {cheap} and it's cost R${minor:,2f}")
