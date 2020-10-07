num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] Converter para Binário
[ 2 ] Converter para Octal
[ 3 ] Converter para Exadecimal''')
op = int(input('Digite a sua opção: '))
if op == 1:
    print(f'{num} convertido para Binário é igual a {bin(num)[2:]}')
elif op == 2:
    print(f'{num} convertido para Octal é igual a {oct(num)[2:]}')
elif op == 3:
    print(f'convertido para Exadecimal é igual a {hex(num)[2:]}')
else:
    print('Opção invalida. Tente novamente.')
