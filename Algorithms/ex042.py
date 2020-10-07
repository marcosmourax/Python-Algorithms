from time import sleep
print('\033[30m-=-\033[m'*8)
print('\033[1;36mAnaisador de Triângulos\033[m')
print('\033[30m-=-\033[m'*8)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
print('\033[30mANALISANDO...\033[m')
sleep(1)
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(f'\033[1;36mOs Segmentos acima formam um Triângulo.\033[m')
    if r1 == r2 == r3:
     print('O triângulo é \033[32mEquilátero!\033[m')
    elif r1 == r2 or r1 == r3 or r2 == r3:
      print('O triângulo é \033[34mIsósceles!\033[m')
    elif r1 != r2 != r3:
     print('O triângulo é \033[35mEscaleno!\033[m')
else:
    print(f'\033[31mOs três Segmentos não podem formar um Triângulo!\033[m')
