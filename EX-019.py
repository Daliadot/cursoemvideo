from random import choice
A1= input('Nome do primeiro aluno:')
A2= input('Nome do segundo Aluno:')
A3=input('Nome do terceiro Aluno:')
A4= input("Nome do quarto Aluno:")
lista= [A1,A2,A3,A4]
escolhido= choice(lista)
print(f'O aluno escolhido é {escolhido}')