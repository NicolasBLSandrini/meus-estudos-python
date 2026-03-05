n1=float(input('Digite a primeria nota: '))
n2=float(input('Digite a segunda nota: '))

media=(n1+n2)/2

if media<5:
    print(f'Infelizmente, o aluno foi reprovado, a média foi de {media:.2f}')

elif media>=5 and media<=6.9:
    print(f'O aluno ta de recuperaão, sua média foi de {media:.2f}')

else:
    print(f'O aluno foi aprovado, sua média foi de {media:.2f}')
