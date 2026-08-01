# student percentage 
'''
LOGIC: 
total sub= 5
eng, hindi, maths, ai, science
percentage= ((e+h+m+s+a)/total)*100
'''
sub_1 = float(input("Enter your subject 1 marks out of 100: "))
sub_2 = float(input("Enter your subject 2 marks out of 100: "))
sub_3 = float(input("Enter your subject 3 marks out of 100: "))
sub_4 = float(input("Enter your subject 4 marks out of 100: "))
sub_5 = float(input("Enter your subject 5 marks out of 100: "))
total = 500
percentage = ((sub_1 + sub_2 + sub_3 + sub_4 +sub_5)*100)/total
print(f'Your percentage is {percentage}%')
