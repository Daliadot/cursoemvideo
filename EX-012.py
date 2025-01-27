produto = float(input('Qual é o preço do produto? R$'))
desconto= produto *0.05
valor= produto-desconto
print(f'O produto que custava R${produto}, na promoção com desconto de 5% vai custar R${valor:.2f}')