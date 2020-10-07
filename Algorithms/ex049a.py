n = int(input('Digite um número: '))
print('''Escolha a tabuada que deseja: 
[m] Multiplicação
[d] Divisão
[a] Adição
[s] Subtração''')
op = str(input('Escolha qual tabuda deseja: '))
while op != 'm' and op != 'd' and op != 'a' and op != 's':
    op = str(input('Tente novamente: ')).lower()
for t in range(1, 11):
    if op == 'm':
        print(f'{n} x {t} = {n * t}')
    elif op == 'd':
        print(f'{n} ÷ {t} = {n / t:.1f}')
    elif op == 'a':
        print(f'{n} + {t} = {n + t}')
    elif op == 's':
        print(f'{n} - {t} = {n - t}')
