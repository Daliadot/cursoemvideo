salario=float(input("Digite o seu salario:"))
if salario>1250:
    aumento=(salario*0.10)+salario
    print(f'O seu salario foi aumentado em 10% e agora será de R${aumento}')
else:
    aumento=(salario*0.15)+salario
    print(f'Seu salario aumentou em 15% e agora é R${aumento}')