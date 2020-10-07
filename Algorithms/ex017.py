from math import hypot
co = float(input('Comprimento do Cateto Oposto:'))
ca = float(input('Comprimento do Cateto Adjacente:'))
print(f'O comprimento da Hipotenusa é {hypot(co,ca):.2f}')
#print(f'O comprimento da Hipotenusa é {(co**2 + ca**2)**(1/2):.2f}')



