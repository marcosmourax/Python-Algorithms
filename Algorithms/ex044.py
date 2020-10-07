print(f"\033[1;35m{'Shihoin Store':=^}\033[m")
price = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[1] Dinheiro
[2] Cartão de Crédito''')
op = int(input('Qual sua opção? '))
if op == 1:
    print(f'Sua compra à vista em dinheiro ou cheque de \033[32mR${price:.2f}\033[m vai custar \033[36mR${price * 0.90:.2f}\033[m no final.')
elif op == 2:
    pa = int(input('Quantas Parcelas? '))
    if pa == 1:
        print(f'Sua compra à vista no catão de \033[32mR${price:.2f}\033[m vai custar \033[36mR${price * 0.95:.2f}\033[m no final.')
    elif pa == 2:
        print(
            f'Sua compra sera parcelada em {pa}x de {price / pa:.2f} \nSua compra de \033[32mR${price:.2f}\033[m vai custar \033[32mR${price:.2f}\033[m')
    elif pa >= 3 or pa <= 10:
        print(f'Sua compra será parcelada em {pa}x de R${(price + (price *  20/100))  / pa:.2f} COM JUROS')
        print(f'Sua compra de \033[32mR${price:.2f}\033[m vai custar \033[31mR${price + (price *  20/100):.2f}\033[m')
else:
    print('\033[1;31mOpção invalida. Tente novamente.\033[m')
