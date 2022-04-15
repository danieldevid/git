import random
from time import sleep
tent=5
chanses=0

while True:
    
    
    num = random.randint(0, 5)
    print("\033[1;32m                      Jogo de Adivinhação \033[m")
    print('\033[1;32m-=-\033[m'*20)
    r = int(input('\033[1;32;40m Eu  pensei em um  número entre 0 e 5, digíte qual você acha que é ?:\033[m'))# Jogador tenta adivinhar
    print('\033[4;31;40m PROCESSANDO...\033[m')
    sleep(3)
    print('\033[1;32m -=-\033[m'*20)
    chanses+=1
    if r == num:
        print(f'\033[32m Você acertou o número  {num} com {chanses} chanse PARABÉNS !\033[m')
        break
        
    else:
        print(f'\033[31mVocê ERROU, o número era {num} ! ')
        tent-=1
        print(f'Agora você tem mais {tent} tentativas')
        
    if tent==0:
        print('Acabou sua tentativas ')
        break
