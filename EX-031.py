distancia= float(input('Qual a distancia da sua viagem em KM?'))
if distancia<=200:
    valor1= distancia*0.50
    print(f'Você pagara R$0,50 por KM nessa viagem. Totalizando R${valor1:.2f}')
else:
    valor2= distancia*0.45
    print(f'Você pagara R$0,45 por KM nessa viagem. Totalizando R${valor2:.2f}')
print('Boa viagem')