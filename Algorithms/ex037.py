numero_converter = int(input('Digite o número inteiro: '))
numero_antigo = numero_converter
base = int(input('Escolha uma das bases para conversão:  \n1 - Converter para Binário \n2 - Converter para Octal e \n3 - Converter para Hexadecimal: '))

if base == 1:
    numero_convertido = str(numero_converter % 2)
    numero_converter = int(numero_converter / 2)
    while numero_converter > 0:
        numero_convertido = str(numero_converter % 2) + numero_convertido
        numero_converter = int(numero_converter / 2)
    print(f'O número {numero_antigo} em binário é {numero_convertido}')
elif base == 2:
    numero_convertido = str(numero_converter % 8)
    numero_converter = int(numero_converter / 8)
    while numero_converter > 0:
        numero_convertido = str(numero_converter % 8) + numero_convertido
        numero_converter = int(numero_converter / 8)
    print(f'O número {numero_antigo} em octal é {numero_convertido}')


elif base == 3:
    numero_convertido = int(numero_converter % 16)
    if numero_convertido > 9:
        a = 1
        if numero_convertido == 10:
            numero_convertido = 'A'
        if numero_convertido == 11:
            numero_convertido = 'B'
        if numero_convertido == 12:
            numero_convertido = 'C'
        if numero_convertido == 13:
            numero_convertido = 'D'
        if numero_convertido == 14:
            numero_convertido = 'E'
        if numero_convertido == 15:
            numero_convertido = 'F'
    else:
        numero_convertido = str(numero_converter % 16)
    numero_converter = int(numero_converter / 16)
    while numero_converter > 0:
        numero_a_ser_adicionado = int(numero_converter % 16)
        if numero_a_ser_adicionado > 9:
            a = 1
            if numero_a_ser_adicionado == 10:
                numero_a_ser_adicionado = 'A'
            if numero_a_ser_adicionado == 11:
                numero_a_ser_adicionado = 'B'
            if numero_a_ser_adicionado == 12:
                numero_a_ser_adicionado = 'C'
            if numero_a_ser_adicionado == 13:
                numero_a_ser_adicionado = 'D'
            if numero_a_ser_adicionado == 14:
                numero_a_ser_adicionado = 'E'
            if numero_a_ser_adicionado == 15:
                numero_a_ser_adicionado = 'F'
        else:
            numero_a_ser_adicionado = str(numero_converter % 16)
        print(numero_a_ser_adicionado)
        numero_convertido = numero_a_ser_adicionado + numero_convertido
        numero_converter = int(numero_converter / 16)
    print(f'O número {numero_antigo} em hexadecimal é {numero_convertido}')
else:
    print('Opção inválida')

