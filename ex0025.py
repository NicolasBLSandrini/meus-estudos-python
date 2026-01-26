nome=str(input('Digite seu nome completo: '))
nome=nome.lower()
nome=nome.strip()
print('No seu nome tem "Silva"? {}'.format('silva' in nome))
