from random import randint



# nome=input('Boa tarde ! Qual é seu nome ? ')
#
# simounao=input('Que nome bonito {}, você quer jogar um jogo ? '.format(nome)).strip().lower()
#
# if simounao == 'sim':
#     tentativas=0
#     tentativasmax=0
#     print('Que legal, então vamos lá.. \nDificuldades:\nFacil: Você vai ter 3 tentativas para acertar um número de 0 a 3\nMedio: Você vai ter 5 tentativas para acertar um número de 0 a 6\nDificil: Você vai ter 8 tentativas para acertar um número de 0 a 9')
#     dificult=input('E então ? Qual vai ser ? ').lower().strip()
#
#     if dificult in ('facil', 'fácil'):
#         print('Vamos de fácil então..')
#         acertou=False
#         d1=randint(0,3)
#         tentativasmax=3
#
#         while not acertou and tentativas<tentativasmax:
#             n1 = int(input('Escolha seu número de 0 a 3, {} '.format(nome)))
#             if n1==d1:
#                 acertou=True
#                 print('Parabens! Você acertou na mosca, {}!'.format(nome))
#                 print('Você usou {} tentativas'.format(tentativas+1))
#
#             elif n1<0 or n1>3:
#                 print('Puts {}.. Parece que esse número não está entre 0 a 3..'.format(nome))
#
#             else:
#                 print('Parece que você errou, {}.. Mas você ainda tem {} tentativas'.format(nome,(tentativasmax-tentativas)))
#                 tentativas=tentativas+1
#
#     elif dificult in ('medio', 'média'):
#         print('Então vamos lá {}..'.format(nome))
#         acertou=False
#         d2=randint(0,6)
#         tentativasmax=5
#
#         while not acertou and tentativas<tentativasmax:
#             n2 = int(input('Escolha seu número de 0 a 6, {} '.format(nome)))
#             if n2==d2:
#                 acertou=True
#                 print('Parabens! Você acertou em cheio nessa {}!'.format(nome))
#                 print('E você so usou {} tentativas'.format(tentativas+1))
#
#             elif n2<0 or n2>6:
#                 print('Puts {}.. Parece que esse número não está entre 0 e 6'.format(nome))
#
#             else:
#                 print('Você errou {}, mas tudo bem.. Você ainda tem {} tentativas'.format(nome,(tentativasmax-tentativas)))
#                 tentativas=tentativas+1
#
#     elif dificult in ('dificil', 'díficil'):
#         print('Então vamos la, {}'.format(nome))
#         acertou=False
#         d3=randint(0,9)
#         tentativasmax=8
#
#         while not acertou and tentativas<tentativasmax:
#             n3 = int(input('Escolha seu número de 0 a 9, {} '.format(nome)))
#             if n3==d3:
#                 acertou=True
#                 print('Parábens {}! Você acertou no modo mais díficil, e so usou {} tentativas'.format(nome,(tentativas+1)))
#
#             elif n3<0 or n3>9:
#                 print('Puts {}.. Parece que esse número não está entre 0 e 9..'.format(nome))
#
#             else:
#                 print('Poxa.. Você errou, mas tudo bem, você ainda tem {} tentativas'.format(tentativasmax-tentativas))
#                 tentativas=tentativas+1
#
# else:
#     print('Poxa vida {}.. Tá bem então, tenha uma boa tarde!'.format(nome))
#
#


nome=input('Qual é o seu nome? ')
print('Prazer em te conhecer, {}!'.format(nome))
simounao=input('Você que jogar um jogo? ').lower().strip()
if simounao=='sim':
    print('O jogo é o seguinte, você vai ter que acertar um número')
    print('Dificuldades:\nFácil: Você vai ter 3 tentativas para acertar um número de 0 a 3\nMédio: Você vai ter 5 tentativas para acertar um número de 0 a 6\nDíficil: Você vai ter 7 tentativas para acertar um número de 0 a 9')
    dificult=input('E então ? Qual vai ser ? ').lower().strip()
    if dificult in ('facil', 'fácil'):
        acertou=False
        numeromax=3
        chance=3
        tentativa=0
        dificuldade_valida=True

    elif dificult in ('medio', 'médio'):
        acertou=False
        numeromax=6
        chance=5
        tentativa=0
        dificuldade_valida=True

    elif dificult in ('dificil', 'difícil'):
        acertou=False
        numeromax=9
        chance=7
        tentativa=0
        dificuldade_valida=True

    else:
        print('Resposta inválida')
        dificuldade_valida=False

    if dificuldade_valida==True:

        numale = randint(0, numeromax)
        while not acertou and dificuldade_valida and tentativa<chance:
            num = int(input('Qual vai ser seu número ? '))
            if num==numale:
                print('Párabens! Você acertou {}!'.format(nome))
                print('E usou só {} tentativas'.format(tentativa+1))
                acertou=True

            elif num<0 or num>numeromax:
                print('Número invalido, {}'.format(nome))

            else:
                tentativa=tentativa+1
                if chance==tentativa and acertou==False:
                    print('Você errou.. E suas chances acabaram..')
                else:
                    print('Você errou, mas ainda tem {} tentativas'.format(chance-tentativa))



        if acertou==False:
            print('Poxa.. Parece que não foi dessa vez, {}.. O número sorteado foi {}.. Até a proxíma!'.format(nome, numale))

    else:
        print('Poxa.. Parece que a dificuldade ta invalida, não vai dar para continuarmos..')





else:
    print('Poxa {}... Tudo bem então, boa tarde!'.format(nome))
