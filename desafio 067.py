c= 0
while True:
    n = int(input('Digite o numero que você quer ver a tabuada: '))
    if n <0:
        break
    for c in range(0, 11):
        print('\033[32m -' * 12)
        print(f' {n} x {c:2} = {n * c}')
print('Fim Do Programa De Tabuada')
