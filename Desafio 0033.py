a = int(input('\033[4;31m Primeiro número:'))
b = int(input('\033[4;32m Segundo número:'))
c = int(input('\033[4;33m Terceiro número:'))
# Verificando quem é menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
maior = a
if b > a and b > c:
    maior = b
if c > b and c > a:
    maior = c
print('\033[7;35m O menor valor digitado foi {}'.format(menor))
print('\033[7;36m O maior valor digitado foi {}'.format(maior))


