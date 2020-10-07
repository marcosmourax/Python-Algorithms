print('\033[36m-=-\033[m' * 8)
print(' \033[1;30mSequência de Fibonacci\033[m')
print('\033[36m-=-\033[m' * 8)
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print(f'{t1} → {t2}', end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(f' → {t3}', end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' → FIM.')
