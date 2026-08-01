# calculating areas of differ shapes
# Area of rectangle 
l = int(input("Enter length of rectangle: "))
b = int(input("Enter breadth of rectangle: "))
area_rectangle = l*b
print(f"Area of Rectangle is: {area_rectangle}")

# Area of circle
# using radius
r = float(input("Enter the radius of circle: "))
area_circle = r*r
print(f"Area of circle is: {area_circle}")

# using diameter
d = float(input("Enter diameter of circle: "))
pi = 3.14
area_circle_d = (pi*d*d)/4
print(f"Area of circle is: {area_circle_d:.2f}")