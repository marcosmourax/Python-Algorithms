r = float(input('Quanto dinheiro você tem? R$'))
d = 1*5.01
print(f'Com R${r:.2f} você pode comprar US${r//d:.2f} e sobra {r%d:.2f}')


