print('\033[30m=-=\033[m' * 5)
print('    \033[1;36mTABUADA\033[m')
print('\033[30m=-=\033[m' * 5)
while True:
    n = int(input('Digite o valor: '))
    if n < 0:
        break
    if n > 0:
        for t in range(0, 11):
            print(f'{n} x {t} = {n * t}')
print('\033[1;30mPROGRAMA ENCERRADO.\033[m')


