tupla = ("Estava", "a", "velha", "em", "seu", "lugar", "Veio", "a", "mosca", "lhe", "fazer",
         "mal", "A", "mosca", "na", "velha", "e", "a", "velha", "a", "fiar", "Estava", "a",
         "mosca", "em", "seu", "lugar", "Veio", "a", "aranha", "lhe", "fazer", "mal", "A",
         "aranha", "na", "mosca", "a", "mosca", "na", "velha", "E", "a", "velha", "a", "fiar")
for pos in tupla:
    print(f'\nA palavra {pos} possui ', end='')
    for letra in pos:
        if letra in 'AaEeIiOoUu':
         print(letra, end=' ')
