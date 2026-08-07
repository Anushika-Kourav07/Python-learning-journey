# celsius to fahrenheit conversion
c = float(input("Enter the celsius value: "))
f = float(input("Enter the fahrenheit value: "))

# celsius to fahrenheit conversion
c_to_f = (c*1.8) + 32
print(f"Fahrenheit of {c} is : {c_to_f}")

# fahrenheit to celsius conversion
f_to_c = (f-32)/1.8
print(f"Celsius of {f} is : {f_to_c}")
