# from random import randint
#
# lista=('Pedra', 'Papel', 'Tesoura')
# acertou=False
# while not acertou==True:
#     cpu=randint(lista)
#     player = input('Escolha: Pedra, Papel e Tesoura').strip().lower()
#     if player==cpu:
#         print('Deu empate')
#
#
#     elif player=='pedra' and cpu=='papel':
#
from operator import truediv
from random import choice

opcoes=('pedra','papel','tesoura')

ganha_de={'tesoura':'papel',
          'pedra':'tesoura',
          'papel':'pedra'}

acertou=False
placar=0

while not acertou:
    cpu=choice(opcoes)
    player=input('Pedra, papel ou tesoura ? ').lower().strip()

    if player not in opcoes:
        print('Resposta invalida')
        continue

    if player==cpu:
        placar=placar+1
        print('Empate')

    elif ganha_de[player]==cpu:
        placar=placar+1
        print('Você ganhou, parábens')
        print(f'Você tentou {placar} vezes')
        acertou=True

    else:
        placar=placar+1
        print('Não foi dessa vez.. Tente de novo')
        print(f'Você está na tentativa {placar}')



