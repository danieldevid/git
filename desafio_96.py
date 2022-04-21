while True:
    def area(largura,comprimento):
        a = largura*comprimento
        print(f'A area de um terreno de {largura:.1f} por {comprimento:.1f} é de {a:.1f}')

    print('+=+'*20)
    print('Controle de Terrenos ')
    comprimento =float(input('COMPRIMENTO(m):  '))
    largura =float(input('LARGURA (m):  '))
    area(largura,comprimento)
    sair=str(input('terminar o programa[S/N]')).upper().strip()[0]

    if sair =='S':
        print('Finalizando o Programa')
        break


