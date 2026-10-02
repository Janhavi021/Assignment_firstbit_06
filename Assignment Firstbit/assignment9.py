# 1. Write a program to find sum of following series using recursive functions:

# i. 1! + 2! + 3! + 4! +..... + n!
# Note : For fact and sum two recursive functions
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def sum_of_factorials(n):
    if n == 0:
        return 0
    else:
        return factorial(n) + sum_of_factorials(n - 1)
print("Sum of factorials:", sum_of_factorials(5))

# Write a program to check if given number is Armstrong or not using recursive function.
def is_armstrong_number(num):
    num_str = str(num)
    num_len = len(num_str)
    sum_of_powers = sum(int(digit) ** num_len for digit in num_str)
    return sum_of_powers == num
print("Is Armstrong number:", is_armstrong_number(153))

# Write a program to reverse a given number using recursive function.
def reverse_number(n):
    if n < 10:
        return n
    else:
        num_digits = len(str(n))
        return (n % 10) * (10 ** (num_digits - 1)) + reverse_number(n // 10)
print("Reverse of number:", reverse_number(12345))

# 4. Write a program to find sum of n numbers using recursion.
def sum_of_numbers(n):
    if n == 0:
        return 0
    else:
        return n + sum_of_numbers(n - 1)
print("Sum of numbers:", sum_of_numbers(5))

# 5. Write a program to find factorial using recursion.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print("Factorial:", factorial(5))

# 6. Write a program to print Fibonacci series using recursion.
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
print("Fibonacci series:")
for i in range(10):
    print(fibonacci(i), end=" ")

# 7. Write a program to find sum of digits using recursion.
def sum_of_digits(n):
    if n < 10:
        return n
    else:
        return (n % 10) + sum_of_digits(n // 10)
print("Sum of digits:", sum_of_digits(12345))

# 8. Write a program to check whether a number is prime or not using recursion.
def is_prime(n, divisor=2):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % divisor == 0:
        return False
    if divisor * divisor > n:
        return True
    return is_prime(n, divisor + 1)
print("Is prime:", is_prime(17))

# 9. Write a program to calculate the m to the power n using recursion.
def power(m, n):
    if n == 0:
        return 1
    else:
        return m * power(m, n - 1)
print("Power:", power(2, 3))
