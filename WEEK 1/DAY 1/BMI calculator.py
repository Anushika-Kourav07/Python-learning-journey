# BMI calculator

print("BMI CALCULATOR: ")
name = str(input("Enter your name: "))
age = int(input("Enter your age: "))
height = float(input("Enter your height in cm: "))
weight = float(input("Enter your kg: "))
h = height/100
bmi = (weight/(h**2))
print(f"Your BMI is {bmi:.2f}")

if bmi < 18.50:
    print("You are UNDERWEIGHT!")
elif bmi <= 25.00 and bmi >= 18.50:
    print("You are HEALTHY!")
else:
    print("You are OVERWEIGHT!")
