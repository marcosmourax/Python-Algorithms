num = int(input("Digite um número: "))
to = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[32m', end='')
        to += 1
    else:
        print('\033[31m', end='')
    print(f'{c} ', end='')
print(f'\n\033[mO número {num} foi divisível {to} vezes.')
if to == 2:
    print('E por isso ele É PRIMO! ')
else:
    print('E por isso ele NÃO É PRIMO! ')
