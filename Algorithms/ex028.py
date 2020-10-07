from random import choice
from time import sleep
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
list = choice([0, 1, 2, 3, 4, 5])
num = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(1)
if list == num:
    print('PARABÉNS! Você me venceu!')
else:
    print(f'GANHEI! Eu pensei no número {list} e não no {num}!')


