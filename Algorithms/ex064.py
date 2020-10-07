num = cont = soma = 0
num = int(input('Digite um número: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número: '))
print(f'Você digitou {cont} números e a soma entre eles foi {soma}')
