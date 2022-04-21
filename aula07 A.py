n1 = int(input('\033[1;32m Um valor:'))
n2 = int(input('\033[1;33mOutro valor:\033[m'))
s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1**n2
print('\033[32mA soma é {}\033[m,\n \033[34mO produto é {}\033[m,\n \033[31m E a  divisão é {:.3f}\033[m '.format(s, m, d),end=' ')
print('\033[36m divisão inteira {}\033[m \n \033[35m E potÊncia {}'.format(di, e))
