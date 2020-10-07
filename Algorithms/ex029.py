vel = float(input('Qual é a velocidade atual do carro: '))
if vel > 80:
    print(f'MULTADO! Você excedeu o limite permitido que é de 80km/h \nVocê deve pagar uma multa de R${(vel - 80)*7:.2f}!')
print('Tenha um bom dia! Dirija com segurança!')


