nome=str(input('Digite seu nome completo: '))
nome=nome.lower()
print('No seu nome tem {} "a", o primeiro fica na {} posição e o último fica na {}'.format(nome.count('a'), nome.find('a')+1, nome.rfind('a')+1))