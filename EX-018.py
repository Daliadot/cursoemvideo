from math import sin,radians,cos,tan
ang= int(input('digite o angulo que você deseja:'))
seno= sin(radians(ang))
cosseno= cos(radians(ang))
tangente=tan(radians(ang))
print(f'O seno de {ang} é {seno:.2f}')
print(f'O cosseno de {ang} é {cosseno:.2f}')
print(f'A tangente de {ang} é {tangente:.2f}')