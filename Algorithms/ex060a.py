print('\033[36m-=-\033[m' * 7)
print("\033[30mCalculo de Fatorial\033[m")
print('\033[36m-=-\033[m' * 7)
n = int(input('Digite um número: '))
c = n
f = 1
print(f'Calculando {n}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' X ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'{f}')
