#Convert the time entered in hh,min and sec into seconds
#start
hh = int(input("Enter hours: "))
mm = int(input("Enter minutes: "))
ss = int(input("Enter seconds: "))
# perform operation
total_seconds = hh * 3600 + mm * 60 + ss
#display Output
print(f"Total seconds: {total_seconds}")
#Convert temp from Celsius to Fahrenheit. (C/5 = (F-32)/9)
#start
celsius = float(input("Enter temperature in Celsius: "))
# perform operation
fahrenheit = (celsius * 9/5) + 32
#display Output
print(f"Temperature in Fahrenheit: {fahrenheit}")
#Convert distant given in feet and inches into meter and centimeter.
#start
feet = float(input("Enter distance in feet: "))
inches = float(input("Enter distance in inches: "))
# perform operation
total_inches = feet * 12 + inches
meter = total_inches * 0.0254
centimeter = meter * 100
#display Output
print(f"Distance in meters: {meter} m")
print(f"Distance in centimeters: {centimeter} cm")
#WAP to calculate area of triangle and rectangle
#start
# For triangle
base = float(input("Enter base of triangle: "))
height = float(input("Enter height of triangle: "))
# perform operation
area_of_triangle = 0.5 * base * height
#display Output
print(f"Area of triangle: {area_of_triangle}")
# For rectangle
length = float(input("Enter length of rectangle: "))
breadth = float(input("Enter breadth of rectangle: "))
# perform operation
area_of_rectangle = length * breadth
#display Output
print(f"Area of rectangle: {area_of_rectangle}")
#WAP to calculate selling price of book based on cost price and discount
#start
cost_price = float(input("Enter cost price of book: "))
discount = float(input("Enter discount percentage: "))
# perform operation
selling_price = cost_price - (cost_price * discount / 100)
#display Output
print(f"Selling price of book: {selling_price}")
#WAP to calculate total salary of employee based on basic, da=10% of basic, ta=12% of basic, hra=15% of basic
#start
basic = float(input("Enter basic salary: "))
# perform operation
da = basic * 0.10
ta = basic * 0.12
hra = basic * 0.15
total_salary = basic + da + ta + hra
#display Output
print(f"Total salary of employee: {total_salary}")
# Find the sum of three-digit number.
num = int(input("Enter a three-digit number: "))
# perform operation
sum_of_digits = sum(int(digit) for digit in str(num))
#display Output
print(f"Sum of digits: {sum_of_digits}")
#Write a program to swap two numbers using third variable
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
# perform operation
temp = a
a = b
b = temp
#display Output
print(f"After swapping: a = {a}, b = {b}")
#Write a program to swap two numbers without using third variable
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
# perform operation
a = a + b
b = a - b
a = a - b
#display Output
print(f"After swapping: a = {a}, b = {b}")
#Write a program to reverse three-digit number
num = int(input("Enter a three-digit number: "))
# perform operation
digit1 = num % 10
digit2 = (num // 10) % 10
digit3 = num // 100
reversed_num = digit1 * 100 + digit2 * 10 + digit3
#display Output
print(f"Reversed number: {reversed_num}")
#Write a program to accept an integer amount from user and tell minimum number of notes needed for representing that amount. 
amount = int(input("Enter the amount: "))
# perform operation
notes_1000 = amount // 1000
amount %= 1000
notes_500 = amount // 500
amount %= 500
notes_100 = amount // 100
amount %= 100
notes_50 = amount // 50
amount %= 50
notes_20 = amount // 20
amount %= 20
notes_10 = amount // 10
amount %= 10
print(f"Notes of 1000: {notes_1000}")
print(f"Notes of 500: {notes_500}")
print(f"Notes of 100: {notes_100}")
print(f"Notes of 50: {notes_50}")
print(f"Notes of 20: {notes_20}")
print(f"Notes of 10: {notes_10}")
print(f"Remaining amount: {amount}")
