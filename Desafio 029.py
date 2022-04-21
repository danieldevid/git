v = float(input('Qual a velocidade atual do carro?km:'))
if v >= 80:
    m = (v - 80) * 7
    print('\033[4;31;40m MULTADO!Você excedeu o limite permitido que é de 80km/h \033[m')
    print(f'\033[32mVocê deve pagar uma multa de R${m}!\033[m')
print('\033[1;32;40m Tenha uma bom dia ! Dirija com segurança! ')
