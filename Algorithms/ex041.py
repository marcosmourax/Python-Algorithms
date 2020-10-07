from datetime import date
year = date.today().year
birth = int(input('Ano de Nascimento: '))
age = year - birth
print(f'O atleta tem {age} anos.')
if age <= 9:
    print('Categoria: \033[30mMIRIM!\033[m')
elif age <= 14:
    print('Categoria: \033[32mINFANTIL!\033[m')
elif age <= 19:
    print('Categoria: \033[33mJUNIOR!\033[m')
elif age <= 25:
    print('Categoria: \033[31mSÊNIOR!\033[m')
else:
    print('Categoria: \033[35mMASTER!\033[m')
