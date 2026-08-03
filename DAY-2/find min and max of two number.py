# minimun and maximum of two numbers
a= float(input('enter first number: '))
b= float(input('enter secone number: '))
if a > b:
    print(f'Maximum number: {a}')
    print(f'Minimum number: {b}')
elif b > a:
    print(f'Maximum number: {b}')
    print(f'Minimum number: {a}')
else:
    print(f'Both are Equal.')