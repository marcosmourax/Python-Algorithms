from time import sleep
num = int(input('Me diga um número qualquer: '))
print('ANALISANDO... ')
sleep(1)
if (num % 2) == 0:
    print(f'O número {num} é Par.')
else:
    print(f'O número {num} é Ímpar.')
