n = int(input('Dígite um número:'))
tot = 0
for c in range(1, n +1):
    if n % c ==0:
        print(f'\033[1;33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print(f'{c}', end=' ')
print(f' \n\033[m O nomero {n} foi divisivel {tot} vezes')
if tot == 2:
    print(f'E por isso ele é PRIMO! ')
else:
    print('E por isso ele NÃO É PRIMO')
