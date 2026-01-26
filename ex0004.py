n1=int(input('Digite um numero: '))
n2=int(input('Digite outro numero: '))
s=n1+n2
su=n1-n2
d=n1/n2
m=n1*n2
so=n1%n2
di=n1//n2
e=n1**n2
print('A soma é igual a {0}, a subtração é igual a {1}'.format(s, su), end=' ')
print('A divisão é igual a {0} e a multiplicação é igual a {1}'.format(d, m), end=' ')
print('A sobra da divisão é igual a {0} e a divisão inteira é igual a {1}'.format(so, di), end=' ')
print('A potência é igual a {}'.format(e))
