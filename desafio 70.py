mil = valortot = menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do Produto: '))
    preço = float(input('Qual o preço :[R$] '))
    cont += 1
    valortot += preço
    if preço > 1000:
        mil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja Continuar [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'Total de gastos {valortot:.2f} R$ , e total de produtos de mais 1000 reais é {mil}')
print(f'O produto mais barato custou {menor:} e foi o {barato} ')
