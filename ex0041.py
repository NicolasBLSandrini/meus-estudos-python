from datetime import date

nasce=int(input('Digite sua data de nascimento: '))
anoatual=date.today().year
idade=anoatual-nasce

print(idade)
if idade<=9:
    print('Você vai participar da categoria mirim')

elif idade<=14:
    print('Você vai participar da categoria infantil')

elif idade<=19:
    print('Você vai participar da categoria junior')

elif idade<=25:
    print('Você vai participar da categoria sênior')

else:
    print('Você vai participar da categoria master')
