from random import randint
cont= 0
while True:
    print('-=-' *20)
    print('VAMOS JOGAR PAR OU IMPAR')
    jogador= int(input('Digite um valor : '))
    computador = randint(0, 10)
    soma =jogador +computador
    tipo =' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar [P/I]: ')).strip().upper()[0]
    print(f'Você jogou {jogador} e eu joguei {computador} . Total de {soma}')
    if tipo == 'P':
        if soma % 2 == 0:
            print(f'Deu PAR você VENCEU')
            cont += 1
        else:
            print('Deu Impar')
            print('Você Perdeu')
            break
    elif tipo == 'I':
        if soma % 2 == 1:
            print('Deu IMPAR você VENCEUU')
            cont += 1
        else:
            print('Deu Par')
            print('Você PERDEU')
            break
    print('Vamos jogar novamente')
print(f'GAME OVER ! Você venceu {cont} vezes')
print('*'*40)

