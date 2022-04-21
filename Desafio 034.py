s = float(input('\033[1;32;40m Qual o sálario do funcionario ? R$:'))
if s <= 1250:
    novo = s + (s * 15 / 100)
else:
    novo = s + (s * 10 / 100)
print('\033[1;31;40m Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora. '.format(s, novo))
