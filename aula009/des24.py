# Analisar se a resposta começa com "Santo"
cidade = input('Em que cidade você nasceu? ').strip()
print(cidade[:5].upper() == 'SANTO')
