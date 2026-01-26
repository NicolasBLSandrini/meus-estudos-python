km=int(input('A  quantos km você passou? '))
if km>80:
    print('Você foi multado')
    print('A multa vai custar R$ {:.2f}'.format((km-80)*7))
print('Bom dia.')