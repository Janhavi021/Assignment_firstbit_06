# 1. Write a program to prompt user to enter userid and password. If Id and
# password is incorrect give him chance to re-enter the credentials. Let him try 3
# times. After that program to terminate.
userid = "admin"
password = "password123"

for _ in range(3):
    entered_userid = input("Enter UserID: ")
    entered_password = input("Enter Password: ")
    if entered_userid == userid and entered_password == password:
        print("Login successful!")
        break
    else:
        print("Incorrect credentials. Please try again.")
else:
    print("Too many failed attempts. Program terminated.")

# 2. Enter number of students from user. For those many students accept marks of 5
# subject marks from user and calculate percentage. Display all percentage and
# average percentage of students.
userid = int(input("Enter number of students: "))
total_percentage = 0
for i in range(userid):
    print(f"Enter marks for student {i + 1}:")
    total_marks = 0
    for j in range(5):
        marks = float(input(f"Subject {j + 1} marks: "))
        total_marks += marks
    percentage = (total_marks / 500) * 100
    total_percentage += percentage
    print(f"Percentage of student {i + 1}: {percentage:.2f}%")
average_percentage = total_percentage / userid if userid > 0 else 0
print(f"Average percentage of all students: {average_percentage:.2f}%")

# 3. Accept no. of passengers from user and per ticket cost. Then accept age of each
# passenger and then calculate total amount to ticket to travel for all of them based on
# following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.
num_passengers = int(input("Enter number of passengers: "))
ticket_cost = float(input("Enter per ticket cost: "))
total_amount = 0
for i in range(num_passengers):
    age = int(input(f"Enter age of passenger {i + 1}: "))
    if age < 12:
        total_amount += ticket_cost * 0.7  # 30% discount
    elif age > 59:
        total_amount += ticket_cost * 0.5  # 50% discount
    else:
        total_amount += ticket_cost  # full price   

print(f"Total amount for all passengers: {total_amount:.2f}")
print("Thank you for using the ticket booking system!")


# 4. WAP to print Armstrong number within a given range
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
print(f"Armstrong numbers between {start} and {end}:")
for num in range(start, end + 1):
    temp = num
    sum_of_cubes = 0
    while temp > 0:
        digit = temp % 10
        sum_of_cubes += digit ** 3
        temp //= 10
    if sum_of_cubes == num:
        print(num, end=" ")
# 5. Write a program to print prime numbers between 1 to 100.
num = int(input("Enter a number: "))
is_prime = True
for i in range(2, int(num ** 0.5) + 1):
    if num % i == 0:
        is_prime = False
        break
if is_prime:
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
    
# 6. Write a program to print first n prime numbers.
num = int(input("Enter a number: "))
count = 0
current = 2
while count < num:
    is_prime = True
    for i in range(2, int(current ** 0.5) + 1):
        if current % i == 0:
            is_prime = False
            break
    if is_prime:
        print(current, end=" ")
        count += 1
    current += 1

# 7. Write a program to solve the following series :
# a. 1! + 2! + 3! + 4! + .....n!
# b. N + N^2 + N^3+N^4 .....+N^N (here ^ means exponent)
# c. Find the sum of a geometric series from 1 to n where the common ratio is 2.
# d. S = a + a2 / 2 + a3 / 3 + ...... + a10 / 10
# e. x - x2/3 + x3/5 - x4/7 + .... to n terms
x=int(input("Enter the value of x: "))
n=int(input("Enter the number of terms: "))
total_sum = 0
for i in range(1, n + 1):
    denominator = 2 * i - 1
    term=(x ** i) / denominator
    if i % 2 == 0:
        total_sum -= term
    else:
        total_sum += term
print(f"The sum of the series is: {total_sum}")