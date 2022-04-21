n1 = float(input('A primeira nota: '))
n2 = float(input('A segunda nota '))
media = (n1 + n2) / 2
if media <= 5.0:
    print(f'\033[1;31;40m A sua média foi {media} você está REPROVADO!\033[m')
elif media >= 5.0  and media  < 7:
    print(f' \033[1;33;40m Como sua media foi {media} você está em RECUPERAÇÃO!\033[m')
elif media >=7.0:
    print(f'\033[1;32;40mMeus parabéns sua média foi {media} vocé está APROVADO!\033[m')