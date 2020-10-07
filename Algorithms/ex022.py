name = str(input('Digite seu nome: '))
print('Analisando seu nome...')
print(f'Seu nome em Maiúsculas é {name.upper()} \nSeu nome em Minúsculas é {name.lower()}')
print(f'Seu nome tem ao todo {len(name) - name.count(" ")} letras.')
print(f'Seu primeiro nome é {name.split()[0]} e ele tem {len(name.split()[0])} letras.')

















