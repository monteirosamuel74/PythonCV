from datetime import date


def voto(ano):
    
    atual=date.today().year
    idade=atual-ano
    if idade<=15:
        return f'Com {idade} o voto NÃO É OBRIGATÓRIO.'
    elif idade>=16 and idade<=17 or idade>65:
        return f'Com {idade} o voto É OPCIONAL.'
    elif idade>=18 and idade<=65:
        return f'Com {idade} o voto É OBRIGATÓRIO.'


ano=int(input("Em que ano você nasceu? "))
print(voto(ano))
