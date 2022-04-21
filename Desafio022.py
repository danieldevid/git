nome =str(input('Qual seu nome completo?:')).strip()
print(f'seu nome em maiúscula é {nome.upper()}')
print(f'Seu nome em minúscula é {nome.lower()}')
print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
print('seu primeiro nome tem {} letras'.format(nome.find(' ')))





