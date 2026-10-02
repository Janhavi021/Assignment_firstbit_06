# Write a program to calculate area of rectangle
def area_of_rectangle(length, breadth):
    return length * breadth

length = 5
breadth = 3
print("Area of rectangle:", area_of_rectangle(length, breadth))

# Write a program to calculate area of circle
def area_of_circle(radius):
    return 3.14 * radius ** 2

radius = 5
print("Area of circle:", area_of_circle(radius))

# Sum of all prime numbers between 1 to n
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

n = 10
prime_sum = sum(i for i in range(2, n + 1) if is_prime(i))
print("Sum of prime numbers between 1 and", n, "is:", prime_sum)
# Write a program to find print the following Fibonacci series using
# functions:
# 1 1 2 3 5 8 n terms
def fibonacci_series(n):
    series = [1, 1]
    for _ in range(2, n):
        series.append(series[-1] + series[-2])
    return series

n = 6
print("Fibonacci series:", fibonacci_series(n))

# 7. Write a program to find sum of digits of a number.
def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))
print("Sum of digits:", sum_of_digits(12345))

# 8. Write a program find reverse of a number
def reverse_number(n):
    return int(str(n)[::-1])
print("Reverse of number:", reverse_number(12345))


# 9. Write a program to check if entered number is a palindrome or
# not.
def is_palindrome(n):
    str_n = str(n)
    return str_n == str_n[::-1]
    
print("Is palindrome:", is_palindrome(12321))

# 10. Write a program to check if entered year is a leap year or not.
def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
print("Is leap year:", is_leap_year(2020))

# 11. WAP to check if a given number is Armstrong number or not. For
# each task create separate functions.
def is_armstrong_number(num):
    num_str = str(num)
    num_len = len(num_str)
    sum_of_powers = sum(int(digit) ** num_len for digit in num_str)
    return sum_of_powers == num
print("Is Armstrong number:", is_armstrong_number(153))
