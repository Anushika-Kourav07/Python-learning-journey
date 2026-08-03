'''
Student Information Program
    Take input:
        Name
        Age
        Roll Number
        College Name
        Marks in 5 subjects
    Output:
        Total Marks
        Percentage
        Average Marks
'''
n= str(input('Enter your name: '))
a= int(input('Enter your age: '))
roll= str(input('Enter your roll number: '))
clg= str(input('Enter College name: '))
print('Now provide marks of 5 subjects -')
m_1= float(input('Enter first subject marks: '))
m_2= float(input('Enter second subject marks: '))
m_3= float(input('Enter third subject marks: '))
m_4= float(input('Enter fourth subject marks: '))
m_5= float(input('Enter fifth subject marks: '))
total = (m_1+m_2+m_3+m_4+m_5)
percentage = ((m_1+m_2+m_3+m_4+m_5)*100)/500
avg = (m_1+m_2+m_3+m_4+m_5)/5

print(f'''Total Marks: {total}/500
Percentage: {percentage:.2f}
Average Marks: {avg:.2f}
''')