numero= int(input('informe um numero:'))
u=numero%10
d= numero//10%10
c=numero//100%10
m=numero//1000%10

print(f'Analisando o número:{numero}')

if(u>0):
    print(f'Unidade:{u}')
else:
    print('Não tem unidade')

if(d>0):
    print(f'Dezena:{d}')
else:
    print('Não tem unidade')

if(c>0):
    print(f'centena:{c}')
else:
    print('Não tem centena')

if(m>0):
    print(f'centena:{m}')
else:
    print('Não tem milhar')