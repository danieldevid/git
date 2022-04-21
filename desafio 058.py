import random
computador = random.randint(0, 10)
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual o seu palpite: '))
    palpites +=1
    if jogador == computador:
        acertou = True
    else:
        if jogador <computador:
            print('Mais...')
        if jogador > computador:
            print('Menos...')
print(f'\033[1;32;40m Você acertou com {palpites} palpites\033[m ')