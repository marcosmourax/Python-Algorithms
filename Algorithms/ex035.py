print('-=-'*10)
print('Analisador de Triângulos')
print('-=-' *10)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(f'Os segmentos acima formam um triângulo.')
else:
    print(f'Os segmentos acima não formam um triângulo.')
