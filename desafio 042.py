s1 = float(input('Primeiro seguimento:'))
s2 = float(input('Segundo seguimento:'))
s3 = float(input('Terceiro seguimento:'))
if s1 < s2 + s3 and s2 + s1 + s3 and s3 < s1 + s2:
    print('Os segmentos  acima PODEM FORMA um triângulos!', end='')
    if s1 == s2 == s3:
        print('EQUILÁTERO')
    if s1 != s2 != s3 != s1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('OS seguimentos acima NÂO PODEM FORMA triângulos ')
