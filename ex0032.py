ano=int(input('Em que ano você está? '))
if (ano%4==0 and not ano%100==0) or ano%400==0:
    print('O ano é bissexto')
else:
    print('O ano não é bissexto')
