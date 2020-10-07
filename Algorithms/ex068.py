from random import randint
v = 0
print('\033[30m=-=\033[m' * 10)
print('   \033[1;35mVAMOS JOGAR PAR OU ÍMPAR\033[m')
print('\033[30m=-=\033[m' * 10)
while True:
    player = int(input('Diga um valor: '))
    pc = randint(0, 10)
    total = player + pc
    type = ' '
    while type not in 'PI':
        type = str(input('Par ou Ímpar? ')).strip().upper()[0]
    print(f'Você jogou {player} e o Computador {pc}. Total de {total}. ', end='')
    print('DEU PAR!' if total % 2 == 0 else 'DEU ÍMPAR!')
    if type == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif type == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente... ')
if v > 1:
    print(f'GAME OVER! Você venceu {v} vezes.')
elif v == 0:
    print(f'GAME OVER! Você não venceu nenhuma vez')
else:
    print(f'GAME OVER! Você venceu {v} vez.')



