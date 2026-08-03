# check whether number is +ve, -ve or 0
num = float(input('enter number to check: '))
if num > 0:
    print(f'{num} is a POSITIVE.')
elif num < 0:
    print(f'{num} is a NEGETIVE.')
else:
    print(f'{num} is ZERO.')