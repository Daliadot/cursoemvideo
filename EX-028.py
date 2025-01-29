import random
num_pc= random.randrange(0,5)
num_usuario= int(input('Adivinhe um numero de 0 a 5 escolhido pela maquina:'))
if num_pc==num_usuario:
    print('Parabens! Você acertou o numero escolhido pela maquina!')
else:
    print(f'Não foi dessa vez, o numero sorteado foi {num_pc}')
