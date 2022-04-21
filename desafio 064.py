num = soma= cont = 0
num = int(input('Digite um número [999 para parar: '))
while num != 999:
    cont+=1
    soma += num
    num = int(input('Digite um número [999 para parar: '))
print(f'Quantos numeros foram {cont} e a soma {soma}')


