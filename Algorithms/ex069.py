t = th = tm = 0
print('\033[30m=-=\033[m' * 10)
print('     \033[1;34mCADASTRE UMA PESSOA!\033[m')
print('\033[30m=-=\033[m' * 10)
while True:
    i = int(input('Idade: '))
    s = ' '
    while s not in 'MF':
        s = str(input('Sexo: ')).strip().upper()[0]
    if i >= 18:
        t += 1
    if s == 'M':
        th += 1
    if s == 'F' and i < 20:
        tm += 1
    r = ' '
    while r not in 'SN':
        print('---' * 10)
        r = str(input('Quer continuar? ')).strip().upper()[0]
        print('---' * 10)
    if r == 'N':
        break
print(f'Temos {t} pessoas com mais de 18 anos')
print(f'Ao todo temos {th} homens cadastrados.')
print(f'Temos {tm} mulher com menos de 20 anos.')
