from random import randint
pc = randint(0, 10)
print('\033[36m-=-\033[m' * 22)
print("\033[30mI'm your computer... I just thought of a number between 0 and 10.\033[m")
print('\033[36m-=-\033[m' * 22)
hit = False
hunches = 0
while not hit:
    player = int(input("\033[30mWhat's your guess?\033[m "))
    hunches += 1
    if player == pc:
        hit = True
    else:
        if player < pc:
            print('Mais... Tente mais uma vez.')
        elif player > pc:
            print('Menos... Tente mais uma vez.')
print(f'Acertou com {hunches} tentativas. Parabéns!')






