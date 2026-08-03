'''
Write a program that asks the user for:
    Name
    Age
    Height (in meters)
    Weight (in kg)

Then print:

    Hello, Anu!

    Age: 20 years
    BMI: 22.4

    Thank you for using the Health Calculator.
'''
n= str(input('Enter your name: '))
a= int(input('Enter your age: '))
h= float(input('Enter your height(in meters): '))
w= float(input('Enter your weight(in kg): '))
bmi= w/(h**2)
print()
print(f'''Hello, {n}!

Age: {a}
BMI: {bmi:.2f}

Thank You for using the Health Calculator.''')