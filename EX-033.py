n1= int(input('Digite o primeiro numero:'))
n2=int(input('Digite o segundo numero:'))
n3=int(input('Digite o terceiro numero:'))

menor=n1
if n2<n1 and n2<n3:
    menor= n2
if n3<n2 and n3<n1:
    menor= n3

maior= n2
if n1>n2 and n1>n3:
    maior=n1
if n3>n2 and n3>n1:
    maior=n3
print(f'O maior valor é: {maior}')
print(f'O menor valor é: {menor}')