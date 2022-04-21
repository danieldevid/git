vc = float(input('Qual o valor da casa?: R$ '))
sc = float(input('Qual o seu sálario?:'))
t = int(input('Em quanto tempo você pretende pagar?:'))
parcelas = (t * 12)
valorP = vc / parcelas
porcS = sc *30 /100
if  valorP <= porcS:
    print(f'\033[1;32;40m Você vai pode pagar {parcelas} parcelas mensais  no valor de R${valorP:.2f} \033[m')
else:
    print('\033[1;31;40m Infelizmente você não pode financiar essa casa \033[m ')


