q = str(input('Digite uma frase: ')).strip().upper()
p = q.split()
j = ''.join(p)
i = j[::-1]
print(f'O inverso de {j} é {i}')
if i == j:
    print(f'Temos um Palíndromo!')
else:
    print(f'A frase digitada não é um Palíndromo!')
