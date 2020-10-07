n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
if ((n1 + n2) / 2) < 5.0:
    print('Você foi \033[31mREPROVADO!\033[m')
elif 5.0 <= ((n1 + n2) / 2) < 7.0:
    print('Você ficou de \033[33mRECUPERAÇÃO!\033[m')
elif ((n1 + n2) / 2) >= 7.0:
    print('Você foi \033[36mAPROVADO!\033[m')
print(f'Sua média final foi de \033[30m{(n1 + n2) / 2:.1f}\033[m')
