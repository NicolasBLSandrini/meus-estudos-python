comprimento=float(input('Digite o comprimento da parede: '))
largura=float(input('Digite a largura da parede: '))
area=(comprimento*largura)
tinta1l=2
print('A área é de {:.2f}, e é necessario {:.2f} litros de tinta para pintá-la completamente.'.format(area,area/tinta1l))
