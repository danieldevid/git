somaidade = 0
mediaidade = 0
maioridadehomen= 0
nomevelho = ''
totmulher20 = 0
for p in range(1,5):
    print(f'--- {p} Pessoa---')
    nome = str(input('Nome:')).strip()
    idade = int(input('Idade:'))
    sexo = str(input('Sexo[M/F]:')).strip()
    somaidade += idade
    if p== 1 and sexo in 'Mn':
        maioridadehomen =idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomen:
        maioridadehomen = idade
        nomevelho = nome
    if sexo in 'fF' and idade <20:
        totmulher20 += 1
mediaidade= somaidade /4
print(f'A media de idade é {mediaidade}')
print(f'O homem mais velho tem {maioridadehomen}anos e se chama {nomevelho}')
print(f'Ao todo são {totmulher20} mulheres com menos de 20 anos ')