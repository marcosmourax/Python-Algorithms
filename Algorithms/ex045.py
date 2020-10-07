from random import choice
from time import sleep
print('-=-'*9)
print("Let's play \033[36mじゃんけんぽん?\033[m ")
print('-=-'*9)
list = ['rock', 'paper', 'scissors']
pc = choice(list)
player = str(input("Type your option: ")).lower()
while player != 'rock' and player != 'paper' and player != 'scissors':
    player = str(input('Type again: ')).lower()
print('JAN')
sleep(1)
print('KEN')
sleep(1)
print('PON!')
if player == 'rock' and pc == 'scissors' or player == 'paper' and pc == 'rock' or player == 'scissors' and pc == 'paper':
    print(f'\033[36mYou Win, I put {pc}!\033[m')
elif player == 'rock' and pc == 'rock' or player == 'paper' and pc == 'paper' or player == 'scissors' and pc == 'scissors':
    print(f'\033[33mDraw, I put {pc}!\033[m')
elif player == 'rock' and pc == 'paper' or player == 'paper' and pc == 'scissors' or player == 'scissors' and pc == 'rock':
    print(f'\033[31mYou lose, I put {pc}!\033[m')
#else:
    #print('\033[31mOpção Invalida.\033[m')
