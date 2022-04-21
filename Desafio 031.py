d = float(input('Qual a Distançia de sau viagem Km:'))
if d <= 200:
    print(f'\033[1;32mVocê esta preste a começar uma viagem de {d:.1f}Km \033[m')
    print('\033[1;32m Sua corida vai lhe custar R${:.2f}'.format(d*0.50))
else:
    print(f'\033[4;31m Você esta prestes a começar uma viagem de {d}Km \033[m')
    print(f'\033[4;31mSua viagem vai lhe custar R$ {d*0.45:.2f}\033[m')





