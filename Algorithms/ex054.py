from datetime import date
m = 0
for c in range(1, 8):
    p = int(input(f'Em que ano a {c}° pessoa nasceu? '))
    if date.today().year - p < 21:
        m += 1
print(f'Ao tudo tevemos {7 - m} pessoas maiores de idade. \nE também tivemos {m} pessoas menores de idade.')