peso = float(input('Qual é o seu peso?:'))
altura = float(input('Qual é sua altura?:'))
imc = peso / (altura * altura)
if imc < 18.5:
    print(f'Seu imc é {imc:.1f} e você está abaixo do peso! ')
elif 18.5 <= imc < 25:
    print(f'O seu imc é {imc:.1f} e você esta no peso ideal! ')
elif 25 <= imc < 30:
    print(f'O seu imc é {imc:.1f} e você esta SOBREPESO ! ')
elif 30 <= imc < 40:
    print(f'O seu imc é {imc:.1f} e você esta OBESO !')
elif imc >= 40:
    print(f'O seu imc é {imc:.1f} e você está em estado de Obesdidade Mórbida')
