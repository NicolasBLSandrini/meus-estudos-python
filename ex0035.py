r1=int(input('Digite o tamanho da primeira reta: '))
r2=int(input('Digite o tamanho da segunda reta: '))
r3=int(input('Digite o valor da terceira reta: '))
if r1+r2>r3 and r1+r3>r2 and r2+r3>r1:
    print('Pode formar um triangulo.')
else:
    print('Não pode formar um triangulo.')
