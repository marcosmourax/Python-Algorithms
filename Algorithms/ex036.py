import time
house = float(input('What is the value of the property: $'))
salary = float(input("Buyer's salary: $"))
years = int(input('How many years of financing? '))
plots = house / (years * 12)
minimum = salary * 30 / 100
print(f'To pay for a property of ${house:.2f} in {years} years the installment will be ${plots:.2f}', end='')
print('\033[30m\nANALYZING...\033[m')
time.sleep(1)
if plots <= minimum:
    print('Loan \033[32mAPPROVED!')
else:
    print('Loan \033[31mDENIED!')

