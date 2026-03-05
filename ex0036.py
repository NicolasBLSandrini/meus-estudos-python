# valor_casa=float(input('Qual o valor da casa ? '))
# salario=float(input('Qual é seu salario atual ? '))
# meses=int(input('Em quantas parcelas você pretende pagar ? '))
#
# limite=salario*0.3
# prestacao=valor_casa/meses
# porcentagem=(prestacao/salario)*100
#
# if prestacao>limite:
#     print('Infelizmente você não podera comprar o imovel. O valor da prestação vai ficar com {:.2f}% do seu sálario.'.format(porcentagem))
#
# else:
#     print('O valor da prestação vai ficar em {}. Sua compra foi autorizada. A prestação vai custar {}% do seu sálario'.format(prestacao, porcentagem))


valor_casa=float(input('Qual o valor do imovel ? '))
salario=float(input('Qual o seu salario atual ? '))
meses=int(input('Em quantos meses você pretende pagar ? '))

porcent=((valor_casa/meses)/salario)*100
valor_mes=valor_casa/meses

if porcent<30:
    print('A prestação do imovel foi aprovada, o valor vai ser {:.2f} por mês e vai custar {:.2f}% do seu sálario'.format(valor_mes,porcent))

else:
    print('A compra do imovel foi negada. O valor da prestação ficaria em {:.2f} e custaria {:.2f}% do seu sálario'.format(valor_mes,porcent))