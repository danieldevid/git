from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pes in range(1,8):
    nasc = int(input(f'Em que ano a {pes}ª pessoa nasceu ?:'))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print(f'Temos {totmaior} de maior e {totmenor} de menor')



