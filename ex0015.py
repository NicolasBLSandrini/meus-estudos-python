km_rodado=float(input('Quantos km foram rodados? '))
dias=int(input('Quantos dias você ficou com o carro? '))
din_km=km_rodado*0.15
din_dias=dias*60
preco_a_pagar=din_km+din_dias
print('O valor a pagar do aluguel do carro é de {:.2f}'.format(preco_a_pagar))

