n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))
mn = n1
if n2 < n1 and n2 < n3:
    mn = n2
if n3 < n1 and n3 < n2:
    mn = n3
print(f'O menor valor digitado foi {mn}')
ma = n1
if n2 > n1 and n2 > n3:
    ma = n2
if n3 > n1 and n3 > n2:
    ma = n3
print(f'O maior valor digitado foi {ma}')
