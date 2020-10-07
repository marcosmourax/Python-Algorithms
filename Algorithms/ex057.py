s = str(input('Informe seu Sexo: ')).strip().upper()[0]
while s not in 'MmFf':
    s = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print(f'Sexo {s} registrado com Sucesso.')
