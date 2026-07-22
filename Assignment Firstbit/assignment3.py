#Write a program to check if the given number is positive or negative
num = int(input("Enter a number: "))
# perform operation
if num > 0:
    print(f"{num} is positive.")
else:
    print(f"{num} is negative.")
    
#Write a program to input any alphabet and check whether it is vowel or consonant
#start
ch = input("Enter an ch: ")
# perform operation
if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U':
    print(f"{ch} is a vowel.")
else:
    print(f"{ch} is a consonant.")
#Write a program to input angles of a triangle and check whether triangle is valid or not
#start
angle1 = float(input("Enter first angle: "))
angle2 = float(input("Enter second angle: "))
angle3 = float(input("Enter third angle: "))
# perform operation
if angle1 + angle2 + angle3 == 180:
    print("The triangle is valid.")
else:
    print("The triangle is not valid.")
#Write a program to input all sides of a triangle and check whether triangle is valid or not
#start
side1 = float(input("Enter first side: "))
side2 = float(input("Enter second side: "))
side3 = float(input("Enter third side: "))
# perform operation
if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
    print("The triangle is valid.")
else:
    print("The triangle is not valid.")
#Write a program to check whether the triangle is equilateral, isosceles or scalene triangle
#start
if side1 == side2 == side3:
    print("The triangle is equilateral.")
elif side1 == side2 or side1 == side3 or side2 == side3:
    print("The triangle is isosceles.")
else:
    print("The triangle is scalene.")
#Write a program to calculate profit or loss
cost_price = float(input("Enter cost price: "))
selling_price = float(input("Enter selling price: "))
if selling_price > cost_price:
    profit = selling_price - cost_price
    print(f"Profit: {profit}")
else:
    loss = cost_price - selling_price
    print(f"Loss: {loss}")
#Write a program to check if user has entered correct userid and password
#start
correct_userid = "admin"
correct_password = "password123"
userid = input("Enter userid: ")
password = input("Enter password: ")
# perform operation
if userid == correct_userid and password == correct_password:
    print("Login successful.")
else:
    print("Invalid userid or password.")
    
