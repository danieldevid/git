from math import sin, cos, tan, radians
angulo = float(input('Digite o ângulo:'))
seno = sin(radians(angulo))
print(f'\033[1;32;40m O ângulo de {angulo} seu SENO é {seno:.2f}')
cosseno = cos(radians(angulo))
print(f'\033[1;32;40m O ângulo de {angulo} seu COSSENO é {cosseno:.2f}')
tangente = tan(radians(angulo))
print(f'\033[1;32;40m O ângulo de {angulo} sua TAGENTE é {tangente:.2f}')


