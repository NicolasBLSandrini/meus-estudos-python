nun_str=str(input('Digite um número de 0 a 9999: '))
nun_int=int(nun_str)
#nun=nun.zfill(4)
# print('Unidade: {}'.format(nun[3]))
# print('Dezena: {}'.format(nun[2]))
# print('Centena: {}'.format(nun[1]))
# print('Milhar: {}'.format(nun[0]))

unidade=nun_int % 10
dezena=(nun_int//10) % 10
centena=(nun_int//100) % 10
milhar=(nun_int//1000) % 10

print('Unidade: {}'.format(unidade))
print('Dezena: {}'.format(dezena))
print('Centena: {}'.format(centena))
print('Milhar: {}'.format(milhar))
