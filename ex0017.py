from math import  hypot
cateto_oposto=float(input('Digite o cateto oposto: '))
cateto_adjacente=float(input('Digite o cateto adjacente: '))
hipo=hypot(cateto_oposto,cateto_adjacente)

print('A medida da hipotenusa é igual a {:.2f}'.format(hipo))
