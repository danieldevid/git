s = float(input('\033[30m Qual salário do funcionário? R$'))
ns = s + (s * 15/100)
print(f'\033[31m Um funcionário que ganhava {s:.2f},\033[32m com 15% de aumento, passa a ganhar R${ns:.2f}')