from random import randint
while True:
    jogador = int(input('Digíte um Número: '))
    computador = randint(1, 10)
    total= jogador+computador
    tipo=' '
    vitorias= 0
    while tipo not in 'IP':
        tipo=str(input('Impar ou Par [I/P]: ')).strip().upper()[0]
        if tipo == 'P':
            if total %2 ==0:
                print(f'Eu pensei em {computador} e você digitou {jogador} deu par ')
                print('Você venceu ')
                vitorias+=1
            else:
                print(f' Eu pensei em {computador} e você digitou {jogador} deu Impar')
                print('As maquinas Vencem !!! ')
        elif tipo == 'I':
            if total %2 ==0:
                print(f'Eu pensei em {computador} e você dígitou {jogador} deu par')
                print('As maquinas Vencem !!!')
            else:
                print(f'Eu pensei em {computador} e você dígitou {jogador} deu impar')
                print('Você ganhou PARABÉNS')
                vitorias+=1

    resp=str(input('Quer continuar [S/N}: ')).strip().upper()[0]
    if resp == 'N':
        break



print(f'Foi um bom  jogo,  você ganhou {vitorias} rodadas ')
