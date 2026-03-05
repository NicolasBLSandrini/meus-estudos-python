peso=float(input('Digite seu peso em kg: '))
altura=float(input('Digite sua altura em metros: '))

imc=peso/(altura**2)

if imc<18.5:
    print(f'Você está abaixo do peso, seu IMC deu {imc:.2f}')

elif imc>=18.5 and imc<25:
    print(f'Você está no peso ideal, seu IMC deu {imc:.2f}')

elif imc>=25 and imc<30:
    print(f'Você está com sobrepeso, seu IMC deu {imc:.2f}')

elif imc>=30 and imc<40:
    print(f'Você está com obesidade, seu IMC deu {imc:.2f}')

else:
    print(f'Você está com obesidade morbida, seu IMC deu {imc:.2f}')
