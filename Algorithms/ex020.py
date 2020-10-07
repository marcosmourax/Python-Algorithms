from random import sample
a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))
print(f'A ordem de apresentação será: \n{sample([a1,a2,a3,a4],k=4)}')
