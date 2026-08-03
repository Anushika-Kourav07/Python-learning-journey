# Profit / Loss calculator
sp = float(input('Enter selling price: '))
cp = float(input('Enter cost price: '))
if sp > cp:
    print(f'You made profit of {sp-cp} with Profit percent of {((sp-cp)/cp)*100:.2f} %')
elif cp > sp:
    print(f'You had a loss of {cp-sp} with Loss percent of {((cp-sp)/cp)*100:.2f} %')

# S.I. Calculator
p = float(input('Enter principal amount: '))
r = float(input('Enter interest rate: '))
t = float(input('Enter time period: '))
si = (p*r*t)/100
print(f'Simple interest is {si:.2f}')