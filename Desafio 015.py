km = float(input('\033[1;32;40m Quantos Km foram percorridos?:'))
dias = int(input('\033[1;31;40m Quantos dias foram alugados?:'))
p = (60 * dias)+( km * 0.15)
print(f'\033[1;35;40m O total a pagar é de R${p:.2f}\033[m')

