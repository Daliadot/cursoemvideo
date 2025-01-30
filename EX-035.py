r1= float(input('Primeiro segmento:'))
r2= float(input('Segundo segmento:'))
r3= float(input('terceiro segmento:'))
if r1+r2>r3 and r2+r3>r1 and r1+r3>r2:
    print('Os segmentos formam um triangulo')
else:
    print('Os segmentos não forma um triangulo')