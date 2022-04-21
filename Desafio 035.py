a = float(input('Primeiro seguimento:'))
b = float(input('Segundo seguimento:'))
c = float(input('Terceiro seguimento'))
print('\033[4;31m-=-'*20)
print('\033[4;32m Analisador de triângulos \033[m ')
print('\033[4;31m-=-'*20)
if a+b > c and a+c > b:
    print('\033[4;32m Os seguimentos assima podem forma um triangulo')
else:
    print('\033[4;31m Os seguimentos acima NÃO podem forma um triângulo')


