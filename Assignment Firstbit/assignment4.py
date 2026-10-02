# 1. WAP to print all even numbers until n.
n = int(input("Enter a number: "))
for i in range(2, n + 1, 2):
    print(i, end=" ")
    
# 1. WAP to print all even numbers until n.
n= int(input("Enter a number: "))
for i in range(2, n + 1, 2):
    print(i, end=" ")
#1.WAP to print sum of series upto n.
n = int(input("Enter a number: "))
sum = 0
for i in range(1, n + 1):
    sum += i
print(f"Sum of series upto {n} is: {sum}")

#WAP to print factorial of a number
n = int(input("Enter a number: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"Factorial of {n} is: {factorial}")

# WAP to print Fibonacci series upto n.
n = int(input("Enter a number: "))
a, b = 0, 1
print("Fibonacci series upto", n, "is:")
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
# 6. WAP to check if a given number is prime number or not.
n = int(input("Enter a number: "))
is_prime = True
if n <= 1:
    is_prime = False
else:
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            is_prime = False
            break
if is_prime:
    print(f"{n} is a prime number.")
else:
    print(f"{n} is not a prime number.")
    
# WAP to print all integers upto n that aren’t divisible by 2 and 3.
n = int(input("Enter a number: "))
for i in range(1, n + 1):
    if i % 2 != 0 and i % 3 != 0:
        print(i, end=" ")
# 8. WAP to find which numbers are divisible by 7 and multiple of 5 in a given range.
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
print("Numbers divisible by 7 and multiple of 5:")
for i in range(start, end + 1):
    if i % 7 == 0 and i % 5 == 0:
        print(i, end=" ")

# # WAP to print all numbers in a range divisible by a given number.
n = int(input("Enter the range: "))
divisor = int(input("Enter the divisor: "))
print(f"Numbers in range 1 to {n} divisible by {divisor}:")
for i in range(1, n + 1):
    if i % divisor == 0:
        print(i, end=" ")
        
# WAP to check if given number is Perfect Number.
n = int(input("Enter a number: "))
sum_of_divisors = 0
for i in range(1, n):
    if n % i == 0:
        sum_of_divisors += i
if sum_of_divisors == n:
    print(f"{n} is a Perfect Number.")

        
# 11. WAP to check if given number Strong Number.
num = int(input("Enter a number: "))
temp=num
total = 0
while temp > 0:
    digit = temp % 10
    factorial = 1
    for i in range(1, digit + 1):
        factorial *= i
    total += factorial
    temp //= 10
if total == num:
    print(f"{num} is a Strong Number.")
else:
    print(f"{num} is not a Strong Number.")
    
    

# 12. Write a program to check if given number is Armstrong number or not.
num = int(input("Enter a number: "))
temp = num
sum_of_cubes = 0
while temp > 0:
    digit = temp % 10
    sum_of_cubes += digit ** 3
    temp //= 10
if sum_of_cubes == num:
    print(f"{num} is an Armstrong Number.")
else:
    print(f"{num} is not an Armstrong Number.")
