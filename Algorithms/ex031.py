d = float(input('Qual a distância da sua viagem? '))
print(f'Você está prestes a começar uma viagem de {d}km.')
#preco = d * 0.50 if d <= 200 else d * 0.45
if d <= 200:
    print(f'O valor de sua viagem é de R${d*0.50:.2f}')
else:
    print(f'O valor de sua viagem é de R${d*0.45:.2f}')
print('Tenha uma ótima viagem!')
#print(preco)




