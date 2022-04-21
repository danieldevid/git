p = float(input('\033[1;32;40mQual preço do produto? R$'))
pa = p - (p * 3/100)
pp = p + (p * 3/100)
print(f'\033[1;32;40m O preço inteiro do produto é de R${p:.2f}')
print(f'\033[1;32;40m o preço com pagamento a vista fica R${pa:.2f}')
print(f'\033[1;32;40m O preço com pagamento parcelado é de R${pp:.2f}')

