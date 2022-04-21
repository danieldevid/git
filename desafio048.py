s = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        s += c
        cont += 1

print(f" A  a soma de todos o {cont} e a soma de todos os valores é {s}")
