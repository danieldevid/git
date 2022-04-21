nom = str(input('Digite uma frase:')).strip().upper()
print('A letra A aparece {} vezes na frase'.format(nom.count('A')))
print('A primeira letra A apareceu na posição {} '.format(nom.find('A')+1))
print('A última letra A apareceu na posição {}'.format(nom.rfind('A')+1))

