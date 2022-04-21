from math import hypot
co = float(input('Comprimento do cateto oposto:'))
ca = float(input('comprimento do cateto adjacente '))
hi = hypot(co,ca)
print(f'\033[1;34;40m A hipotenusa vai medir {hi:.2f}')


