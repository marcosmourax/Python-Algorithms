print('-=-'*10)
print('     \033[36m10 TERMOS DE UMA PA!\033[m')
print('-=-'*10)
pt = int(input('Primeiro termo: '))
rz = int(input('Razão: '))
dc = pt + (10 - 1) * rz
for c in range(pt, dc + rz, rz):
    print(c, end=' → ')
print('Finish.')
