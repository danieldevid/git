produto = float(input('Qual o valor do produto:'))
print(''' FORMAS DE PAGAMENTO 
[ 1 ] à vista dinheiro/Cheque 
[ 2 ] à vista no cartão 
[ 3 ] 2x no cartão 
[ 4 ] 3x ou  mais no cartão ''')
pagamento = int(input('Qual a opção?:'))
desconto10 = produto - (produto * 10 / 100)
desconto5 = produto - (produto * 5 / 100)
em2x = produto / 2
juros = (produto + (produto * 20 / 100))
if pagamento == 1:
    print(f'O valor do produto custa R${produto:.2f} se a forma de pagamento é à vista dinheiro/cheque o produto sai '
          f'por R${desconto10:.2f}')
elif pagamento == 2:
    print(f'O valor do produto custa R${produto:.2f} se a forma de pagamento é à vista no cartão o produto sai por R${desconto5:.2f}')
elif pagamento == 3:
    print(f'O valor do produto custa R${produto:.2f} se a forma de pagamento for em 2x no cartão o produto sai por '
          f'duas parcelas de R${em2x:.2f}')
elif pagamento == 4:
    totaparc = int(input('Quantas parcelas ?'))
    parcela = juros / totaparc
    print(f'Sua compra será parcelada em {totaparc}x com parcelas de {parcela:.2f} vai sair por {juros:.2f} ')
else:
    total = 0
    print(' OPÇÃO DE PAGAMENTO INVALIDA  ')



