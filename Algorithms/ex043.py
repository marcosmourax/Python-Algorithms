a = float(input('Digite sua altura: '))
p = float(input('Digite seu peso: '))
imc = p / (a ** 2)
print(f'Seu peso atual é \033[32m{imc:.1f}\033[m \nVocê está ', end='')
if imc < 18.5:
    print('\033[32mAbaixo do Peso.\033[m')
elif imc < 25:
    print('com o \033[36mPeso Ideal.\033[m')
elif imc < 30:
    print('com \033[35mSobrepeso.\033[m')
elif imc < 40:
    print('com \033[33mObesidade.\033[m')
else:
    print('com \033[31mObesidade Mórbida.\033[m')
