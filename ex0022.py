# nome=str(input('Digite seu nome completo: ')).strip()
# dividindo=nome.split()
# print(nome.upper())
# print(nome.lower())
# #nome=''.join(nome)
# print(len(''.join(dividindo)))
# print('Seu primeiro nome é {}, e tem {} letras'.format(dividindo[0],len(dividindo[0])))


#ou
nome=str(input('Digite seu nome completo: ')).strip()
print(nome.upper())
print(nome.lower())
print('Seu nome tem {} letras'.format(len(nome)-nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
