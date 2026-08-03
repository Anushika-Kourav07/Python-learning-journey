# Largest of two numbers
a= float(input('enter first number: '))
b= float(input('enter secone number: '))
if a > b:
    print(f'First number {a} is largest number.')
elif b > a:
    print(f'Second number {b} is largerst number.')
else:
    print(f'Both {a} and {b} are equal')
