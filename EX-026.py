frase= input('Digite uma frase:').strip()
min=frase.lower()
print(f'A letra A aparece {min.count('a')} vezes na frase')
print(f'A primeira letra A aparece na posição {min.find('a')+1}')
print(f'A ultima letra A aparece na posição {min.rfind('a')+1}')