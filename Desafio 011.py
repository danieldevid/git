larg = float(input('\033[1;32;40m Largura da parede \033[m :'))
alt = float(input('\033[1;31;40m Altura da parede \033[m:'))
área = larg * alt
tinta = área / 2
print(f'\033[1;35;40mA sua parede tem {área} m² será nescessario {tinta} L de tinta para pinta-lá \033[m')
