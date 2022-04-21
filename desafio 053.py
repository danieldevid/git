frase = str(input('Qual a frase :')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
'''tem essa solução sem o for ^'''
'''for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]'''
print(f'O inverso de {junto} é {inverso} ')
if junto == inverso:
    print('ele é um palidromo')
else:
    print(' E por isso ele não é um palindromo')