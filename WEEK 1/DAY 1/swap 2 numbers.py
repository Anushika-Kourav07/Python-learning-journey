# swap of two number 
'''
LOGIC: 
a, b, c
c=a-b
a=a-c
b=b+c
print a,b
'''
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print('BEFORE SWAP -')
print(f'First number: {a}     second number: {b}')
c = a-b
a = a-c
b = b+c
print('AFTER SWAP -')
print(f'First number: {a}     second number: {b}')
