from datetime import date

ano=int(input('Digite o seu ano de nascimento: '))
anoatual=date.today().year
idade=(anoatual-ano)
if idade<18:
    tempo=18-idade
    print('Você ainda não precisa se alistar no exército, falta {} anos ainda'.format(tempo))

elif idade==18:
    print('Você vai ter que se alistar esse ano')

elif idade>18:
    tempo=idade-18
    print('Você ja se alistou, se caso não tenha se alisatado ainda, ja se passaram {} anos'.format(tempo))
