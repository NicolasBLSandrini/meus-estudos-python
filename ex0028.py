# import random
# num=int(input('Tente adivinhar um número de 1 a 5: '))
# ran=random.randint(1,5)
# if num<1 or num>5:
#     print('Número inválido')
# elif num==ran:
#     print('Párabens, você acertou')
# else:
#     print('Não foi dessa vez..')
# print('O número sorteado foi {}'.format(ran))



from random import randint
from time import sleep

print('\033[33m--__--__--'*20)
print('\033[36mVamos jogar um jogo, tente acertar o número certo.')
pronto=str(input('\033[31mVocê está pronto? ')).strip().lower()
if pronto=='sim':
    tentativamax=0
    print('\033[m___'*20)
    print('Muito bem então, \033[31mescolha uma dificuldade')
    sleep(1)
    print('\033[37mFácil: seu jogo será mais fácil de acertar... É tão sem graça.. Você vai ter 3 chances de acertar\n\033[33mMédia: Seu jogo será razoavelmente divertido.. Você vai ter 5 tentativas de acerto\n\033[31mDifícil: Seu jogo sera maravilhosamente divertido, você vai ter 7 chances de acertar')
    dificult=(input('\033[mE então ? Qual vai ser? ')).strip().lower()
    print('\033[m___'*20)
    if dificult in('facil', 'fácil'):
        acertou=False
        tentativa=0
        tentativamax=3
        compu1 = randint(0, 3)
        print('Tãooooo sem graça... mas vamos la')
        print('O jogo é o seguinte, eu vou pensar em um número, e você vai ter que acertar')
        while not acertou and tentativa<tentativamax:
            nund1=int(input('Tente adivinhar um número de \033[33m0 a 3\033[m: '))

            sleep(1.5)
            if nund1==compu1:
                print('Você acertou, seu bobão sem graça')
                acertou=True

            elif nund1>3 or nund1<0:
                print('O que foi bobão ? ta com medinho de jogar e passar vergonha errando')

            else:
                tentativa=tentativa+1
                print('Não acredito que você foi capaz de errar nessa dificuldade, vamos, tente de novo\nChances restantes: {}'. format(tentativamax-tentativa))

        if not acertou:
            print('Suas chences acabaram, eu pensei no número {}'.format(compu1))


    elif dificult in('media', 'média', 'medio', 'médio'):
        acertou=False
        tentativa=0
        tentativamax=5
        compu2 = randint(0, 6)
        print('Vamos la, pelo menos vai ser mais divertido do que se fosse no fácil..')
        print('O jogo é o seguinte, eu vou pensar em um número, e você vai ter que acertar')
        while not acertou and tentativa<tentativamax:
            nund2=int(input('\033[36Tente adivinhar em um número de \033[33m0 a 6\033[m: '))

            sleep(1.5)
            if nund2==compu2:
                print('Parábens, você acertou, mas téria sido mais divertido no difícil..')
                acertou=True

            elif nund2>6 or nund2<0:
                print('Sério que você não vai escolher um número decente ?')

            else:
                tentativa=tentativa+1
                print('Você errou, mas tudo bem.. Teria sido pior se fosse no fácil, tente de novo\nTentativas restantes: {}'.format(tentativamax-tentativa))
        if not acertou:
            print('Suas chances acabaram... Eu pensei no número {}'.format(compu2))


    elif dificult in ('dificil', 'difícil'):
        acertou=False
        tentativa=0
        tentativamax=7
        compu3 = randint(0, 10)
        print('Nossa, então você tem coragem... vou caprichar nessa')
        print('O jogo é o seguinte, eu vou pensar em um número, e você vai ter que acertar')
        while not acertou and tentativa<tentativamax:
            nund3=int(input('escolha um número de \033[33m0 a 10\033[m: '))

            sleep(1.5)
            if nund3==compu3:
                print('Não acredito que você acertou... Olha, eu tiro o chapeu pra você..')
                acertou=True

            elif nund3>10 or nund3<0:
                print('Vamos, escolha um número de 0 a 10 logo, ou sua coragem ja foi em bora?')

            else:
                tentativa=tentativa+1
                print('Você errou.. Mas tudo bem, essa dificuldade é realmente difícil, tente de novo\nTentativas restantes: {}'.format(tentativamax-tentativa))

        if not acertou:
            print('Suas chances acabaram, eu pensei no número {}'.format(compu3))
    else:
        print('Vamos, escolha logo uma das opções, você não queria jogar meu jogo?')

elif pronto in ('nao', 'não'):
    print('Nossa.. Não sábia que meu jogo te assustava tanto assim, que sem graça')
else:
    print('Resposta invalida, você ta tentando me enganar ?')
print('--__--__--'*20)


