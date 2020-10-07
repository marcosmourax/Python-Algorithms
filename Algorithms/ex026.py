quote = str(input('Digite uma frase: ')).upper().strip()
print(f'A letra A aparece {quote.count("A")} vezes na frase.')
print(f'Ela aparece pela primeira vez na posição {quote.find("A")+1} e na ultima {quote.rfind("A")+1}.')


