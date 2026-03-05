r1=float(input('Digite o valor da primeira reta: '))
r2=float(input('Digite o valor da segunda reta: '))
r3=float(input('Digite o valor da terceira reta: '))

if r1+r2>r3 and r1+r3>r2 and r2+r3>r1:
    print('É um triangulo')
    if r1==r2==r3:
        print('Seu triangulo é equilátero, todos os lados são iguais')

    elif r1==r2 or r1==r3 or r2==r3:
        print('Seu triangulo é isósceles, apenas 2 lados são iguais')

    else:
        print('Seu triangulo é escaleno, todos os lados são diferentes')


else:
    print('Não da pra fazer um triangulo')