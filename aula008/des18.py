from math import acos, asin, atan, radians
ang = float(input('Informe o ângulo: '))
print('O seno do ângulo é {}.'.format(asin(radians(ang))))
print('O cosseno do ângulo é {}.'.format(acos(radians(ang))))
print('A tangente do ângulo é {}.'.format(atan(radians(ang))))
