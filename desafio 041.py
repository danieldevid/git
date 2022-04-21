from datetime import date
nasc = int(input('Em que ano você nasceu?: '))
atual = date.today().year
idade = atual - nasc
if idade <= 9:
    print(f'Como sua idade é {idade} anos você está na categoria MIRIM ')
elif idade <= 14:
    print(f'Como sua idade é {idade} anos sua categoria é INFANTIL')
elif idade <= 19:
    print(f'Como sua idade é {idade} anos sua catedoria é JUNIOR')
elif idade <= 20:
    print(f'Como sua idade é {idade} anos sua categoria é SÊNIOR')
elif idade > 20:
    print(f'Como sua idade é {idade} anos sua categoria é MASTER ')
