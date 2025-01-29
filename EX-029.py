velocidade= float(input('Quantos KM/h você está dirigindo? '))
if velocidade>80:
    multa=(velocidade-80)*7.00
    print(f'Você ultrapassou o limite de velocidade e foi multado em R${multa:.2f}')
else:
    print('Você está dentro do limite, Boa viagem!')