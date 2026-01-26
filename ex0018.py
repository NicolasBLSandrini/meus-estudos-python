from math import (sin, cos, tan, radians)
angulo=float(input('Digite qualquer angulo: '))
an_ra=radians(angulo)
seno=sin(an_ra)
cosseno=cos(an_ra)
tangente=tan(an_ra)
print('O seno do seu angulo é {:.2f}\nO cosseno é {:.2f}\nE a tangente é {:.2f}'.format(seno, cosseno, tangente))

