preco=float(input('Digite o preço do produto: '))
porcentagem=(preco*0.05)
preco_final=preco-porcentagem
print('O valor com 5% de desconto fica {:.2f}'.format(preco_final))