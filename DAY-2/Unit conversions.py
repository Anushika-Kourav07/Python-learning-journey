#Unit Conversions 

#Celsius → Fahrenheit
c = float(input('enter temperature in Celsius: '))
f = (c*1.8) + 32
print(f'converted Fahrenheit value is, {f:.2f}')

#Fahrenheit → Celsius
f = float(input('enter temperature in Fahrenheit: '))
c = (f-32) / 1.8
print(f'converted Celsius value is, {c:.2f}')

#Kilometers → Meters
km = float(input('enter km value: '))
m = km*1000
print(f'converted meter value is, {m:.2f}')

# Meters → Kilometers
m = float(input('enter m value: '))
km = m/1000
print(f'converted kilometer value is, {km:.2f}')

# Minutes → Hours
min = float(input('enter time in minute: '))
hr = min/60
print(f'converted kilometer value is, {hr:.2f}')

# Hours → Minutes
hr = float(input('enter time in hour: '))
min = hr*60
print(f'converted minutes value is, {min:.2f}')

# Days → Hours
day = float(input('enter number of days: '))
hr = 24*day
print(f'converted hour value is, {hr:.2f}')

# Rupees → Dollars (use a fixed exchange rate)
rupee = float(input('enter currency in rupee: '))
dollar = rupee/95.39
print(f'converted dollar value is, {dollar:.2f}')

# KG → Grams 
kg = float(input('enter kg value: '))
gm = kg * 1000
print(f'converted gram value is, {gm:.2f}')
