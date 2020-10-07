from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo Valor: '))
op = 0
while op != 5:
    print('''    [1]Somar
    [2]Multiplicar
    [3]Maior
    [4]Novos números
    [5]Sair''')
    op = int(input('Qual a sua opção? '))
    if op == 1:
        print(f'O resultado de {n1} + {n2} = {n1 + n2}')
    elif op == 2:
        print(f'O resultado de {n1} x {n2} = {n1 * n2}')
    elif op == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
            print(f'Entre {n1} e {n2} o maior valor é {maior}')
    elif op == 4:
        print('Informe od números novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo Valor: '))
    elif op == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente.')
    print('-=-' *10)
    sleep(3)
print('Fim do programa.')



