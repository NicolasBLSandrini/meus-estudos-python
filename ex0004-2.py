n1=int(input('Digite um número: '))
n2=int(input('digite outro número: '))
s=n1+n2
sub=n1-n2
m=n1*n2
div=n1/n2
divi=n1//n2
sdiv=n1%n2
p=n1**n2
print('A soma do número é {} e a subtração é {} \n A multiplicação é igual a {} e a divisão é igual a {:.3f} \n A divisão inteira é igual a {} e a sobra da divisão é igual a {} \n E a potência é igual a {:.3f}'.format(s, sub, m, div, divi, sdiv, p))