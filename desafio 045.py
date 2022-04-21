from random import randint
from time import sleep
itens = ('PEDRA', 'PAPEL','TESOURA' )
computador = randint(0, 2)
print('''Suas opçôes:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Sua opção ?'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
print('\033[1;32;40m-=-\033[m'*11)
print('computador jogou {} '.format(itens[computador]))
print('JOgador jogou {} '.format(itens[jogador]))
print('--=--'*20)
if computador == 0:                                          # computador jogou pedra
    if jogador == 0:
        print(f'\033[1;33;40M NÓS EMPATAMOS \033[M ')
    elif jogador == 1:
        print(f'\033[1;32;40M JOGADOR VENCEU !!\033 ')
    elif jogador == 2:
        print(f'\033[1;31;40M COMPUTADOR VENCEU\033[M')
    else:
        print('JOGADA INVALIDA')
elif computador == 1:                                            # COMPUTADOR JOGOU TESOURA
    if jogador ==0:
        print('COMPUTADOR GANHA ')
    elif jogador == 1:
        print('NÓS EMPATAMOS')
    elif jogador == 2:
        print('\033[1;32;40m JOGADOR VENCE \033[m')
    else:
        print('OPÇÃO INVALIDA')
elif computador == 2:                                        # COMPUTADOR JOGOU TESOURA
    if jogador == 0:
        print('\033[1;32;40m JOGADOR GANHOU \033[m')
    elif jogador ==1:
        print('COMPUTADOR GANHOU ')
    elif jogador == 2:
        print('NÓS EMPATAMOS')
    else:
        print('OPÇÃO INVALIDA')




