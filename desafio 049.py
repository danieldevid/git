n1 = int(input('\033[1;31;40m Digite um número para ver sua taboada!\033[m'))
for c in range(0, 11):
    print('\033[32m-'* 12)
    print(f'{n1} x {c:2} = {n1*c}')


