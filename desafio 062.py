print('-=-'*20)
num = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = num
cont = 1
total = 0
mais = 10
while mais != 0:
    total+=mais
    while cont <= total:
        print(f'{termo}',end='>')
        termo +=razão
        cont+= 1
    print('PAUSA')
    mais = int(input('Quantos mais termos você quer ver ? '))
print(f'Progressão finalizada com {total} termos')
