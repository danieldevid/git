from time import sleep
v1 = int(input('Digite um valor: '))
v2 = int(input('Digite outro valor: '))
opção = 0
while opção != 5:
    print('-=-'*20)
    print('''    [ 1 ]somar
    [ 2 ]multiplicar
    [ 3 ]maior
    [ 4 ]novos números 
    [ 5 ]sair do programa''')
    print('-=-'*20)
    opção = int(input('Qual sua opção?: '))
    if opção == 1:
        soma = v1 + v2
        print(f'A soma de {v1} e {v2} é {soma}')
    elif opção ==2:
        multiplicação = v1 * v2
        print(f'O resultado de {v1} x {v2} é {multiplicação}')
    elif opção == 3:
        if v1 > v2:
            valorg = v1
            print(f'O maior valor entre {v1} e {v2} é {valorg}')
        elif v1 == v2:
            print('Os valores são iguais ')
        else:
            valorp = v2
            print(f'O maior valor entre {v1} e {v2} é {valorp}')
    elif opção == 4:
        v1 = int(input('Digite valor: '))
        v2 = int(input('Digite outro valor: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção invalida ')
    print('-=-'*20)
    sleep(2)

print('Fim do programa , volte sempre !')
