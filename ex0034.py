salario=float(input('Digite seu sálario: '))
if salario>1250:
    print('Seu salario terá reajuste de 10%, ficando {:.2f}'.format(salario*1.10))
else:
    print('Seu salario terá reajuste de 15%, ficando {:.2f}'.format(salario*1.15))
