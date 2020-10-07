list = []
for c in range(1, 6):
    p = float(input(f'Peso da {c}° pessoa: '))
    list += [p]
print(f'O maior peso lido é de {max(list):.1f}Kg e o menor é {min(list):.1f}Kg.')

