print('Gerador de PA')
print('-=-' * 7)
pt = int(input('Primeiro termo: '))
rz = int(input('Razão: '))
te = pt
cont = 1
t = 0
m = 10
while m != 0:
    t += m
    while cont <= t:
        print(f'{te} → ', end='')
        te += rz
        cont += 1
    print('Pausa')
    m = int(input('Quantos termo você quer mostrar a mais? '))
print(f'Progressão finalizada com {t} termos mostrados.')
