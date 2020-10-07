num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))
if num1 > num2:
    print(f'O número \033[1;32m{num1}\033[m é maior que o número \033[1;31m{num2}\033[m ')
elif num1 < num2:
    print(f'O número \033[1;31m{num1}\033[m é menor que o \033[1;32m{num2}\033[m')
elif num1 == num2:
    print(f'O número \033[1;36m{num1}\033[m é igual a \033[1;36m{num2}\033[m ')
