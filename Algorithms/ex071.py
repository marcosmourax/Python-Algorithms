print('\033[30m=-=\033[m' * 7)
print('    \033[1;35mShihoin Bank\033[m')
print('\033[30m=-=\033[m' * 7)
valor = int(input('Informe o valor do saque: R$'))
nota50 = valor // 50
valor %= 50
nota20 = valor // 20
valor %= 20
nota10 = valor // 10
valor %= 10
nota1 = valor // 1
print(f'Notas de 50 = {nota50}')
print(f'Notas de 20 = {nota20}')
print(f'Notas de 10 = {nota10}')
print(f'Notas de 1 = {nota1}')