print('-=-'*20)
num =int(input('Primeiro termo: '))
razão=int(input('A razão: '))
termo = num
cont= 1
while cont <= 10:
    print(f'{termo} >',end='')
    termo+= razão
    cont+= 1
print('FIM')
