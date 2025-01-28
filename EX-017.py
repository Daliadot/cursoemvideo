from math import hypot
oposto= float(input('digite o cateto oposto:'))
adjacente= float(input('digite o cateto adjacente:'))
hipotenusa= hypot(oposto, adjacente)
print(f'A ipotenusa deste triangulo retangulo é {hipotenusa:.2f}')