n1=int(input('Digite um número: '))
n2=int(input('Digite outro número'))
n3=int(input('Digite o terceiro número'))
if n1>n2 and n1>n3:
    print('O número {} é o maior'.format(n1))
elif n2>n3 and n2>n1:
    print('O número {} é o maior'.format(n2))
else:
    print('O número {} é o maior'.format(n3))
