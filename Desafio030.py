n = int(input('Digite um número:'))
resultado = n % 2
if resultado == 0:
    print(f'\033[1;32;40m o número {n} é PAR \033[m' )
else:
    print(f'\033[1;31;40m O número {n} é ÍMPAR\033[m')