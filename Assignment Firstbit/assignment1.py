# 1. Write a program to calculate the percentage of student based on marks of any 5 subjects.
#start 
maths=int(input("enter marks of maths : ")) 
physics=int(input("enter marks of physics : ")) 
chemistry=int(input("enter marks of chemistry : ")) 
biology=int(input("enter marks of biology : ")) 
english=int(input("enter marks of english : ")) 
#Perform Operation 
total_sum = maths+physics+chemistry+biology+english
percentage = total_sum/500*100
#Display Output
print(f'Percentage of student is {percentage}% ')

# Write a program to calculate area of rectangle based on length and breadth.
#start
length=int(input("enter length of rectangle : "))
breadth=int(input("enter breadth of rectangle : ")) 
# Perform Operation 
area_of_rectangle = length*breadth
#Display Output
print(f' Area Of Rectangle is : {area_of_rectangle}')

# Program to find quotient and remainder of two numbers. 
num1=float(input(" enter number1 : "))
num2=float(input(" enter number2 : "))
# perform operation 
quotient= num1 // num2
remainder= num1 % num2 
#Display Output
print(f'quotient is { quotient} and remainder is {remainder}')

#Write a program to enter P, T, R and calculate simple Interest 
# start 
principal=float(input(" Enter the principal : "))
time=float(input(" enter time : "))
rate= float(input(" enter the  rate  of intrest % : "))
# Perfrom operation
simple_interest=principal*time*rate/100
#display Output
print(f' Simple Interest is : {simple_interest}')

# Write a program to enter P, T, R and calculate Compound Interest. 
#start 
principal=float(input(" Enter the principal : "))
time=float(input(" enter time : "))
rate= float(input(" enter the  rate of interest % : "))
# Perfrom operation
amount = principal*pow(1+rate/100,time)
compound_interest= amount-principal
#Display Output
print(f'Compound Interest is : {compound_interest}')

#Write a Program to input two angles from user and find third angle of the triangle.
#start
angle1=float(input("enter first angle : "))
angle2=float(input("enter second angle : "))
# perform operation
angle3=180-(angle1+angle2)
#Display Output
print(f'Third angle of triangle is : {angle3}')

#Program to Find the Roots of a Quadratic Equation 
# Program to solve quadratic equation: ax^2 + bx + c = 0

# Input coefficients from the user
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# Calculate the discriminant (b^2 - 4ac)
d = b**2 - 4*a*c
# perform operation to find the roots
root1 = (-b + d**0.5) / (2 * a)
root2 = (-b - d**0.5) / (2 * a)

# Display the results
print("Root 1:", root1)
print("Root 2:", root2)

#Write a program to enter base and height of a triangle and find its area.
#start
base=float(input("enter base of triangle : "))
height=float(input("enter height of triangle : "))  
# perform operation
area_of_triangle=0.5*base*height
#Display Output
print(f'Area of triangle is : {area_of_triangle}')


#Write a program to calculate area of an equilateral triangle. 
#start
side=float(input("enter side of equilateral triangle : "))
area_of_equilateral_triangle=(3**0.5)/4 * side**2

#Display Output
print(f'Area of equilateral triangle is : {area_of_equilateral_triangle}')

#Find the area and circumference of circle. 
radius=float(input("enter radius of circle : "))
area_of_circle=3.14*radius**2
circumference_of_circle=2*3.14*radius

#Display Output
print(f'Area of circle is : {area_of_circle}')
print(f'Circumference of circle is : {circumference_of_circle}')

#Find the volume of sphere
radius=float(input("enter radius of sphere : "))
volume_of_sphere=(4/3)*3.14*radius**3

#Display Output
print(f'Volume of sphere is : {volume_of_sphere}')



 

