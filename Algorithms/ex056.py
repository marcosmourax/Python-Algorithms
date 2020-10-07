sa = 0
ma = 0
om = 0
on = ''
w = 0
for c in range(1, 5):
    print(f'\033[1;36m=== {c}° PESSOA ===\033[m')
    name = str(input('Nome: ')).strip()
    age = int(input('Idade: '))
    sex = str(input('Sexo [M/F]: ')).strip()
    sa += age
    if c == 1 and sex in 'Mm':
        om = age
        on = name
    if sex in 'Mm' and age > om:
        om = age
        on = name
    if sex in 'Ff' and age > 20:
        w += 1
ma = sa / 4
print(f'A média de idade do grupo é de {ma:.1f} \nO homem mais velho tem {om} anos e se chama {on}. \nAo todo são {w} mulheres com menos de 20 anos.')
