km=int(input('Quantos km tem sua viagem? '))
# km200=0.50
# kmmais=0.45
if km<200:
    print('Sua viagem vai custar 0,50 reais por km, e no total vai ficar {:.2f}'.format(km*0.5))
else:
    print('Sua viagem vai custar 0,45 reais por km, e no total vai ficar {:.2f}'.format(km*0.45))
print('Tenha uma boa viagem')