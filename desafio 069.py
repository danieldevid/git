tot18 = toth = tot20 = 0
while True:
    idade = int(input('Idade: '))
    sexo =' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [F/M]')).strip().upper()[0]
    if idade>= 18:
        tot18 += 1
    if sexo =='M':
        toth += 1
    if sexo == 'F':
        if idade <20:
            tot20 += 1
    resp =' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {toth} de homens cadastrados')
print(f'e temos {tot20} mulheres com menos de 20 anos')
