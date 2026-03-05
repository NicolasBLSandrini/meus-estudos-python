valor=float(input('Digite o valor do produto: '))
cond=input('Digite a condição de pagamento:\nEX: Dinheiro, cheque, cartão parcelado (em quantas vezes), a vista, etc ')

if cond in ('cheque', 'dinheiro', 'pix'):
    desconto=valor*(10/100)
    print(f'Você vai receber 10% de desconto, ficando {desconto}$ de desconto, o valor total vai ficar {valor-desconto}')

elif cond in ('cartão', 'cartao'):
    desconto=valor*(5/100)
    print(f'Você vai receber 5% de desconto, ficando {desconto}$ de desconto, o valor total vai fica {valor-desconto}')

elif cond in ('pacelado em 2 vezes', '2 vezes', '2', 'parcelado em 2', 'pacelado em 2x'):
    print(f'Você não receber desconto, o preço normal de {valor}')

elif cond in ('parcelado em 3 vezes', '3 vezes', '3', 'parcelado em 3x'):
    juros=valor*(20/100)
    print(f'Você vai pagar 20% de juros, ficando {juros} de juros, o valor total vai ficar {valor+juros}')

else:
    juros=valor*(20/100)
    print(f'Você vai pagar 20% de juros, ficando {juros} de juros, o valor total vai ficar {valor+juros}')

