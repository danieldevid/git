resp = 'Ss'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    quant+=1
    soma+=num
    if quant==1:
        maior=menor=num
    else:
        if num> maior:
            maior =num
        if num <menor:
            menor =num

    resp =str(input('Você quer continuar [S/N]')).upper().strip()[0]
media=soma/quant
print(f'Você digitou {quant} números e a media é {media}')
print(f'E o maior valor é {maior} e o menor é {menor}')