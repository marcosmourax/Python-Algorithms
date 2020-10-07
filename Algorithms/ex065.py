r = 'S'
soma = quant = media = maior = menor = 0
while r in 'Ss':
    n = int(input('Digite um número: '))
    soma += n
    quant += 1
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    r = str(input('Quer continuar? ')).upper().strip()[0]
media = soma / quant
print(f'Você digitou {quant} números e a média foi {media} \nO maior número digitado foi {maior} e o menor foi {menor} ')

