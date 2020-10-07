print('Gerador de PA')
print('-=-' * 7)
pt = int(input('Primeiro termo: '))
rz = int(input('Razão: '))
te = pt
cont = 1
while cont <= 10:
    print(f'{te} → ', end='')
    te += rz
    cont += 1
print('End.')
