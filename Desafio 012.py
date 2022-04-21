p = float(input('Preço do produto? R$'))
d = int(input('Qual o valor do desconto?:'))
np = p - (p * d /100)
print(f'\033[1;31m O produto custava R${p:.2f} ,na promoção com {d} % de desconto vai custar R$ {np:.2f} ')
