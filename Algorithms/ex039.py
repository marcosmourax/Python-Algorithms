from datetime import date
current = date.today().year
birth = int(input('Ano de nascimento: '))
age = current - birth
print(f'Quem nasceu em {birth} tem {age} anos em {current}.')

if age == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif age < 18:
    balance = 18 - age
    print(f'Você ainda não tem 18 anos. Ainda falta {balance} anos para o alistamento.')
    year = current + balance
    print(f'Seu alistamento será em {year}')
elif age > 18:
    balance = age - 18
    print(f'Você já deveria ter se alistado há {balance} anos.')
    year = current - balance
    print(f'Seu alistamento foi em {year}')
