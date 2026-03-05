num=int(input('Digite seu número para conversão: '))
conver=input('Você quer converter esse número para binário, octal ou hexadecimal? ').strip().lower()

if conver in ('hexadecimal','hexa'):
    print(f'Seu número, em hexadecimal é {num:X}')

elif conver in ('octal', 'oct'):
    print(f'Seu número em octal ficou {num:o}')

elif conver in ('binário', 'bin'):
    print(f'Seu número em binário ficou {num:b}')

elif conver in ('todas'):
    print(f'hexa ficou {num:X}      oct ficou {num:o}    e bin ficou {num:b}')
