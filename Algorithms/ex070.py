print('\033[30m=-=\033[m' * 7)
print("    \033[1;35mMOURA'S STORE!\033[m")
print('\033[30m=-=\033[m' * 7)
t = tm = mn = c = 0
b = ' '
while True:
    p = str(input('Nome do produto: ')).strip().upper()
    v = float(input('Preço: R$'))
    c += 1
    t += v
    if v > 1000:
        tm += 1
    if c == 1 or v < mn:
        b = p
        mn = v
    r = ' '
    while r not in 'SN':
        print('---' * 7)
        r = str(input('Quer continuar? ')).strip().upper()[0]
        print('---' * 7)
    if r == 'N':
        break
print(f"{'FIM DO PROGRAMA!':^}")
print(f'O total da compra foi R${t:.2f}')
print(f'Temos {tm} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {b} que custa R${mn:.2f}')
